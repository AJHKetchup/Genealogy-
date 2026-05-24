---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524130713031
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-revision-postconv-evidence-extraction-20260524130713031.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
page_reference: "assigned page 1; Dario Pulgar evidence belongs to embedded printed/source pages 7 and 8"
literal_support: "page-0007.jpg corresponds to the Dario Pulgar named-person, Chilean descriptor, Chile state-film role, and 1973 flight passage; page-0008.jpg corresponds to the Spanish mother-tongue, English/French language context, and Vision Habitat distribution-rights passage."
conversion_confidence: medium-high
conversion_qa_concern: "The rendered page images page-0007.jpg and page-0008.jpg are present in this checkout. The remaining blocker is the unresolved discrepancy between the assigned page-1 chunk/manifest metadata and printed/source pages 7-8 evidence."
uncertainty: "Do not promote canonical claims from this chunk until page-boundary/citation QA resolves or formally documents the discrepancy."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This note responds to proof-review follow-up without editing raw sources, converted Markdown, chunks, or page Markdown.

## Image Availability

Both rendered source images referenced by earlier proof review are present in this checkout:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

## Reconciliation Status

The missing-rendered-image blocker for the mother-tongue sentence appears resolved locally because `page-0008.jpg` exists. The page-reference blocker remains unresolved: `CHUNK-a048d567968b-P0001-03` is assigned to page 1 in the chunk manifest, but the Dario Pulgar support is in embedded printed/source pages 7 and 8, and the chunk body continues into later page metadata.

## Promotion Recommendation

Keep the related Dario Pulgar claim drafts on `hold_for_conversion_qa`. The negative relationship candidate remains `do_not_promote` because the chunk states no family relationship.
