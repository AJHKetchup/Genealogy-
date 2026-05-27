---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527181213154"
subject: "Entry 172 row-control conflict after proof-review revision"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-proof-review-revision-postconv-evidence-extraction-20260527181213154.md"
conversion_confidence: "blocked_without_local_image_recapture"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row-Control Hold

The assigned chunk and the current converted Markdown remain in direct conflict.

- Assigned chunk: entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- Current converted Markdown: entry `172` is `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Prior staged image-reviewed QA notes, especially `research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527151217239.md`, report that the physical row numbered `172` controls as Pulgar/Arriagada and that the father field should be preserved only as visible `Jose del Carmen Pulgar` unless the suffix is separately certified.

This worker could not independently recertify the image because `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` and a job `page-images/page-0001.png` derivative are absent from this checkout.

Recommendation: keep all revised source packets, atomic claims, and relationship candidates from this entry at `hold_for_conversion_qa`. Before promotion, proof review should either accept the existing image-reviewed QA note as sufficient row-control evidence or require a new image-openable QA pass.
