---
type: identity_analysis
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524140648224
subject: "Jose del Carmen Segundo Pulgar Arriagada"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-20260524140804469.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
identity_confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Pulgar/Arriagada Cluster

The family-relevant identity cluster supported by the image and assigned chunk is:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father: `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`.

The assigned converted Markdown conflicts with this cluster and gives a different entry 172: `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`. This is a row-level identity conflict.

## Identity Guardrails

Do not merge the child, father, or mother into any other Pulgar identity by surname context alone. This entry does not name Dario. The father's suffix must remain unresolved until conversion QA decides whether the field has no suffix, a clear `S.`, or an uncertain final mark.

## Recommendation

Keep identity and relationship work at `hold_for_conversion_qa`. Once the derivative transcript is reconciled, rerun proof review on the child identity, birth event, child-father relationship, child-mother relationship, and parent attributes.
