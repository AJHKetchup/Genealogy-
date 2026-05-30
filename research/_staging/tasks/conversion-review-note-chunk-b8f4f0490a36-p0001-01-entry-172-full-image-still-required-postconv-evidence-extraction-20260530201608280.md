---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530201608280"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Full Image Still Required

The assigned chunk and current converted Markdown remain in conflict.

- Assigned chunk row `172`: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- Current converted Markdown row `172`: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- Available crop assets in `research/_staging/conversion-review-assets/` support the Pulgar/Arriagada parent and informant fields at crop level.
- The original full source PNG was not found in `raw/sources` or the conversion job directory during this extraction turn, so this worker cannot certify the physical row controlling entry `172`.

The father field should remain bounded to `Jose del Carmen Pulgar`; the trailing `S.` is not promotion-ready.

Required follow-up: make the original full source image for SHA `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2` available, then run targeted row-control QA comparing the full image, assigned chunk, current converted Markdown, and staged source packet. After QA, rerun proof review before any canonical claim, relationship, identity merge, Dario-line attachment, or wiki update.
