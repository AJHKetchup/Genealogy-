---
type: identity_conflict_candidate
status: draft
conflict_type: row_level_conversion_conflict
subject: "Entry 172, Los Angeles birth register, 1888"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Conflict Candidate: Entry 172 Row-Level Conversion Conflict

The assigned chunk and source image support a Pulgar/Arriagada row for entry `172`, while the current converted Markdown records a Burgos/de la Cruz row for the same entry number. This is a material row-level conflict, not a spelling variant or a same-person question.

## Pulgar/Arriagada Reading

- Child: `Jose del Carmen Segundo Pulgar Arriagada`, male.
- Registration: 7 April 1888.
- Birth: 8 March 1888, about 3 p.m., Calle de Valdivia.
- Father: `Jose del Carmen Pulgar`; assigned chunk reads `Jose del Carmen Pulgar S.` and the image shows a trailing mark compatible with `S.`, but the final father-field reading still needs targeted QA certification.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employee, resident at Calle de Valdivia.

## Current Converted Markdown Reading

- Child: `José Miguel`, male.
- Registration: 7 April 1888.
- Birth: 6 April 1888, 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Hold

Keep all dependent claims, relationship candidates, identity analyses, parent merges, and Dario-line comparisons at `hold_for_conversion_qa` until targeted conversion QA certifies the controlling row and father-field reading, followed by proof review.
