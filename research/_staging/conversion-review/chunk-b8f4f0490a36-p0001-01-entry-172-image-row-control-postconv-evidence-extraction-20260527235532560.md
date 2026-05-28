---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527235532560"
subject: "Entry 172 row-control correction: Pulgar/Arriagada row"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
conversion_confidence: "image_reviewed_row_control"
promotion_recommendation: "promote_after_review"
---

# Conversion Review Note: Entry 172 Row Control

## Finding

The original image controls entry `172`. On register page 58, the physical row numbered `172` is the Pulgar/Arriagada row. It is not the Burgos/de la Cruz row recorded in the current converted Markdown.

The image-reviewed row supports: child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`; birth `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; birthplace `Calle de Valdivia`; father visible as `Jose del Carmen Pulgar`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at birth, age 26, employed, resident at `Calle de Valdivia`.

## Derivative Conflict

The assigned chunk agrees with the image-controlled Pulgar/Arriagada row, but transcribes the father field as `Jose del Carmen Pulgar S.`. The current converted Markdown instead assigns entry `172` to `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. That converted-file reading should be treated as stale, row-shifted, or from a different page/image for this entry.

## Father-Field Boundary

This note certifies the father field only to the visible level `Jose del Carmen Pulgar`. The terminal mark after `Pulgar` is not clear enough here to promote `S.` as part of the name.

## Promotion Boundary

No raw source, converted Markdown, chunk, or page Markdown is revised by this note. Canonical use still requires proof review of these staged drafts.
