---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530014639534"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-conflict-postconv-evidence-extraction-20260530014639534.md"
conversion_confidence: derivative_conflict_source_image_unavailable
conversion_qa_concern: "The assigned chunk identifies entry 172 as the Pulgar/Arriagada birth row, while the current converted Markdown identifies entry 172 as Jose Miguel, child of Oswaldo Burgos and Concepcion de la Cruz. The original source image is not available in raw/sources, and the conversion job has no extracted image directory for a fresh visual QA pass."
literal_support: "Assigned chunk row 172: Nombre. Jose del Carmen Segundo Pulgar Arriagada; Sexo. Hombre; Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde; Lugar. Calle de Valdivia; Nombre del padre Jose del Carmen Pulgar S.; Nombre de la madre Juana Arriagada de Pulgar; informant Ernesto Herrera L."
uncertainty: "This worker cannot certify the physical row from image review. Father is bounded only to Jose del Carmen Pulgar in held drafts; the trailing S. remains uncertified."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Source Image Blocker

This revision preserves the material conflict between local derivatives:

- The assigned chunk for `CHUNK-b8f4f0490a36-P0001-01` records entry `172` as the Pulgar/Arriagada row.
- The current converted Markdown for the same `converted_sha256` records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888.
- The original image named in the task is not present under `raw/sources`, and the conversion job contains page Markdown and work orders but no extracted image file.

Because this pass cannot perform the requested targeted visual QA, the attached evidence remains held. Do not promote the child, parent, relationship, or father-suffix readings until a reviewer with the source image certifies row control or formally supersedes the stale derivative.

