---
type: conflict_candidate
status: draft
conflict_type: row_level_conversion_mismatch
subject: "Entry 172 birth registration row control"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: high
promotion_recommendation: promote_after_review
worker: "postconv-evidence-extraction-20260526232217567"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Conflict Candidate: Entry 172 Row-Level Conversion Mismatch

## Conflict

The current converted Markdown identifies entry `172` as a Burgos/de la Cruz birth entry for `Jose Miguel`, while the source image and assigned chunk identify physical entry `172` as the Pulgar/Arriagada birth entry for `Jose del Carmen Segundo Pulgar Arriagada`.

## QA-Controlled Resolution For Staging

The targeted conversion QA note certifies that physical entry `172` is the Pulgar/Arriagada row on register page 58. Staged evidence from this task should use that row, not the stale converted Markdown row.

## Remaining Uncertainty

The father field should remain bounded to `Jose del Carmen Pulgar` unless proof review accepts a visible suffix. The assigned chunk's `S.` suffix is not promoted by this extraction.

## Promotion Guidance

Promote only after proof review accepts the targeted QA note and the row-control resolution. Do not use this conflict note to infer any Dario-line identity or later-family attachment.
