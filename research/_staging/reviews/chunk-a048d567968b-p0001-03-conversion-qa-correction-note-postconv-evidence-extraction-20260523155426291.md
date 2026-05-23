---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523155426291
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; Dario Pulgar support in this chunk is documented against rendered page images page-0007.jpg and page-0008.jpg / printed pages 7 and 8"
literal_support: "page-0007.jpg supports the Dario Pulgar Chilean/Chile state film distribution/fleeing-1973 paragraph; page-0008.jpg supports `His mother tongue was Spanish`, the English/French language passage, and the Vision Habitat distribution-rights/off-shore printing-materials passage."
conversion_confidence: medium
conversion_qa_concern: "The prior missing-image issue for page-0008.jpg is not reproduced in this checkout because page-0008.jpg is present. The active blocker remains the derivative page-boundary/citation conflict: the manifest assigns this chunk to page 1 while the converted chunk body contains later page metadata and family-relevant support from rendered/printed pages 7 and 8."
uncertainty: "This note does not alter the raw source, converted Markdown, chunk text, or page Markdown. The derivative transcript/image disagreement about authoritative citation remains unresolved, so related promotable Dario Pulgar claims should stay staged."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker reviewed the existing staged outputs for `CHUNK-a048d567968b-P0001-03` in response to proof-review follow-up.

## Current Staged State

- The source packet `research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md` documents Dario Pulgar evidence and keeps `promotion_recommendation: hold_for_conversion_qa`.
- The six atomic Dario Pulgar claim drafts for this chunk all retain `promotion_recommendation: hold_for_conversion_qa`.
- The identity candidate remains `hold_for_conversion_qa`.
- The negative relationship candidate remains `do_not_promote` because the chunk states no kinship relationship.
- The page-boundary research task remains `hold_for_conversion_qa`.

## Proof-Review Follow-Up

The checkout contains both rendered page images cited by prior correction notes:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

The staged drafts now preserve the disagreement instead of promoting through it: assigned chunk metadata says page 1, while the Dario Pulgar support in the converted chunk is tied by prior visual checks to rendered/printed pages 7 and 8. The remaining blocker is authoritative page citation/page-boundary QA, not the substance of the Dario Pulgar memoir passages.

## Promotion Recommendation

Keep the Dario Pulgar claims from this chunk on `hold_for_conversion_qa` until the conversion/page-boundary issue is corrected or explicitly documented by the conversion QA process. After that, the occupation/role, language, migration-context, and Vision Habitat work claims can be reconsidered for proof review with memoir-source attribution.
