---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530135819337"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
reported_source_path: "raw/sources/Registro de Nacimientos, CircunscripciÃ³n de Los Ãngeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; disputed entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-proof-review-revision-hold-postconv-evidence-extraction-20260530135819337.md"
conversion_confidence: "hold_derivative_conflict_crop_assets_only"
conversion_qa_concern: "The full original PNG is absent from raw/sources and the manifest-listed page image path is absent from the conversion job, so this worker cannot certify physical full-row control. The assigned chunk and staged crop assets support Pulgar/Arriagada parent/informant readings only at derivative/crop level; the current converted Markdown assigns entry 172 to Burgos/de la Cruz."
literal_support: "Assigned chunk entry 172 reads Jose del Carmen Segundo Pulgar Arriagada, male, born 8 March 1888 at Calle de Valdivia, with father Jose del Carmen Pulgar S., mother Juana Arriagada de Pulgar, and informant Ernesto Herrera L."
uncertainty: "Preserve father only as Jose del Carmen Pulgar. Do not promote the trailing S. or any expanded paternal surname until full-page source-image QA certifies it."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Proof-Review Revision Hold

## Finding

The assigned chunk and current converted Markdown remain materially inconsistent for entry `172`.

- Assigned chunk: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`
- Current converted Markdown: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`

The full original source image was not found at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`. The conversion-job manifest lists `page-images/page-0001.png`, but that path is also absent in this checkout.

## Image-Reviewed Partial Support

Two staged crop assets were inspected:

- `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png`
- `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-bottom-postconv-evidence-extraction-20260529000036877.png`

The crops support the Pulgar/Arriagada parent and Ernesto Herrera informant readings at crop level. They are not a substitute for full-page row-control certification. The father field should be bounded to `Jose del Carmen Pulgar`; the trailing mark or `S.` after `Pulgar` is not promotion-ready.

## Recommendation

Keep all dependent source packets, atomic claims, relationship candidates, identity analysis, Dario-line attachments, and wiki updates on `hold_for_conversion_qa`. The next required step is full-page original-image QA followed by proof review.
