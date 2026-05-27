---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0004-01
worker: postconv-evidence-extraction-20260527120509718
created_at: 2026-05-27T12:06:16Z
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0004-01
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_reference: page 4
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md
conversion_confidence: low_for_page_control
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Hold: CHUNK-fb0a0000636f-P0004-01

## Reason For Hold

The staged derivative evidence for this chunk preserves 1982-1989 CV work-history text, including FAO in Ndola, CIDA in Ethiopia, WIF in Rome, WIF project countries, and independent communications consulting for CIDA-related work. The current converted page 4 instead contains continuation text for consulting categories, then `2000 / International Bank for Reconstruction and Development (IBRD) / Bolivia, Peru / Senior Consultant` and `1999 - 2000 / Antamina Mining Company / Huarmey, Peru / Head Community Relations`.

The chunk manifest lists `CHUNK-fb0a0000636f-P0004-01` twice for the same page/path with different `chars` and `sha256` values. This prevents the derivative 1982-1989 text from being treated as confirmed page-4 evidence.

## Evidence Preserved

- Referenced chunk path: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md`
- Converted page text reviewed: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`, page 4
- Staged source packet held: `research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md`
- Staged claims held: `research/_staging/claims/chunk-fb0a0000636f-p0004-01-001` through `005`

## Required QA

Run targeted source-prep/conversion QA to reconcile the duplicate manifest entries, the current chunk file, and the physical page image. Determine which physical page controls the 1982-1989 entries. After page control is corrected through the normal workflow, regenerate or update affected source packets and claims, then rerun proof review before any canonical promotion.
