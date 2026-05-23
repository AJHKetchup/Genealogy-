---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523214858359
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; Dario Pulgar support in the staged drafts is documented against rendered page images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
literal_support: "The staged source packet quotes the Dario Pulgar Chilean/Chile state film distribution/fleeing-1973 paragraph, the mother-tongue and English/French language sentence, and the Vision Habitat distribution-rights/off-shore printing-materials sentence."
conversion_confidence: medium-high
conversion_qa_concern: "The rendered page image paths cited by the revised staged outputs are present in this checkout. The remaining blocker is the derivative page-boundary/citation conflict: the chunk manifest assigns this material to page 1 while the family-relevant support is documented as rendered/printed pages 7 and 8."
uncertainty: "This note does not alter raw sources, converted Markdown, chunks, or page Markdown. It preserves the derivative transcript/page-reference disagreement and keeps related claim promotion blocked until conversion QA reconciles the authoritative page reference."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker reviewed `CHUNK-a048d567968b-P0001-03` after proof review requested reconciliation before canonical promotion.

The existing staged outputs are already revision-aware:

- `research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md` records the Dario Pulgar evidence and keeps `promotion_recommendation: hold_for_conversion_qa`.
- Six atomic Dario Pulgar claim drafts for this chunk remain staged with `promotion_recommendation: hold_for_conversion_qa`.
- `research/_staging/relationships/chunk-a048d567968b-p0001-03-no-family-relationship-stated.md` documents negative relationship evidence and remains `do_not_promote`.
- `research/_staging/research-tasks/chunk-a048d567968b-p0001-03-conversion-qa-page-boundary.md` keeps the unresolved page-boundary task open.

The current checkout contains the rendered page images cited by those staged revisions:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

The active blocker is therefore not image absence in this checkout. The active blocker is authoritative citation/page-boundary QA: the assignment and chunk manifest identify the chunk as page 1, while the Dario Pulgar support in the converted chunk is documented in staged materials against rendered/printed pages 7 and 8.

## Promotion Recommendation

Keep this packet and its Dario Pulgar claims on `hold_for_conversion_qa` until conversion QA corrects or explicitly documents the page-reference discrepancy. After that, the relevant contextual occupation, language, migration/displacement, and Vision Habitat work claims can be reconsidered for proof review with memoir-source attribution.
