---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528170150642"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
conversion_confidence: "image_reviewed_row_control"
conversion_qa_concern: "Current converted Markdown conflicts with the source image and assigned chunk by recording Burgos/de la Cruz for entry 172."
promotion_recommendation: promote_after_review
---

# Targeted Row-Control QA: Entry 172

Direct review of the original page image supports the middle row on register page 58 as physical entry `172`. That row is the Pulgar/Arriagada birth registration. It is not the Burgos/de la Cruz row recorded in the current converted Markdown.

Image-controlled row-level reading:

- Entry number: `172`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at about `tres de la tarde`
- Birth place: `Calle de Valdivia`
- Father: `Jose del Carmen Pulgar`
- Mother: `Juana Arriagada de Pulgar`
- Parents' residence: `Calle de Colipi`
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at `Calle de Valdivia`

The father field is certified only as `Jose del Carmen Pulgar`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the trailing suffix or mark after `Pulgar` is not visibly certified here and should not be promoted from this extraction.

The current converted Markdown is materially inconsistent because it records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and birth on 6 April 1888. Preserve that text as a derivative conversion conflict. Do not merge it into the Pulgar/Arriagada family evidence.

Staged evidence may proceed to proof review using the image-controlled Pulgar/Arriagada row. No canonical claim, relationship, identity merge, parent merge, Dario-line attachment, or wiki update should occur until proof review accepts this QA note.
