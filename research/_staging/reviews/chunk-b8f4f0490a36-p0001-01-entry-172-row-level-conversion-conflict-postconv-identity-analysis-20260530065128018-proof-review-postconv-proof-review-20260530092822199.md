---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530092822199
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md"
reviewed_sources:
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
  - "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
  - "research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png"
  - "research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-bottom-postconv-evidence-extraction-20260529000036877.png"
source_quality_score: 0.62
conversion_confidence_score: 0.50
evidence_quantity_score: 0.58
agreement_score: 0.43
identity_confidence_score: 0.70
claim_probability: 0.68
relevance_level: direct
relevance_confidence: 0.96
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md`.
- The raw source PNG referenced by the chunk, packet, and manifests was not present at either checked `raw/sources/` path.
- The conversion job page image referenced in the manifest was also not present at `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`.
- Because the full page image is unavailable in this checkout, this proof review cannot certify physical row control for entry `172`.
- The assigned chunk and current converted Markdown materially disagree for entry `172`; this is a row-control conflict, not a spelling or identity-variant issue.
- The father-field suffix after `Jose del Carmen Pulgar` remains unresolved. The visible crop supports the base Pulgar parent field but does not make the trailing mark promotion-ready.
- No canonical claim, relationship, identity merge, Dario-line bridge, or wiki update is ready from this evidence set.

## Evidence Reviewed

- The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`.
- The current converted Markdown reads entry `172` as `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, informant `Oswaldo Burgos`.
- The source packet correctly preserves the conflict and recommends `hold_for_conversion_qa`.
- The conversion review note correctly states that original-image certification was unavailable and that the staged crop supports only the lower parent/informant fields for the Pulgar/Arriagada row.
- The inspected staged crops visibly support the presence of the Pulgar/Arriagada parent and informant area, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`, but they do not show enough full-row context to independently certify the full entry number, child name, birth details, and row boundaries.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | Civil birth registration is a strong source type, but only derivative files and partial staged crops were available; the original/full page image was missing. |
| conversion_confidence_score | 0.50 | The chunk is internally coherent and partly supported by crops, while the canonical converted Markdown conflicts on all identity-bearing fields. |
| evidence_quantity_score | 0.58 | There are multiple derivative materials plus two crops, but no full source image for independent row-control verification. |
| agreement_score | 0.43 | The chunk, packet, and QA note agree with each other; the converted Markdown directly disagrees. |
| identity_confidence_score | 0.70 | The Pulgar/Arriagada staged identity is plausible as a row reading, but not proof-ready without full row control. Same-person linkage to Burgos/de la Cruz or Dario candidates is unsupported. |
| claim_probability | 0.68 | Probable staged Pulgar/Arriagada reading pending original-image/full-page QA; not enough for canonical promotion. |
| relevance_level | direct | The reviewed materials directly address the assigned entry `172` conflict. |
| relevance_confidence | 0.96 | All reviewed materials concern the exact staged draft, chunk id, and entry number. |
| canonical_readiness | blocked | Full original-image or full-page row-control QA is required before promotion. |

## Identity And Relationship Risk

- Treat `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` Burgos/de la Cruz as separate competing row-control readings, not as variants or duplicates.
- Do not attach Burgos/de la Cruz parents to the Pulgar child.
- Do not attach the Pulgar/Arriagada row to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar-Arriagada`; the reviewed source context contains no direct Dario bridge.
- Do not merge `Juana Arriagada de Pulgar` with similarly named Juana candidates from other clusters from this task alone.

## Evidence Strengths

- The staged draft accurately identifies the central conflict between the assigned chunk and converted Markdown.
- The source packet and conversion review note appropriately preserve uncertainty rather than forcing a correction.
- The staged crop evidence supports the lower parent/informant section of the Pulgar/Arriagada reading.
- The recommendation to hold for conversion QA is proportionate to the evidence and conflict severity.

## Next Action

Keep the staged draft at `hold_for_conversion_qa` / `canonical_readiness: blocked`. A later worker must inspect the original source PNG or a complete full-page image for register page 58 and certify physical row `172`, including row boundaries, child name, birth date/time/place, parent fields, informant field, and the unresolved mark after `Jose del Carmen Pulgar`.
