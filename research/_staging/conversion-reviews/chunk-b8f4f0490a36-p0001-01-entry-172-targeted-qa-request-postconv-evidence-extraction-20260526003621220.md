---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260526003520985"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526003621220.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Targeted QA Request

## Finding

The assigned chunk supports a Pulgar/Arriagada row for register page 58, entry 172. The current converted Markdown supports a Burgos/de la Cruz row for entry 172. This is a material row-level conflict affecting identity, birth facts, and parent-child relationships.

## Chunk Row Needing Certification

- Entry number: 172
- Registration date: Siete de Abril de mil ochocientos ochenta i ocho
- Child: Jose del Carmen Segundo Pulgar Arriagada
- Sex: Hombre
- Birth: Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde
- Birthplace: Calle de Valdivia
- Father in assigned chunk: Jose del Carmen Pulgar S.
- Mother in assigned chunk: Juana Arriagada de Pulgar
- Informant: Ernesto Herrera L., present at birth

## Required QA Decision

QA should explicitly decide whether the controlling source row for entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row currently in the converted Markdown. If the Pulgar/Arriagada row controls, QA should certify the father field only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Promotion Guidance

Keep all dependent staged evidence on `hold_for_conversion_qa`. After QA, rerun proof review before any canonical child identity, birth fact, parent name, parent-child relationship, parent identity merge, or Pulgar/Arriagada line comparison is promoted.
