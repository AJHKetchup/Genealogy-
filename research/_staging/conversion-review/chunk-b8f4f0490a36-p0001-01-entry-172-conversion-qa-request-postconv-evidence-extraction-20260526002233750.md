---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260526002233750"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002233750.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Request: Entry 172

The assigned converted Markdown and assigned chunk disagree at row level.

- Current converted Markdown entry 172: child `Jose Miguel`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; birth `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Assigned chunk and image-visible entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`; father begins `Jose del Carmen Pulgar` and is read by the chunk as `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; birth `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`; informant `Ernesto Herrera L.`

Requested QA result:

1. Identify the controlling row for entry 172.
2. Explain why the current converted Markdown records a Burgos/de la Cruz row while the chunk and source image support a Pulgar/Arriagada row.
3. Certify the father field exactly as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Preserve source-visible spellings for names, dates, residences, and informant fields.

Until this QA exists and proof review is rerun, keep dependent claims, relationship candidates, identity merges, parent candidates, and Dario-line comparisons at `hold_for_conversion_qa`.
