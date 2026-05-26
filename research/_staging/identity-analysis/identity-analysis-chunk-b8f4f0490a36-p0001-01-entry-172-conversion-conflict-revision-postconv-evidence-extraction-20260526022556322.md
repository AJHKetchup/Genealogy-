---
type: identity_analysis
status: draft
analysis_type: conversion_conflict
subject: "Jose del Carmen Segundo Pulgar Arriagada"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526022556322.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: low
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526022456786"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Identity Analysis: Entry 172 Conversion Conflict

The assigned chunk presents entry 172 as a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, male, born 1888-03-08 at 3 p.m. on Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.

The current converted Markdown presents entry 172 as a different birth registration for `Jose Miguel`, male, born 1888-04-06 at 10 p.m., with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`.

These cannot both be the same controlling entry-172 transcription. This extraction therefore treats the Pulgar/Arriagada material as family-relevant staged evidence only, not as promotion-ready proof.

## Required QA

Targeted conversion QA must reconcile the source image, converted Markdown, chunk, and source packet; decide the controlling entry-172 row; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Recommendation

Keep all dependent claims and relationship candidates at `hold_for_conversion_qa`. Rerun proof review after QA before any canonical claim, relationship, identity merge, parent merge, or Dario-line comparison is promoted.
