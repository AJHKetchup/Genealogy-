---
type: identity_conflict
status: draft
conflict_type: row_level_conversion_conflict
subject: "entry 172 child and parents"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002233750.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: low
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526002233750"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Identity Conflict: Entry 172 Row And Father Suffix

The assigned chunk and image-reviewed evidence support a Pulgar/Arriagada birth row for entry 172, while the current converted Markdown assigns entry 172 to a Burgos/de la Cruz child.

## Conflicting Readings

- Assigned chunk and image-reviewed row: child `Jose del Carmen Segundo Pulgar Arriagada`; father begins `Jose del Carmen Pulgar`; mother `Juana Arriagada de Pulgar`; birth 8 March 1888 at 3 p.m.; place `Calle de Valdivia`; informant `Ernesto Herrera L.`
- Current converted Markdown: child `Jose Miguel`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; birth 6 April 1888 at 10 p.m.; place `En esta`; declarant `Oswaldo Burgos`.

## Blocker

This is not a name-variant conflict. It is a row-level conversion conflict that changes the subject child and both parents. The father field in the Pulgar/Arriagada row also remains unresolved and should be certified as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Recommendation

Keep all dependent identity, birth, residence, informant, and parent-child relationship claims at `hold_for_conversion_qa`. After targeted conversion QA, rerun proof review before any canonical promotion, parent merge, or Dario-line comparison.
