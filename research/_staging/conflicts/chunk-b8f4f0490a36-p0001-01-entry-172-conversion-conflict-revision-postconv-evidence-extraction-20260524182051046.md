---
type: identity_conflict_candidate
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524182051046
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524182051046.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
conflict_type: row_level_conversion_conflict
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Conflict Candidate: Entry 172 Row-Level Transcript Conflict

The assigned chunk and source image support entry 172 as the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.

The assigned converted Markdown instead records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`. This is a row-level conflict, not a minor name variant.

The father-name ending is a separate unresolved literal-reading issue. Preserve all three QA outcomes: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

Keep all dependent identity, claim, relationship, and parent-candidate drafts at `hold_for_conversion_qa`.
