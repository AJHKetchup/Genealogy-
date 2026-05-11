from __future__ import annotations

from statistics import mean
from typing import Any

from historic_doc_ingest.models import DocumentPage


def page_quality_report(page: DocumentPage, low_confidence_threshold: float = 0.86) -> dict[str, Any]:
    text_blocks = [block for block in page.blocks if block.text.strip()]
    confidences = [block.confidence for block in text_blocks if block.confidence is not None]
    low_confidence_blocks = [
        index
        for index, block in enumerate(page.ordered_blocks(), start=1)
        if block.text.strip() and block.confidence is not None and block.confidence < low_confidence_threshold
    ]
    image_blocks = [block for block in page.blocks if block.kind == "image"]

    review_reasons: list[str] = []
    if not text_blocks:
        review_reasons.append("no_text_blocks_detected")
    if not confidences:
        review_reasons.append("no_ocr_confidence_available")
    if low_confidence_blocks:
        review_reasons.append("low_confidence_text")
    if image_blocks and any("caption" not in block.metadata for block in image_blocks):
        review_reasons.append("uncaptioned_image_regions")

    return {
        "mean_confidence": round(mean(confidences), 4) if confidences else None,
        "text_block_count": len(text_blocks),
        "image_block_count": len(image_blocks),
        "low_confidence_block_ordinals": low_confidence_blocks,
        "needs_review": bool(review_reasons),
        "review_reasons": review_reasons,
    }
