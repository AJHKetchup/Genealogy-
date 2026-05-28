---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528174144159
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-identity-analysis-20260528170836626.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-identity-analysis-20260528170836626.md"
reviewed_context:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-evidence-extraction-20260528133324374.md"
  - "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260528133324374.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.82
conversion_confidence_score: 0.34
evidence_quantity_score: 0.58
agreement_score: 0.38
identity_confidence_score: 0.62
claim_probability: 0.74
relevance_level: high
relevance_confidence: 0.94
canonical_readiness: blocked
recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Row Conflict Revision

## Blockers First

- The exact staged draft reviewed is `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-identity-analysis-20260528170836626.md`.
- Canonical readiness is blocked. The source image and assigned chunk support physical entry `172` as a Pulgar/Arriagada registration, but the assigned converted Markdown records entry `172` as a Burgos/de la Cruz registration. This derivative row-control conflict is unresolved.
- The staged draft's hold recommendation is supported. No child identity, parent-child relationship, same-person merge, Dario-line attachment, or wiki update should proceed from this evidence until conversion QA identifies the controlling row.
- The father-name claim must remain bounded. The image and source packet support `Jose del Carmen Pulgar` at the current review level; the chunk's trailing `S.` is not secure enough for promotion.
- Same-person claims connecting entry `172` child `Jose del Carmen Segundo Pulgar Arriagada` to any Dario, Arturo, Pulgar-Smith, or later Pulgar-Arriagada candidate are not supported by the reviewed source context.

## Evidence Strengths

- The original source image visibly places physical entry `172` on page 58 in the Pulgar/Arriagada row. The row includes child `Jose del Carmen Segundo Pulgar Arriagada`, male sex, registration date 7 April 1888, birth date 8 March 1888, birth place Calle de Valdivia, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and declarant `Ernesto Herrera L.`.
- The assigned chunk agrees with the Pulgar/Arriagada row and preserves the relevant literal fields, including the child, parents, birth event, and declarant.
- The source packet explicitly preserves the conflict instead of silently correcting the converted Markdown. That is the right treatment for this stage.
- The staged identity analysis accurately treats the Burgos/de la Cruz converted entry as a blocker rather than as a mere variant.

## Scored Judgment

| factor | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a strong original source for a birth registration, though the image is high contrast and some handwriting remains hard to certify. |
| conversion_confidence_score | 0.34 | Low because the converted Markdown and chunk disagree on the entire entry set for the same source path/hash. |
| evidence_quantity_score | 0.58 | One direct source image plus derivative chunk/source packet support the conflict finding, but there is no independent corroborating source for identity bridging. |
| agreement_score | 0.38 | Image, chunk, and packet agree with each other; converted Markdown materially conflicts. |
| identity_confidence_score | 0.62 | Confidence is moderate for the literal Pulgar/Arriagada row reading, but low for any downstream identity attachment beyond the row. |
| claim_probability | 0.74 | The staged draft's claim that this is a derivative row-control conflict is likely correct. The underlying promotable genealogical facts remain on hold. |
| relevance_level | high | Pulgar and Arriagada names make the row materially relevant to the family research cluster. |
| relevance_confidence | 0.94 | Relevance is clear from the surnames and parent-child registration context. |
| canonical_readiness | blocked | Conversion QA must resolve row control before promotion or canonical edits. |

## Claim-Level Review

| reviewed claim or hypothesis | support | probability | canonical_readiness |
| --- | --- | ---: | --- |
| Physical entry `172` is a Pulgar/Arriagada registration. | Supported by source image, chunk, and source packet; opposed by converted Markdown. | 0.78 | blocked |
| The converted Markdown's Burgos/de la Cruz entry is a derivative-row conflict for this task. | Supported by direct comparison of converted Markdown against image/chunk/source packet. | 0.86 | hold_for_qa |
| Father is recorded as `Jose del Carmen Pulgar`. | Supported at bounded level by image and source packet. | 0.72 | blocked |
| Father is recorded as `Jose del Carmen Pulgar S.`. | Present in chunk, but not certified by source packet or this visual review. | 0.42 | blocked |
| Mother is recorded as `Juana Arriagada de Pulgar`. | Supported by image, chunk, and source packet, subject to row-control QA. | 0.76 | blocked |
| Entry 172 child is a Dario/Pulgar-Smith/Pulgar-Arriagada later identity. | No direct support in reviewed context; given-name and bridge evidence are missing. | 0.04 | blocked |
| `Juana Arriagada de Pulgar` should merge with `Juana de Dios Amagada de Pulgar`. | No support in reviewed context. | 0.12 | blocked |

## Source Reliability And Conversion Confidence

The source image is the best available evidence and is stronger than either derivative transcription. It supports the row-control concern in the staged draft. The converted Markdown is unreliable for this assignment because it transcribes entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. The assigned chunk is more consistent with the visible image for physical entry `172`, but the presence of conflicting derivative outputs keeps conversion confidence low.

## Relationship And Identity Risk

Relationship jumps are the main risk. The row can support a narrow parent-child registration only after QA resolves the row-control conflict; it cannot support a same-person bridge to any Dario candidate. The staged draft correctly avoids promoting parent merges, Dario attachments, and normalized father suffix claims.

## Next Action

Run targeted conversion QA on the exact source image, converted Markdown, and chunk for page 58 entry `172`. QA should decide the controlling derivative transcription, explain why the converted Markdown and chunk diverge, and certify whether the father field is only `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical promotion.
