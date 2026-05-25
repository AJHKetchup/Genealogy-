---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260525233630497"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525233718526.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Request: Entry 172

The current converted Markdown and the assigned chunk disagree at the entry-172 row level.

- Current converted Markdown entry 172: child `Jose Miguel`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; birth `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`.
- Assigned chunk and source-image row 172: child `Jose del Carmen Segundo Pulgar Arriagada`; father `Jose del Carmen Pulgar S.` by chunk reading; mother `Juana Arriagada de Pulgar`; birth `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`; informant `Ernesto Herrera L.`.

Requested QA result:

- Identify the controlling row for entry 172.
- Explain why the current converted Markdown records a Burgos/de la Cruz row while the assigned chunk and source image support a Pulgar/Arriagada row.
- Certify the father field only to the extent visible, using one of: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Preserve source-visible spellings for names, dates, residences, occupations, and informant fields.

Until this QA exists and proof review is rerun, keep dependent claims, relationship candidates, identity merges, parent candidates, and Dario-line comparisons at `hold_for_conversion_qa`.
