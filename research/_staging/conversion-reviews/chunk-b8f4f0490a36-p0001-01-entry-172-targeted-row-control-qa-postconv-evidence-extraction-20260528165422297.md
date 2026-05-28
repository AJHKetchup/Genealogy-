---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528165333500"
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

This note responds to proof-review requests to compare the original source image, assigned chunk, chunk manifest, current converted Markdown, and staged source evidence for entry `172`.

## Row-Control Certification

Direct review of the original page image supports the middle row on register page 58 as physical entry `172`. That row is the Pulgar/Arriagada birth registration. It is not the Burgos/de la Cruz row that appears in the current converted Markdown.

Image-controlled row-level reading:

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

## Father-Field Boundary

The father field is certified only as `Jose del Carmen Pulgar`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the trailing suffix or mark after `Pulgar` is not visually certified in this extraction pass. Dependent claims and relationships should not promote a terminal `S.` unless later proof review independently accepts that reading.

## Derivative Transcript Conflict

The assigned chunk matches the image-controlled Pulgar/Arriagada row for entry `172`, except that the father-name suffix remains too uncertain for promotion. The current converted Markdown is materially inconsistent with both the image and assigned chunk because it records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at `En esta`.

This is not a spelling variant. It is a row/page-content conflict in the derivative converted Markdown. Preserve the Burgos/de la Cruz text as a conversion conflict; do not merge it into the Pulgar/Arriagada family evidence.

## Promotion Guidance

Staged evidence may proceed to proof review using the image-controlled Pulgar/Arriagada row. No canonical claim, relationship, identity merge, parent merge, Dario-line attachment, or wiki update should occur until proof review accepts this QA note and determines how to handle the conflicting converted Markdown.
