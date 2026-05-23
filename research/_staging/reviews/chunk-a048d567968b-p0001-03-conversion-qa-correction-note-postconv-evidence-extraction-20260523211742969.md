---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523211742969
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "chunk manifest/frontmatter assign page 1; visually checked family-relevant support appears on rendered/printed page 7 and rendered/printed page 8"
literal_support: "page-0007.jpg: `A couple of my UN Habitat Secretariat confreres stayed on, notably Dario Pulgar... In Chile under Allende... Dario had been the number two man in Chile's state film distribution system...`; page-0008.jpg: `His mother tongue was Spanish...` and `Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.`"
conversion_confidence: medium-high
conversion_qa_concern: "This checkout contains page-images/page-0007.jpg and page-images/page-0008.jpg, and this worker visually checked both images. The earlier missing-page-0008 image blocker is not reproduced here. The unresolved blocker is authoritative page/chunk reconciliation because the controller-assigned chunk is page 1 while the Dario Pulgar evidence is on printed/source pages 7-8 and the chunk body continues into later converted pages."
uncertainty: "This note does not edit raw sources, converted Markdown, chunks, or page Markdown. It preserves the derivative-layer disagreement and keeps all related Dario Pulgar claims in staging until conversion QA documents or corrects the authoritative page reference."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision responds to proof-review follow-up for `CHUNK-a048d567968b-P0001-03`.

## Image And Transcript Check

The conversion job page-images directory currently contains:

- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg`
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg`

Visual review confirms that printed/rendered page 7 supports the Dario Pulgar full-name paragraph, Chilean descriptor, Chile state film-distribution role, and fleeing-after-1973 context. Visual review also confirms that printed/rendered page 8 supports the sentence `His mother tongue was Spanish` and the later statement that Dario was primarily occupied with acquiring distribution rights and locating off-shore printing materials.

The page-level Markdown files `page-0007.md` and `page-0008.md` agree with those image-reviewed readings for the family-relevant Dario Pulgar passages.

## Remaining Blocker

The proof-review blocker is narrowed but not cleared. The assigned chunk and chunk manifest still identify `page_start: 1` / `page_end: 1`, while the family-relevant support belongs to printed/source pages 7 and 8. This task is not authorized to edit raw sources, converted Markdown, chunk files, or conversion job page Markdown, so the citation/page-boundary disagreement remains unresolved.

## Staging Recommendation

Keep the Dario Pulgar source packet, claim drafts, identity candidate, and related research task on `hold_for_conversion_qa`. The occupation/role and language claims are textually and visually supported as memoir evidence, but they should not be promoted until conversion QA either regenerates the chunk/page metadata or explicitly documents the authoritative citation as printed/source pages 7-8 rather than assigned page 1.
