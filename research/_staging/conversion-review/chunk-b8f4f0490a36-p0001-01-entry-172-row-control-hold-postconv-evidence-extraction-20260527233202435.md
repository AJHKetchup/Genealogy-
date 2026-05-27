---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527233106550"
subject: "Entry 172 row-control hold: Pulgar/Arriagada image row versus Burgos/de la Cruz converted text"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "image_reviewed_row_control_with_derivative_conflict"
conversion_qa_concern: "The original image and assigned chunk identify physical entry 172 as the Pulgar/Arriagada row; the current converted Markdown identifies entry 172 as a Burgos/de la Cruz row."
uncertainty: "Low for row control from the visible image; moderate for the trailing mark after the father's surname; high for canonical promotion until proof review accepts the reconciliation."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row Control

The original source image controls this extraction. On register page 58, physical row `172` is the Pulgar/Arriagada birth-registration row.

## Image-Reviewed Reading

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father field: certified only as `Jose del Carmen Pulgar`; a possible terminal suffix or mark after `Pulgar` is not certified here.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

## Derivative Conflict Preserved

The assigned chunk agrees with the Pulgar/Arriagada row but transcribes the father as `Jose del Carmen Pulgar S.`. This note does not certify the `S.` suffix.

The current converted Markdown instead records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. That text does not match the physical row numbered `172` in the source image for this task and should be treated as stale, row-shifted, or from a different page/image until proof review and conversion control resolve it.

Because proof review has not yet accepted this reconciliation, dependent staged claims and relationships remain held.
