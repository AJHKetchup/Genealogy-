---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528233456153"
subject: "CHUNK-b8f4f0490a36-P0001-01 entry 172 targeted row-control QA"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "image_reviewed_row_control_with_converted_markdown_conflict"
conversion_qa_concern: "The assigned chunk and original image identify physical row 172 as the Pulgar/Arriagada row, while the current converted Markdown assigns entry 172 to a Burgos/de la Cruz row."
literal_support: "Physical row numbered 172 on register page 58 records Jose del Carmen Segundo Pulgar Arriagada, father Jose del Carmen Pulgar, mother Juana Arriagada de Pulgar, birth at Calle de Valdivia, and declarant Ernesto Herrera L."
uncertainty: "Father field is certified only through Jose del Carmen Pulgar. A possible trailing suffix or mark after Pulgar is not certified here."
promotion_recommendation: hold_for_conversion_qa
---

# Targeted Conversion QA: Entry 172 Row Control

The original page image controls this revision pass. On register page `58`, the physical row numbered `172` is the Pulgar/Arriagada row. It is not the Burgos/de la Cruz row currently assigned to entry `172` in the converted Markdown.

## Certified Row

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father field: certified only as `Jose del Carmen Pulgar`.
- Mother field: `Juana Arriagada de Pulgar`.
- Declarant: `Ernesto Herrera L.`, present at the birth, age twenty-six, employee, domiciled at `Calle de Valdivia`.

## Conversion Conflict

The current converted Markdown records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and birth on 6 April 1888. That derivative reading appears stale, row-shifted, or sourced from a different image/page relative to the assigned original source image. It does not control this source packet or the staged family claims for the Pulgar/Arriagada row.

## Father-Field Boundary

The image supports the father name through `Jose del Carmen Pulgar`. The assigned chunk's `Jose del Carmen Pulgar S.` is preserved as a derivative reading, but the terminal `S.` is not certified here. Staged claims and relationships use only `Jose del Carmen Pulgar`.
