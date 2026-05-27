---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527201841903"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260527201841903.md"
source_path: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Hold

This evidence-extraction revision cannot certify the physical row controlling entry `172`. The expected 1888 source image is not present in `raw/sources`, the conversion-job directory has `page-markdown` and `work-orders` but no `page-images` directory, and a SHA-256 scan of raw image files found no file matching `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`.

The derivative sources still materially disagree:

- Assigned chunk: entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- Current converted Markdown: entry `172` is `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

Keep the new source packet, atomic claims, and relationship candidates at `hold_for_conversion_qa`. The next QA worker should restore or locate the source image, compare it against the assigned chunk and current converted Markdown, certify whether entry `172` is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row, and record the father field only to the visible level of certainty.
