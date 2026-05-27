---
type: identity_conflict_candidate
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527020704452"
conflict_type: "row_level_conversion_conflict"
subject: "Entry 172 Pulgar/Arriagada versus Burgos/de la Cruz"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
confidence: "high"
promotion_recommendation: "hold_for_conversion_qa"
---

# Conflict Candidate: Entry 172 Row-Level Conversion Conflict

## Conflict

The current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. The assigned chunk and direct source-image review identify physical row `172` on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

## Controlling Evidence For Staging

The source image controls the staged evidence. The visible row number `172` aligns with the Pulgar/Arriagada entry on the left page. The Burgos/de la Cruz text should be preserved as a derivative conversion conflict, not merged into the Pulgar/Arriagada person or family record.

## Identity Boundaries

- Do not merge `Jose del Carmen Pulgar` with any existing father candidate based on this entry alone.
- Do not promote a suffix after `Pulgar`; this review certifies only `Jose del Carmen Pulgar`.
- Do not attach this record to any Dario/Dario Arturo/Dario Jose Pulgar identity without separate bridging evidence.
- Do not equate `Juana Arriagada de Pulgar` with any other Juana variant from this entry alone.

## Recommended Next Step

Run proof review against this staged source packet and targeted conversion QA note before any canonical claim, relationship, merge, or wiki update.
