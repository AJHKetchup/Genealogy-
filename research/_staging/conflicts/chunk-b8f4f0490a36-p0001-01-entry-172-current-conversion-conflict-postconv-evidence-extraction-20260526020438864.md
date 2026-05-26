---
type: identity_conflict_candidate
status: draft
conflict_type: conversion_row_conflict
subject: "Entry 172 child and parents"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: high
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526020438864"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Conflict Candidate: Entry 172 Row-Level Conversion Conflict

## Competing Readings

- Assigned chunk reading: entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- Current converted Markdown reading: entry 172 names `Jose Miguel`, sex `Varon`, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

## Conversion Confidence And QA Concern

This is a material row-level conflict, not a spelling variant. It affects the child identity, birth date, birth place, father, mother, informant, and all downstream relationship candidates. The father-field reading also remains specifically unresolved for proof-review purposes.

## Uncertainty

The Pulgar/Arriagada row is high relevance because of the matched family terms, but no canonical identity, event, relationship, merge, or Dario-line bridge should be promoted until targeted conversion QA resolves the controlling row.

## Promotion Recommendation

`hold_for_conversion_qa`. QA should decide the controlling row and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`; then proof review should be rerun.
