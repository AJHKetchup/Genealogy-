---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527020704452"
subject: "Entry 172 row-control QA: Pulgar/Arriagada versus Burgos/de la Cruz"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "mixed_derivative_conflict_image_reviewed"
promotion_recommendation: "hold_for_conversion_qa"
---

# Targeted Conversion QA Note: Entry 172

## QA Finding

The physical row controlling entry `172` is the Pulgar/Arriagada row on register page 58, not the Burgos/de la Cruz row in the current converted Markdown.

Direct source-image review shows the row number `172` at the left margin of page 58. Reading across that row gives:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

## Derivative Conflict

The assigned chunk agrees with the Pulgar/Arriagada row, except that it transcribes the father as `Jose del Carmen Pulgar S.`. The current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born on 6 April 1888. That Burgos/de la Cruz text does not match the visible physical row numbered `172` in the source image for this task and should be treated as stale, row-shifted, or from a different page/image set until conversion-control resolves the derivative file.

## Father Field Boundary

This QA note certifies the father field only as `Jose del Carmen Pulgar`. The terminal mark after `Pulgar` is not clear enough in this review to certify `S.` as part of the name. Do not promote a father-name suffix from this source without a focused crop or proof-review acceptance.

## Promotion Boundary

This note does not revise raw sources, converted Markdown, chunks, or page Markdown. It supports proof review of staged Pulgar/Arriagada claims, but those claims should remain held while the derivative conversion conflict remains unresolved.
