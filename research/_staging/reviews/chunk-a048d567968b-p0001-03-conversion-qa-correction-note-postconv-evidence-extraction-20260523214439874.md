---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523214439874
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260523214439874.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; evidence visually checked on rendered/printed pages 7 and 8"
literal_support: "page-0007.jpg supports the Dario Pulgar Chile film-distribution and 1973 displacement passage; page-0008.jpg supports `His mother tongue was Spanish` and the Vision Habitat distribution-rights passage."
conversion_confidence: medium-high
conversion_qa_concern: "Visual support is present, but the authoritative page/chunk citation remains unresolved because the manifest assigns the chunk to page 1 while the evidence is on rendered/printed pages 7-8."
uncertainty: "Do not treat this as promotion-ready until conversion QA resolves whether canonical citations should follow the assigned page-1 chunk, printed/rendered pages 7-8, or regenerated chunk metadata."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This note responds to the proof-review revision request for `CHUNK-a048d567968b-P0001-03` and preserves the disagreement between the derivative transcript/chunk metadata and the image-reviewed evidence.

## Checks Performed

- Checked the controller-assigned chunk `raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md`.
- Checked the chunk manifest, which still assigns this chunk to `page_start: 1` and `page_end: 1`.
- Visually checked `page-0007.jpg`; it supports the Dario Pulgar full-name paragraph, Chilean descriptor, Chile state film-distribution role under Allende, and flight after Pinochet's 1973 overthrow of the Allende government.
- Visually checked `page-0008.jpg`; it supports the mother-tongue Spanish sentence, English/French language context, and Dario's Vision Habitat distribution-rights/off-shore printing-materials work.

## Revision Outcome

The prior blocker about the missing rendered page 8 image is resolved in this checkout because `page-0008.jpg` is present and readable. The page-reference discrepancy remains unresolved: the assignment says page 1, the chunk manifest says page 1, the converted chunk text carries later page metadata, and the image-reviewed support is on printed/rendered pages 7 and 8.

The staged Dario Pulgar claim drafts should therefore remain on `hold_for_conversion_qa`. They are useful as memoir-source family-story context, but they should not be promoted canonically until the page/chunk citation issue is corrected or explicitly documented by conversion QA.

## No Relationship Claim

No parent, spouse, child, sibling, or other kinship relationship is stated for Dario Pulgar in the checked passage. Existing negative relationship staging should remain `do_not_promote`.
