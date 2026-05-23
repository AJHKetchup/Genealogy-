---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523175636372
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1 in chunk frontmatter/manifest; image-reviewed family-relevant support is on rendered page-0007.jpg and page-0008.jpg, printed pages 7 and 8"
literal_support: "Rendered page-0007.jpg visibly supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, Chile state film distribution role under Allende, and fleeing after Pinochet's 1973 overthrow. Rendered page-0008.jpg is present and visibly supports `His mother tongue was Spanish`, English/French language context, and Dario's Vision Habitat distribution-rights/off-shore printing-materials work."
conversion_confidence: medium
conversion_qa_concern: "The image-reviewed text agrees with the family-relevant converted transcription, including the previously blocked mother-tongue sentence. The remaining blocker is derivative citation/page control: CHUNK-a048d567968b-P0001-03 is assigned to page 1, while the supported Dario Pulgar evidence belongs to rendered/printed pages 7 and 8 embedded in the chunk body."
uncertainty: "This note preserves the disagreement between derivative transcript metadata and image-reviewed evidence. It does not alter raw sources, converted Markdown, chunks, page Markdown, or canonical wiki pages."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision rechecked the proof-review blockers for `CHUNK-a048d567968b-P0001-03` using the existing staged outputs and rendered page images.

## Image-Reviewed Evidence

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` is present and visibly contains the Dario Pulgar paragraph. It names Dario Pulgar, describes him as Chilean, states that under Allende he had been the number two man in Chile's state film distribution system while still in his twenties, and states that he fled after Pinochet's 1973 overthrow of the Allende government.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg` is present and visibly contains the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario was primarily occupied with acquiring distribution rights and determining where off-shore printing materials were.

## Staged Draft State

The existing source packet, six Dario Pulgar atomic claim drafts, identity/conflict staging, negative relationship note, and conversion-QA research tasks already keep the relevant Dario Pulgar evidence in staging with `promotion_recommendation: hold_for_conversion_qa`. No new family relationship is stated by this chunk.

## Remaining Blocker

The prior missing-image blocker for `page-0008.jpg` is resolved in this checkout because the image is present and visually supports the mother-tongue passage. The active blocker remains the page-reference discrepancy: the chunk frontmatter and chunk manifest assign the chunk to page 1, while the family-relevant evidence is on rendered/printed pages 7 and 8 and the chunk body includes later converted page metadata.

Keep the related Dario Pulgar claims on `hold_for_conversion_qa` until conversion QA reconciles or explicitly documents the authoritative citation/page-boundary issue. The negative relationship note remains `do_not_promote`.
