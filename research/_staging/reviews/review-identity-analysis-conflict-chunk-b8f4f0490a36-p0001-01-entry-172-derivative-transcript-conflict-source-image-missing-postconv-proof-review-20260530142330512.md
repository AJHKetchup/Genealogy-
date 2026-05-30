---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260530142330512"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
reviewed_context:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
  - "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
  - "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.48
conversion_confidence_score: 0.30
evidence_quantity_score: 0.45
agreement_score: 0.22
identity_confidence_score: 0.56
claim_probability: 0.64
relevance_level: "conditional_high"
relevance_confidence: 0.62
canonical_readiness: "not_ready_hold_for_conversion_qa"
promotion_recommendation: "hold_for_conversion_qa"
---

# Proof Review: Entry 172 Derivative Transcript Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md`.

## Blockers First

- The source image named by the packet and manifests is not available to this review, and the conversion QA note reports that the expected conversion-job page image was also unavailable.
- Row control for physical entry `172` cannot be certified from an image. The available evidence consists of conflicting derivative text layers.
- The assigned chunk/source packet identifies entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the current converted Markdown identifies entry `172` as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- This is a material identity, birth-event, informant, and relationship conflict. It is not a spelling variant or harmless translation difference.
- No canonical child identity, parent-child relationship, spouse clue, duplicate merge, Dario-line attachment, or wiki update is ready from this staged draft.
- The father-field form `Jose del Carmen Pulgar S.` remains derivative only. The terminal `S.` must not be normalized, expanded, or discarded unless a later image-controlled reread supports that action.

## Evidence Strengths

- The staged identity analysis accurately preserves the central conflict between the assigned chunk and the current converted Markdown.
- The assigned chunk, source packet, conflict draft, and conversion QA note agree internally that the Pulgar/Arriagada reading exists in the chunk layer.
- The current converted Markdown supplies the competing Burgos/de la Cruz reading, which directly supports the staged draft's conclusion that row control is unresolved.
- The conversion QA note correctly treats the missing image as a hard blocker and recommends `hold_for_conversion_qa`.
- The staged identity analysis does not promote a same-person conclusion for any Dario candidate and keeps Dario relevance at a very low, separately reviewable level.

## Scored Judgment

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.48 | A civil birth register would normally be a strong source, but this review cannot inspect the source image. |
| conversion_confidence_score | 0.30 | The chunk and converted Markdown disagree on child, parents, birth date/time/place, and informant. |
| evidence_quantity_score | 0.45 | Several derivative files are available, but they trace to conflicting conversion layers rather than independent image-controlled evidence. |
| agreement_score | 0.22 | Agreement is low across the controlling text layers; only entry number and registration date align. |
| identity_confidence_score | 0.56 | The Pulgar/Arriagada candidate is coherent within the chunk layer, but physical row control remains uncertified. |
| claim_probability | 0.64 | Probability that the staged Pulgar/Arriagada row is relevant to entry `172`; this remains below canonical acceptance because of the unresolved conversion conflict. |
| relevance_level | conditional_high | High if image QA certifies the Pulgar/Arriagada row; low if the Burgos/de la Cruz conversion controls. |
| relevance_confidence | 0.62 | Pulgar/Arriagada names are directly family-relevant, but relevance depends on unresolved row control. |
| canonical_readiness | not_ready_hold_for_conversion_qa | No canonical promotion or relationship update is ready. |

## Claim Probability Notes

- Pulgar/Arriagada row controls entry `172`: 0.64. Supported by assigned chunk and staged packet, blocked by missing image and converted-file conflict.
- Burgos/de la Cruz row controls entry `172`: 0.24. Supported by current converted Markdown, contradicted by assigned chunk and packet.
- The two derivative layers represent different physical rows, pages, or row targets under one entry assignment: 0.88. The breadth of disagreement makes this the strongest procedural finding.
- Any Dario candidate is the child in this entry: 0.02. No Dario name form appears in the reviewed materials.
- Existing `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar` wiki identity can be strengthened from this item now: 0.18. The names are relevant but the row is not certified.

## Next Action

Keep this staged identity analysis and dependent evidence on `hold_for_conversion_qa`. A later conversion-QA worker must restore or locate the original/page image and reread physical entry `172` before any proof worker can accept child identity, parent names, father suffix, mother identity, or parent-child relationships for canonical promotion.
