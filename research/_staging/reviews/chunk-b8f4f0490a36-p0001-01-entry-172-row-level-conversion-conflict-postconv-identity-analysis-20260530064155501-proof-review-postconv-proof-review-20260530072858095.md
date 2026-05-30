---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530072858095
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064155501.md`.
- The original source PNG referenced by the source packet, chunk manifest, and conversion review is not present in this checkout under either the accented or unaccented `raw/sources/` path checked.
- The assigned chunk records entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888 at three in the afternoon at Calle de Valdivia.
- The converted Markdown records entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at ten at night in `En esta`.
- These are incompatible row-control readings, not spelling variants or a same-person identity conflict.
- Existing staged crop images visibly support the Pulgar/Arriagada parent and informant area, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`, but they do not provide a complete fresh original-image certification for the whole row.
- The possible suffix after `Jose del Carmen Pulgar` is not promotion-ready from the reviewed crop context.
- No reviewed evidence supports attaching this entry directly to any Dario Pulgar identity, Smith line, spouse, child, or descendant bridge.

## Scores

| Metric | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.72 | Civil birth register is a strong source type, but this review could not inspect the original source image. |
| conversion_confidence_score | 0.45 | The chunk and converted Markdown materially disagree on entry 172; crop support is partial. |
| evidence_quantity_score | 0.58 | Multiple local derivatives and two crop assets support the conflict assessment, but one full original-image check is missing. |
| agreement_score | 0.34 | Agreement is strong among staged Pulgar/Arriagada derivatives, but the canonical converted Markdown conflicts on the controlling row. |
| identity_confidence_score | 0.76 | Probable that the staged Pulgar/Arriagada row is the intended local subject; not enough to promote as resolved identity proof. |
| claim_probability | 0.70 | The Pulgar/Arriagada row reading is more probable than the Burgos/de la Cruz reading for this staged task, but remains blocked. |
| relevance_level | 1.00 | The evidence directly addresses the reviewed row-control and anti-conflation question. |
| relevance_confidence | 0.96 | The reviewed artifacts all concern `CHUNK-b8f4f0490a36-P0001-01`, entry 172, register page 58. |
| canonical_readiness | 0.10 | Blocked pending original-image row-control QA and reconciliation of the converted Markdown conflict. |

## Evidence Strengths

- The assigned chunk gives a coherent row for entry `172`: registration date 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; male; birth 8 March 1888; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- The source packet correctly preserves the row-control conflict and limits the father field to the base name `Jose del Carmen Pulgar` for staged discussion.
- The conversion review accurately warns that the converted Markdown has a different entry 172 and that dependent claims should remain at `hold_for_conversion_qa`.
- The reviewed crop assets are consistent with the Pulgar/Arriagada parent and informant fields and inconsistent with promoting Burgos/de la Cruz facts into the Pulgar row.

## Risk Review

- Literal support: partial. The chunk supports the full Pulgar/Arriagada row; crops support the parent/informant portion; the original page image is unavailable.
- Uncertainty: high for canonical row control, medium for the father's trailing suffix, low that the Burgos/de la Cruz facts should be attached to the Pulgar/Arriagada child.
- Source reliability: the civil register would be high quality if directly visible; derivative conflict lowers present review confidence.
- Conversion confidence: not promotion-ready because the converted Markdown and chunk disagree at child, parents, birth date, birth time, and place.
- Claim confidence: staged Pulgar/Arriagada claim is probable, but only as a hold/revise item.
- Identity risk: high risk of a false composite if Burgos/de la Cruz and Pulgar/Arriagada are merged or treated as name variants.
- Relationship jumps: parent-child claims for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` should not move to canonical form until row-control QA certifies the source image.
- Conflicts: material row-control conflict remains unresolved.
- Relevance: direct to the assigned staged identity-analysis draft.

## Reviewed Determination

The staged draft's central conclusion is supported: this is a row-control conversion conflict, not a same-person or name-variant conflict. The Pulgar/Arriagada reading is the better-supported staged hypothesis from the chunk and crop assets, but the missing original source image and contradictory converted Markdown block canonical use.

Canonical readiness: `blocked`.

Promotion recommendation: `hold_for_conversion_qa`.

## Next Action

Run targeted original-image row-control QA for `CHUNK-b8f4f0490a36-P0001-01`, register page 58, physical row entry 172. The next review should certify the controlling row from the visible source image and explicitly decide whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain bounded form.
