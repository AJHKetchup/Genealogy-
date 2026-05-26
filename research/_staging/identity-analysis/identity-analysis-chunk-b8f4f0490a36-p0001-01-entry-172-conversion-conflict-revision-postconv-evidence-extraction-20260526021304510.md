---
type: identity_analysis
status: draft
analysis_type: conversion_conflict
subject: "Jose del Carmen Segundo Pulgar Arriagada"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526021304510.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: low
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526021149073"
---

# Identity Analysis: Entry 172 Conversion Conflict

The assigned chunk presents entry 172 as a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, male, born 1888-03-08 at 3 p.m. on Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.

The current converted Markdown presents entry 172 as a different birth registration for `Jose Miguel`, male, born 1888-04-06 at 10 p.m., with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`.

Local image review during this pass visually favors the Pulgar/Arriagada row for entry 172, but this evidence-extraction pass does not replace targeted conversion QA. The father-field reading remains blocked for canonical use until QA certifies whether the visible text should be represented as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Recommendation

Keep all dependent claims and relationships at `hold_for_conversion_qa`. After targeted QA reconciles the source image, converted Markdown, chunk, and source packet, rerun proof review before any canonical promotion.
