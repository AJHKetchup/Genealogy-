---
type: identity_analysis
status: draft
analysis_type: "conversion_conflict"
subject: "Jose del Carmen Segundo Pulgar Arriagada"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063958736.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: low
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526063917014"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Identity Analysis: Entry 172 Conversion Conflict

## Person-First Focus

The family-relevant candidate is `Jose del Carmen Segundo Pulgar Arriagada`, a male child recorded in the assigned chunk as born 8 March 1888 at Calle de Valdivia, with recorded parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.

## Conflict

The assigned chunk and source image support a Pulgar/Arriagada row for register page 58, entry 172. The current converted Markdown instead records entry 172 as a Burgos/de la Cruz row for child `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.

## Current Assessment

The source image review favors the Pulgar/Arriagada row as the visible entry 172 in the assigned image. However, this evidence set remains blocked because the canonical converted Markdown for the same assigned source path has a different row-level transcription. The father field appears to begin `Jose del Carmen Pulgar`; the ending is not certified here.

## Required QA

Targeted conversion QA must decide the controlling entry-172 row and certify the father field as one of:

- `Jose del Carmen Pulgar`
- `Jose del Carmen Pulgar S.`
- `Jose del Carmen Pulgar [?]`

After QA, rerun proof review for child identity, birth facts, parent names, parent-child relationship candidates, and any identity merge or Dario-line comparison.
