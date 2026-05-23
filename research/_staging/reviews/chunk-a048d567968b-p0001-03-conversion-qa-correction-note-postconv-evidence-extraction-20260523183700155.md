---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523183700155
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; derivative page Markdown identifies support on printed/source pages 7 and 8; manifest lists rendered images page-0007.jpg and page-0008.jpg, but the page-images directory is absent in this checkout"
literal_support: "page-0007.md states: `A couple of my UN Habitat Secretariat confreres stayed on, notably Dario Pulgar`; it also states Dario was Chilean, had been the number two man in Chile's state film distribution system under Allende, and fled after Pinochet's 1973 overthrow. page-0008.md states: `His mother tongue was Spanish`; it also states Dario was primarily occupied with acquiring distribution rights and determining where off-shore printing materials were."
conversion_confidence: medium
conversion_qa_concern: "The family-relevant Dario Pulgar text is consistent between the assigned chunk and page-markdown/page-0007.md plus page-markdown/page-0008.md. Independent visual verification cannot be repeated in this checkout because the conversion job has no page-images directory, despite prior staged notes reporting visual checks and the conversion manifest referencing page image paths. The authoritative citation also remains unresolved because the chunk manifest assigns this chunk to page 1 while the relevant derivative page Markdown is for pages 7 and 8."
uncertainty: "This note does not resolve the proof-review blocker. It preserves the disagreement between derivative transcripts/page references and the unavailable image-reviewed evidence. Claims from this chunk should remain staged until rendered images are restored or regenerated and the canonical page reference is documented."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker reviewed the assigned chunk, the chunk manifest, existing staged claim/source-packet outputs, and the conversion job page Markdown for pages 7 and 8. I did not edit raw sources, converted Markdown, chunks, page Markdown, or conversion job files.

## Evidence State

- The controller assigns `CHUNK-a048d567968b-P0001-03` to page 1.
- The chunk body includes later page metadata and literal transcription for printed/source pages 7, 8, 9, and 10.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-markdown/page-0007.md` contains the full-name Dario Pulgar paragraph and the Chile film-distribution/fleeing-1973 support.
- `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-markdown/page-0008.md` contains the mother-tongue Spanish sentence and the Vision Habitat distribution-rights support.
- The current checkout contains `page-markdown` and `work-orders`, but no `page-images` directory under the conversion job. Therefore the image checks requested by proof review cannot be independently repeated in this task.

## Staging Decision

Existing staged outputs already include a source packet, atomic Dario Pulgar claim drafts, a negative relationship note, identity/conflict candidates, and a research task for conversion QA. Their current `hold_for_conversion_qa` posture is still appropriate.

No canonical promotion is recommended from this chunk until conversion QA restores or regenerates the rendered page images and documents whether the authoritative page reference should be assigned page 1, printed/source pages 7-8, rendered image paths, or corrected chunk metadata.
