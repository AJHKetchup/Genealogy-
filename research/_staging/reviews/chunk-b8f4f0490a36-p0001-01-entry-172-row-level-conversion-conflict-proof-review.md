---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525234628432
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
reviewed_staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- The staged identity analysis correctly identifies a material row-control conflict. The assigned chunk/source packet present entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, while the converted Markdown presents entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The conflict is not a same-person variant. The two readings differ on child name, birth date, birthplace, father, mother, informant, and residence details.
- The father field in the Pulgar/Arriagada reading is not proof-ready beyond a bounded QA question. The chunk/source packet give `Jose del Carmen Pulgar S.`, but the staged analysis properly keeps the final element unresolved.
- No Dario attachment is supported by this source. The visible/referenced row names a Jose/Juana/child cluster, not Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Darío Pulgar Arriagada.
- Parent-child claims, parent identity merges, and Pulgar/Arriagada-to-Pulgar-Smith bridge claims must remain staged until conversion QA reconciles the converted Markdown, chunk, source packet, and image.

## Scoring

- source_quality_score: 0.87
- conversion_confidence_score: 0.36
- evidence_quantity_score: 0.62
- agreement_score: 0.40
- identity_confidence_score: 0.63
- claim_probability: 0.72 for the Pulgar/Arriagada row being the visible entry-172 row; 0.40 for the exact father suffix `S.`
- relevance_level: high for Pulgar/Arriagada family reconstruction; low for any Dario identity claim
- relevance_confidence: 0.88 for Pulgar/Arriagada relevance; 0.95 that direct Dario relevance is unsupported
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The staged draft is well bounded: it treats the problem as row-control/conversion-control conflict rather than promoting a person, relationship, or merge.
- The source packet and chunk agree with each other on the Pulgar/Arriagada row: registration date 7 April 1888, child `Jose del Carmen Segundo Pulgar Arriagada`, birth 8 March 1888 at 3 p.m., father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The converted Markdown is internally coherent for a different entry-172 family, which helps explain why this must be treated as a conversion-control issue rather than a simple name uncertainty.
- Visual review of the referenced page image supports the staged analysis' concern that the current converted Markdown and the assigned chunk are not describing the same row.
- The staged draft explicitly separates literal readings from identity hypotheses and assigns low readiness to Dario attachment, Jose/Juana merges, and parent-child promotion.

## Review Judgment

The staged identity analysis is supported as a conflict analysis and should remain on hold. The probability is moderately high that the Pulgar/Arriagada row exists in the referenced image and assigned chunk, but the derivative converted Markdown still records a different entry-172 family. That disagreement prevents canonical promotion even where the Pulgar/Arriagada reading appears plausible.

The review accepts the staged draft's main conclusion: this is a row-level conversion conflict requiring targeted conversion QA. It does not support canonical person creation, relationship promotion, father-suffix certification, mother-name merging, or any Dario identity bridge from this draft alone.

## Next Action

Send to targeted conversion QA for entry 172. QA should decide whether the controlling row is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and if the Pulgar/Arriagada row controls, certify the father field only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review before promoting any child identity, birth fact, parent-child relationship, Jose/Juana identity merge, or Dario-related bridge.
