---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260528165723762
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224814036.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224814036.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers only the staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224814036.md`.

## Blockers First

- Conversion-control blocker: the assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth, while the current converted Markdown reads entry 172 as a Burgos/de la Cruz birth. These are mutually incompatible rows, not variants of one identity.
- Canonical-readiness blocker: no identity, parent-child, duplicate-person, or bridge claim should be promoted from this staged draft while the controlling conversion remains disputed.
- Father-field blocker: under the Pulgar/Arriagada reading, the father appears as `Jose del Carmen Pulgar S.` in the chunk/source packet, but the suffix still needs targeted QA before normalization or attachment.
- Relationship-jump blocker: the source does not name Dario, Arturo, Smith, Dario Jose, or Dario Pulgar. Any use of this row as a bridge to a Dario candidate would be unsupported by this record alone.
- Source-boundary blocker: this proof review can say the image spot-check favors the Pulgar/Arriagada row, but it should not rewrite the converted Markdown or certify a fresh full transcription.

## Evidence Checked

- Staged identity/conflict analysis named above.
- Source packet `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md`.
- Assigned chunk `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, checked only for row-control support.

## Evidence Strengths

- The source is a civil birth register image, a strong primary-source type for birth-registration facts when the row and fields are certified.
- The chunk and source packet agree that page 58, entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
- The source image spot-check visibly aligns more closely with the Pulgar/Arriagada row than with the Burgos/de la Cruz row for entry 172.
- The staged draft correctly treats the conflict as a row-level conversion problem and keeps the claim on hold rather than promoting a speculative identity conclusion.

## Scored Judgment

| Dimension | Score / value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil registration image is a strong source type, but image legibility and field-level handwriting still require careful QA. |
| conversion_confidence_score | 0.35 | Derivative files materially disagree on the controlling row and several core facts. |
| evidence_quantity_score | 0.55 | One source image plus three derivative artifacts; enough to identify the conflict, not enough to promote. |
| agreement_score | 0.42 | Chunk and source packet agree with each other, but the converted Markdown conflicts on child, parents, birth date, place, and informant. |
| identity_confidence_score | 0.52 | Moderate confidence that the staged analysis identifies the conflict correctly; low confidence for canonical attachment. |
| claim_probability | 0.56 | Pulgar/Arriagada reading is plausible and visually favored, but remains below promotion level because conversion control is unresolved. |
| relevance_level | high | If certified, this row is directly relevant to Pulgar/Arriagada family evidence. |
| relevance_confidence | 0.90 | Relevance is high for Pulgar/Arriagada review and low for Dario-bridge claims. |
| canonical_readiness | not_ready / 0.10 | Hold for conversion QA; do not promote or attach relationships. |

## Claim-Level Review

| Claim or hypothesis | Support | Risk | Probability | Disposition |
| --- | --- | --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by chunk, source packet, and image spot-check. | Current converted Markdown gives a different family for entry 172. | 0.64 | Hold for conversion QA. |
| Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | Supported only by current converted Markdown. | Conflicts with chunk, source packet, and source-image spot-check. | 0.18 | Revise or hold pending QA; not Pulgar-relevant as stated. |
| `Jose del Carmen Pulgar S.` is the father in the Pulgar/Arriagada row. | Supported by chunk/source packet and visually plausible. | Suffix and exact literal reading need certification. | 0.58 | Hold for field-level QA. |
| `Juana Arriagada de Pulgar` is the mother in the Pulgar/Arriagada row. | Supported by chunk/source packet and visually plausible. | Dependent on row-control QA. | 0.62 | Hold for row-control QA. |
| This row bridges to a Dario Pulgar candidate. | No direct source wording names or links a Dario candidate. | High identity-conflation risk from surname overlap alone. | 0.04 | Do not use as bridge evidence. |

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. The next worker should run targeted conversion QA against the source image, converted Markdown, assigned chunk, and source packet for page 1 / register page 58 / entry 172. That QA should decide the controlling row and certify the father field before any narrow birth, parent-child, or identity claim is promoted.
