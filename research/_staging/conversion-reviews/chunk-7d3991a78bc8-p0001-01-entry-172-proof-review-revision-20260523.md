---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-7d3991a78bc8-P0001-01
worker: postconv-evidence-extraction-20260523003053538
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md"
chunk_id: CHUNK-7d3991a78bc8-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/chunk-7d3991a78bc8-p0001-01-entry-172-image-reread-pulgar-arriagada.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Proof-Review Revision

The original source image was present at the expected Unicode path and was reread for register page 58, entry 172. The image supports the Pulgar/Arriagada reading preserved in prior staging, not the Bunster/de la Maza reading in the assigned converted derivative.

This note covers the proof-review revision requests for the staged birth-name, sex, birth date/time, birth place, child-father, child-mother, and child-parents drafts. The relationship drafts now preserve the image-supported Pulgar/Arriagada candidates and no longer assert the unsupported `Jose Miguel` to `Amelia de la Maza` or Bunster/de la Maza family links as promotable tree relationships.

## Image-Reviewed Reading

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`; a final suffix is not clearly visible.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at Calle de Valdivia.
- Official/signature: `Emilio Riquelme V.`

## Conversion QA Concern

The assigned chunk and converted file still read entry 172 as `José Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`, and official `Camilo Luis osorio`. This extraction revision does not edit raw converted Markdown or chunks. Keep the conversion-layer conflict visible until conversion QA corrects or retires the derivative transcript.

## Proof-Review Revision Coverage

- `research/_staging/claims/chunk-7d3991a78bc8-p0001-01-001-child-birth-name.md`: revised/kept as image-supported Pulgar/Arriagada evidence, `hold_for_conversion_qa`.
- `research/_staging/claims/chunk-7d3991a78bc8-p0001-01-002-child-sex.md`: revised/kept as image-supported `Hombre`, `hold_for_conversion_qa`.
- `research/_staging/claims/chunk-7d3991a78bc8-p0001-01-003-birth-date-time.md`: revised/kept as image-supported 8 March 1888 at 3 p.m., `hold_for_conversion_qa`.
- `research/_staging/claims/chunk-7d3991a78bc8-p0001-01-004-birth-place.md`: revised/kept as image-supported `Calle de Valdivia`, `hold_for_conversion_qa`.
- `research/_staging/relationships/chunk-7d3991a78bc8-p0001-01-001-child-father.md`: revised/kept as image-supported child-father candidate for `Jose del Carmen Segundo Pulgar Arriagada` and `Jose del Carmen Pulgar`, `hold_for_conversion_qa`.
- `research/_staging/relationships/chunk-7d3991a78bc8-p0001-01-002-child-mother.md`: revised so it no longer asserts the unsupported `Jose Miguel` to `Amelia de la Maza` relationship; staged as the image-supported Pulgar/Arriagada candidate, `hold_for_conversion_qa`.
- `research/_staging/relationships/chunk-7d3991a78bc8-p0001-01-003-child-parents.md`: revised so it no longer asserts the unsupported Bunster/de la Maza parent set; staged as the image-supported Pulgar/Arriagada parent set, `hold_for_conversion_qa`.

## Promotion Guidance

Use `hold_for_conversion_qa` for all entry-172 claims and relationship candidates from this chunk. The source image supports Pulgar/Arriagada, but the canonical promotion path should wait for conversion QA because the assigned derivative text remains materially wrong.
