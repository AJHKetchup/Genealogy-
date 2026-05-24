---
type: identity_analysis
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524131706940
subject: "Jose del Carmen Segundo Pulgar Arriagada"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
identity_confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Pulgar/Arriagada Cluster

The family-relevant identity cluster in the image/current chunk is:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Father: `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`
- Mother: `Juana Arriagada de Pulgar`
- Informant: `Ernesto Herrera L.`

The assigned converted Markdown currently gives a materially different entry 172: child `Jose Francisco`, father `Oswaldo Gomez`, and mother `Rosario de la Cruz de la Maza`. That is a row-level identity conflict, not a spelling variant.

## Identity Guardrails

This record does not name Dario. Do not merge this child, father, or mother into Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or any other Dario Pulgar identity by surname or family context alone.

The father-name suffix remains unresolved. Until conversion QA records the source-visible form, father-dependent identity work should preserve both readings: `Jose del Carmen Pulgar` and `Jose del Carmen Pulgar S.` as an unresolved exact-name issue.

## Recommendation

Keep this identity analysis and all dependent claims at `hold_for_conversion_qa`. After conversion QA corrects or supersedes the assigned converted Markdown and explicitly decides the father-name suffix, rerun proof review on the child identity, birth facts, and child-parent relationships before canonical promotion.
