---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260530092033351
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
review_decision: hold
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530065128018.md`.
- The referenced original source PNG is not present at either checked `raw/sources/` path, so this review cannot certify the physical row directly from the full original image.
- The assigned chunk and the current converted Markdown materially disagree for entry `172`.
- The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The current converted Markdown reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- Existing staged crop assets support the Pulgar/Arriagada parent and informant fields, but they are not a complete substitute for full original-image row-control certification.
- The suffix or mark after `Jose del Carmen Pulgar` remains unresolved. Do not promote the suffix as certain.
- No Dario-line identity bridge, same-person merge, parent-cluster merge, or canonical relationship promotion is supported from this staged proof state.

## Evidence Strengths

- The staged draft accurately identifies the conflict as a row-control conflict, not a name-variant conflict.
- The source packet, conversion review note, and assigned chunk agree on the Pulgar/Arriagada reading for the staged row.
- The viewed crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png` visibly supports the presence of `Juana Arriagada de Pulgar` and `Ernesto Herrera` in the relevant lower fields, and is consistent with a father field beginning `Jose del Carmen Pulgar`.
- The viewed crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-bottom-postconv-evidence-extraction-20260529000036877.png` also supports the staged Pulgar/Arriagada parent/informant cluster and confirms that the trailing mark after `Pulgar` should remain cautious.
- The current converted Markdown supplies the opposing Burgos/de la Cruz reading, so the conflict is explicitly documented rather than inferred.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | Civil birth registration is a strong source type, but this review used derivative transcription plus staged crops because the full source PNG is unavailable. |
| conversion_confidence_score | 0.48 | The chunk and crops support Pulgar/Arriagada, while the current converted Markdown gives a different entry 172. |
| evidence_quantity_score | 0.56 | Multiple staged artifacts agree, but all depend on unresolved conversion context and no full-image certification here. |
| agreement_score | 0.50 | Strong agreement inside the staged Pulgar/Arriagada packet; direct disagreement with the converted file. |
| identity_confidence_score | 0.70 | Probable narrow staged identity for the Pulgar/Arriagada child if row control is accepted; not enough for canonical identity attachment. |
| claim_probability | 0.66 | The Pulgar/Arriagada row is more likely than the converted Burgos/de la Cruz reading in this staged packet, but the unresolved row-control conflict prevents promotion. |
| relevance_level | high | The evidence directly addresses the assigned row-level identity conflict. |
| relevance_confidence | 0.95 | The reviewed artifacts all concern entry 172 and the same staged conflict. |
| canonical_readiness | blocked | Hold until full original-image row-control QA resolves which entry 172 reading controls and how to record the father field. |

## Identity And Relationship Risk

- Same-person probability for Pulgar/Arriagada and Burgos/de la Cruz readings: `0.02`; only the entry number overlaps.
- Direct Dario identity-bridge probability from this row: `0.00-0.02`; the row does not name Dario, Arturo, Smith, Alexander, a spouse, a child, or a later-life identifier.
- Stated father claim probability if Pulgar/Arriagada row is certified: `0.68` for base name `Jose del Carmen Pulgar`; suffix unresolved.
- Stated mother claim probability if Pulgar/Arriagada row is certified: `0.70` for `Juana Arriagada de Pulgar`.
- Relationship promotion risk is high until row control is resolved because attaching either parent set canonically could create a false family cluster.

## Next Action

Keep this staged draft at `hold_for_conversion_qa` with `canonical_readiness: blocked`.

Route the source to targeted full original-image row-control QA for register page 58, physical entry 172. The next review should decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and should record the father field conservatively as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` based only on visible source support.

Do not promote claims, relationships, Dario-line attachments, same-person conclusions, wiki updates, or canonical merges from this proof review.
