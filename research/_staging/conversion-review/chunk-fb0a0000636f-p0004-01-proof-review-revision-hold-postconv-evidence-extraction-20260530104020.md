---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0004-01
worker: postconv-evidence-extraction-20260530103924352
created_at: 2026-05-30T10:40:20Z
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_current: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
converted_sha256_recorded_in_chunk: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0004-01
current_chunk_sha256: c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15
manifest_chunk_sha256_values: 5e6aed90f2420572473987255df4bbec4de8750bd2f9701a9b71b2896f27a43f; 504f69374f1d289f20e70388a7653b8f8673e10ae649490cb6df74fe04fc3112
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_reference: page 4
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md
conversion_confidence: low_for_page_control
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Hold: Page-Control Revision

The derivative chunk assigned to `CHUNK-fb0a0000636f-P0004-01` currently contains potentially family-relevant CV work-history text for Dario Arturo Pulgar: FAO in Ndola in 1988-1989, CIDA in Ethiopia in 1988, WIF in Rome in 1986-1987 with project countries, and independent communications consulting connected with CIDA in 1982-1985.

Those claims remain held. Prior proof review records a material page-control disagreement: image-reviewed page-4 control evidence was reported as 2000 IBRD / Bolivia and Peru text plus 1999-2000 Antamina / Huarmey, Peru text, while the current derivative chunk preserves 1982-1989 text. This extraction task did not run source preparation or document conversion and did not edit raw, converted, chunk, or page Markdown.

The manifest still lists `CHUNK-fb0a0000636f-P0004-01` twice for the same path and page with different character counts and hashes:

| manifest chunk_number | chars | sha256 |
|---:|---:|---|
| 1 | 4572 | `5e6aed90f2420572473987255df4bbec4de8750bd2f9701a9b71b2896f27a43f` |
| 4 | 3985 | `504f69374f1d289f20e70388a7653b8f8673e10ae649490cb6df74fe04fc3112` |

The current on-disk chunk hash observed in this revision is `c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15`, which matches neither manifest entry. The current converted Markdown hash is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`, while the chunk front matter records `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`. The expected page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg` was not present when checked.

## Staged Evidence Status

- Refreshed source packet remains held: `research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md`.
- Refreshed atomic claim drafts remain held: `research/_staging/claims/chunk-fb0a0000636f-p0004-01-001` through `005`.
- Refreshed relationship note remains negative kinship evidence only: `research/_staging/relationships/chunk-fb0a0000636f-p0004-01-no-family-relationship-stated.md`.
- Refreshed research task asks for targeted source-prep/conversion QA before proof review: `research/_staging/research-tasks/chunk-fb0a0000636f-p0004-01-proof-review-cv-work-history.md`.

No canonical claim, relationship, identity merge, or wiki page update should be made from this chunk until targeted source-prep/conversion QA reconciles the duplicate manifest entries, restores or regenerates page-4 image control, determines which physical page contains the 1982-1989 text, and affected staged evidence is proof-reviewed through the normal workflow.
