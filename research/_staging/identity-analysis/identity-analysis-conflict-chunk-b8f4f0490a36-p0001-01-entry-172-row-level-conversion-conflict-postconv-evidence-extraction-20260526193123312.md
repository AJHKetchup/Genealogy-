---
type: identity_analysis
status: draft
analysis_type: row_level_conversion_conflict
subject: "Entry 172 identity conflict: Pulgar/Arriagada versus Burgos/de la Cruz"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526193123312.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: low
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526193123312"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Identity Conflict: Entry 172

The family-relevant identity supported by the assigned chunk and original image is `Jose del Carmen Segundo Pulgar Arriagada`, male child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. The current converted Markdown for the same converted file records entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

## Evidence Considered

- Assigned chunk: entry 172 is the Pulgar/Arriagada row and includes matched family terms `Pulgar` and `Arriagada`.
- Original image: register page 58 visually shows entry number 172 aligned with the Pulgar/Arriagada row.
- Current converted Markdown: entry 172 is a different Burgos/de la Cruz row.

## Father Field

The assigned chunk gives `Jose del Carmen Pulgar S.`. Image review in this extraction supports `Jose del Carmen Pulgar` but does not certify whether the trailing mark is `S.`, another mark, or an unresolved stroke. Preserve the father as `Jose del Carmen Pulgar; trailing mark possibly S.` until targeted QA.

## Recommendation

Keep all identity, claim, relationship, merge, and lineage comparison work on `hold_for_conversion_qa`. QA should decide the controlling row for entry 172 and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review before canonical promotion.
