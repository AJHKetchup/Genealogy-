---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527201359035"
subject: "Entry 172 Pulgar/Arriagada versus Burgos/de la Cruz derivative conflict"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172 per assigned chunk"
conversion_confidence: "blocked_source_image_missing_derivative_conflict"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Follow-Up: Entry 172

Fresh source-image certification could not be completed in this pass. The image path named by the task and chunk is not present in `raw/sources`, and a SHA-256 scan of image files under `raw` found no file matching `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`.

The derivative evidence remains materially conflicted:

- Assigned chunk: entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888 at Calle de Valdivia.
- Current converted Markdown: entry `172` is `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888.

Because the original image is unavailable, this note cannot certify whether physical row `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row. It also cannot certify the father-field suffix after `Jose del Carmen Pulgar`.

Required follow-up: restore or locate the source image by SHA-256, compare the image against the assigned chunk and current converted Markdown, certify physical row control for entry `172`, and record the father field only to the visible level of certainty before proof review or canonical promotion.
