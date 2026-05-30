---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0004-01
worker: postconv-evidence-extraction-20260530114926285
created_at: 2026-05-30T11:50:18Z
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

# Conversion Review Hold: Page-Control And Manifest Conflict

This revision keeps the staged evidence for `CHUNK-fb0a0000636f-P0004-01` on hold. The assigned chunk currently preserves derivative CV work-history entries for Dario Arturo Pulgar covering 1988-1989 FAO in Ndola, 1988 CIDA in Ethiopia, 1986-1987 Worldview International Foundation in Rome and project countries, and 1982-1985 independent communications consulting connected with CIDA.

The blocker remains unresolved. Prior proof review reports page-control disagreement between derivative transcript evidence for the 1982-1989 entries and image-reviewed page-4 evidence reported as 2000 IBRD / Bolivia and Peru plus 1999-2000 Antamina / Huarmey, Peru. This extraction pass did not perform source preparation, conversion, or image regeneration.

The chunk manifest still contains duplicate records for the same chunk id, path, and page:

| manifest chunk_number | chars | sha256 |
|---:|---:|---|
| 1 | 4572 | `5e6aed90f2420572473987255df4bbec4de8750bd2f9701a9b71b2896f27a43f` |
| 4 | 3985 | `504f69374f1d289f20e70388a7653b8f8673e10ae649490cb6df74fe04fc3112` |

The current on-disk chunk hash is `c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15`, which matches neither manifest record. The current converted Markdown hash is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`, while the chunk front matter records `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`. The expected page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg` is not present.

## Staged Evidence Status

- Source packet refreshed with current task metadata: `research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md`.
- Atomic claim drafts remain `promotion_recommendation: hold_for_conversion_qa`: `research/_staging/claims/chunk-fb0a0000636f-p0004-01-001` through `005`.
- Relationship candidate remains negative evidence only and `promotion_recommendation: do_not_promote`: `research/_staging/relationships/chunk-fb0a0000636f-p0004-01-no-family-relationship-stated.md`.
- Research task remains directed to targeted source-prep/conversion QA: `research/_staging/research-tasks/chunk-fb0a0000636f-p0004-01-proof-review-cv-work-history.md`.

Do not promote canonical claims, relationships, identity merges, or wiki updates from this chunk until source-prep/conversion QA reconciles the duplicate manifest entries, restores or regenerates page-4 image control, determines which physical page contains the 1982-1989 CV entries, refreshes affected staged evidence if necessary, and reruns proof review.
