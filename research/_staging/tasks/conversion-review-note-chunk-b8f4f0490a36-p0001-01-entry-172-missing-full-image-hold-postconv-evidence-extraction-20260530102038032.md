---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530102038032"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102038032.md"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
literal_support: "Assigned chunk entry 172 gives the Pulgar/Arriagada row; current converted Markdown gives a Burgos/de la Cruz row for entry 172."
conversion_confidence: "blocked_full_source_image_absent"
conversion_qa_concern: "Proof review requested full-image row-control certification. The reported source PNG is absent from raw/sources, and the conversion job does not include a full page image in this checkout."
uncertainty: "Parent-field crop assets support the Pulgar/Arriagada parent names only to a partial-crop level. They do not certify the entry number or whole physical row. Father suffix after Pulgar remains uncertified."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Full-Image QA Still Blocked

This pass compared the assigned chunk, current converted Markdown, manifest, available staged crop assets, and local source folders.

The assigned chunk records entry `172` as the Pulgar/Arriagada birth row. The current converted Markdown records entry `172` as the Burgos/de la Cruz birth row. The original source image required to decide between those readings is not present in `raw/sources`, and no full page image is available in the conversion job directory.

Available crop assets support only a limited reading of the parent fields. They are consistent with father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`; they are not sufficient to certify the physical entry number or resolve whether the current converted Markdown is stale, row-shifted, or derived from a different image/page.

Keep all dependent staged evidence at `hold_for_conversion_qa`.
