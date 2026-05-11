from __future__ import annotations

from pathlib import Path

from historic_doc_ingest.models import BoundingBox, DocumentBlock


def classify_text_block(text: str, bbox: BoundingBox, page_height: float) -> str:
    stripped = text.strip()
    if not stripped:
        return "unknown"
    if bbox.y0 > page_height * 0.92 and len(stripped) <= 12:
        if any(char.isdigit() for char in stripped):
            return "page_number"
        return "footer"
    if bbox.y0 < page_height * 0.12 and len(stripped) <= 120:
        return "heading"
    lower = stripped.lower()
    if lower.startswith(("fig.", "figure", "plate", "caption", "image:")):
        return "caption"
    return "body"


def extract_embedded_pdf_blocks(
    page: object,
    page_width: float,
    page_height: float,
    scale_x: float = 1.0,
    scale_y: float = 1.0,
) -> list[DocumentBlock]:
    blocks: list[DocumentBlock] = []
    get_text = getattr(page, "get_text", None)
    if get_text is None:
        return blocks

    raw = get_text("dict")
    for raw_block in raw.get("blocks", []):
        block_type = raw_block.get("type")
        bbox = scale_bbox(BoundingBox(*raw_block.get("bbox", (0, 0, 0, 0))), scale_x, scale_y)
        if block_type == 0:
            lines: list[str] = []
            for line in raw_block.get("lines", []):
                spans = [span.get("text", "") for span in line.get("spans", [])]
                text = "".join(spans).strip()
                if text:
                    lines.append(text)
            text = "\n".join(lines).strip()
            if text:
                blocks.append(
                    DocumentBlock(
                        kind=classify_text_block(text, bbox, page_height),
                        bbox=bbox,
                        text=text,
                        confidence=1.0,
                        metadata={"source": "pdf_text_layer"},
                    )
                )
        elif block_type == 1:
            blocks.append(
                DocumentBlock(
                    kind="image",
                    bbox=bbox,
                    metadata={"source": "pdf_image_block"},
                )
            )

    return blocks


def attach_image_assets(blocks: list[DocumentBlock], page_image_path: Path, images_dir: Path, page_number: int) -> None:
    image_blocks = [block for block in blocks if block.kind == "image"]
    if not image_blocks:
        return

    try:
        from PIL import Image
    except ImportError:
        return

    images_dir.mkdir(parents=True, exist_ok=True)
    with Image.open(page_image_path) as page_image:
        for index, block in enumerate(image_blocks, start=1):
            box = (
                max(0, int(block.bbox.x0)),
                max(0, int(block.bbox.y0)),
                min(page_image.width, int(block.bbox.x1)),
                min(page_image.height, int(block.bbox.y1)),
            )
            if box[2] <= box[0] or box[3] <= box[1]:
                continue
            crop = page_image.crop(box)
            asset = images_dir / f"page-{page_number:04d}-image-{index:02d}.png"
            crop.save(asset)
            block.asset_path = asset.as_posix()


def attach_nearest_captions(blocks: list[DocumentBlock]) -> None:
    captions = [block for block in blocks if block.kind == "caption" and block.text]
    images = [block for block in blocks if block.kind == "image"]
    for image in images:
        below = [
            caption
            for caption in captions
            if caption.bbox.y0 >= image.bbox.y1 and horizontal_overlap(image.bbox, caption.bbox) > 0.25
        ]
        if below:
            nearest = min(below, key=lambda caption: caption.bbox.y0 - image.bbox.y1)
            image.metadata["caption"] = nearest.text


def horizontal_overlap(a: BoundingBox, b: BoundingBox) -> float:
    overlap = max(0.0, min(a.x1, b.x1) - max(a.x0, b.x0))
    return overlap / max(1.0, min(a.width, b.width))


def scale_bbox(bbox: BoundingBox, scale_x: float, scale_y: float) -> BoundingBox:
    return BoundingBox(
        x0=bbox.x0 * scale_x,
        y0=bbox.y0 * scale_y,
        x1=bbox.x1 * scale_x,
        y1=bbox.y1 * scale_y,
    )
