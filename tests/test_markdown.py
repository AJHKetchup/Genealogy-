from pathlib import Path

from historic_doc_ingest.markdown import render_block
from historic_doc_ingest.models import BoundingBox, DocumentBlock


def test_render_heading_block() -> None:
    block = DocumentBlock(kind="heading", bbox=BoundingBox(0, 0, 10, 10), text="  Chapter I\n")

    assert render_block(block, Path("out")) == "### Chapter I\n\n"


def test_render_image_with_caption() -> None:
    block = DocumentBlock(
        kind="image",
        bbox=BoundingBox(0, 0, 10, 10),
        asset_path="assets/images/page-0001-image-01.png",
        metadata={"caption": "Plate 1. Harbor view"},
    )

    assert render_block(block, Path("out")) == "![Plate 1. Harbor view](assets/images/page-0001-image-01.png)\n\n"
