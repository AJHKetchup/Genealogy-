---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260530135818675"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md"
reviewed_files:
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
  - "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
source_quality_score: 0.60
conversion_confidence_score: 0.35
evidence_quantity_score: 0.45
agreement_score: 0.20
identity_confidence_score: 0.30
claim_probability: 0.32
relevance_level: "conditional_high_if_pulgar_row_certified"
relevance_confidence: 0.55
canonical_readiness: "not_ready"
recommendation: "hold_for_conversion_qa"
---

# Proof Review: Entry 172 Derivative Transcript Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md`.

## Blockers First

- Source-image control is unavailable. The expected original source image and conversion-job page image are both absent in this workspace, so the physical row for entry `172` cannot be reread.
- The assigned chunk/source packet and the current converted Markdown describe materially different people for entry `172`: Pulgar/Arriagada in the chunk layer versus Burgos/de la Cruz in the converted layer.
- The staged draft correctly treats this as a derivative transcript conflict, not a spelling, translation, or name-order variation.
- No canonical birth claim, parent-child relationship, spousal clue, same-person conclusion, Dario-line attachment, merge, rename, or wiki update is proof-ready from this evidence.
- The father reading `Jose del Carmen Pulgar S.` remains bounded as a derivative chunk reading only. The suffix or terminal mark cannot be strengthened without image-controlled QA.

## Evidence Strengths

- The assigned chunk and source packet agree internally that entry `172` is a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about three in the afternoon at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The converted Markdown clearly states a conflicting entry `172`: `Jose Miguel`, male, registered 7 April 1888, born 6 April 1888 at about ten at night, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.
- The staged source packet and conversion-review note preserve the conflict and already recommend `hold_for_conversion_qa`, which is supported by this proof review.
- If the Pulgar/Arriagada row is later certified from the image, the source type would be genealogically relevant and potentially strong for a child birth identity and named parents. That conditional relevance does not overcome the current row-control failure.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.60 | Civil birth registration would normally be strong, but this review has only derivative text and no visible source image. |
| conversion_confidence_score | 0.35 | The chunk and converted Markdown conflict on child, parents, birth date, place, and informant. |
| evidence_quantity_score | 0.45 | There are several derivative layers, but they trace to the same unavailable image and disagree at the controlling point. |
| agreement_score | 0.20 | Agreement is internal within each derivative layer, not across the assigned chunk and converted Markdown. |
| identity_confidence_score | 0.30 | Pulgar/Arriagada identity support is plausible only within the chunk layer; Dario-related identity support is near zero. |
| claim_probability | 0.32 | Overall probability that the staged identity conclusions are canonically usable now is low because row control is unresolved. |
| relevance_level | conditional_high_if_pulgar_row_certified | Pulgar/Arriagada relevance would be high only after image-controlled certification; Burgos/de la Cruz control would make it low for the Pulgar line. |
| relevance_confidence | 0.55 | The relevance assessment is conditional and depends on the missing image. |
| canonical_readiness | not_ready | The evidence must remain staged and held for conversion QA. |

## Claim Probability Detail

| Claim or hypothesis | Probability | Readiness |
| --- | ---: | --- |
| Entry `172` is the Pulgar/Arriagada row described by the assigned chunk. | 0.58 | hold_for_conversion_qa |
| Entry `172` is the Burgos/de la Cruz row described by the converted Markdown. | 0.30 | hold_for_conversion_qa |
| The two derivative layers are describing different physical rows, images, or conversion states under the same target. | 0.88 | needs_source_image_resolution |
| The Pulgar/Arriagada child can be attached to Dario Arturo Pulgar-Smith or another Dario Pulgar candidate from this draft. | 0.02 | not_ready |
| The named Pulgar/Arriagada parents can be promoted as canonical parent-child relationships now. | 0.08 | not_ready |

## Next Action

Keep this staged draft on `hold_for_conversion_qa`. A conversion-QA worker needs to restore or locate the original source image or certified page image, then reread physical entry `172` against both derivative transcripts. Only after row control is certified should proof review reconsider the child name, birth event, father field, mother field, informant field, and any parent-child relationship claims.
