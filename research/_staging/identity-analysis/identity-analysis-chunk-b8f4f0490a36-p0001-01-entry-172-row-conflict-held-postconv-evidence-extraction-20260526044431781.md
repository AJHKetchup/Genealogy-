---
type: identity_analysis
status: draft
analysis_type: row_level_conversion_conflict
subject: "Entry 172 child identity"
candidate_identity: "Jose del Carmen Segundo Pulgar Arriagada"
conflicting_identity: "Jose Miguel, child of Oswaldo Burgos and Concepcion de la Cruz"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526044431781.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
confidence: low
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526044431781"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Identity Analysis: Entry 172 Row Conflict

The family-relevant candidate is `Jose del Carmen Segundo Pulgar Arriagada`, recorded in the assigned chunk as a male child born 8 March 1888 on Calle de Valdivia to `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.

The current converted Markdown for the same source path assigns entry 172 to a different child and family: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 in `En esta`.

The source image visually supports the Pulgar/Arriagada row at entry 172 on register page 58, but this extraction is not a targeted conversion-QA decision. The father field should remain unresolved until QA certifies it as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Recommendation

Keep this identity analysis and all dependent claims or relationships at `hold_for_conversion_qa`. After targeted conversion QA reconciles the source image, converted Markdown, assigned chunk, and source packet, rerun proof review before any canonical claim, identity merge, parent-child relationship, or broader Dario-line comparison is promoted.
