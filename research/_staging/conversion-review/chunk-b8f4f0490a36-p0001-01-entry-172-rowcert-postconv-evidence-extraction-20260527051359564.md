---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527051359564"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "mixed_derivative_conflict_image_reviewed"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row Control

Targeted image review for this evidence-extraction pass confirms that physical row `172` on the left page/register page 58 controls this source packet. That row is the Pulgar/Arriagada birth registration, not the Burgos/de la Cruz registration currently present in the converted Markdown.

## Certified Visible Reading

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father field: visible and certifiable only as `Jose del Carmen Pulgar`; any terminal suffix or mark after `Pulgar` remains unresolved.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, resident at Calle de Valdivia.

## Derivative Conflict

The assigned chunk agrees with the Pulgar/Arriagada row, except that it renders the father field as `Jose del Carmen Pulgar S.`. The current converted Markdown instead assigns entry `172` to `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, with different dates and context. Treat the converted Markdown as stale, row-shifted, or sourced from another page/image until conversion-control reconciles it against the source image.

## Promotion Guidance

Hold all claims, relationships, identity analysis, Dario-line attachments, and wiki edits for this entry at `hold_for_conversion_qa`. Rerun proof review after conversion-control either supersedes the converted Markdown or explicitly accepts the image-reviewed row-control note.
