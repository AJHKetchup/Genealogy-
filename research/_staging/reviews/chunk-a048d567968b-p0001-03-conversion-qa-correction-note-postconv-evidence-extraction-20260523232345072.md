---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523232345072
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1 in task/chunk manifest; Dario Pulgar support is on rendered/printed pages 7 and 8"
literal_support: "page-0007.jpg supports the named Dario Pulgar Chilean/Chile state-film/fled-after-1973 passage; page-0008.jpg supports `His mother tongue was Spanish` and Dario's Vision Habitat distribution-rights work."
conversion_confidence: medium-high
conversion_qa_concern: "The derivative transcript and available rendered page images agree on the Dario Pulgar evidence, including the formerly blocked page-0008 mother-tongue sentence. The unresolved blocker is authoritative page/chunk citation: this assigned page-1 chunk contains support from printed/source pages 7-8 and continues into later converted page metadata."
uncertainty: "This note documents image-reviewed support and preserves the discrepancy; it does not correct raw, converted, chunk, or canonical files."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker-specific revision addresses the proof-review follow-up for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunks, page Markdown, or canonical wiki pages.

## Image-Reviewed Evidence

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present in this checkout. It supports the Dario Pulgar paragraph naming him as a Chilean colleague, describing his Chile state-film role under Allende, and stating that he arrived at "The Board" after fleeing Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present in this checkout. It supports the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario worked on distribution rights and off-shore printing materials.

## Remaining Blocker

The evidence-image issue for page 8 is resolved in this checkout, but the citation/page-boundary issue is not resolved. The task and chunk manifest assign `CHUNK-a048d567968b-P0001-03` to page 1, while the family-relevant Dario Pulgar support appears on printed/source pages 7 and 8 and the chunk body includes converted page metadata for additional later pages.

## Staging Decision

Keep the source packet and related Dario Pulgar atomic claims in staging with `promotion_recommendation: hold_for_conversion_qa`. They should not flow to canonical pages until a conversion/page-boundary reviewer corrects the metadata or documents the intended citation scheme. The existing negative relationship note remains `do_not_promote` because this chunk states no family relationship.
