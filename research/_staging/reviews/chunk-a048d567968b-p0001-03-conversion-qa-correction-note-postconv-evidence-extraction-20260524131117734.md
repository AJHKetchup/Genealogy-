---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524131117734
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Correction Note

This revision does not alter raw sources, converted Markdown, chunks, or page Markdown. It preserves the disagreement between derivative transcript metadata and image-reviewed evidence.

## Findings

- The rendered source image `page-0007.jpg` is present and visually verifies the Dario Pulgar paragraph on printed/source page 7, including the Chilean descriptor, Allende-era Chile state-film role, and 1973 flight context.
- The rendered source image `page-0008.jpg` is present and visually verifies the sentence `His mother tongue was Spanish` plus the English/French and Vision Habitat distribution-rights passages.
- The chunk manifest still assigns `CHUNK-a048d567968b-P0001-03` to page 1, while the supporting evidence is on printed/source pages 7 and 8 and the chunk body contains later page metadata.

## Correction

The prior blocker about missing rendered page-8 image support is partially resolved for evidence extraction because the image exists and the sentence was visually checked. The remaining blocker is page/chunk boundary reconciliation. Claims should not be promoted canonically until citation metadata can identify the correct printed/source page(s) rather than the assigned page-1 chunk label.

## Recommendation

Keep the related source packet and claims at `promotion_recommendation: hold_for_conversion_qa`.
