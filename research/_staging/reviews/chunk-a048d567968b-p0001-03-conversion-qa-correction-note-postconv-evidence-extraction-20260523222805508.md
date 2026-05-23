---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523222805508
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260523222805508.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; Dario Pulgar support visually checked on rendered/printed pages 7 and 8"
literal_support: "page-0007.jpg supports the Dario Pulgar Chilean/Chile film distribution/fleeing-1973 paragraph; page-0008.jpg supports `His mother tongue was Spanish`, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium-high
conversion_qa_concern: "The source-image wording is visually supported, but the derivative page reference remains contradictory: assigned page 1 versus rendered/printed pages 7-8. Raw source, converted Markdown, chunks, and page Markdown were not edited."
uncertainty: "The passage can support staged contextual Dario Pulgar claims, but the authoritative page citation cannot be promoted until conversion/page-boundary QA is completed."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker reviewed the proof-review follow-up for `CHUNK-a048d567968b-P0001-03` and preserved the disagreement between derivative transcript metadata and image-reviewed evidence.

## Visual Checks

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` visibly supports the Dario Pulgar paragraph naming him, describing him as Chilean, stating that he had been the number two man in Chile's state film distribution system under Allende while still in his twenties, and stating that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` visibly supports the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario was primarily occupied with acquiring distribution rights and determining where off-shore printing materials were.

## Remaining Blocker

The evidence remains blocked for canonical promotion because the derivative references still conflict. The chunk manifest and frontmatter assign `CHUNK-a048d567968b-P0001-03` to page 1, but the family-relevant support is on rendered/printed pages 7 and 8, and the chunk body includes later converted page metadata. This is a page-boundary/citation QA problem, not a contradiction in the Dario Pulgar wording.

## Promotion Recommendation

Keep related Dario Pulgar claims on `hold_for_conversion_qa`. The existing negative relationship note should remain `do_not_promote` because this chunk states no kinship relationship.
