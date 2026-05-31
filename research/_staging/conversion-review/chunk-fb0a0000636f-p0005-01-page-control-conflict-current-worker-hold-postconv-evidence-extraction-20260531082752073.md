---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260531082659454
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256_recorded: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
source_available_locally: false
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded_in_chunk: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
page_image: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531082752073.md
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: CV Page 5 Page-Control Conflict

This current worker pass could not resolve page control because both the source PDF and rendered `page-0005.jpg` are unavailable locally. It records derivative disagreement only.

## Assigned Chunk Reading

The assigned chunk reads page 5 as a 1979-1970 work-history sequence:

- 1979-1982, United Nations Centre for Human Settlements (HABITAT), Nairobi, Development Support Communications Officer.
- 1974-1978, National Film Board of Canada, Montreal, Audio Visual Consultant.
- 1972-1973, Chile Films, Santiago, General Manager Distribution and Exhibition, Head of International Department.
- 1970-1972, Cine, Television y Comunicaciones (CITELCO), Santiago, Producer.

## Conversion-Job Page Markdown Reading

The available conversion-job page Markdown for `page-0005.md` reads page 5 as a different 1999-1997 sequence:

- 1999, National Trust Fund for Protected Areas in Peru (PROFONANPE), Peru, Consultant.
- Television Trust for the Environment (TVE), London, Consultant.
- 1998-1999, Arca Consulting/European Commission, Lesotho, Team Leader.
- 1997-1998, Klohn Crippen Consultants, Huaraz, Peru, Socio-economic Consultant.
- SNC Lavalin Agriculture, Maracaibo, Venezuela, Training Consultant.

## Current QA Finding

The manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with incompatible recorded character counts and chunk hashes. The observed converted-file hash and observed chunk hash also differ from recorded values. Because no authoritative physical page image or source PDF is available in this checkout, this pass cannot choose the controlling page-5 transcription.

## Required Next Action

Keep all source packets, claims, identity notes, and relationship notes from this page on hold. Conversion QA must restore or regenerate the source PDF/page image, compare physical page 5 against both derivative readings, repair manifest/hash drift through the conversion workflow, and only then rerun proof review. A separate identity-bridge review is required before attaching accepted CV claims to `Dario Arturo Pulgar-Smith` or merging with any Pulgar-Arriagada/Jose/Juana-linked identity.
