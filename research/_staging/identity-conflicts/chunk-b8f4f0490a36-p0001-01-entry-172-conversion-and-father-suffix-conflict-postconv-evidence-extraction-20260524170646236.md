---
type: identity_conflict
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524170600190
subject: "Entry 172 Pulgar/Arriagada row and father suffix"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524170646236.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Identity Conflict: Converted Row And Father Suffix

The assigned converted Markdown conflicts materially with the assigned chunk and source image.

- Converted Markdown: entry 172 is an unrelated `Jose Francisco` child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`.
- Assigned chunk and source image: entry 172 is `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- Father suffix issue: the chunk renders the father as `Jose del Carmen Pulgar S.`; the source image supports `Jose del Carmen Pulgar`, but the final mark or suffix is not resolved in this extraction pass.

Resolution needed: targeted conversion QA should decide the controlling row and record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
