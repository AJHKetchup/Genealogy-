---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260530142757483"
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

- The source image named by the source packet is absent at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.
- The conversion-job page image is also absent at `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`.
- Physical row control for entry `172` cannot be certified from a visible image. The reviewable evidence is limited to conflicting derivative text layers.
- The assigned chunk/source packet identify entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the current converted Markdown identifies entry `172` as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The conflict covers child identity, parents, birth date/time/place, and informant. This is material, not a spelling variant.
- No canonical child identity, parent-child relationship, spouse clue, duplicate merge, Dario-line attachment, or wiki update is ready from this staged draft.
- The father reading `Jose del Carmen Pulgar S.` remains derivative only. The terminal `S.` must not be normalized, expanded, or dropped unless a later image-controlled reread supports that reading.

## Evidence Strengths

- The staged identity analysis accurately preserves the material conflict between the assigned chunk and the current converted Markdown.
- The assigned chunk, source packet, conflict draft, and conversion QA note agree internally that a Pulgar/Arriagada reading exists in the chunk layer.
- The current converted Markdown supplies a direct competing Burgos/de la Cruz reading for the same entry number, supporting the staged conclusion that row control is unresolved.
- The conversion QA note correctly treats the unavailable source/page image as a hard blocker and recommends `hold_for_conversion_qa`.
- The staged identity analysis avoids promoting any Dario same-person conclusion; no reviewed text literally names Dario in this entry.

## Scored Judgment

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.48 | A civil birth register would normally be high quality, but the controlling image is unavailable for this review. |
| conversion_confidence_score | 0.30 | The chunk and converted Markdown materially disagree on identity-bearing fields. |
| evidence_quantity_score | 0.45 | Multiple derivative files exist, but they do not provide independent image-controlled confirmation. |
| agreement_score | 0.22 | Agreement is low across controlling text layers; entry number and registration date align, while most identity facts conflict. |
| identity_confidence_score | 0.56 | The Pulgar/Arriagada candidate is coherent within one derivative layer, but physical row control is uncertified. |
| claim_probability | 0.64 | Probability that the staged Pulgar/Arriagada row is relevant to entry `172`; insufficient for canonical use while the conversion conflict remains open. |
| relevance_level | conditional_high | High only if image QA certifies the Pulgar/Arriagada row; low if Burgos/de la Cruz controls. |
| relevance_confidence | 0.62 | Pulgar/Arriagada names are family-relevant, but relevance depends on unresolved row control. |
| canonical_readiness | not_ready_hold_for_conversion_qa | No canonical promotion or relationship update is ready. |

## Claim Probability Notes

- Pulgar/Arriagada row controls entry `172`: 0.64. Supported by assigned chunk and staged source packet, blocked by missing image and converted-file conflict.
- Burgos/de la Cruz row controls entry `172`: 0.24. Supported by current converted Markdown, contradicted by assigned chunk and packet.
- The derivative layers represent different physical rows, pages, or row targets under one entry assignment: 0.88. This is the strongest procedural finding.
- Any Dario candidate is the child in this entry: 0.02. No Dario name form appears in the reviewed materials.
- Existing `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar` wiki identity can be strengthened from this item now: 0.18. The names are relevant only if later row-control QA certifies the Pulgar/Arriagada row.

## Next Action

Keep this staged identity analysis and dependent evidence on `hold_for_conversion_qa`. A later conversion-QA worker must restore or locate the original source image or certified page image and reread physical entry `172` before accepting child identity, parent names, father suffix, mother identity, or parent-child relationships for canonical promotion.
