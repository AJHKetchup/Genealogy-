---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527222756266"
subject: "Entry 172 row-control QA: Pulgar/Arriagada row versus converted Burgos/de la Cruz text"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "image_reviewed_row_control_with_derivative_conflict"
promotion_recommendation: "promote_after_review"
---

# Targeted Conversion QA Note: Entry 172

Direct inspection of the original source image confirms that physical row `172` on register page 58 is the Pulgar/Arriagada birth-registration row. The Burgos/de la Cruz text currently in the converted Markdown does not match the source image for this task and should be treated as stale, row-shifted, or from a different page/image set until conversion control supersedes it.

## Certified Row-Control Reading

- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father field: visible and certified only as `Jose del Carmen Pulgar`; a trailing mark or suffix after `Pulgar` is not certified.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

## Derivative Conflict Preserved

The assigned chunk agrees with the Pulgar/Arriagada row, but transcribes the father as `Jose del Carmen Pulgar S.`. This QA note does not certify the suffix. The current converted Markdown instead assigns entry `172` to `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. That derivative text conflicts with the original image and is not used for the staged Pulgar/Arriagada claims below.

Canonical promotion still requires proof review, but the row-control blocker requested in the prior reviews is now answered for this task-owned extraction set.
