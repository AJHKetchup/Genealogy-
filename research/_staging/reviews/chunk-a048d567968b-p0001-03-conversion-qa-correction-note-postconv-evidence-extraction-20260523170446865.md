---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523170446865
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1 in chunk frontmatter/manifest; image-reviewed Dario Pulgar support is on rendered images page-0007.jpg and page-0008.jpg, printed pages 7 and 8"
literal_support: "page-0007.jpg visibly supports the Dario Pulgar Chilean descriptor, Chile state film distribution role, and fleeing-after-1973 passage; page-0008.jpg visibly supports `His mother tongue was Spanish`, the English/French language context, and Dario's Vision Habitat distribution-rights/off-shore printing-materials work."
conversion_confidence: medium
conversion_qa_concern: "The earlier missing page-0008.jpg blocker is resolved in this checkout because page-0008.jpg is present and visually supports the mother-tongue sentence. The remaining blocker is the derivative citation/page-boundary conflict: CHUNK-a048d567968b-P0001-03 is assigned to page 1, while the family-relevant support belongs to rendered/printed pages 7 and 8 embedded in the chunk body."
uncertainty: "This note preserves the disagreement between derivative chunk metadata and image-reviewed evidence. It does not edit raw sources, converted Markdown, chunk Markdown, page Markdown, or canonical wiki pages."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction pass revisited the proof-review blockers for `CHUNK-a048d567968b-P0001-03` and did not perform external research or source conversion.

## Current Visual Check

The rendered page images are present in this checkout:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

Visual review confirms that rendered/printed page 7 supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, the Chile state film distribution role under Allende, and the statement that he fled after Pinochet's 1973 overthrow of the Allende government. Rendered/printed page 8 supports the sentence `His mother tongue was Spanish`, the English/French language context, and the Vision Habitat distribution-rights/off-shore printing-materials work passage.

## Staged Output State

The source packet and six atomic Dario Pulgar claims remain in staging with `promotion_recommendation: hold_for_conversion_qa`. The negative relationship candidate remains `promotion_recommendation: do_not_promote` because this chunk states colleague/work relationships but no kinship relationship.

The substantive transcription for the Dario Pulgar passages agrees with the checked images. The unresolved blocker is authoritative citation control: the chunk frontmatter and manifest assign the chunk to page 1, while the relevant evidence is on rendered/printed pages 7 and 8 and the chunk body continues into later page metadata.

## Promotion Recommendation

Keep the Dario Pulgar claims and source packet on `hold_for_conversion_qa` until conversion QA reconciles or explicitly documents the page-boundary/citation issue. After that, the occupation/role, language, migration-context, and Vision Habitat work claims can be reconsidered for canonical promotion with memoir-source attribution.
