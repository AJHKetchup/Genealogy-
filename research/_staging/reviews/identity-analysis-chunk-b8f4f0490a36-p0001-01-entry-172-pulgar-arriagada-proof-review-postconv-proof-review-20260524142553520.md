---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260524142553520
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
review_status: hold
canonical_readiness: hold_for_conversion_qa
reviewed:
  - research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-postconv-20260524131706940.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.86
conversion_confidence_score: 0.38
evidence_quantity_score: 0.64
agreement_score: 0.46
identity_confidence_score: 0.80
claim_probability: 0.82
relevance_level: critical
relevance_confidence: 0.98
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- canonical_readiness: `hold_for_conversion_qa`. The staged draft is well framed as a conflict/hold identity analysis, but it is not promotion-ready because the assigned converted Markdown and the assigned chunk disagree on entry 172 at the row-identity level.
- The assigned converted Markdown transcribes entry 172 as child `Jose Francisco`, father `Oswaldo Gomez`, and mother `Rosario de la Cruz de la Maza`. The assigned chunk, source packet, and visible source image instead support a Pulgar/Arriagada row for entry 172. This is a material conflict, not a spelling or normalization issue.
- The disagreement affects the child name, parents, birth date/time, birth place, residence, informant, and row context. No child identity, birth claim, parent-child relationship, or broader family relationship should be promoted from this staged draft while the conversion conflict remains unresolved.
- The father-name suffix remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet appropriately preserves `Jose del Carmen Pulgar` and `Jose del Carmen Pulgar S.` as alternate readings pending targeted conversion QA.
- The record does not name Dario. The draft's warning not to merge the child, father, or mother into a Dario Pulgar identity by surname or family context alone is necessary and should remain in force.

## Evidence Strengths

- The source type is strong for identity work: an image of a civil birth registration for Los Angeles/La Laja, Chile, 1888, page 58, entry 172.
- The visible image of page 58, entry 172 is consistent with the chunk and source packet on the Pulgar/Arriagada cluster, including child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The staged draft does not overclaim. It identifies the row-level conflict, preserves the father-suffix uncertainty, and recommends `hold_for_conversion_qa`.
- Relationship-jump risk is controlled because the draft explicitly blocks any Dario Pulgar merge based only on surname or surrounding family context.

## Scores

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Direct civil registration image; relevant row is visible, though dense handwriting requires careful targeted QA. |
| conversion_confidence_score | 0.38 | The chunk aligns with the image, but the controlling converted Markdown contains a materially different entry 172. |
| evidence_quantity_score | 0.64 | One direct image, the chunk, source packet, and converted Markdown were reviewed; no independent corroborating source was used. |
| agreement_score | 0.46 | Image, chunk, source packet, and staged draft mostly agree, but the assigned converted Markdown sharply conflicts. |
| identity_confidence_score | 0.80 | Likely Pulgar/Arriagada identity cluster in the visible row, reduced by derivative conflict and father-suffix uncertainty. |
| claim_probability | 0.82 | High probability that the staged draft is correct as a conflict/hold analysis, not as canonical proof. |
| relevance_level | critical | The issue controls identity, birth facts, and parent-child relationship candidates for this entry. |
| relevance_confidence | 0.98 | All reviewed materials directly concern the same staged draft, chunk id, source image, and entry number. |
| canonical_readiness | hold_for_conversion_qa | Requires conversion QA correction, supersession, or explicit reconciliation before canonical use. |

## Review Judgment

Hold. The staged identity analysis is supported as a conservative review note because it correctly flags the Pulgar/Arriagada versus Gomez/de la Cruz conflict and avoids canonical promotion. The visible source image gives meaningful support to the Pulgar/Arriagada reading, but the unresolved contradiction in the assigned converted Markdown prevents reliable canonical use.

## Next Action

Send to targeted conversion QA for page 58, entry 172. QA should reconcile or supersede the assigned converted Markdown, decide whether the father field visibly includes a final suffix after `Pulgar`, and preserve source-visible spellings for names and residences. After QA, rerun proof review on the child identity, birth facts, and parent-child relationship drafts before any canonical promotion.
