---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526021148421
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
reviewed_staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
canonical_readiness: hold_for_conversion_qa
created: "2026-05-26"
---

# Proof Review: Entry 172 Row-Level Conversion Conflict Identity Analysis

## Blockers

- Row-control remains unresolved between the referenced converted Markdown and the chunk/source-packet/image evidence. The converted Markdown records entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the chunk, source packet, and visible page image support a Pulgar/Arriagada row for entry 172.
- Canonical relationship or identity promotion is blocked because the conflict changes the child, parents, birth date, birth time, place, residence context, and informant. This is not a minor transcription variant.
- The father field is not safe for a finalized canonical name beyond the visible start `Jose del Carmen Pulgar`; the suffix or trailing mark remains unresolved between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- The staged analysis correctly treats Dario-line attachment as unsupported. The visible entry names `Jose del Carmen Segundo Pulgar Arriagada`, not any Dario candidate, and provides no identity bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.
- Parent-identity merges are blocked. This evidence does not prove that `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person, nor that all `Jose del Carmen Pulgar` references in local context identify the same man.

## Scoring

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is an original-style source for birth registration facts, with direct page and entry context visible. |
| conversion_confidence_score | 0.46 | The chunk and source packet align with the visible image, but the current converted Markdown is materially contradictory. |
| evidence_quantity_score | 0.62 | One primary page image plus derivative chunk/source-packet support; no independent corroborating record for identity merges. |
| agreement_score | 0.54 | Strong agreement among image, chunk, and source packet; severe disagreement with the referenced converted Markdown. |
| identity_confidence_score | 0.72 | Good confidence that the visible entry-172 child is a Pulgar/Arriagada child, reduced by unresolved row-control and father-suffix QA. |
| claim_probability | 0.74 | The staged hold-for-QA conclusion is probable and well supported; canonical facts remain withheld. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parentage, and useful as an anti-conflation checkpoint for Dario candidates. |
| relevance_confidence | 0.93 | The surnames, entry number, page, and staged evidence make the relevance clear. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical claim, relationship, merge, or wiki promotion. |

## Evidence Strengths

- The staged draft accurately identifies the controlling proof problem: the same entry number is represented by two incompatible row readings.
- The source packet explicitly documents the conflict and recommends `hold_for_conversion_qa`, which is appropriate for the evidence state.
- The referenced chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- Direct visual review of the referenced page image supports the Pulgar/Arriagada row at page 58, entry 172, and does not support the Burgos/de la Cruz converted-row reading for that visible row.
- The staged analysis appropriately avoids promoting Dario identity claims or parent merges from surname resemblance alone.

## Review Judgment

The staged identity/conflict analysis is supported as a proof-review judgment. Its main conclusion should remain `hold_for_conversion_qa`: the Pulgar/Arriagada reading is likely the correct visible row for page 58, entry 172, but the workspace still contains a contradictory converted Markdown reading for the same entry number. Until that row-control conflict is resolved, no child identity, birth fact, parent-child relationship, parent merge, or Dario-line comparison is canonical-ready.

Claim probability is moderately high for the narrow conclusion that the staged conflict analysis correctly identifies a row-level conversion conflict and recommends holding the evidence. Claim probability is not high enough for canonical fact promotion because the derivative conversion conflict remains active.

## Next Action

Run targeted conversion QA against the source image, the converted Markdown, and `CHUNK-b8f4f0490a36-P0001-01` to certify the controlling row for entry 172 and the exact father-field reading. After QA resolves row control, rerun proof review before any promotion to canonical claims, relationships, people, families, or wiki pages.
