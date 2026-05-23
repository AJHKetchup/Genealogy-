---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523224817011
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "controller and chunk manifest assign page 1; the Dario Pulgar support appears in embedded converted/printed page 7 and page 8 text within this chunk"
literal_support: "The chunk names Dario Pulgar, describes him as Chilean, says he had been the number two man in Chile's state film distribution system under Allende, says he fled after Pinochet's 1973 overthrow of the Allende government, states `His mother tongue was Spanish`, and says Dario worked primarily on distribution rights and off-shore printing materials."
conversion_confidence: medium
conversion_qa_concern: "Do not treat the page citation as resolved. In this checkout the referenced rendered images page-0007.jpg and page-0008.jpg exist, and prior staged notes report visual checks against them, but this task did not alter raw, converted, chunk, or page Markdown. The authoritative citation still conflicts between assigned page 1 and supporting printed/rendered pages 7-8."
uncertainty: "The claim wording is useful Dario Pulgar memoir evidence, but it is not promotion-ready because the derivative chunk/page boundary is inconsistent. The source states no kinship relationship."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision reviewed the staged extraction for `CHUNK-a048d567968b-P0001-03` under worker `postconv-evidence-extraction-20260523224817011`. No raw source, converted Markdown, chunk Markdown, page Markdown, or canonical wiki page was edited.

## Staged Evidence Status

The current staging set already contains the required person-first outputs for this chunk:

- Source packet: `research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md`.
- Atomic Dario Pulgar claim drafts `001` through `006` in `research/_staging/claims/`, each retained on `promotion_recommendation: hold_for_conversion_qa`.
- Negative relationship note: `research/_staging/relationships/chunk-a048d567968b-p0001-03-no-family-relationship-stated.md`, retained as `do_not_promote`.
- QA follow-up task: `research/_staging/research-tasks/chunk-a048d567968b-p0001-03-conversion-qa-page-boundary.md`.

## Evidence And Preserved Disagreement

The family-relevant evidence is limited to Dario Pulgar narrative context: Chilean descriptor, Chile state-film distribution work under Allende, displacement after the 1973 Pinochet overthrow, Spanish mother tongue and other language context, and Vision Habitat distribution-rights/off-shore-printing-materials work.

The staged claims and packet should remain held because the evidence layers still disagree. The controller assignment and chunk manifest identify this as page 1, while the chunk body embeds later converted page text and metadata. Prior staged notes report visual support on rendered/printed `page-0007.jpg` for the Dario full-name and Chile-film paragraph and `page-0008.jpg` for the mother-tongue and Vision Habitat role passages. Those image files are present in this checkout, but their presence does not itself reconcile the authoritative page reference.

## Relationship Scope

No family relationship is stated in this chunk. Do not create or promote parent, spouse, child, sibling, grandchild, or other kinship claims from this source passage. Any later attachment to `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or other Pulgar clusters requires separate identity review.

## Recommendation

Keep the source packet and all promotable Dario Pulgar claims from this chunk on `hold_for_conversion_qa` until conversion QA corrects or explicitly documents the page boundary and canonical citation target. The negative relationship note remains `do_not_promote`.
