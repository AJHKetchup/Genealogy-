---
type: identity_conflict_candidate
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527202810626"
subject: "Entry 172 controlling row"
conflict_type: derivative_transcript_row_conflict
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260527202810626.md"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: low
literal_support: "Assigned chunk identifies entry 172 as Jose del Carmen Segundo Pulgar Arriagada; current converted Markdown identifies entry 172 as Jose Miguel, son of Oswaldo Burgos and Concepcion de la Cruz."
conversion_confidence: "blocked_source_image_missing_derivative_conflict"
conversion_qa_concern: "Original image is missing in this checkout, so this worker cannot certify which physical row controls entry 172 or whether the father field includes a visible S. suffix."
uncertainty: "Do not merge identities or attach this record to the Dario line until source-image QA resolves the row conflict."
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Row Conflict Candidate: Entry 172

The assigned chunk and the current converted Markdown disagree about the person and family recorded in entry `172`.

- Assigned chunk: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- Current converted Markdown: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.

The source image named by the task is absent from this checkout, so this draft cannot certify whether the Pulgar/Arriagada row or the Burgos/de la Cruz row controls the physical entry. Preserve the father field only as `Jose del Carmen Pulgar [suffix uncertain]` in held staging.
