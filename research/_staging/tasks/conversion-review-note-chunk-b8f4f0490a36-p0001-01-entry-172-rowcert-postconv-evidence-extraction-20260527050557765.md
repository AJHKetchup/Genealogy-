---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527050557765"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-rowcert-postconv-evidence-extraction-20260527050557765.md"
page_reference: "page 1; register page 58; physical row entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row Control

Targeted QA compared the original page image, assigned chunk, current converted Markdown, and staged evidence requirements for entry `172`.

## Certification

- The physical row numbered `172` on the original image controls this evidence set.
- The controlling row is on the left page/register page 58.
- The controlling row is the Pulgar/Arriagada birth-registration row for `Jose del Carmen Segundo Pulgar Arriagada`.
- The father field is certified only to `Jose del Carmen Pulgar`. A small terminal suffix or mark may be present after `Pulgar`, but this extraction does not certify it.
- The mother field is read as `Juana Arriagada de Pulgar`.

## Derivative Conflict

The assigned chunk matches the visible Pulgar/Arriagada row. The current converted Markdown instead records entry `172` as a Burgos/de la Cruz row with child `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`. Treat the converted Markdown as stale, row-shifted, or sourced from a different image/page until conversion-control reconciles the mismatch.

## Promotion Guidance

Keep source packet evidence, atomic claims, relationship candidates, identity merges, Dario-line attachments, and wiki edits on `hold_for_conversion_qa`. Rerun proof review after this row-control note is considered.
