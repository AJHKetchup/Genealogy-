---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260530072500936
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_reference: "page 1; register page 58; physical row entry 172"
review_decision: hold
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md`.
- The referenced original source image is not available in this checkout at either the unaccented source-packet path or the accented chunk metadata path. This review therefore cannot certify the physical row from the original page image.
- The assigned chunk and source packet identify entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, with father field `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The current converted Markdown identifies entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. This is a material row-control conflict, not a name variant.
- The staged crop assets support the Pulgar/Arriagada parent and informant area, but they do not provide full-page row-control certification and do not make the possible suffix after `Jose del Carmen Pulgar` promotion-ready.
- No reviewed source names Dario, Arturo, Smith, Alexander John Heinz, a spouse, a child, or a descendant bridge. Any Dario-line attachment remains unsupported by this entry.

## Evidence Strengths

- The assigned chunk gives a coherent literal row for entry `172`: registration date 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; male; birth 8 March 1888 at three in the afternoon at Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- The source packet accurately preserves the conflict and recommends `hold_for_conversion_qa`.
- The conversion review note correctly frames the conflict as derivative row-control disagreement and states that original-image certification was unavailable.
- The reviewed staged crop visibly supports the base parent/informant readings `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.` at a bounded crop level.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.62 | Civil birth registration is high-quality source type, but this review lacks the original page image and relies on derivative transcription plus staged crop assets. |
| conversion_confidence_score | 0.50 | Chunk and crop support Pulgar/Arriagada, while the current converted Markdown materially disagrees. |
| evidence_quantity_score | 0.58 | Multiple local artifacts were available, but they are not independent original-image certifications. |
| agreement_score | 0.38 | Strong agreement between chunk, packet, QA note, and crop for Pulgar/Arriagada; strong disagreement with converted Markdown for entry 172. |
| identity_confidence_score | 0.70 | Probable that the staged Pulgar/Arriagada row is the intended extraction target, but identity confidence remains reduced by unresolved row control. |
| claim_probability | 0.68 | Pulgar/Arriagada reading is more probable than the Burgos/de la Cruz converted-file reading for this staged task, but not promotion-ready. |
| relevance_level | high | Directly relevant to the staged row-control and anti-conflation question. |
| relevance_confidence | 0.96 | All reviewed artifacts concern the same chunk, entry number, and conflict. |
| canonical_readiness | blocked | Do not promote any claims, relationships, or identity attachments until original-image row-control QA resolves the conflict. |

## Identity And Relationship Risk

- Same-person probability for `Jose Miguel` Burgos/de la Cruz and `Jose del Carmen Segundo Pulgar Arriagada`: `0.02`. Shared entry number in conflicting artifacts is not identity evidence.
- Parent-child claim probability for `Jose del Carmen Pulgar` as father of the Pulgar/Arriagada child: `0.68` staged, `0.10` canonical-ready.
- Parent-child claim probability for `Juana Arriagada de Pulgar` as mother of the Pulgar/Arriagada child: `0.70` staged, `0.10` canonical-ready.
- Probability that this entry directly identifies or bridges to any Dario Pulgar candidate: `0.00` direct, `0.20` possible family-line relevance only if row-control is later certified.
- Relationship jump risk: high if Burgos/de la Cruz facts are attached to the Pulgar/Arriagada child, or if the Pulgar/Arriagada row is attached to Dario-line identities by surname context alone.

## Review Decision

Hold. The staged identity-analysis draft is materially supported as a conflict analysis and anti-conflation warning, but the underlying row-control problem remains unresolved. The safest canonical action is no promotion.

## Next Action

Run targeted original-image row-control QA for `CHUNK-b8f4f0490a36-P0001-01`, register page 58, physical row entry 172. The next reviewer should certify the controlling row from the full source image and separately decide whether the father field supports `Jose del Carmen Pulgar S.`, only `Jose del Carmen Pulgar`, or an uncertain bounded suffix.
