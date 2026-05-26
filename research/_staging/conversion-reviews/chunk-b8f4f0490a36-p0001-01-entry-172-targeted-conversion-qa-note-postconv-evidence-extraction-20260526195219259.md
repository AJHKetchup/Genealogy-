---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260526195219259"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: promote_after_review
---

# Targeted Conversion QA Note: Entry 172

## QA Scope

Reviewed the original page image, assigned chunk, current converted Markdown, and existing staged conflict context for page 58 entry 172.

## Controlling Row

The physical row controlling entry `172` is the middle row on register page 58. It is the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the current converted Markdown.

Visible row-level reading:

- Entry number: `172`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`
- Birth place: `Calle de Valdivia`
- Father field: `Jose del Carmen Pulgar`
- Mother field: `Juana Arriagada de Pulgar`
- Informant: `Ernesto Herrera L.`, present at the birth

## Father Field Certification

The father field is certified only to the visible reading `Jose del Carmen Pulgar`. Any trailing mark or possible abbreviation after `Pulgar` is not clear enough in the image to certify as `S.`.

## Derivative Transcript Conflict

The assigned chunk matches the image-reviewed Pulgar/Arriagada row, except that the chunk expands the father field to `Jose del Carmen Pulgar S.`. The current converted Markdown is materially mismatched for this source because it gives entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, with surrounding entries also differing from the page image.

## Promotion Guidance

Use the image-reviewed row for staged evidence drafts and preserve the converted-Markdown conflict in every dependent claim or relationship candidate. Dependent drafts may proceed to proof review with `promotion_recommendation: promote_after_review`, but no canonical claim, relationship, identity merge, or wiki update should be promoted until proof review accepts this QA resolution.
