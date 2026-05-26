---
type: identity_analysis
status: draft
analysis_type: "row_level_conversion_conflict"
subject: "Entry 172 birth registration identity candidate"
candidate_identity: "Jose del Carmen Segundo Pulgar Arriagada"
conflicting_identity: "Jose Miguel, child of Oswaldo Burgos and Concepcion de la Cruz"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526061756173.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: low
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526061756173"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Identity Analysis: Entry 172 Row-Level Conflict

## Family-First Summary

The family-relevant candidate is `Jose del Carmen Segundo Pulgar Arriagada`, with parents recorded in the assigned chunk as `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. This would be a high-value birth and parentage source if confirmed.

## Conflict

The assigned chunk and source image support the Pulgar/Arriagada row for entry 172. The current converted Markdown records a different entry 172: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m.

## Father-Field Issue

The assigned chunk reads the father as `Jose del Carmen Pulgar S.`. The image appears to support `Jose del Carmen Pulgar` with a possible trailing letter or mark, but this extraction does not certify whether the field should be rendered as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Recommendation

Keep all dependent claims and relationships at `hold_for_conversion_qa`. Targeted QA must decide the controlling row, certify the father-field reading, and identify whether the converted Markdown, chunk, source packet, or previous staged drafts require correction. Rerun proof review after QA before any canonical promotion.
