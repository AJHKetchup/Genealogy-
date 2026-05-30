---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530153130162"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-held-postconv-evidence-extraction-20260530153130162.md"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
literal_support: "Assigned chunk row 172 gives the Pulgar/Arriagada birth row; current converted Markdown gives the Burgos/de la Cruz birth row; staged crop assets show Pulgar/Arriagada parent and informant fields but not the full physical row."
conversion_confidence: "blocked_full_source_image_absent_crop_supported_parent_fields"
conversion_qa_concern: "The original full page PNG is not available locally, so this pass cannot certify which physical row controls entry 172. The father suffix after Pulgar is not certified."
uncertainty: "Current converted Markdown may be stale, row-shifted, or derived from a different page/image. No canonical claims or relationships should be promoted from this pass."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Held Row Conflict

Targeted QA cannot be completed to promotion standard in this checkout because the full original PNG named by the manifest/source path is absent from `raw/sources`.

Available evidence:

- Assigned chunk: entry `172` is the Pulgar/Arriagada row.
- Current converted Markdown: entry `172` is the Burgos/de la Cruz row.
- Staged crop assets: support the Pulgar/Arriagada parent and informant fields at crop level, but do not certify the full physical row or entry number.

Held reading for downstream review: `Jose del Carmen Segundo Pulgar Arriagada`; father only as `Jose del Carmen Pulgar`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`

Required follow-up: restore or provide the original full source image, rerun targeted row-control QA against the image, assigned chunk, converted Markdown, and staged source packet, then rerun proof review before any promotion.
