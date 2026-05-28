---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528045502562"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
confidence: 0.82
conversion_confidence: "image_reviewed_row_control_with_converted_markdown_conflict"
promotion_recommendation: "promote_after_review"
---

# Conversion Review Note: Entry 172 Row Control

The original page image controls this revision. On register page 58, the physical row numbered `172` is the Pulgar/Arriagada row. It is not the Burgos/de la Cruz row found in the current converted Markdown.

## Certified Row

Image review of the row numbered `172` supports:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`; no terminal suffix is certified from the image.
- Mother: `Juana Arriagada de Pulgar`.
- Parent domicile: `Calle de Colipi`.
- Compareciente: `Ernesto Herrera L.`, present at the birth, age 26, empleado, domiciled at Calle de Valdivia.

## Conversion Conflict

The current converted Markdown records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. That derivative transcript is materially inconsistent with the physical row numbered `172` in the original image and appears stale, row-shifted, or derived from a different image/page.

## Father-Field Boundary

The assigned chunk records `Jose del Carmen Pulgar S.`, but the image does not certify a terminal suffix after `Pulgar` clearly enough for promotion. Claims and relationships from this source should use only `Jose del Carmen Pulgar` unless a later proof review certifies the suffix.

## Promotion Guidance

This note resolves the row-control question for this extraction draft while preserving the derivative-transcript conflict. Claims may proceed to proof review with `promotion_recommendation: promote_after_review` only if they use the image-controlled Pulgar/Arriagada row and keep the father field limited to `Jose del Carmen Pulgar`.
