---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260526220522738"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: promote_after_review
---

# Targeted Conversion QA Note: Entry 172

## Scope

Reviewed the original page image, assigned chunk, current converted Markdown, and existing staged source-packet context for register page 58, entry 172. No raw source, converted Markdown, chunk, or page Markdown was edited.

## Controlling Row Certification

The physical row controlling entry `172` is the middle row on register page 58. It is the Pulgar/Arriagada row, not the Burgos/de la Cruz row currently recorded in the current converted Markdown.

Visible row-level reading:

- Entry number: `172`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`
- Birthplace: `Calle de Valdivia`
- Father field: `Jose del Carmen Pulgar`
- Mother field: `Juana Arriagada de Pulgar`
- Parents' residence: `Calle de Colipi`
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at `Calle de Valdivia`

## Father Field Certification

The father field is certified only to the visible reading `Jose del Carmen Pulgar`. The assigned chunk's trailing `S.` after `Pulgar` is not clear enough in the image to certify and should not be promoted.

## Derivative Transcript Conflict

The assigned chunk is aligned to the image-reviewed Pulgar/Arriagada row except for the father-name suffix. The current converted Markdown is materially mismatched for this source image because it records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888, and place `En esta`.

## Promotion Guidance

Use the image-reviewed row for staged evidence drafts, while preserving the converted-Markdown conflict in every dependent claim and relationship candidate. These staged drafts may proceed to proof review with `promotion_recommendation: promote_after_review`; no canonical claim, relationship, identity merge, parent merge, or wiki update should occur until proof review accepts this QA-controlled reading.
