---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526165338916
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-identity-researcher-20260526135632244.md
staged_draft_reviewed: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-identity-researcher-20260526135632244.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
review_decision: hold
canonical_readiness: hold
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

- The assigned staged draft is correctly held from canonical promotion because the referenced converted Markdown and referenced chunk disagree at the row level for register page 58, entry 172.
- The converted Markdown identifies entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m.
- The chunk identifies entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m.
- The source packet and direct page-image inspection support the Pulgar/Arriagada row as the visible entry 172, but the converted Markdown conflict is material and must be resolved by targeted conversion QA before promotion.
- The staged draft includes statements about existing canonical pages and Dario-line comparisons. Those claims were not independently verified in this review because the task scope allowed only the staged draft and referenced source/conversion artifacts. Treat those sections as anti-conflation context, not proof.
- The father field ending remains unresolved. The visible and staged support is sufficient for `Jose del Carmen Pulgar`; the final `S.` or other trailing mark should remain uncertified until targeted conversion QA.

## Evidence Strengths

- The staged draft accurately identifies the central conversion conflict and does not treat `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` as name variants.
- The draft preserves uncertainty and recommends `hold_for_conversion_qa`, which is supported by the available artifacts.
- The source packet, chunk, and page image agree on the broad Pulgar/Arriagada reading for entry 172.
- The converted Markdown plainly supplies the incompatible Burgos/de la Cruz reading, so the conflict is literal and not speculative.
- The draft appropriately blocks parent-child relationships, identity merges, Dario-line bridges, and canonical promotion.

## Scored Judgment

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register page image is a strong primary source; derivative artifacts disagree. |
| conversion_confidence_score | 0.34 | Chunk and image align, but the converted Markdown is materially inconsistent. |
| evidence_quantity_score | 0.62 | One primary page image plus two local derivative layers and a source packet; no independent external corroboration was used. |
| agreement_score | 0.55 | Source packet, image, and chunk agree with each other; converted Markdown conflicts across child, parents, date, place, and informant. |
| identity_confidence_score | 0.68 | Pulgar/Arriagada as the visible row is probable, but identity claims remain held because the conversion artifact conflict is unresolved. |
| claim_probability | 0.76 | The staged draft's main claim that this is a conversion row conflict favoring Pulgar/Arriagada is probable. |
| relevance_level | high | The reviewed draft directly concerns the assigned entry 172 conflict. |
| relevance_confidence | 0.98 | All reviewed artifacts reference the same source image, chunk id, page, and entry number. |
| canonical_readiness | hold | No canonical promotion should occur until targeted conversion QA reconciles the derivative files and certifies the father-field ending. |

## Claim-Level Review

| claim | probability | support | review judgment |
| --- | ---: | --- | --- |
| Entry 172 has a material conversion conflict. | 0.95 | Converted Markdown and chunk give incompatible rows for the same entry number. | Supported; hold for QA. |
| The visible/source-packet-supported row is Pulgar/Arriagada. | 0.78 | Chunk, source packet, and page-image inspection align on Pulgar/Arriagada. | Probable; not canonical-ready. |
| The converted Markdown row is Burgos/de la Cruz. | 1.00 | The converted file explicitly transcribes that row as entry 172. | Supported as the competing derivative reading. |
| Father is `Jose del Carmen Pulgar S.`. | 0.55 | Chunk reads `S.`, while source packet only certifies `Jose del Carmen Pulgar`. | Revise/hold exact suffix. |
| Mother is `Juana Arriagada de Pulgar`. | 0.72 | Chunk, source packet, and image-level review support the mother name. | Probable if Pulgar row controls; hold relationship promotion. |
| Entry 172 bridges to any Dario Pulgar candidate. | 0.05 | The reviewed source artifacts do not name Dario, Arturo, Smith, spouse, child, or a linking event. | Not supported; retain only as an anti-conflation warning. |
| Existing canonical pages resolve the conflict. | 0.00 | Canonical pages were outside this review scope and would be derivative of the same held evidence. | Not usable as proof for this review. |

## Source Reliability And Identity Risk

The civil register image is a high-quality source type for a birth event, but this proof package is not ready for canonical use because the conversion layer is internally inconsistent. The identity risk is high if the converted Markdown row is accepted without QA, because it would create a completely different child and parental pair. The identity risk is also high if the Pulgar/Arriagada row is used to merge or bridge Dario-line candidates by surname alone.

## Next Action

Targeted conversion QA should compare the source image, converted Markdown, chunk, and source packet for page 58, entry 172. It should certify which row controls, explain why the converted Markdown and chunk disagree, and record whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before promoting any child identity, birth fact, parent-child relationship, or Dario-line comparison.
