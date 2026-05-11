from __future__ import annotations

from pathlib import Path

from historic_doc_ingest.layout import classify_text_block
from historic_doc_ingest.models import BoundingBox, DocumentBlock


class OcrError(RuntimeError):
    pass


def ocr_page(image_path: Path, page_height: float, language: str) -> list[DocumentBlock]:
    try:
        import pytesseract
        from pytesseract import Output
    except ImportError as exc:
        raise OcrError(
            "OCR requires pytesseract and the Tesseract binary. Install Python dependency with: pip install -e \".[ocr]\""
        ) from exc

    data = pytesseract.image_to_data(str(image_path), lang=language, output_type=Output.DICT)
    lines: dict[tuple[int, int, int], list[int]] = {}
    for index, text in enumerate(data.get("text", [])):
        if not text or not text.strip():
            continue
        key = (
            int(data["block_num"][index]),
            int(data["par_num"][index]),
            int(data["line_num"][index]),
        )
        lines.setdefault(key, []).append(index)

    blocks: list[DocumentBlock] = []
    for indices in lines.values():
        x0 = min(int(data["left"][index]) for index in indices)
        y0 = min(int(data["top"][index]) for index in indices)
        x1 = max(int(data["left"][index]) + int(data["width"][index]) for index in indices)
        y1 = max(int(data["top"][index]) + int(data["height"][index]) for index in indices)
        words = [data["text"][index].strip() for index in indices if data["text"][index].strip()]
        confidences = [
            float(data["conf"][index])
            for index in indices
            if str(data["conf"][index]).replace(".", "", 1).lstrip("-").isdigit() and float(data["conf"][index]) >= 0
        ]
        text = " ".join(words)
        bbox = BoundingBox(float(x0), float(y0), float(x1), float(y1))
        blocks.append(
            DocumentBlock(
                kind=classify_text_block(text, bbox, page_height),
                bbox=bbox,
                text=text,
                confidence=(sum(confidences) / len(confidences) / 100) if confidences else None,
                metadata={"source": "tesseract"},
            )
        )

    return blocks
