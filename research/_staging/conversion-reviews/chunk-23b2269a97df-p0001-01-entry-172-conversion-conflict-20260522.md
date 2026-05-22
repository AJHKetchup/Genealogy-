---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-23b2269a97df-P0001-01
worker: postconv-evidence-extraction-20260522130512074
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: 23b2269a97df3f6f46f35b0e31112a0c544788f12685bceea234c8bab5504084
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md"
chunk_id: CHUNK-23b2269a97df-P0001-01
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/manifest.json"
page_reference: "image page 1; register page 58; entry 172"
proof_reviews:
  - "research/_staging/reviews/proof-review-relationship-chunk-23b2269a97df-p0001-01-001-child-mother-postconv-proof-review-20260522125900173.md"
  - "research/_staging/reviews/proof-review-relationship-chunk-23b2269a97df-p0001-01-002-child-father-postconv-proof-review-20260522130103057.md"
  - "research/_staging/reviews/proof-review-research-staging-relationships-chunk-23b2269a97df-p0001-01-003-parental-pair-postconv-proof-review-20260522130308689.md"
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Image/Derivative Conflict

## Literal Support From Image Review

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.
- Page reference: image page 1; register page 58; entry 172.
- Visible entry number: `172`.
- Child field: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex field: `Hombre`.
- Registration date field: `Siete de Abril ... de mil ochocientos ochenta i ocho`.
- Birth field: `Ocho de Marzo ... de mil ochocientos ochenta i ocho; a las tres de la tarde`.
- Birth place field: `Calle de Valdivia`.
- Father field: appears as `Jose del Carmen Pulgar`.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant field: appears as `Oswaldo Arriagada`; this needs targeted crop confirmation.

## Conflicting Converted/Chunk Text

The assigned converted Markdown and assigned chunk currently transcribe entry 172 as `Jose Miguel`, sex `Varon`, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

## Conversion Confidence And QA Concern

Conversion confidence for entry 172 is mixed to low because the derivative transcript conflicts with the visible source image on the child, father, mother, birth date, birth place, and informant fields. The staged claims and relationships preserve the image-reviewed Pulgar/Arriagada evidence, but every candidate remains `hold_for_conversion_qa`.

## Uncertainty

The image-level conclusion that entry 172 is a Pulgar/Arriagada birth registration is strong. The exact father-name ending, the informant's exact name, and any canonical identity mapping remain unresolved. This note does not edit or replace the converted Markdown or chunk.

## Promotion Recommendation

Keep `promotion_recommendation: hold_for_conversion_qa`. Do not promote the relationship candidates or canonical claims until conversion QA corrects the converted Markdown/chunk or explicitly records the image reread as the controlling transcript for entry 172.
