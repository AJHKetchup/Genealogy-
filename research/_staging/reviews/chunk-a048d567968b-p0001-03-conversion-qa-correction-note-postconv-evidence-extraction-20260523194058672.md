---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523194058672
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; relevant Dario Pulgar support appears in derivative page Markdown for printed/source pages 7 and 8; rendered source images page-0007.jpg and page-0008.jpg are not present in this checkout"
literal_support: "page-0007.md states: `A couple of my UN Habitat Secretariat confreres stayed on, notably Dario Pulgar`; it also states that Dario was a Chilean, had been the number two man in Chile's state film distribution system under Allende, and fled after Pinochet's 1973 overthrow. page-0008.md states: `His mother tongue was Spanish`; it also states he was fluent in English, had learned French in Montreal, and was primarily occupied with acquiring distribution rights and locating off-shore printing materials."
conversion_confidence: medium
conversion_qa_concern: "The assigned chunk and conversion job page Markdown agree on the family-relevant Dario Pulgar wording, but this task cannot independently repeat the requested image verification because the conversion job has no page-images directory in the current checkout. The chunk manifest still assigns this chunk to page 1 while the relevant derivative page Markdown is for printed/source pages 7 and 8."
uncertainty: "This note does not resolve the proof-review blocker or authorize promotion. It preserves the disagreement between the assigned chunk page, derivative page transcripts, and previously reported image-reviewed evidence."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision reviewed the assigned chunk, chunk manifest, existing staged source packet, existing staged Dario Pulgar atomic claim drafts, the negative relationship note, and conversion job page Markdown for pages 7 and 8. No raw source, converted Markdown, chunk, or conversion page Markdown was edited.

## Current Evidence State

- `CHUNK-a048d567968b-P0001-03` remains assigned to page 1 in the chunk manifest.
- The chunk body contains embedded literal transcription and page metadata for later printed/source pages, including pages 7 and 8.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-markdown/page-0007.md` contains the full-name Dario Pulgar passage, Chilean descriptor, Chile state film-distribution role, and fleeing-after-1973 context.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-markdown/page-0008.md` contains the mother-tongue Spanish sentence, English/French language context, and Vision Habitat distribution-rights work.
- The conversion job directory currently contains `page-markdown`, `work-orders`, `manifest.json`, and `README.md`, but no `page-images` directory. The requested visual verification of rendered `page-0007.jpg` and `page-0008.jpg` therefore cannot be repeated by this worker.

## Staging Decision

The existing staged packet and claim drafts are appropriate to keep in staging with `promotion_recommendation: hold_for_conversion_qa`. The Dario claims have useful family narrative value, but they should not move to canonical pages until conversion QA restores or regenerates rendered page images and documents the authoritative citation/page reference.

No family relationship is stated in this chunk. The existing negative relationship candidate should remain `promotion_recommendation: do_not_promote`.

