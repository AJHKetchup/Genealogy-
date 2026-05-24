---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524044109549
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-jose-del-carmen-segundo-pulgar-arriagada.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Proof-Review Revision

The source image is present at the expected path and matches the manifest SHA-256. Direct visual review of register page 58, entry 172 supports the Pulgar/Arriagada row staged in the chunk, not the unrelated Bunster/de la Maza row in the assigned converted Markdown file.

This note does not edit raw sources, converted Markdown, chunks, or page Markdown. It records the disagreement that blocks canonical promotion.

## Image-Reviewed Reading

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`; no final `S.` is clear enough for promotion from this image reread.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at `Calle de Valdivia`.
- Official/signature: `Emilio Riquelme V.`

## Derivative Conflict

The assigned chunk transcribes entry 172 as the Pulgar/Arriagada row and includes the father as `Jose del Carmen Pulgar S.`. The assigned converted Markdown file transcribes entry 172 as `José Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`, with different birth details and event participants. The source image supports the Pulgar/Arriagada family row, but the father suffix still requires targeted conversion QA.

## Promotion Guidance

Keep the source packet, child birth facts, parent relationship candidates, parent attributes, informant note, and identity/conflict analyses at `hold_for_conversion_qa`. The next QA pass should correct or supersede the converted Markdown and explicitly decide whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form.
