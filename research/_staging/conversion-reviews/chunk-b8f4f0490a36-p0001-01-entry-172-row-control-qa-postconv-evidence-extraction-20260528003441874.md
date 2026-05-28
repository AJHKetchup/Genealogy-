---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528003441874"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "image_reviewed_row_control_with_converted_markdown_conflict"
promotion_recommendation: "promote_after_review"
---

# Targeted Row-Control QA: Entry 172

## Scope

Reviewed the original source image, assigned chunk, current converted Markdown, and chunk manifest for `CHUNK-b8f4f0490a36-P0001-01`.

## Row-Control Certification

The controlling physical row for entry `172` is the middle row on register page 58, left page of the image. The row number `172` aligns horizontally with the Pulgar/Arriagada birth registration. It is not the Burgos/de la Cruz entry found in the current converted Markdown.

Image-reviewed row reading:

- Entry number: `172`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`
- Birth place: `Calle de Valdivia`
- Father: `Jose del Carmen Pulgar`
- Mother: `Juana Arriagada de Pulgar`
- Parents' residence: `Calle de Colipi`
- Compareciente: `Ernesto Herrera L.`, present at the birth, age 26, employed, domiciled at `Calle de Valdivia`

## Father Field Boundary

The image and chunk support the father as `Jose del Carmen Pulgar`. The assigned chunk transcribes a possible terminal `S.` after `Pulgar`, but this QA note does not certify that suffix. Downstream staged claims and relationships should use only `Jose del Carmen Pulgar` unless later proof review accepts the suffix from direct image review.

## Derivative Transcript Conflict

The assigned chunk matches the image-controlled Pulgar/Arriagada row except for the father-suffix certainty. The current converted Markdown materially conflicts because it records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at `En esta`.

## Promotion Guidance

Proceed to proof review using the image-controlled Pulgar/Arriagada row and the limited father reading. No canonical claim, relationship, identity merge, parent merge, or wiki update should occur until proof review accepts this QA note and resolves the conflicting converted Markdown.
