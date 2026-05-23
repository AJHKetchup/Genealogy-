---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523143204380
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; relevant Dario Pulgar support visually checked on page-0007.jpg and page-0008.jpg"
literal_support: "page-0007.jpg supports the Dario Pulgar Chilean/Chile film distribution/fleeing-1973 paragraph; page-0008.jpg supports `His mother tongue was Spanish`, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium
conversion_qa_concern: "Rendered source images now include page-0008.jpg, but chunk manifest/page assignment remains inconsistent with the family-relevant page-image evidence."
uncertainty: "The family-relevant text appears visually supported, but the authoritative citation still cannot be resolved between assigned page 1 and rendered/printed pages 7-8 without conversion/page-boundary QA."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision addresses proof-review follow-up for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunks, or page Markdown.

## Visual Checks

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` visually supports the full-name Dario Pulgar passage, including the description as Chilean, the statement that he had been the number two man in Chile's state film distribution system under Allende, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present in this checkout and visually supports the sentence `His mother tongue was Spanish`, the English/French language passage, and the Vision Habitat distribution-rights passage.

## Remaining QA Blocker

The chunk manifest still assigns `CHUNK-a048d567968b-P0001-03` to page 1, while the family-relevant evidence is on rendered/printed pages 7 and 8 and the chunk body continues into later converted page metadata. This is a derivative page-boundary/citation problem rather than a contradiction in the Dario Pulgar claim substance.

## Revision Applied

Updated the staged source packet, claims, identity candidate, negative relationship note, conflict note, and QA task to document the visual checks and correct the earlier "converted page 9" references for the mother-tongue/language/Vision Habitat passages to rendered `page-0008.jpg` / printed page 8.

The 2026-05-23 revision also corrected stale staged chunk references from the older `...page-7cd35b519c/page-0001-chunk-03.md` path to the controller-assigned chunk path `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md`. This does not resolve the page-boundary problem; it only makes the staged draft paths match the current assignment while preserving the rendered page 7/8 evidence disagreement.

## Promotion Recommendation

Keep related Dario Pulgar drafts on `hold_for_conversion_qa` until the authoritative page reference for this chunk is reconciled. The negative relationship note remains `do_not_promote` because this chunk states no kinship relationship.
