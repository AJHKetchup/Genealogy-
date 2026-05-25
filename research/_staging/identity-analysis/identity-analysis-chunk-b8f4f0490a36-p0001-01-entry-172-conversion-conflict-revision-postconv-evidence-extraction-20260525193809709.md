---
type: identity_conflict_analysis
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260525193809709
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525193809709.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold_for_conversion_qa
---

# Identity And Conversion Conflict Note: Entry 172

## Blocker

The assigned chunk and visible source image support a Pulgar/Arriagada birth row for entry 172, while the assigned converted Markdown currently records a Burgos/de la Cruz row for entry 172. The disagreement changes the child, parents, birth date/time, birth place, and informant. This extraction therefore cannot promote identity, birth, or relationship claims.

## Held Pulgar/Arriagada Reading

- Registration number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: chunk reading `Jose del Carmen Pulgar S.`; father-field suffix remains uncertified.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth.

## Converted Markdown Reading

The assigned converted Markdown's entry 172 reads as `Jose Miguel`, born 6 April 1888 at 10 p.m., father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, with `Oswaldo Burgos` as compareciente.

## Assessment

This is not a same-person or spelling-variant issue. It is a row-level or file-assignment conflict between derivative transcripts and image-reviewed evidence. The father field must be certified only after targeted conversion QA as one of the proof-review-requested readings: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Recommendation

Keep all dependent staged claims and relationships on `hold_for_conversion_qa`. After QA decides the controlling entry-172 row and father-field reading, rerun proof review before any canonical claim, relationship, identity merge, parent merge, or wider Dario-line comparison is promoted.
