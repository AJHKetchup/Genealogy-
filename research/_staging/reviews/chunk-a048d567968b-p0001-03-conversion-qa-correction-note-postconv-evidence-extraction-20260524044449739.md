---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524044449739
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
assigned_page_reference: "chunk manifest page_start 1, page_end 1"
image_pages_checked:
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg"
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg"
conversion_confidence: medium-high
conversion_qa_concern: "Rendered images page-0007.jpg and page-0008.jpg are present and visually support the Dario Pulgar wording staged from this chunk. The unresolved blocker is still page/chunk reference reconciliation: the manifest assigns CHUNK-a048d567968b-P0001-03 to page 1, while the family-relevant support is on printed/source pages 7 and 8 and the chunk body also includes later converted pages."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note: CHUNK-a048d567968b-P0001-03

This evidence-extraction revision found the relevant rendered page images present in the checkout and visually checked the Dario Pulgar passages against them.

`page-0007.jpg` visibly supports the paragraph naming Dario Pulgar as a UN Habitat Secretariat colleague, describing him as Chilean, stating that under Allende and while still in his twenties he had been the number two man in Chile's state film distribution system, and stating that he came to "The Board" after fleeing Pinochet's 1973 overthrow of the Allende government.

`page-0008.jpg` visibly supports the paragraph stating that Dario's mother tongue was Spanish, that he was fluent in English, and that he had learned French in Montreal. The same rendered page also supports the later statement that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

The previous missing-image blocker for the mother-tongue sentence is therefore resolved for this checkout. The remaining blocker is not the literal wording of the family-relevant Dario passages; it is the unresolved page-reference disagreement. The chunk manifest assigns this chunk to page 1, while the checked source images show the support on printed/source pages 7 and 8, and the chunk text continues into later converted page metadata.

Keep the related source packet, six Dario Pulgar atomic claim drafts, and negative family-relationship note in staging. Their `promotion_recommendation` should remain `hold_for_conversion_qa` for claims and `do_not_promote` for the negative relationship note until the authoritative citation/page boundary is corrected or explicitly documented for canonical use. No parent, spouse, child, sibling, household, or other tree-link relationship is stated in this chunk.
