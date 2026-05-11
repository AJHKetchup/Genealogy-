from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from historic_doc_ingest.layout import attach_image_assets, attach_nearest_captions, extract_embedded_pdf_blocks
from historic_doc_ingest.markdown import write_markdown
from historic_doc_ingest.models import DocumentPage, IngestedDocument, display_path
from historic_doc_ingest.ocr import OcrError, ocr_page
from historic_doc_ingest.providers import NoOpRefinementProvider, RefinementProvider
from historic_doc_ingest.quality import page_quality_report
from historic_doc_ingest.render import render_pdf_pages


@dataclass(frozen=True)
class IngestOptions:
    dpi: int = 400
    ocr_language: str = "eng"
    use_ocr: bool = True
    prefer_pdf_text_layer: bool = True


def ingest_pdf(
    pdf_path: Path,
    output_dir: Path,
    options: IngestOptions | None = None,
    refinement_provider: RefinementProvider | None = None,
) -> IngestedDocument:
    options = options or IngestOptions()
    refinement_provider = refinement_provider or NoOpRefinementProvider()

    pdf_path = pdf_path.resolve()
    output_dir = output_dir.resolve()
    assets_dir = output_dir / "assets"
    pages_dir = assets_dir / "pages"
    images_dir = assets_dir / "images"
    output_dir.mkdir(parents=True, exist_ok=True)

    rendered_pages = render_pdf_pages(pdf_path, pages_dir, options.dpi)
    pages: list[DocumentPage] = []
    warnings: list[str] = []

    for rendered in rendered_pages:
        blocks = []
        if options.prefer_pdf_text_layer:
            blocks.extend(
                extract_embedded_pdf_blocks(
                    rendered.page,
                    rendered.width,
                    rendered.height,
                    rendered.scale_x,
                    rendered.scale_y,
                )
            )

        has_text = any(block.text.strip() for block in blocks)
        if options.use_ocr and not has_text:
            try:
                blocks.extend(ocr_page(rendered.image_path, rendered.height, options.ocr_language))
            except OcrError as exc:
                warnings.append(f"Page {rendered.number}: {exc}")

        attach_image_assets(blocks, rendered.image_path, images_dir, rendered.number)
        _make_paths_relative(blocks, output_dir)
        attach_nearest_captions(blocks)

        page = DocumentPage(
            number=rendered.number,
            width=rendered.width,
            height=rendered.height,
            image_path=display_path(rendered.image_path, output_dir),
            blocks=blocks,
            metadata={"dpi": options.dpi},
        )
        refined_page = refinement_provider.refine_page(page)
        refined_page.metadata["quality"] = page_quality_report(refined_page)
        pages.append(refined_page)

    document = IngestedDocument(
        source_path=str(pdf_path),
        pages=pages,
        metadata={
            "warnings": warnings,
            "format": "markdown+manifest",
            "accuracy_notes": [
                "Coordinates are retained for audit.",
                "Low-confidence OCR should be reviewed against page images.",
                "Use a RefinementProvider for vision-model or specialist HTR correction.",
            ],
        },
    )

    write_markdown(document, output_dir / "document.md", output_dir)
    (output_dir / "manifest.json").write_text(
        json.dumps(document.to_manifest(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return document


def _make_paths_relative(blocks: list, output_dir: Path) -> None:
    for block in blocks:
        if block.asset_path:
            block.asset_path = display_path(Path(block.asset_path), output_dir)
