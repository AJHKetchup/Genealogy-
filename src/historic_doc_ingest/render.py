from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RenderedPage:
    number: int
    width: float
    height: float
    scale_x: float
    scale_y: float
    image_path: Path
    page: object


class PdfRenderError(RuntimeError):
    pass


def render_pdf_pages(pdf_path: Path, pages_dir: Path, dpi: int) -> list[RenderedPage]:
    try:
        import fitz
    except ImportError as exc:
        raise PdfRenderError(
            "PDF rendering requires PyMuPDF. Install with: pip install -e \".[pdf]\""
        ) from exc

    pages_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    rendered: list[RenderedPage] = []
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)

    for index, page in enumerate(doc, start=1):
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        image_path = pages_dir / f"page-{index:04d}.png"
        pixmap.save(image_path)
        rendered.append(
            RenderedPage(
                number=index,
                width=float(pixmap.width),
                height=float(pixmap.height),
                scale_x=float(pixmap.width) / float(page.rect.width),
                scale_y=float(pixmap.height) / float(page.rect.height),
                image_path=image_path,
                page=page,
            )
        )

    return rendered
