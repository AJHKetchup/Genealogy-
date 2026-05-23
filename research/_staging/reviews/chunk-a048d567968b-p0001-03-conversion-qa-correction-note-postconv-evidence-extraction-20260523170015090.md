---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523170015090
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1 in chunk manifest; image-reviewed support is on rendered/source images page-0007.jpg and page-0008.jpg, printed pages 7 and 8"
literal_support: "page-0007.jpg visibly supports the Dario Pulgar Chilean/Chile state film distribution/fleeing-1973 paragraph; page-0008.jpg visibly supports `His mother tongue was Spanish`, English/French language context, and Dario's Vision Habitat distribution-rights/off-shore printing-materials work."
conversion_confidence: medium
conversion_qa_concern: "The earlier missing page-0008.jpg blocker is not reproduced in this checkout: page-0008.jpg is present and visually supports the mother-tongue sentence. The unresolved blocker remains the derivative page-boundary/citation conflict: CHUNK-a048d567968b-P0001-03 is assigned to page 1 while the family-relevant support belongs to rendered/printed pages 7 and 8 embedded in the chunk body."
uncertainty: "This correction note does not edit raw sources, converted Markdown, chunk Markdown, page Markdown, or canonical wiki pages. The staging continues to preserve the disagreement between derivative chunk metadata and image-reviewed page evidence."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision reviewed the staged Dario Pulgar outputs for `CHUNK-a048d567968b-P0001-03` after proof review requested conversion-QA reconciliation.

## Image Check

The rendered page images are present in this checkout:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

Visual review confirms that rendered/printed page 7 supports the Dario Pulgar Chilean descriptor, Chile state film distribution role, and fleeing-after-1973 passage. Rendered/printed page 8 supports the sentence `His mother tongue was Spanish`, the English/French language context, and the Vision Habitat distribution-rights/off-shore printing-materials work passage.

## Staged Output State

The existing source packet, atomic Dario claim drafts, identity candidate, negative relationship note, and page-boundary research task already keep promotion blocked. No relationship is stated in the chunk, and no canonical tree relationship should be promoted from this evidence.

The active blocker is not the substance of the Dario Pulgar passages. The blocker is authoritative citation control: the assigned chunk and manifest say page 1, while the support visually belongs to rendered/printed pages 7 and 8 and the chunk body includes later page metadata.

## Promotion Recommendation

Keep `promotion_recommendation: hold_for_conversion_qa` for the Dario Pulgar claims and source packet from this chunk until conversion QA reconciles or explicitly documents the page-boundary/citation issue. After that, the occupation/role, language, migration-context, and Vision Habitat work claims can be reconsidered for proof review with memoir-source attribution.
