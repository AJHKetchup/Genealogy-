---
type: conflict_candidate
status: draft
conflict_type: row_level_conversion_conflict
subject: "Los Angeles birth register entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: high
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526002904836"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Conflict Candidate: Entry 172 Row Control

## Conflict

The assigned chunk supports a Pulgar/Arriagada row for entry 172, while the current converted Markdown records a Burgos/de la Cruz row for the same entry number.

## Pulgar/Arriagada Reading In Assigned Chunk

- Child: Jose del Carmen Segundo Pulgar Arriagada.
- Sex: Hombre.
- Birth: 8 March 1888, about 3 p.m., Calle de Valdivia.
- Father: Jose del Carmen Pulgar S. according to the assigned chunk.
- Mother: Juana Arriagada de Pulgar.
- Informant: Ernesto Herrera L., present at birth.

## Burgos/de la Cruz Reading In Current Converted Markdown

- Child: Jose Miguel.
- Birth: 6 April 1888, about 10 p.m., En esta.
- Father: Oswaldo Burgos.
- Mother: Concepcion de la Cruz.
- Informant: Oswaldo Burgos.

## Required Resolution

Targeted conversion QA should decide the controlling row for entry 172 and certify the father field only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Until then, this conflict blocks canonical claims, relationships, identity merges, and Dario-line comparisons.
