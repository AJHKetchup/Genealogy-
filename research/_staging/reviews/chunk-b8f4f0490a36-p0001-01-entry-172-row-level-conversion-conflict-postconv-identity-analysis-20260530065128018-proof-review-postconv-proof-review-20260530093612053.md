---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530093612053
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md"
reviewed_files:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
  - "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
  - "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png"
  - "research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-bottom-postconv-evidence-extraction-20260529000036877.png"
canonical_readiness: blocked
review_decision: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The exact staged draft reviewed is `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md`.
- The original source PNG referenced by the chunk/source packet is not present under either checked `raw/sources/` path, so this review cannot certify the complete physical row from the original page image.
- The assigned chunk and the current converted Markdown materially disagree for entry `172`.
- The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The converted Markdown reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The available crop images support the Pulgar/Arriagada parent and informant area, but they do not replace complete original-image row-control QA.
- The trailing mark after `Jose del Carmen Pulgar` remains unresolved. It may be carried as staged literal text `Jose del Carmen Pulgar S.`, but promotion-ready wording should remain `Jose del Carmen Pulgar [?]` or omit the suffix until image QA certifies it.
- No canonical claim, relationship, person merge, Dario-line bridge, or wiki update is ready from this staged draft.

## Evidence Strengths

- The staged identity analysis accurately reports the central conflict between the assigned chunk and converted Markdown.
- The source packet and conversion review note are consistent with the assigned chunk on the Pulgar/Arriagada reading.
- The staged crop images visibly support the parent/informant area for the Pulgar/Arriagada row: `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`.
- The staged draft correctly treats Burgos/de la Cruz as a competing derivative row-control reading, not as a spelling variant or same-person hypothesis.
- The anti-conflation guidance is well supported: the record does not identify `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or any Dario/Dario Pulgar identity.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.70 | Civil birth registration is a strong source type, but this review lacks the original full source image and relies on derivative text plus staged crops. |
| conversion_confidence_score | 0.50 | The assigned chunk and crops support Pulgar/Arriagada fields, while the converted Markdown gives a materially different entry 172. |
| evidence_quantity_score | 0.58 | Multiple staged artifacts agree on the conflict and Pulgar/Arriagada reading, but independent original-image confirmation is missing. |
| agreement_score | 0.48 | Agreement is strong among staged extraction artifacts and poor between the chunk and converted Markdown. |
| identity_confidence_score | 0.74 | Pulgar/Arriagada is probable as the staged row reading, but not canonically settled while row control is unresolved. |
| claim_probability | 0.70 | The narrow claim that the staged Pulgar/Arriagada row exists is probable; canonical acceptance remains blocked. |
| relevance_level | 1.00 | The evidence directly concerns the assigned entry 172 conflict. |
| relevance_confidence | 0.98 | All reviewed artifacts are explicitly tied to `CHUNK-b8f4f0490a36-P0001-01` and entry `172`. |
| canonical_readiness | 0.15 | Blocked pending original-image row-control QA and proof acceptance of the father-field wording. |

## Claim-Level Review

| Claim or hypothesis | Probability | Review finding |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row | 0.70 | Supported by the assigned chunk, source packet, conversion QA note, and crop evidence, but held for full original-image row-control QA. |
| Entry 172 is the Burgos/de la Cruz row | 0.28 | Supported only by the current converted Markdown in this review set and contradicted by the assigned chunk/crop-supported staging. |
| Pulgar/Arriagada and Burgos/de la Cruz are the same person or variant readings | 0.02 | Unsupported. Names, parents, date/time/place, and informant differ materially. |
| Entry 172 directly bridges to a Dario Pulgar identity | 0.01 | Unsupported. The reviewed entry does not name Dario or provide a later-life identity bridge. |
| `Juana Arriagada de Pulgar` should be merged with `Juana de Dios Amagada de Pulgar` | 0.05 | Unsupported by this row. Requires separate parent-cluster proof review. |

## Reliability And Risk

- Source reliability is potentially high because the underlying source is a civil birth register, but current review reliability is reduced by absent original-page access.
- Conversion confidence is mixed: the chunk is coherent and crop-supported for the parent/informant area, but the canonical converted Markdown conflicts across the whole row.
- Identity risk is high if this evidence is used to merge or bridge Pulgar identities before row-control QA.
- Relationship risk is high if father/mother links are promoted from the staged draft without resolving the row conflict.
- Relevance is high for the narrow conflict-review task and low for any broader Dario-line claim.

## Next Action

Keep the staged identity analysis at `hold_for_conversion_qa` with `canonical_readiness: blocked`. Route entry `172`, register page `58`, physical row entry `172`, for full original-image row-control QA. The next reviewer should explicitly decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and whether the father field can be certified as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
