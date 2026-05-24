---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524014657391
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; visually checked support is on rendered/source page images page-0007.jpg and page-0008.jpg"
literal_support: "page-0007.jpg supports the Dario Pulgar Chilean descriptor, Chile state-film role, and 1973 fleeing/displacement context; page-0008.jpg supports `His mother tongue was Spanish`, the English/French language statement, and Dario's Vision Habitat distribution-rights work."
conversion_confidence: medium-high
conversion_qa_concern: "The family-relevant text is visually supported by rendered page images 7 and 8, but the assigned chunk and chunk manifest still identify this as page 1 and the chunk body spans multiple embedded converted pages. This is a page-boundary/citation blocker, not a substantive contradiction in the Dario Pulgar evidence."
uncertainty: "The staged claims remain memoir-derived contextual evidence. The exact authoritative page reference must be reconciled or explicitly documented by conversion QA before canonical promotion."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker reviewed the existing staged evidence for `CHUNK-a048d567968b-P0001-03` in response to proof-review follow-up. No raw source, converted Markdown, chunk Markdown, or page Markdown was edited.

## Visual Evidence Checked

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` visibly contains the paragraph naming Dario Pulgar, describing him as Chilean, stating that he had been the number two man in Chile's state film distribution system under Allende, and stating that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and visibly contains the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario was primarily occupied with acquiring distribution rights and locating off-shore printing materials.

## Current Staging State

The source packet and six atomic Dario Pulgar claim drafts already preserve the image-reviewed evidence while keeping `promotion_recommendation: hold_for_conversion_qa`. The negative relationship note remains `do_not_promote` because this chunk states no kinship relationship.

## Remaining Blocker

The blocker is still the derivative page reference discrepancy: the controller assignment and chunk manifest place `CHUNK-a048d567968b-P0001-03` on page 1, while the reviewed family-relevant text is on rendered/source pages 7 and 8 and the chunk body continues into later converted page sections. These claims should not be promoted until conversion QA reconciles the authoritative citation/page boundary or documents the chunk as intentionally contaminated across pages.

