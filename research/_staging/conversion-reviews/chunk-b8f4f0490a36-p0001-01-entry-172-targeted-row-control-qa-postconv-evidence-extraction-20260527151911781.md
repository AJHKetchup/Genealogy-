---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527151911781"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "image_reviewed_row_control"
promotion_recommendation: promote_after_review
---

# Targeted Row-Control QA: Entry 172

## Scope

Reviewed the original source image, assigned chunk, chunk manifest, and current converted Markdown for `CHUNK-b8f4f0490a36-P0001-01`.

## Certification

The controlling physical row for entry `172` is the middle row on register page 58. The source image shows this row as the Pulgar/Arriagada birth registration, not the Burgos/de la Cruz entry found in the current converted Markdown.

Visible row-level reading:

- Entry number: `172`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`
- Birth place: `Calle de Valdivia`
- Father: `Jose del Carmen Pulgar`
- Mother: `Juana Arriagada de Pulgar`
- Parents' residence: `Calle de Colipi`
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at `Calle de Valdivia`

## Father Field Boundary

The image supports the father field as `Jose del Carmen Pulgar`. A trailing suffix or abbreviation after `Pulgar` is not certified for promotion in this extraction pass. Dependent drafts should not promote `Pulgar S.` unless a later proof review accepts that reading.

## Derivative Transcript Conflict

The assigned chunk matches the image-controlled Pulgar/Arriagada row except for the father-name suffix certainty. The current converted Markdown is materially inconsistent with the image and chunk because it records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at `En esta`.

## Promotion Guidance

Staged evidence may proceed to proof review using the image-controlled Pulgar/Arriagada row. No canonical claim, relationship, identity merge, parent merge, or wiki update should occur until proof review accepts this QA note and resolves how to supersede or correct the conflicting converted Markdown.
