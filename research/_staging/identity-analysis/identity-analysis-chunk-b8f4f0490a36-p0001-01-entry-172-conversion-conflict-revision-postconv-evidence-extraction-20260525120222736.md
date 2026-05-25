---
type: identity_conflict_analysis
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260525120222736
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525120222736.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold_for_conversion_qa
---

# Identity And Conversion Conflict: Entry 172

The current chunk and assigned converted Markdown disagree on the identity of entry 172.

## Pulgar/Arriagada Reading In Current Chunk

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/place: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk, with final `S.` requiring image-level QA.
- Mother: `Juana Arriagada de Pulgar`.

## Gomez/de la Cruz Reading In Assigned Converted Markdown

- Child: `Jose Francisco`.
- Birth date/place: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`; `En esta`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.

## Extraction Decision

Because the derivative records are mutually exclusive, the Pulgar/Arriagada claims and relationships are staged only as family-relevant candidates. They are not ready for canonical promotion, parent merge, or Dario-line comparison. The blocker is targeted conversion QA, which must determine the controlling row and certify the father-field reading as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
