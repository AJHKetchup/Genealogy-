---
type: identity_conflict_analysis
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524153029581
subject: "Entry 172 Pulgar/Arriagada vs converted Markdown row"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524153029581.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
conflict_severity: high
promotion_recommendation: hold_for_conversion_qa
---

# Identity Conflict: Entry 172 Row And Father Suffix

## Conflict 1: Same Entry Number, Different Family Row

Assigned chunk and image-reviewed evidence support:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father: `Jose del Carmen Pulgar S.` in the chunk, with the final suffix unresolved for canonical use.
- Mother: `Juana Arriagada de Pulgar`.
- Birth place: `Calle de Valdivia`.

Assigned converted Markdown supports a different row:

- Child: `José Francisco`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.
- Birth place: `En esta`.

This is a material row-level conflict. Do not promote identities or facts from either derivative transcript until conversion QA confirms the controlling transcript against the source image.

## Conflict 2: Father Name Suffix

The assigned chunk reads the father as `Jose del Carmen Pulgar S.`. The source image supports a Pulgar father broadly, but this extraction pass does not settle whether the final mark after `Pulgar` is absent, a clear `S.`, or uncertain. Preserve the father as `Jose del Carmen Pulgar [suffix unresolved]` in staged drafts.

## Promotion Recommendation

`hold_for_conversion_qa`. Conversion QA should reconcile or supersede the converted Markdown, decide the father suffix, and trigger proof review before any canonical promotion or parent-candidate merge.
