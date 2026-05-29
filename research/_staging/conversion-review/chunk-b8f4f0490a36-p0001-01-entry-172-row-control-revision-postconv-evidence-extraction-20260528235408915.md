---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260528235408915"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260528235408915.md"
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row Control

## Certification

The physical row controlling entry `172` on the original image is the Pulgar/Arriagada row on register page `58`.

Image-reviewed and assigned-chunk-supported reading:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father: certified only through `Jose del Carmen Pulgar`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant/declarant: assigned chunk reads `Ernesto Herrera L.`, present at birth.

## Current Converted Markdown Conflict

The current converted Markdown assigns entry `172` to a different row: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. That converted text is materially incompatible with the original image for physical row `172` and should be treated as stale, row-shifted, or sourced from a different page/image until a conversion worker reconciles it.

## Father Field Boundary

This revision does not promote the father as `Jose del Carmen Pulgar S.`. The certified visible reading is `Jose del Carmen Pulgar`; any trailing mark after `Pulgar` remains unresolved.

## Required Follow-Up

Rerun proof review against the new source packet and dependent staged claims/relationships. Do not promote canonical claims, relationships, identity merges, Dario-line attachments, or wiki updates until proof review accepts this row-control note.
