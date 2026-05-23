---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523231922317
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; visually checked support appears on rendered/printed pages 7 and 8"
literal_support: "Rendered page-0007.jpg supports the named Dario Pulgar paragraph; rendered page-0008.jpg supports the mother-tongue, English/French, and Vision Habitat distribution-rights passages."
conversion_confidence: medium-high
conversion_qa_concern: "Visual support is present for the Dario Pulgar passages, including page-0008.jpg for the sentence previously blocked by missing image availability. The remaining blocker is page/chunk reference reconciliation: the chunk manifest assigns page 1 while the supported passages are on printed/source pages 7-8 and the chunk text continues into later page metadata."
uncertainty: "This note documents evidence-image agreement for the targeted passages but does not resolve the authoritative citation boundary or change canonical readiness."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker-specific note revises the proof-review context for `CHUNK-a048d567968b-P0001-03` without editing raw sources, converted Markdown, chunks, page Markdown, or canonical wiki pages.

## Image-Reviewed Evidence

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present. It visually supports the Dario Pulgar paragraph naming him as a Chilean colleague, describing his Chile state-film role under Allende, and stating that he arrived at "The Board" after fleeing the 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present. It visually supports the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario worked on distribution rights and off-shore printing materials.

## Remaining Blocker

The blocker is no longer absence of the rendered page-0008 image in this checkout. The blocker remains citation/page-boundary QA: the task and chunk manifest assign `CHUNK-a048d567968b-P0001-03` to page 1, while the family-relevant support is on printed/source pages 7 and 8 and the chunk body includes converted page metadata for additional pages.

## Staging Decision

Keep the source packet and all related Dario Pulgar atomic claims in staging with `promotion_recommendation: hold_for_conversion_qa`. They can be reconsidered after a conversion/page-boundary reviewer corrects the metadata or documents the intended citation scheme. The negative relationship note remains appropriate because this chunk states no family relationship.
