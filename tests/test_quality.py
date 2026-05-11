from historic_doc_ingest.models import BoundingBox, DocumentBlock, DocumentPage
from historic_doc_ingest.quality import page_quality_report


def test_page_quality_flags_low_confidence_text() -> None:
    page = DocumentPage(
        number=1,
        width=100,
        height=100,
        image_path="assets/pages/page-0001.png",
        blocks=[
            DocumentBlock(
                kind="body",
                bbox=BoundingBox(0, 0, 10, 10),
                text="uncertain",
                confidence=0.42,
            )
        ],
    )

    report = page_quality_report(page)

    assert report["needs_review"] is True
    assert report["review_reasons"] == ["low_confidence_text"]
    assert report["low_confidence_block_ordinals"] == [1]
