---
type: identity_analysis
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524141515582
subject: "Jose del Carmen Segundo Pulgar Arriagada"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
identity_confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Pulgar/Arriagada Cluster

The family-relevant identity cluster supported by the source image and assigned chunk is:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father: `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`.

## Literal Support

The assigned chunk records entry 172 as a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, male, born on `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, at `Calle de Valdivia`. It names father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.

Direct image review in this extraction pass supports the Pulgar/Arriagada row and the broad father reading, but does not resolve the final father-name suffix enough for canonical identity use.

## Conflict And Guardrails

The assigned converted Markdown gives a materially different entry 172: `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born in `Pellin`. Treat that as a conversion/file-assignment conflict unless targeted conversion QA proves otherwise.

This entry does not name Dario. Do not attach it to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, or any Dario passenger candidate by surname or family context alone.

## Recommendation

Keep this identity analysis and dependent claims at `hold_for_conversion_qa`. After conversion QA reconciles or supersedes the converted Markdown and explicitly decides the father-name suffix, rerun proof review on child identity, birth facts, child-parent relationships, and any Jose/Juana parent-candidate merge question.
