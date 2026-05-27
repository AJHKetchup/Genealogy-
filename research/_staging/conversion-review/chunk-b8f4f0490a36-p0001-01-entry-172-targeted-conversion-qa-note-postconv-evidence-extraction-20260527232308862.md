---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527232308862"
subject: "Entry 172 row-control QA: Pulgar/Arriagada versus Burgos/de la Cruz"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "image_reviewed_row_control"
promotion_recommendation: "promote_after_review"
---

# Targeted Conversion QA Note: Entry 172

## QA Finding

The original page image controls this revision. Physical row `172` on register page 58 is the Pulgar/Arriagada row, not the Burgos/de la Cruz row found in the current converted Markdown.

Image-reviewed row `172` supports:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at Calle de Valdivia.

## Derivative Conflict

The assigned chunk agrees with the Pulgar/Arriagada row, except that it transcribes the father field as `Jose del Carmen Pulgar S.`. The current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born on 6 April 1888. That Burgos/de la Cruz text does not match the visible physical row numbered `172` in the source image and should be treated as stale, row-shifted, or derived from a different page/image until conversion-control resolves the derivative file.

## Father-Field Boundary

This QA note certifies the father field only as `Jose del Carmen Pulgar`. The terminal mark after `Pulgar` is not clear enough in this review to certify `S.` as part of the name. Do not promote a father-name suffix from this source without proof-review acceptance of a focused image reading.

## Promotion Boundary

This note does not revise raw sources, converted Markdown, chunks, or page Markdown. It resolves the row-control blocker for staged Pulgar/Arriagada evidence, but canonical use still requires proof review.
