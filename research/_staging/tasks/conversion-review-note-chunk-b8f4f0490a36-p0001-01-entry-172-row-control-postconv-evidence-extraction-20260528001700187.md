---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528001700187"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row numbered 172"
conversion_confidence: "targeted_image_review"
promotion_recommendation: "promote_after_review"
---

# Conversion Review Note: Entry 172 Row Control

The original image controls this targeted QA pass. On register page 58, the physical row numbered `172` is the Pulgar/Arriagada row. It is not the Burgos/de la Cruz row in the current converted Markdown.

## Certified Physical Row

Image review supports the following row-level readings for entry `172`:

- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth date/time/place: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`; Chilean; employed; domiciled at `Calle de Colipi`.
- Mother: `Juana Arriagada de Pulgar`; Chilean; occupation recorded as `Su sexo`; domiciled at `Calle de Colipi`.
- Compareciente: `Ernesto Herrera L.`; present at the birth; age 26; employed; domiciled at `Calle de Valdivia`.

## Derivative Conflict Preserved

The assigned chunk transcribes entry `172` as the Pulgar/Arriagada row. The current converted Markdown instead transcribes entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. That converted Markdown content is materially inconsistent with the original image for physical row `172` and appears stale, row-shifted, or derived from a different page image.

## Father-Field Boundary

The father field should be staged only as `Jose del Carmen Pulgar`. The assigned chunk includes a trailing `S.` after `Pulgar`, but the image does not make that suffix sufficiently certain for promotion. Do not stage or promote `Jose del Carmen Pulgar S.` as a certified name form from this record.

## Promotion Guidance

The conversion-QA blocker is resolved for row control but not for canonical promotion. Revised source packets, claims, and relationship candidates may proceed to proof review if they preserve this derivative conflict and limit the father name to `Jose del Carmen Pulgar`.
