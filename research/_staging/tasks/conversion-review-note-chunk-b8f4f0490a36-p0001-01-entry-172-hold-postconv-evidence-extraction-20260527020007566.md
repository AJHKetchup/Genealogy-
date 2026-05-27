---
type: research_task
status: draft
task_type: targeted_conversion_qa
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527020007566"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527020007566.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Task: Targeted Conversion QA For Entry 172

Prior proof reviews requested conversion QA before promotion. This extraction pass confirms a live row-level conflict:

- Original image: physical row 172 on left page/register page 58 visibly corresponds to Jose del Carmen Segundo Pulgar Arriagada, with father Jose del Carmen Pulgar and mother Juana Arriagada de Pulgar.
- Assigned chunk: records the same Pulgar/Arriagada entry 172.
- Current converted Markdown: records entry 172 as Jose Miguel, father Oswaldo Burgos, mother Concepcion de la Cruz.

## Required QA Decisions

1. Certify whether physical row 172 in the original image controls this source packet.
2. Determine whether the converted Markdown is stale, row-shifted, or sourced from another image/page.
3. Preserve the father field only to the visible/certified level: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Hold Instruction

Keep this packet, claims, and relationship candidates at `hold_for_conversion_qa`. After QA, rerun proof review before canonical claim, relationship, parent merge, Dario-line attachment, or wiki update.
