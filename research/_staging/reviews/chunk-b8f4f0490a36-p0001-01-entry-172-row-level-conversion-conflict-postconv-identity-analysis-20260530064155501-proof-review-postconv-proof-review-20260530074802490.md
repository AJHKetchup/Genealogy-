---
type: proof_review_note
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530074802490
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md`.
- The original source PNG is not available in this checkout at either cited spelling tested from the referenced materials, so I cannot freshly certify the full physical page image.
- The converted Markdown and assigned chunk materially disagree for entry `172`. The converted Markdown gives `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. The assigned chunk gives `Jose del Carmen Segundo Pulgar Arriagada`, father field `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888.
- This is a row-control/conversion conflict, not a name variant. The staged identity analysis correctly blocks canonical promotion and warns against attaching Burgos/de la Cruz facts to the Pulgar/Arriagada child.
- The father suffix after `Jose del Carmen Pulgar` remains insufficiently certified for canonical use. The bounded base reading `Jose del Carmen Pulgar` is better supported than the suffix.
- No relationship bridge to any Dario Pulgar identity is proved by the verified materials reviewed here.

## Evidence Strengths

- The staged draft's conflict summary is directly supported by the referenced converted Markdown, which assigns entry `172` to the Burgos/de la Cruz child.
- The assigned chunk directly supports the Pulgar/Arriagada reading for entry `172`, including child name, sex, registration date, birth date/time/place, parents, and informant.
- The referenced conversion-review note and source packet consistently describe the same row-control conflict and recommend `hold_for_conversion_qa`.
- The referenced staged crop assets are present. Visual inspection of the parent/informant crop supports the Pulgar/Arriagada parent and informant fields: `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`. The crop does not independently settle the full row-control question because the original full source page is unavailable.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | Civil registration is a strong source type, but this review could inspect only derivative conversion/chunk files and staged crops, not the original full page image. |
| conversion_confidence_score | 0.48 | The assigned chunk and crop assets support Pulgar/Arriagada, but the canonical converted Markdown remains in direct conflict. |
| evidence_quantity_score | 0.58 | Multiple staged artifacts agree on the conflict and Pulgar reading, but there is no fresh original-image certification. |
| agreement_score | 0.42 | Agreement is good among staged Pulgar-focused artifacts and poor between those artifacts and the converted Markdown. |
| identity_confidence_score | 0.73 | The draft is persuasive that the Pulgar/Arriagada and Burgos/de la Cruz readings should not be merged; confidence is reduced for any positive canonical identity claim. |
| claim_probability | 0.70 | Probable that the staged Pulgar/Arriagada row reading reflects the intended assigned chunk, but not ready for canonical assertion. |
| relevance_level | high | The draft directly addresses a row-level conflict for a family-relevant Pulgar/Arriagada entry and prevents a false merge. |
| relevance_confidence | 0.90 | The materials reviewed are exactly the staged draft and cited verification artifacts for this task. |
| canonical_readiness | 0.15 | Blocked pending original-image row-control QA and repair or annotation of the conflicting converted Markdown. |

## Review Decision

Canonical readiness: `blocked`.

Recommended disposition: keep the staged identity analysis at `hold_for_conversion_qa`. Do not promote birth facts, parent-child relationships, or identity bridges from this item into canonical claims, relationships, person pages, family pages, or broader Dario-line analysis until original-image row-control QA certifies which entry `172` reading controls.

## Next Action

Run targeted original-image row-control certification for `CHUNK-b8f4f0490a36-P0001-01`, register page `58`, physical row entry `172`. The certifying worker should explicitly decide whether the controlling father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or a bounded uncertain form, and should preserve the Burgos/de la Cruz text only as a competing conversion artifact unless the full source image supports it for this physical row.
