---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523203220561
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; derivative page Markdown and chunk body place the Dario Pulgar support on source/printed pages 7 and 8"
literal_support: "Page-markdown page-0007.md supports the Dario Pulgar Chilean/Chile film-distribution/fleeing-1973 paragraph; page-markdown page-0008.md supports the mother-tongue Spanish sentence, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium
conversion_qa_concern: "The derivative transcripts agree on the family-relevant Dario Pulgar passages, but the rendered source images cannot be rechecked in this checkout because the page-images directory is absent. The conversion job manifest lists page-images/page-0007.jpg and page-images/page-0008.jpg, while the chunk manifest assigns CHUNK-a048d567968b-P0001-03 to page 1. This preserves the unresolved disagreement between assigned chunk page, derivative page Markdown/page metadata, and prior proof-review image checks."
uncertainty: "No new contradiction was found in the Dario Pulgar wording. Canonical citation remains blocked until conversion QA restores or regenerates rendered source images or otherwise reconciles the authoritative source page references."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision preserves the proof-review blocker for `CHUNK-a048d567968b-P0001-03`. I did not edit raw sources, converted Markdown, chunks, page Markdown, or canonical wiki pages.

## Files Checked

- Assigned chunk: `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md`
- Chunk manifest: `page_start: 1`, `page_end: 1`, `part: 3`
- Converted file: contains Dario Pulgar support in the same chunk body, with embedded page metadata/transcription for later pages.
- Conversion job page Markdown: `page-markdown/page-0007.md` and `page-markdown/page-0008.md` are present and support the staged Dario Pulgar passages.
- Conversion job manifest: lists rendered page images `page-images/page-0007.jpg` and `page-images/page-0008.jpg`.
- Current checkout: the `page-images` directory is absent, so this worker could not independently repeat visual verification.

## Evidence State

The derivative text supports the family-relevant Dario Pulgar cluster already staged:

- `page-0007.md` names `Dario Pulgar`, describes him as Chilean, says he had been the number two man in Chile's state film distribution system under Allende while still in his twenties, and says he arrived after fleeing Pinochet's 1973 overthrow of the Allende government.
- `page-0008.md` states that Dario's mother tongue was Spanish, that he was fluent in English, that he had learned French in Montreal, and that he was primarily occupied with acquiring distribution rights and locating off-shore printing materials.

## QA Disagreement Preserved

The staged claims and source packet should remain blocked because the authoritative page reference is still unresolved. The chunk is assigned to page 1, while the derivative evidence belongs to source/printed pages 7 and 8. Prior proof review and correction notes refer to rendered image checks, but this checkout does not currently provide the images needed to confirm those checks.

## Promotion Recommendation

Keep the related source packet and Dario Pulgar claim drafts on `hold_for_conversion_qa`. Keep the negative relationship candidate at `do_not_promote`. The next conversion QA step is to restore or regenerate the rendered source images for pages 7 and 8, visually verify the Dario Pulgar passages, and reconcile the page/chunk citation before canonical promotion.
