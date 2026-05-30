---
type: proof_review
status: completed
role: claim_reviewer
worker: "postconv-proof-review-20260530102444060"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
reviewed_context:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
  - "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530072501797.md"
  - "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530072501797.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
  - "research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png"
  - "research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-bottom-postconv-evidence-extraction-20260529000036877.png"
source_quality_score: 0.82
conversion_confidence_score: 0.42
evidence_quantity_score: 0.58
agreement_score: 0.34
identity_confidence_score: 0.62
claim_probability: 0.69
relevance_level: high
relevance_confidence: 0.95
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md`.

## Blockers First

- Full-page source blocker: the referenced source image is not present at either checked path, so this review cannot certify the complete physical row for entry `172`.
- Derivative conflict blocker: the current converted Markdown records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888, while the assigned chunk records entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father field beginning `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, born 8 March 1888.
- Row-control blocker: the assigned chunk and current converted Markdown disagree under the same converted SHA and manifest context. Treat this as a conversion row-control conflict, not a genealogical identity variant.
- Crop-scope blocker: the two staged crop assets visibly support Pulgar/Arriagada parent and informant fields, but they are partial crops and do not replace full-page row-control review.
- Father-name blocker: the visible crop support is sufficient for `Jose del Carmen Pulgar`; the possible trailing suffix after `Pulgar` is not proof-ready from this review.
- Identity bridge blocker: no reviewed source text names Dario, Arturo, Smith, Dario Jose, or a later-life bridge. Do not attach this evidence to any Dario Pulgar candidate.
- Canonical blocker: no birth claim, parent-child relationship, identity merge, Dario-line comparison, or wiki update is ready for canonical promotion from this staged draft.

## Evidence Strengths

- Source type is strong: a civil birth registration is a high-quality source class for birth, parent, and informant facts if row-control is certified.
- The assigned chunk gives internally coherent Pulgar/Arriagada evidence for entry `172`: registration on 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; male sex; birth on 8 March 1888 at 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- The staged crop assets support the parent and informant field region at local visual level, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`
- The conflict draft, source packet, and conversion review note all consistently classify the issue as row-control/conversion QA, not a same-person or relationship proof.
- The staged identity analysis correctly keeps Dario-related links as review leads only and does not promote a Dario identity claim.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration is strong, but the full-page original image is absent for this review. |
| conversion_confidence_score | 0.42 | Local crops and assigned chunk favor Pulgar/Arriagada fields, but the current converted Markdown materially conflicts. |
| evidence_quantity_score | 0.58 | Multiple derivative/staged items and two crops support the issue, but only one underlying registration row is at stake and full-page certification is missing. |
| agreement_score | 0.34 | Agreement is strong among staged packet/QA/chunk/crops, but poor between those materials and the current converted Markdown. |
| identity_confidence_score | 0.62 | Moderate for a row-local Pulgar/Arriagada child if row-control later passes; low for broader family identity linkage. |
| claim_probability | 0.69 | Pulgar/Arriagada is the leading local hypothesis, but unresolved row-control prevents a stronger probability. |
| relevance_level | high | The draft directly addresses the assigned entry `172` conversion conflict. |
| relevance_confidence | 0.95 | Reviewed files and crops all point to the same row-control dispute. |
| canonical_readiness | hold | Not ready for canonical claims, relationships, merges, or wiki edits. |

## Claim Probability Notes

- Probability that the assigned chunk/crop-local Pulgar/Arriagada reading reflects a real row in the source image: `0.78`.
- Probability that entry `172` can be canonically promoted as Pulgar/Arriagada from this review alone: `0.18`.
- Probability that the Burgos/de la Cruz and Pulgar/Arriagada readings are same-person/name-variant evidence: `0.01`.
- Probability that this draft provides direct evidence for any Dario Pulgar identity: `0.02`.

## Next Action

Keep the staged draft at `hold_for_conversion_qa`. The next required action is a targeted full-page original-image row-control review for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, comparing the source image against the converted Markdown, assigned chunk, manifest, source packet, QA note, and staged crop assets. Only after that review certifies the controlling physical row should narrow birth facts and parent-child relationship candidates be reconsidered for proof review.
