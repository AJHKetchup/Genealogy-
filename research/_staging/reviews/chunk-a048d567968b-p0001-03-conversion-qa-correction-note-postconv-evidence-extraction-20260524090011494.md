---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524090011494
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-revision-postconv-evidence-extraction-20260524090011494.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; Dario Pulgar evidence visually checked on rendered/printed pages 7 and 8"
literal_support: "page-0007.jpg supports the Dario Pulgar named-person, Chilean descriptor, Chile state-film role, and 1973 flight passage; page-0008.jpg supports the Spanish mother-tongue, English/French language context, and Vision Habitat distribution-rights passage."
conversion_confidence: medium-high
conversion_qa_concern: "The relevant rendered images are present and support the wording. The remaining blocker is the unresolved discrepancy between assigned page 1 chunk/manifest metadata and printed/source pages 7-8 evidence."
uncertainty: "Do not promote canonical claims from this chunk until page-boundary/citation QA resolves or formally documents the discrepancy."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision responds to proof-review follow-up without editing raw sources, converted Markdown, chunks, or page Markdown.

## Visual Check Result

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present and visually supports the Dario Pulgar named-person passage, Chilean descriptor, Chile state-film role, and 1973 flight context.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and visually supports `His mother tongue was Spanish`, the English/French language context, and Dario's Vision Habitat distribution-rights work.

## Remaining Blocker

The missing rendered-image concern for the mother-tongue sentence is resolved in this checkout. The page-reference problem remains unresolved: the chunk manifest assigns `CHUNK-a048d567968b-P0001-03` to page 1, while the supporting source images are rendered/printed pages 7 and 8 and the chunk body includes later page metadata.

## Promotion Recommendation

Keep related Dario Pulgar staged claims on `hold_for_conversion_qa`. The negative relationship note remains `do_not_promote` because this chunk states no family relationship.
