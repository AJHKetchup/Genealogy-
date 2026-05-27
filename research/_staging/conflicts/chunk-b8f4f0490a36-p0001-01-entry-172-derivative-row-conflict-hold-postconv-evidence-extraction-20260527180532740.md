---
type: conflict_candidate
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527180532740"
conflict_type: derivative_transcript_row_control
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; entry 172"
confidence: medium
conversion_confidence: "blocked_missing_source_image"
conversion_qa_concern: "Assigned chunk and current converted Markdown describe different entry-172 families; source image unavailable to this worker."
uncertainty: "Cannot certify physical row control or father suffix in this worker."
promotion_recommendation: hold_for_conversion_qa
---

# Conflict Candidate: Entry 172 Derivative Transcript Mismatch

The assigned chunk and current converted Markdown cannot both be treated as reliable transcripts of entry `172`.

- Assigned chunk: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- Current converted Markdown: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This worker could not inspect the original image because both the raw source image and manifest page image are absent from the checkout.

Keep the Pulgar/Arriagada family claims and relationship candidates at `hold_for_conversion_qa`, and do not promote the Burgos/de la Cruz reading from this converted Markdown as controlling entry `172` unless a later image review proves it.
