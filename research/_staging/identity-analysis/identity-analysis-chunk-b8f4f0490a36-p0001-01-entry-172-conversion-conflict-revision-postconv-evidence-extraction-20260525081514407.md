---
type: identity_conflict_analysis
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260525081514407
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525081514407.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Conversion Conflict

## Blockers

1. The current chunk and assigned converted Markdown disagree on the identity-bearing entry 172 row.
2. The father field must remain unresolved until QA certifies `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. No canonical claim, parent-child relationship, parent merge, or Dario-line comparison is promotion-ready from this evidence pass.

## Current Chunk Reading

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Father: `Jose del Carmen Pulgar S.` in the chunk.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

## Converted Markdown Reading

- Child: `José Francisco`.
- Birth: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birth place: `En esta`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.
- Informant: `Oswaldo Gomez`.

## Interpretation

These readings are mutually incompatible as a single birth registration. Treat the issue as a conversion or assignment conflict until targeted conversion QA compares the source image, current chunk, and converted Markdown.

The Pulgar/Arriagada row is family-relevant if confirmed, but it should not be used to merge `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, entry-513 Juana variants, or any Dario Pulgar candidate. This entry does not name Dario, Arturo, Smith, Alexander John Heinz, a spouse, a later residence, or an occupation bridge.

## Recommendation

Send this source set to targeted conversion QA. After QA, rerun proof review on the source packet, child identity claims, birth event claims, father and mother claims, and parent-child relationships before any canonical promotion.
