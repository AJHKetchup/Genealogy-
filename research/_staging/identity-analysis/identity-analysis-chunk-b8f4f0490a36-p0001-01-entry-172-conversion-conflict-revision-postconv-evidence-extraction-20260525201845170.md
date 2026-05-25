---
type: identity_conflict_analysis
status: hold
role: evidence_extractor
worker: postconv-evidence-extraction-20260525201845170
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525201845170.md
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
conflict_type: row_level_conversion_conflict
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
---

# Identity Conflict Analysis: Entry 172 Row Conflict

## Blocker

Canonical readiness is `hold_for_conversion_qa`. The assigned chunk and assigned converted Markdown identify different people for entry 172.

## Pulgar/Arriagada Reading From Assigned Chunk

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk, with suffix unresolved pending QA.
- Mother: `Juana Arriagada de Pulgar`.
- Parent residence: `Calle de Colipi`.
- Informant: `Ernesto Herrera L.`, present at the birth.

## Burgos/de la Cruz Reading From Assigned Converted Markdown

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birth place: `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Evidence Judgment

This is a severe row-level conflict. The two readings differ by child name, parent names, birth date, birth place, and informant. The Pulgar/Arriagada reading is family-relevant and should remain staged, but no claim, relationship, identity merge, or Dario-line comparison should be promoted until conversion QA resolves the controlling row.

The father field is specifically unresolved. QA must certify the father field only to the extent visible, using one of the requested forms: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Promotion Recommendation

`hold_for_conversion_qa`. After QA, rerun proof review for the child identity, birth facts, parent names, parent-child relationship candidate, and any proposed same-person action involving similarly named Pulgar or Arriagada candidates.
