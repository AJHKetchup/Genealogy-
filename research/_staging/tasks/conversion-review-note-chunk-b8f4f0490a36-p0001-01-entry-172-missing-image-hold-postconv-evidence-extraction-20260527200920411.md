---
type: conversion_review_note
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527200920411"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260527200920411.md"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Entry 172 Hold

This worker could not locate the original 1888 source image in `raw/sources` under the expected path. A directory listing showed only `.gitkeep`, several unrelated PDFs, and the 1889 certificate image for entry 513. Therefore this pass cannot certify the physical row controlling entry `172`.

The assigned chunk and current converted Markdown still materially disagree:

- Assigned chunk: entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- Current converted Markdown: entry `172` is `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

Keep the new source packet, atomic claims, and relationship candidates at `hold_for_conversion_qa`. The next worker should restore or locate the source image whose SHA-256 is `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, compare it with the assigned chunk and converted Markdown, certify whether entry `172` is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row, and preserve the father field only as far as visible evidence supports.
