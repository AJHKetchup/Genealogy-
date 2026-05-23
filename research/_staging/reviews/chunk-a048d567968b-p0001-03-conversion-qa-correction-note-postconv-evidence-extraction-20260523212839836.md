---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523212839836
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned chunk page 1; derivative text embeds converted page metadata for pages 8-10 and visually reviewed Dario Pulgar support is on rendered/printed pages 7-8"
literal_support: "The chunk text includes `A couple of my UN Habitat Secretariat confreres stayed on, notably Dario Pulgar`, `Dario had been the number two man in Chile's state film distribution system`, `His mother tongue was Spanish`, and `Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.`"
conversion_confidence: medium-high
conversion_qa_concern: "The image files page-0007.jpg and page-0008.jpg are present in this checkout and prior staged revisions report visual support for the family-relevant Dario Pulgar passages. This pass did not alter raw, converted, chunk, or page Markdown. The unresolved blocker remains authoritative citation/page-boundary reconciliation: the controller and chunk manifest assign page 1 while the supported evidence belongs to printed/source pages 7-8."
uncertainty: "The source is a 2006 memoir-style account rather than a contemporary official employment, language, or migration record. No kinship relationship is stated in this chunk."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision leaves the existing Dario Pulgar source packet, atomic claim drafts, and negative relationship note in staging. They already contain the required source paths, converted-file references, chunk references, literal support, conversion-confidence notes, uncertainty, and `hold_for_conversion_qa` recommendations.

## Family-Relevant Evidence

The chunk supports biographical context for Dario Pulgar: he stayed on with the UN Habitat Secretariat group, was described as Chilean, had held a senior role in Chile's state film distribution system under Allende while still in his twenties, had fled after Pinochet's 1973 overthrow of the Allende government, had Spanish as his mother tongue, was fluent in English, had learned French in Montreal, and worked on Vision Habitat distribution rights and off-shore printing materials.

No parent-child, spouse, sibling, or other family relationship is stated in this chunk. Broad institutional details about Vision Habitat and UNCHS should remain contextual only when tied directly to Dario Pulgar's work narrative.

## Conversion QA Status

The derivative layers still disagree. The controller assignment and chunk manifest identify `page_start: 1` / `page_end: 1`, while the relevant source support is reported in the chunk body and staged revisions as printed/source pages 7 and 8. Earlier proof review also identified that the mother-tongue claim could not be promoted until `page-0008.jpg` was restored or regenerated; subsequent staged revisions record that `page-0008.jpg` is now present and visually supports the sentence `His mother tongue was Spanish`.

This note does not resolve the authoritative page-reference problem because this task is not authorized to edit raw sources, converted Markdown, chunks, or conversion job page Markdown. The disagreement should be preserved for conversion QA rather than hidden in claim promotion.

## Recommendation

Keep all Dario Pulgar claims from `CHUNK-a048d567968b-P0001-03` on `hold_for_conversion_qa`. After conversion QA corrects or explicitly documents the page/chunk boundary issue, the existing claim drafts can be reconsidered for proof review as memoir-attributed contextual claims.
