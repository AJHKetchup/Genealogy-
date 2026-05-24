---
type: identity_conflict_analysis
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524141515582
subject: "Entry 172 Pulgar/Arriagada vs converted Markdown row"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
conflict_severity: high
promotion_recommendation: hold_for_conversion_qa
---

# Identity Conflict: Entry 172 Row And Father Suffix

## Conflict 1: Same Entry, Different Family Row

Source image and assigned chunk support:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father: `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.`.
- Mother: `Juana Arriagada de Pulgar`.
- Birth place: `Calle de Valdivia`.

Assigned converted Markdown supports a different row:

- Child: `José Francisco`.
- Father: `Oswaldo Gomez`.
- Mother: `Rosario de la Cruz de la Maza`.
- Birth place: `Pellin`.

This is a material row-level conflict. Do not promote identities or facts from the converted Markdown row for this chunk unless conversion QA confirms it is the correct controlling transcript.

## Conflict 2: Father Name Suffix

The assigned chunk reads the father as `Jose del Carmen Pulgar S.`. Image review supports `Jose del Carmen Pulgar` broadly, but the final suffix or mark is unresolved. Preserve the father as `Jose del Carmen Pulgar [suffix unresolved]` in staged relationship and attribute drafts until conversion QA explicitly decides the suffix.

## Promotion Recommendation

`hold_for_conversion_qa`. Conversion QA should reconcile or supersede the converted Markdown, decide the father suffix, and then trigger proof review before canonical promotion or parent-candidate merging.
