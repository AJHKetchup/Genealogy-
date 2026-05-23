---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523225149059
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1 in controller/chunk manifest; support appears in embedded converted text for printed/source pages 7-8 within the chunk"
literal_support: "The staged source packet and claims preserve Dario Pulgar support for his Chilean descriptor, Chile state film distribution role under Allende, flight after the 1973 Pinochet overthrow, Spanish mother tongue, English/French language context, and Vision Habitat distribution-rights/off-shore-printing-materials work."
conversion_confidence: medium
conversion_qa_concern: "The wording is already staged with reported visual checks against rendered page-0007.jpg and page-0008.jpg, and those image files are present in this checkout. The unresolved blocker is the authoritative page/chunk citation conflict: the controller and manifest assign this as page 1 while the family-relevant support belongs to printed/rendered pages 7-8."
uncertainty: "This task did not edit raw sources, converted Markdown, chunk Markdown, page Markdown, or canonical wiki pages. The memoir evidence is useful but must remain staged until conversion/page-boundary QA reconciles or explicitly documents the citation discrepancy. No kinship relationship is stated in the chunk."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This task reviewed the existing staged extraction for `CHUNK-a048d567968b-P0001-03` in response to proof-review revision requests. The requested `$genealogy-claim-extraction` skill was not available as a local `SKILL.md`, so this note follows the extraction contract embedded in the assignment.

## Existing Staging Reviewed

- Source packet: `research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md`.
- Atomic claim drafts: `research/_staging/claims/chunk-a048d567968b-p0001-03-001-dario-pulgar-chilean-descriptor.md` through `research/_staging/claims/chunk-a048d567968b-p0001-03-006-dario-pulgar-vision-habitat-distribution-rights.md`.
- Negative relationship note: `research/_staging/relationships/chunk-a048d567968b-p0001-03-no-family-relationship-stated.md`.
- Identity/conflict and QA follow-up materials: `research/_staging/identities/chunk-a048d567968b-p0001-03-dario-pulgar-identity-candidate.md`, `research/_staging/conflicts/chunk-a048d567968b-p0001-03-page-boundary-and-biographical-qa.md`, and `research/_staging/research-tasks/chunk-a048d567968b-p0001-03-conversion-qa-page-boundary.md`.

## Evidence Status

The current staged packet and claims already preserve the disagreement requested by proof review. They document that the controller and manifest assign the chunk to page 1, while the chunk body contains embedded converted page metadata and family-relevant Dario Pulgar support from later printed/source pages. Prior staged notes report visual support on `page-0007.jpg` for the Dario full-name/Chile-film-distribution/fleeing-1973 passage and on `page-0008.jpg` for the mother-tongue, English/French, and Vision Habitat role passages; both rendered image files are present in this checkout.

## Recommendation

Keep all promotable Dario Pulgar claims from this chunk on `promotion_recommendation: hold_for_conversion_qa`. The blocking issue is no longer framed as missing staged extraction, but as unresolved conversion/page-boundary QA and authoritative citation selection. The relationship note remains `do_not_promote` because this chunk gives no parent, spouse, child, sibling, or other kinship relationship for Dario Pulgar.
