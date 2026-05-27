---
type: proof_review
status: completed
role: claim_reviewer
worker: "postconv-proof-review-20260527202636890"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
reviewed_files:
  - "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.68
conversion_confidence_score: 0.25
evidence_quantity_score: 0.52
agreement_score: 0.18
identity_confidence_score: 0.60
claim_probability: 0.84
relevance_level: high
relevance_confidence: 0.88
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold
---

# Proof Review: Entry 172 Derivative Row Conflict Hold

## Blockers

1. Physical row control cannot be independently verified in this review. The referenced source image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` is absent, and the referenced job page image `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` is also absent.
2. The assigned chunk and source packet conflict materially with the current converted Markdown. The chunk/source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted Markdown reads entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
3. The father-field suffix is not promotion-ready. The available derivative chunk gives `Jose del Carmen Pulgar S.`, but this review cannot verify whether the terminal `S.` is a suffix, abbreviation, surname mark, or transcription artifact from the visible source.
4. No reviewed source text for this task names a Dario candidate. Any connection from entry `172` to a Dario-line identity would be an unsupported identity jump from this evidence.

## Scores

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.68 | A civil birth register is strong source material in principle, but this review only had derivative text and no image. |
| conversion_confidence_score | 0.25 | The current conversion and chunk are mutually incompatible for the same entry number. |
| evidence_quantity_score | 0.52 | There are several derivative files, but they reduce to two conflicting transcript families rather than independent corroboration. |
| agreement_score | 0.18 | Agreement is low because the child, parents, birth date, locality wording, and surrounding rows differ between derivatives. |
| identity_confidence_score | 0.60 | Moderate that the draft correctly identifies a conflict and hold state; lower for any positive identity conclusion. |
| claim_probability | 0.84 | High probability that the staged draft's hold recommendation is warranted. |
| relevance_level | high | Entry `172` is directly relevant to the Pulgar/Arriagada row-control problem. |
| relevance_confidence | 0.88 | The staged draft, source packet, chunk, and converted file all reference the same assigned entry/chunk. |
| canonical_readiness | hold_for_conversion_qa | No canonical claim, relationship, merge, rename, or source promotion should proceed from this review. |

## Evidence Strengths

- The staged draft accurately identifies the central derivative conflict: the chunk/source packet and converted Markdown cannot both be literal transcripts of the same physical entry `172`.
- The draft's hold recommendation is directly supported by the source packet and conflict note, both of which already flag missing image review and conversion QA concern.
- The draft correctly treats the Pulgar/Arriagada reading as plausible from the assigned chunk while keeping the current Burgos/de la Cruz converted Markdown from controlling canonical promotion.
- The draft correctly avoids a Dario attachment; no reviewed task source names Dario, Arturo, or an equivalent Dario-line identity.

## Review Judgment

The staged draft is supported as a conflict/hold analysis, not as proof of a promoted identity or relationship. Its central claim should be read as: entry `172` has unresolved derivative row control and must remain held for conversion QA. The Pulgar/Arriagada reading has better task relevance because it is present in the assigned chunk and source packet, but it is not independently image-certified in this review.

The Burgos/de la Cruz reading remains a live conflicting derivative reading only because it appears in the current converted Markdown. It should not be promoted as controlling entry `172` unless later source-image review proves that the converted Markdown is the correct physical row.

## Next Action

Keep the staged draft at `hold_for_conversion_qa`. The next required action is targeted image-level conversion QA for physical entry `172`, including explicit resolution of whether the entry is the Pulgar/Arriagada row or the Burgos/de la Cruz row and whether the father field should be recorded as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain variant.

Do not promote any child identity, parent-child relationship, parent identity attachment, Dario bridge, or canonical wiki update from this staged draft until that image-level row-control review is available.
