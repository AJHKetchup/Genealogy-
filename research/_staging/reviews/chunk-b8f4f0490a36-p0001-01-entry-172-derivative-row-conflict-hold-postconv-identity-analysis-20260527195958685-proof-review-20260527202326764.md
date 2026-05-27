---
type: proof_review
status: completed
role: claim_reviewer
worker: "postconv-proof-review-20260527202326764"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
reviewed_files:
  - "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Row Conflict

## Blockers

1. The staged draft is supported as a hold judgment, not as a canonical claim. The directly reviewed derivatives disagree on the person and family for entry `172`.
2. The assigned chunk and held source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
3. The current converted Markdown reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.
4. The referenced raw source image and job page image are not present in this checkout, so this review cannot independently inspect the handwriting, physical row, or father-field suffix.
5. The available evidence does not name `Dario`, `Dario Arturo`, or a Dario-line identity in entry `172`. Any Dario attachment would be an unsupported identity bridge from this review set.

## Evidence Strengths

- The staged draft accurately identifies a material derivative-row conflict: the child name, parents, birth date, and family cluster differ between the chunk/source-packet reading and the converted Markdown reading.
- The source type is a civil birth register, which would be high-value evidence if the row transcription were image-certified.
- The held source packet correctly preserves the Pulgar/Arriagada reading as derivative evidence while warning that row control is unresolved.
- The staged draft correctly avoids promoting a parent-child relationship, Dario identity bridge, or canonical merge from the conflicting derivatives.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration birth records are strong genealogical sources in principle, but the actual source image was unavailable for this review. |
| conversion_confidence_score | 0.30 | The current converted Markdown and assigned chunk give incompatible entry-172 families; image-level verification is absent. |
| evidence_quantity_score | 0.46 | Several derivatives were available, but they trace to the same unresolved image and conflict rather than independent corroboration. |
| agreement_score | 0.28 | The chunk/source packet agree with each other, but they materially conflict with the converted Markdown for the same entry number. |
| identity_confidence_score | 0.58 | Moderate for treating Pulgar/Arriagada as a plausible held row hypothesis; low for any canonical identity or relationship action. |
| claim_probability | 0.87 | High probability that the staged draft's hold-for-QA conclusion is the correct handling. |
| relevance_level | high | The conflict directly affects a Pulgar/Arriagada family-relevant birth row and parent candidates. |
| relevance_confidence | 0.90 | The reviewed derivatives explicitly contain Pulgar and Arriagada names, even though row control is unresolved. |
| canonical_readiness | hold_for_conversion_qa | Do not promote, merge, rename, or attach relationships from this review. |

## Review Determination

The staged draft is acceptable as a hold analysis. Its central claim is not that the Pulgar/Arriagada row is proven, but that the derivative conflict blocks canonical use until conversion QA or image-level proof review resolves the physical entry `172`.

The Pulgar/Arriagada hypothesis has better family relevance for this workspace than the Burgos/de la Cruz converted reading, but the proof boundary remains hard: this reviewer did not see the source image, and the conversion derivatives cannot be reconciled by assertion. The father suffix should remain unresolved and should not be normalized beyond what a future image review supports.

## Next Action

Keep the item at `hold_for_conversion_qa`. The next worker should perform targeted image-level row control for entry `172`, reconciling the chunk against the converted Markdown and explicitly certifying or rejecting the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain reading. No Dario-line attachment should be made unless a separate identity-bearing source explicitly supports it.
