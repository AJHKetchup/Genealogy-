---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526002449991"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md"
output_area: "research/_staging/reviews/"
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.82
conversion_confidence_score: 0.38
evidence_quantity_score: 0.62
agreement_score: 0.52
identity_confidence_score: 0.56
claim_probability: 0.64
relevance_level: high
relevance_confidence: 0.98
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

Review of staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md`.

## Blockers First

1. Canonical promotion remains blocked. The current converted Markdown and the assigned chunk do not agree on the family represented by entry 172.
2. The visible source image supports the Pulgar/Arriagada row for page 58, entry 172, but the canonical conversion artifact still records entry 172 as a Burgos/de la Cruz birth. That artifact conflict must be resolved by targeted conversion QA before any claim is promoted.
3. The father field is not fully proof-certified. The visible row supports a father beginning `Jose del Carmen Pulgar`, but the final trailing element should not be normalized or expanded until QA decides whether it reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. No relationship bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada is supported by this reviewed row. Any such bridge would require separate evidence.
5. Existing Jose/Juana wiki context cannot resolve this row-control problem and should not be used to merge parent identities from this source.

## Evidence Reviewed

- Staged identity analysis: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md`.
- Underlying conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source is a civil birth register image, a strong source type for names, dates, places, and parent-child assertions when the row is correctly controlled.
- The source image visibly places row `172` on page 58 beside a child name read as `Jose del Carmen Segundo Pulgar Arriagada`, with parents in the Pulgar/Arriagada fields and compareciente `Ernesto Herrera L.`.
- The assigned chunk and source packet agree with the visible source image on the Pulgar/Arriagada row-level reading.
- The staged identity analysis correctly treats the issue as a row-level conversion-control conflict rather than a same-person merge or ordinary name variant.
- The staged identity analysis correctly keeps Dario/Pulgar-line context as anti-conflation context rather than proof of identity.

## Scored Judgment

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration is strong, and the image is available, but the handwriting and derivative conflict reduce usable certainty. |
| conversion_confidence_score | 0.38 | The assigned chunk matches the visible source image better than the converted Markdown, but the official converted file is materially wrong or mismatched for this row. |
| evidence_quantity_score | 0.62 | One direct source image plus multiple derivative notes; enough to identify the conflict, not enough for canonical promotion while conversion control is unresolved. |
| agreement_score | 0.52 | Source image, chunk, and source packet agree; converted Markdown disagrees completely. |
| identity_confidence_score | 0.56 | Moderate confidence for the Pulgar/Arriagada row as the intended entry 172; low confidence for attaching this to any canonical person identity. |
| claim_probability | 0.64 | The Pulgar/Arriagada reading is more probable than the Burgos/de la Cruz reading for the referenced image, but still held because of artifact conflict and father-field uncertainty. |
| relevance_level | high | The row directly controls Pulgar/Arriagada child, parent, birth, and relationship claims. |
| relevance_confidence | 0.98 | The staged draft is highly relevant to the exact row-control problem. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until the converted artifact or QA note resolves entry 172 row control and father-field transcription. |

## Claim-Level Review

| Claim or hypothesis | Probability | Support | Limits |
| --- | ---: | --- | --- |
| Entry 172 in the referenced source image is the Pulgar/Arriagada row. | 0.78 | Visible source image, assigned chunk, and source packet align. | Converted Markdown gives a different family, so conversion QA must adjudicate the artifact conflict. |
| The Burgos/de la Cruz converted Markdown row is controlling for this task. | 0.12 | It appears in the current converted Markdown. | It is not supported by the visible source image reviewed for this exact source path. |
| The child name is `Jose del Carmen Segundo Pulgar Arriagada`. | 0.72 | Visible row and chunk support this reading. | Still tied to row-control QA before canonical use. |
| The mother is `Juana Arriagada de Pulgar`. | 0.68 | Visible row and chunk support this reading. | Does not prove identity with any existing Juana page. |
| The father is `Jose del Carmen Pulgar` with possible trailing `S.` or uncertainty. | 0.60 | Visible row and chunk support the beginning of the name. | Trailing element remains uncertified; do not normalize. |
| This row supports any Dario identity bridge. | 0.03 | Only broad Pulgar surname context. | No Dario, Arturo, Smith, chronology bridge, or explicit relationship appears in this row. |

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, source packet, and current converted Markdown. The QA decision should explicitly state whether entry 172 controls as the Pulgar/Arriagada row and should certify the father field exactly as visible. After QA, create separate proof reviews for the child identity, birth facts, mother claim, father claim, and parent-child relationships before any canonical promotion.
