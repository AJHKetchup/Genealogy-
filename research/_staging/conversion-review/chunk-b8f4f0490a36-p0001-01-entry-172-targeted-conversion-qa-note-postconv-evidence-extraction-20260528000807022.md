---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528000807022"
subject: "Entry 172 row-control QA: Pulgar/Arriagada row controls the source image"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "image_reviewed_derivative_conflict"
promotion_recommendation: "promote_after_review"
---

# Targeted Conversion QA Note: Entry 172

Direct review of the original page image shows that physical row `172` on register page 58 is the Pulgar/Arriagada row. It is not the Burgos/de la Cruz row currently recorded for entry `172` in the converted Markdown.

Image-controlled row reading:

- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`; no trailing suffix is certified for promotion.
- Father details: Chilean, employed, domiciled at `Calle de Colipí`.
- Mother: `Juana Arriagada de Pulgar`.
- Mother details: Chilean, occupation `Su sexo`, domiciled at `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, domiciled at `Calle de Valdivia`.

The assigned chunk agrees with the image-controlled Pulgar/Arriagada row, except that it transcribes the father field as `Jose del Carmen Pulgar S.`. This QA note preserves the father only to the visible/certified level: `Jose del Carmen Pulgar`.

The current converted Markdown is materially inconsistent with both the source image and assigned chunk. It gives entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. Treat that converted Markdown reading as stale, row-shifted, or sourced from another page/image until conversion control corrects or supersedes it.

Promotion path: the image-controlled Pulgar/Arriagada evidence may proceed to proof review. No canonical claim, relationship, identity merge, Dario-line attachment, or wiki update should be made before proof review accepts this row-control QA and the limited father reading.
