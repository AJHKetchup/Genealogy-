---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0004-01
worker: postconv-evidence-extraction-20260527144006439
created_at: 2026-05-27T14:41:15Z
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0004-01
current_chunk_sha256: c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_reference: page 4
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md
conversion_confidence: low_for_page_control
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Hold: Proof-Review Revision

## Control Problem

The assigned derivative chunk currently preserves work-history text for 1988-1989 FAO in Ndola, 1988 CIDA in Ethiopia, 1986-1987 WIF in Rome with project countries, and 1982-1985 independent communications consulting. These entries are potentially useful for the Dario Arturo Pulgar family narrative, but they remain blocked as page-4 evidence.

Proof-review notes report that the physical page-4 image/control evidence shows different page content: 2000 IBRD work in Bolivia/Peru and 1999-2000 Antamina work in Huarmey, Peru. The converted file and chunk state also preserve multiple page bodies in the same page-range derivative, so the disagreement should be kept visible until source-prep QA resolves it.

The manifest lists `CHUNK-fb0a0000636f-P0004-01` twice for the same page/path with differing values:

| manifest chunk_number | chars | sha256 |
|---:|---:|---|
| 1 | 4572 | `5e6aed90f2420572473987255df4bbec4de8750bd2f9701a9b71b2896f27a43f` |
| 4 | 3985 | `504f69374f1d289f20e70388a7653b8f8673e10ae649490cb6df74fe04fc3112` |

The current on-disk chunk hash observed during this revision is `c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15`, which matches neither manifest entry.

## Staged Evidence Status

- Source packet refreshed and held: `research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md`.
- Atomic claims refreshed and held: `research/_staging/claims/chunk-fb0a0000636f-p0004-01-001` through `005`.
- Relationship note refreshed as negative kinship evidence only: `research/_staging/relationships/chunk-fb0a0000636f-p0004-01-no-family-relationship-stated.md`.

No canonical claim, relationship, identity merge, or wiki update should be made from this chunk until targeted source-prep/conversion QA determines which physical page controls the 1982-1989 text and affected staged evidence is regenerated or proof-reviewed through the normal workflow.
