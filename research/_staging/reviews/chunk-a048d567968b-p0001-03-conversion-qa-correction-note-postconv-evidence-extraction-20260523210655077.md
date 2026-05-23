---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523210655077
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; family-relevant Dario Pulgar passages appear in derivative converted/page-markdown text for printed/source pages 7 and 8"
literal_support: "Page 7 derivative text names Dario Pulgar, describes him as a Chilean colleague, says he had been the number two man in Chile's state film distribution system under Allende, and says he fled after Pinochet's 1973 overthrow. Page 8 derivative text says his mother tongue was Spanish, he was fluent in English, he had learned French in Montreal, and he worked on acquiring distribution rights and locating off-shore printing materials."
conversion_confidence: low-to-medium
conversion_qa_concern: "The chunk manifest assigns this chunk to page 1, but the chunk body embeds later page metadata and text. Page-markdown files for page-0007.md and page-0008.md contain the Dario Pulgar passages, and the conversion manifest lists rendered images page-images/page-0007.jpg and page-images/page-0008.jpg. In this checkout the page-images directory is absent, so this worker could not independently repeat image-level verification. Prior proof-review and correction notes reporting or requesting visual checks should be preserved as separate evidence-layer history, not overwritten."
uncertainty: "This note documents staging status only. It does not alter raw source text, converted Markdown, chunks, or page Markdown, and it does not resolve the authoritative page citation discrepancy."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision keeps the Dario Pulgar material in staging and preserves the disagreement between the derivative transcripts, prior image-review history, and current workspace image availability.

## Evidence Layer Check

- The assigned chunk is `CHUNK-a048d567968b-P0001-03`, with manifest page range 1-1.
- The chunk body contains embedded converted text and page metadata for printed/source pages 7-10.
- `page-markdown/page-0007.md` contains the Dario Pulgar full-name paragraph, including the Chilean descriptor, Allende-era film-distribution role, and flight after Pinochet's 1973 overthrow.
- `page-markdown/page-0008.md` contains the Dario first-name paragraph, including mother tongue Spanish, English/French language context, and Vision Habitat distribution-rights work.
- The conversion manifest lists `page-images/page-0007.jpg` and `page-images/page-0008.jpg`, but `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images` is absent in this checkout.

## Staging Decision

The existing source packet, six atomic Dario Pulgar claim drafts, and negative relationship note are appropriate staging outputs for this chunk. Their `promotion_recommendation` values should remain as currently staged: Dario Pulgar claim drafts on `hold_for_conversion_qa`, and the negative relationship note on `do_not_promote`.

Do not promote the Dario Pulgar claims until conversion QA restores or regenerates the rendered page images, verifies the page 7 and page 8 passages visually, and reconciles the page reference discrepancy between assigned page 1 and printed/source pages 7-8.
