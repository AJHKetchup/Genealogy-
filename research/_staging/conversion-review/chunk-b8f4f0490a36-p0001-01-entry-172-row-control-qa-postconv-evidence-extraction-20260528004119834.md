---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528004119834"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "image_reviewed_row_control_with_converted_markdown_conflict"
conversion_qa_concern: "Current converted Markdown assigns entry 172 to a Burgos/de la Cruz row, while the original image and assigned chunk assign physical row 172 to the Pulgar/Arriagada birth registration. Father suffix after Pulgar is not certified."
uncertainty: "Low uncertainty for row control; moderate uncertainty for any terminal suffix after the father's surname."
promotion_recommendation: "promote_after_review"
created: "2026-05-28"
---

# Targeted Conversion QA: Entry 172 Row Control

## Scope

Reviewed the original page image, assigned chunk, chunk manifest, and current converted Markdown for `CHUNK-b8f4f0490a36-P0001-01`.

## Certification

The controlling physical row for entry `172` is the middle row on register page 58, left page of the image. The row number `172` aligns with the Pulgar/Arriagada registration, not the Burgos/de la Cruz registration in the current converted Markdown.

Image-reviewed row-control reading:

- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`
- Birth place: `Calle de Valdivia`
- Father: `Jose del Carmen Pulgar`
- Mother: `Juana Arriagada de Pulgar`
- Parent residence: `Calle de Colipi` / assigned chunk `Calle de Colipí`
- Compareciente: `Ernesto Herrera L.`, present at birth, age 26, employed, domiciled at `Calle de Valdivia`

## Father Field Boundary

Use only `Jose del Carmen Pulgar` for staged father-name claims and relationship candidates from this pass. The assigned chunk transcribes `Jose del Carmen Pulgar S.`, but direct image review does not certify the terminal `S.` clearly enough for promotion.

## Derivative Transcript Conflict

The current converted Markdown gives entry `172` as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at `En esta`. That is a material derivative-transcript conflict and should remain visible in proof review.

## Promotion Guidance

The row-control issue is sufficiently certified for proof review to evaluate the staged Pulgar/Arriagada claims. No canonical claim, relationship, identity merge, or wiki update should occur until proof review accepts this QA note and the limited father-field reading.
