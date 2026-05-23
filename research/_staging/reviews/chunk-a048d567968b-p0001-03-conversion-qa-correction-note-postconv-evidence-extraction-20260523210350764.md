---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523210350764
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; chunk body contains converted page metadata/text for printed/source pages 7-10, with Dario Pulgar support on printed/source pages 7 and 8"
literal_support: "Printed/source page 7 derivative text names Dario Pulgar, describes him as Chilean, states he had been the number two man in Chile's state film distribution system under Allende, and says he fled after Pinochet's 1973 overthrow; printed/source page 8 derivative text says his mother tongue was Spanish and describes English/French ability and Vision Habitat distribution-rights work."
conversion_confidence: medium
conversion_qa_concern: "This run found page-markdown for pages 7 and 8, and the conversion manifest/work orders list page-images/page-0007.jpg and page-images/page-0008.jpg, but the current checkout does not contain the page-images directory or either rendered image. Prior correction notes report visual checks when those images were available; this worker could not independently repeat them. The assigned chunk still cites page 1 while the family-relevant support belongs to later printed/source pages."
uncertainty: "Preserve the disagreement between derivative transcripts, prior image-reviewed correction notes, and current image availability. Do not treat this note as a correction to source text or as a final page-citation decision."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision records the current extraction state for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunks, page Markdown, or canonical wiki pages.

## Current Evidence State

- The chunk manifest assigns `CHUNK-a048d567968b-P0001-03` to page 1.
- The chunk body includes later converted page metadata and text, including printed/source page 7 and page 8 Dario Pulgar passages.
- Page-markdown files exist for `page-0007.md` and `page-0008.md` and contain the family-relevant Dario Pulgar passages.
- The conversion manifest and work orders list rendered images `page-images/page-0007.jpg` and `page-images/page-0008.jpg`.
- In this checkout, `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images` is absent, so this worker could not independently recheck either rendered image.

## Staged Output Review

The staged source packet and atomic Dario Pulgar claims already preserve the blocker: derivative text is clear enough for staging, but promotion remains held because the authoritative page citation and image-backed transcription cannot be resolved in this task. The negative relationship note remains `do_not_promote` because this chunk states no kinship relationship for Dario Pulgar.

## Required Follow-Up

Restore or regenerate the rendered page images outside this evidence-extraction task, visually compare the page 7 and page 8 Dario Pulgar passages against the source image, and reconcile the page reference between assigned page 1 and printed/source pages 7-8. Until that QA is complete, keep all promotable Dario Pulgar claims from this chunk on `hold_for_conversion_qa`.
