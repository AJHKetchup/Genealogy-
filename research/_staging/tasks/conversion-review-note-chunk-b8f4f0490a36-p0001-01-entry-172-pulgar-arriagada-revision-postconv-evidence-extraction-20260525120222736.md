---
type: research_task
status: draft
task_type: conversion_qa_followup
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260525120222736
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525120222736.md"
priority: high
promotion_recommendation: hold_for_conversion_qa
---

# Research Task: Targeted Conversion QA For Entry 172

Run targeted conversion QA against the source image, assigned converted Markdown, current chunk, and revised source packet for register page 58, entry 172.

The current chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born `Ocho de Marzo de mil ochocientos ochenta i ocho` at `Calle de Valdivia`.

The assigned converted Markdown records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born `El veinte i seis de Marzo de mil ochocientos ochenta i ocho` at `En esta`.

Required QA decisions:

- Decide whether the controlling source row for entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row, or whether one derivative is misassigned and must be superseded.
- Preserve source-visible spellings for the child, parents, place, residence, and informant.
- Explicitly record whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- After QA, rerun proof review for child identity, birth claims, father and mother claims, parent-child relationships, and any parent-candidate merge or Dario-line comparison.

Until that QA result exists, keep all dependent staged claims and relationships at `hold_for_conversion_qa`.
