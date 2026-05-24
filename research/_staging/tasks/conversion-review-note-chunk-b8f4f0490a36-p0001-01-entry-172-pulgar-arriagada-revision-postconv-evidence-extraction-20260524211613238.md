---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524211613238
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524211613238.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Pulgar/Arriagada Conflict

This evidence-extraction revision preserves the disagreement between the source-image/assigned-chunk evidence and the assigned converted Markdown.

## Source-Image And Chunk Reading

The assigned chunk and current source image support entry 172 on register page 58 as the Pulgar/Arriagada row:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father: broad reading `Jose del Carmen Pulgar`; final suffix unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

## Converted Markdown Conflict

The assigned converted Markdown transcribes entry 172 as a different birth:

- Child: `José Miguel`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Birth date/time: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birthplace: `En esta`.

This is a material row-level conflict. Do not resolve it in canonical claims from evidence extraction alone.

## Required Follow-Up

Targeted conversion QA should reconcile or supersede the assigned converted Markdown against the source image and chunk. The QA note should explicitly decide the controlling row and record the father field as one of:

- `Jose del Carmen Pulgar`
- `Jose del Carmen Pulgar S.`
- `Jose del Carmen Pulgar [?]`

After conversion QA, rerun proof review for the child identity, birth facts, child-mother relationship, child-father relationship, and parent-pair clue before any canonical promotion or merge.
