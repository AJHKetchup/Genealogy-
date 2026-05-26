---
type: identity_conflict
status: draft
conflict_type: "conversion_row_conflict"
subject: "register page 58, entry 172"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: low
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526063217904"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Conflict: Entry 172 Derivative Transcript Disagreement

## Competing Readings

- Assigned chunk/source-image-supported reading: entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- Current converted Markdown reading: entry 172 records `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

## Assessment

This is a row-level or derivative-file conflict, not a normal spelling variant. The source image visually supports the Pulgar/Arriagada row at register page 58, entry 172, but the converted Markdown currently conflicts with it. The father field appears to begin `Jose del Carmen Pulgar`; its ending must remain uncertified until targeted conversion QA.

## Promotion Recommendation

Keep all dependent claims and relationships at `hold_for_conversion_qa`. QA must decide the controlling row and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before canonical promotion or any parent/Dario-line comparison.
