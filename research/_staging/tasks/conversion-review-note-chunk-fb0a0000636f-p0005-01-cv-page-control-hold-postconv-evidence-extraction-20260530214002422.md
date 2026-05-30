---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530214002422
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded_in_chunk: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
page_reference: page 5
literal_support: Assigned chunk contains HABITAT/NFB/Chile Films/CITELCO work-history text; conversion job page-markdown/page-0005.md contains PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin text.
conversion_qa_concern: Rendered page image page-0005.jpg is absent locally, page Markdown disagrees with the assigned chunk, current hashes differ from recorded metadata, and the chunk manifest duplicates page-0005 with different hashes.
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: CHUNK-fb0a0000636f-P0005-01 Page-Control Hold

The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` contains work-history entries for HABITAT, National Film Board of Canada, Chile Films, and CITELCO. By contrast, `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` contains 1999/1998 entries for PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.

The current manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for the same chunk path, with different character counts and SHA-256 values. The observed converted-file hash during this revision is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`, not the recorded `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`. The observed chunk hash is `d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d`, which matches neither page-5 manifest row.

The expected rendered page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` was not present. Only `page-markdown/page-0005.md`, `page-markdown/page-0005.visuals.json`, and `work-orders/page-0005.md` were found for page 5.

No claims from this chunk should be promoted until conversion QA restores or re-renders the authoritative page image, reconciles the page Markdown/aggregate converted file/chunk manifest, and selects the controlling page-5 transcript. If the HABITAT/NFB/Chile Films/CITELCO transcript survives QA, a separate identity-bridge review should decide whether document-level `Dario Arturo Pulgar` can be attached to canonical `Dario Arturo Pulgar-Smith`.
