---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260531000652338
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded_in_chunk: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
page_reference: page 5
literal_support: Assigned chunk and current aggregate converted file contain HABITAT/NFB/Chile Films/CITELCO work-history text; conversion job page-markdown/page-0005.md contains PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin consulting text.
conversion_qa_concern: Rendered page image page-0005.jpg is absent locally, page-markdown/page-0005.md disagrees with the assigned chunk/current aggregate converted file, current hashes differ from recorded metadata, and the chunk manifest duplicates page-0005 with different hashes.
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page-Control Conflict Remains

The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` and the current aggregate converted file both contain the 1979-1970 work-history sequence: HABITAT in Nairobi, National Film Board of Canada in Montreal, Chile Films in Santiago, and CITELCO in Santiago.

The conversion-job page Markdown for the same page, `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`, contains a different 1999-1997 consulting sequence: PROFONANPE in Peru, Television Trust for the Environment in London, Arca Consulting/European Commission in Lesotho, Klohn Crippen Consultants in Huaraz, and SNC Lavalin Agriculture in Maracaibo.

The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for the same chunk path, with different character counts and SHA-256 values. Current observed hashes are:

- converted file: `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`
- assigned chunk: `d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d`

Both observed hashes differ from the recorded converted SHA-256 in the assigned chunk, and the observed chunk hash matches neither page-5 manifest row. The expected image files `page-images/page-0005.jpg` and `extracted-images/page-0005.jpg` were absent locally. This evidence-extraction task did not run source preparation, document conversion, or external research.

No page-5 claim from either derivative transcription should be promoted until conversion QA restores or re-renders the authoritative physical page image, reconciles the page Markdown, aggregate converted file, and chunk manifest, and identifies the controlling page-5 transcript.
