---
type: identity_conflict_candidate
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530110059001"
subject: "Entry 172 Pulgar/Arriagada versus Burgos/de la Cruz conversion conflict"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530110059001.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_reference: "page 1; register page 58; entry 172"
conflict_type: "row_control_and_identity"
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conversion Conflict: Entry 172

## Conflict

Two derivative readings disagree about the same entry number:

- Assigned chunk: entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- Current converted Markdown: entry `172` is `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

## Assessment

This is a row-control and identity conflict, not a same-person merge problem. The Burgos/de la Cruz child and Pulgar/Arriagada child should remain separate unless full-image QA proves one derivative reading is wrong for this source.

The source image needed to certify physical row control is not present in this checkout. This worker therefore cannot resolve whether the converted Markdown is stale, row-shifted, or from a different page/image.

## Recommendation

Keep all dependent claims and relationships on `hold_for_conversion_qa`. Do not attach this record to the Dario/Pulgar line, do not merge any identities, and do not update canonical wiki pages until full-image row-control QA and proof review pass.
