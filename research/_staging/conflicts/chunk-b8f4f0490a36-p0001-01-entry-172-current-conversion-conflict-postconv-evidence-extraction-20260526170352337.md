---
type: identity_conflict_candidate
status: draft
conflict_type: row_level_conversion_conflict
subject: "Entry 172, Los Angeles birth register, 1888"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Conflict Candidate: Entry 172 Row-Level Conversion Conflict

The assigned chunk and source image support a Pulgar/Arriagada row for entry `172`, while the current converted Markdown records a Burgos/de la Cruz row for the same entry number. This affects child identity, birth date/time/place, father, mother, informant, and all relationship candidates.

## Pulgar/Arriagada Reading

- Child: `Jose del Carmen Segundo Pulgar Arriagada`, male.
- Birth: 8 March 1888, about 3 p.m., Calle de Valdivia.
- Father: `Jose del Carmen Pulgar`; assigned chunk reads `Jose del Carmen Pulgar S.` but the trailing mark remains unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth.

## Current Converted Markdown Reading

- Child: `Jose Miguel`, male.
- Birth: 6 April 1888, 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Hold

This is not a same-person or spelling-variant issue. Keep all dependent claims and relationship candidates at `hold_for_conversion_qa` until targeted conversion QA certifies the controlling row and father-field reading.
