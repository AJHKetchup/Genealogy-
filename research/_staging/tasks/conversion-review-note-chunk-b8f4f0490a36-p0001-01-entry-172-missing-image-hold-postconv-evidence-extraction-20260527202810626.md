---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527202810626"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260527202810626.md"
source_path: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Hold

This evidence-extraction revision cannot certify the physical row controlling entry `172`. The expected 1888 source image is not present in `raw/sources`, and a recursive raw image search did not locate a matching 1888 entry-172 image in this checkout.

The derivative sources still materially disagree:

- Assigned chunk: entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- Current converted Markdown: entry `172` is `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

Keep this worker's source packet, atomic claims, identity-conflict candidate, and relationship candidates at `hold_for_conversion_qa`. The next QA worker should restore or locate the source image, compare it against the assigned chunk and current converted Markdown, certify whether entry `172` is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row, and record the father field only to the visible level of certainty.
