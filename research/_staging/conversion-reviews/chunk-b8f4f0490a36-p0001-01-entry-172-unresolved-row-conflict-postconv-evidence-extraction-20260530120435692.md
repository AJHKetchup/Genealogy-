---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530120435692"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-held-conflict-postconv-evidence-extraction-20260530120435692.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
literal_support: "Assigned chunk entry 172 gives the Pulgar/Arriagada row; current converted Markdown entry 172 gives the Burgos/de la Cruz row."
conversion_confidence: "blocked_original_source_image_missing"
conversion_qa_concern: "Targeted QA cannot certify physical row control because the original PNG is absent from raw/sources in this checkout, and the conversion job has page Markdown but no full page image."
uncertainty: "Father field should be preserved only to the bounded derivative reading Jose del Carmen Pulgar, with the chunk's trailing S./mark not promoted."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Row Conflict Still Unresolved

This worker compared the assigned chunk, current converted Markdown, chunk manifest, conversion job files, and available staged outputs.

The assigned chunk records entry `172` as the Pulgar/Arriagada row. The current converted Markdown records entry `172` as the Burgos/de la Cruz row. The original source image needed to decide which physical row controls entry `172` is not present under `raw/sources`; the conversion job directory contains Markdown and work-order files but no full page image.

Result: the proof-review requested row-control QA remains blocked. Keep all dependent source packets, claims, relationships, identity analysis, and wiki work at `hold_for_conversion_qa` until the original image is restored and reviewed.

