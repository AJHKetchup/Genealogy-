---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523203646259
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; converted/chunk body contains printed/converted pages 7-10, including Dario Pulgar support on printed pages 7 and 8"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: CHUNK-a048d567968b-P0001-03

This revision preserves the disagreement between the derivative transcript, page/chunk metadata, and image-reviewed evidence.

## What Was Checked

- Assigned chunk: `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md`.
- Converted source: `raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md`.
- Chunk manifest: `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json`.
- Conversion job manifest: `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/manifest.json`.
- Existing proof reviews for claims `002` and `004`.

## Findings

- The chunk manifest assigns `CHUNK-a048d567968b-P0001-03` to `page_start: 1` and `page_end: 1`.
- The chunk body contains a sequence of later-page text. It includes printed/converted page 7 text naming `Dario Pulgar` and saying he had been the number two man in Chile's state film distribution system, followed by printed/converted page 8 text stating `His mother tongue was Spanish` and describing Dario's Vision Habitat distribution-rights work.
- The conversion job manifest lists rendered images including `page-0007.jpg` and `page-0008.jpg`, but the local checkout currently has no `page-images` directory under this conversion job.
- Prior proof review for the Chile film-distribution role reports visual agreement on `page-0007.jpg`.
- Prior proof review for the mother-tongue claim reports that `page-0008.jpg` was unavailable, so the sentence `His mother tongue was Spanish` remained converted-text supported but not image verified.

## Staging Revisions Made

- Updated the source packet to state that the page-7 Dario Pulgar/Chile-film passage has prior visual-review support, while the page-8 language and Vision Habitat role passages remain transcript-supported but not independently image-verified in this checkout.
- Updated page-8 claim drafts `004`, `005`, and `006` to use `conversion_confidence: low-to-medium` and to carry the missing `page-0008.jpg` / page-boundary blocker explicitly.
- Left all Dario Pulgar claims on `promotion_recommendation: hold_for_conversion_qa`.
- Left the relationship candidate as negative evidence with `promotion_recommendation: do_not_promote`; this chunk states colleague/work context, not a family relationship.

## Promotion Recommendation

Keep all canonical claim promotion for `CHUNK-a048d567968b-P0001-03` on hold until conversion QA restores or regenerates the rendered page images, visually checks printed pages 7 and 8 against the converted text, and resolves the chunk's assigned page-1 citation against the embedded page-7/page-8 evidence.
