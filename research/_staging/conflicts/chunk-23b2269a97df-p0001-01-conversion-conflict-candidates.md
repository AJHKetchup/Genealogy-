---
type: conflict_candidate
status: draft
task_id: evidence-extraction:CHUNK-23b2269a97df-P0001-01
conflict_type: conversion_vs_source_image
source_packet: "research/_staging/source-packets/chunk-23b2269a97df-p0001-01-entry-172-pulgar-arriagada.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md"
chunk_id: CHUNK-23b2269a97df-P0001-01
page_reference: "image page 1; register page 58; entry 172"
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Conflict Candidate: Entry 172 Conversion Mismatch

- Literal support from image: entry 172 reads `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- Literal support from converted/chunk text: entry 172 is transcribed as `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- Conversion confidence/QA concern: this is a material derivative-transcript conflict for the same source image, page, and entry number. It should be resolved by conversion QA before relying on the converted Markdown as a source transcript.
- Uncertainty: Low that the source image visible in the workspace shows the Pulgar/Arriagada entry; high for the current converted text as evidence for entry 172.
- Promotion recommendation: hold_for_conversion_qa. Do not promote the Burgos/de la Cruz entry 172 claims from this converted text.

## Secondary QA Notes

- Father exact name form: image appears to read `Jose del Carmen Pulgar`, but prior derivative material has included a possible suffix; hold exact father-name and father-relationship promotion.
- Informant exact name: image appears to read `Oswaldo Arriagada`; hold informant identity until a targeted crop confirms the name.
- Source path encoding: task JSON contains mojibake in the path, but the source SHA-256 is stable.
