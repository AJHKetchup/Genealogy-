---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260531084403223
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
page_image_checked: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531084403223.md
literal_support: Assigned chunk presents 1979-1970 work-history text; conversion-job page-markdown/page-0005.md presents competing 1999-1997 consulting text.
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Page 5 Still Blocked

The proof-review revision request cannot be resolved by evidence extraction alone. The assigned chunk and the conversion job page Markdown disagree about the contents of page 5.

## Assigned Chunk Candidate

The assigned chunk begins with `1979 - 1982` and lists the United Nations Centre for Human Settlements (HABITAT), Nairobi, Kenya, followed by National Film Board of Canada, Chile Films, and CITELCO entries. It ends at the `EDUCATION` heading.

## Conversion-Job Page Candidate

`page-markdown/page-0005.md` begins with `1999` and lists National Trust Fund for Protected Areas in Peru (PROFONANPE), Television Trust for the Environment (TVE), Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture. It ends mid-sentence after `a study tour`.

## Current Blockers

- Source PDF access is absent in this checkout: `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- Rendered page image access is absent in this checkout: `page-images/page-0005.jpg`.
- The chunk manifest contains duplicate `CHUNK-fb0a0000636f-P0005-01` records with conflicting character counts and SHA-256 values.
- The observed converted file hash and chunk hash do not match the recorded metadata.
- The controller contract bars this worker from source preparation or conversion repair.

## Required Next Action

Restore or regenerate authoritative access to physical page 5 through the controlled conversion workflow, reconcile `page-markdown/page-0005.md`, the aggregate converted Markdown, the assigned chunk, and the duplicate manifest entries, then rerun proof review only on certified page-5 text. Keep all page-5 work-history claims and identity attachment claims on `hold_for_conversion_qa`.

