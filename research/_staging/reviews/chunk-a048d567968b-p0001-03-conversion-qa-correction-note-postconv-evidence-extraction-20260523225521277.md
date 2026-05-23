---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523225521277
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "controller and aggregate chunk manifest assign page 1; visually checked support is on rendered/printed pages 7 and 8"
literal_support: "page-0007.jpg supports the full-name Dario Pulgar passage, Chilean descriptor, Chile state film distribution role under Allende, and flight after Pinochet's 1973 overthrow; page-0008.jpg supports the Spanish mother-tongue sentence, English/French language context, and Vision Habitat distribution-rights/off-shore-printing-materials work."
conversion_confidence: medium-high
conversion_qa_concern: "The relevant wording is visually supported on rendered pages 7-8, but the assigned chunk path and manifest still identify this work item as page 1 and the chunk body contains multiple embedded converted pages. Promotion should wait for authoritative page-boundary/citation reconciliation."
uncertainty: "This note does not edit raw sources, converted Markdown, chunks, page Markdown, or canonical wiki pages. The source is memoir evidence and states no kinship relationship for Dario Pulgar."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision reviewed the existing staged outputs for `CHUNK-a048d567968b-P0001-03` after proof review requested conversion-QA reconciliation.

## Evidence Checked

- `page-0007.jpg` visibly contains the Dario Pulgar full-name passage, including the Chilean descriptor, the statement that Dario had been the number two man in Chile's state film distribution system under Allende while still in his twenties, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government.
- `page-0008.jpg` visibly contains the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario was primarily occupied with acquiring distribution rights and determining where off-shore printing materials were.

## Staging Status

The staged source packet and atomic claim drafts already preserve the required disagreement between the derivative chunk assignment and the image-reviewed evidence. The claims remain individual staged drafts with source path, converted file, chunk reference, literal support, conversion confidence/QA concern, uncertainty, and `promotion_recommendation: hold_for_conversion_qa`.

The negative relationship note remains appropriate because the chunk gives Dario Pulgar colleague/work context but states no parent, spouse, child, sibling, or other family relationship.

## Remaining Blocker

Do not promote the Dario Pulgar claims from this chunk until conversion/page-boundary QA reconciles or explicitly documents the authoritative citation target. The immediate conflict is: assigned aggregate chunk `P0001-03` and manifest page 1 versus visual support on rendered/printed pages 7 and 8.
