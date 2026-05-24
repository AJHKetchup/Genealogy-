---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524003400694
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260524003400694.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; image-reviewed support is printed/source page 7 for the Chilean/film-distribution/fleeing-1973 paragraph and printed/source page 8 for the mother-tongue, language, and Vision Habitat role passages"
literal_support: "page-0007.jpg supports the named Dario Pulgar paragraph and Chile film-distribution/displacement context; page-0008.jpg supports `His mother tongue was Spanish` and Dario's Vision Habitat distribution-rights work."
conversion_confidence: medium-high
conversion_qa_concern: "The requested missing rendered page-0008.jpg is present in this checkout and visually verifies the mother-tongue sentence, but the assigned page 1 versus printed/source pages 7-8 discrepancy remains unresolved."
uncertainty: "The wording of the Dario Pulgar passages is supported by available page images; the unresolved uncertainty is the authoritative citation/page boundary for canonical use."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision did not edit raw sources, converted Markdown, chunk Markdown, or page Markdown.

## What Was Checked

- `page-0007.jpg` is present and visually supports the Dario Pulgar full-name passage, the Chilean descriptor, the statement that he had been the number two man in Chile's state film distribution system under Allende, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government.
- `page-0008.jpg` is present and visually supports the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario was primarily occupied with acquiring distribution rights and locating off-shore printing materials.

## Remaining Blocker

The proof-review blocker is not fully resolved. The image-reviewed evidence is on printed/source pages 7 and 8, but the controller and chunk manifest assign this chunk to page 1. The derivative chunk also contains embedded page metadata beyond assigned page 1. That disagreement should be preserved in staged evidence and resolved by conversion/page-boundary QA before any canonical promotion.

## Staging Decision

Keep the existing Dario Pulgar claim drafts and the source-packet supplement on `hold_for_conversion_qa`. The negative relationship note remains `do_not_promote` because this chunk states no family relationship.
