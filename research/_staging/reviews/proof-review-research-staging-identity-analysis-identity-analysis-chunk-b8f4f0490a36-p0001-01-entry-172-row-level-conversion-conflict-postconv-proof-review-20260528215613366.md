---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260528215613366"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md"
output_area: "research/_staging/reviews/"
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold
source_quality_score: 0.82
conversion_confidence_score: 0.38
evidence_quantity_score: 0.62
agreement_score: 0.44
identity_confidence_score: 0.54
claim_probability: 0.60
relevance_level: high
relevance_confidence: 0.96
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225648188.md`.

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The source image and assigned chunk support a Pulgar/Arriagada entry 172, but the current converted Markdown for the same converted file reads a different entry 172 with Burgos/de la Cruz names.
2. The current converted Markdown cannot be used as literal support for the Pulgar/Arriagada claims because it names `Jose Miguel`, father/informant `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
3. The conflict is row-control/conversion-control, not a name variant or same-person conflict. The child name, parents, birth date, birthplace, and informant differ.
4. The father field in the Pulgar/Arriagada row remains uncertified at fine detail. The visible source supports a father name beginning `Jose del Carmen Pulgar`, but the final suffix/mark should remain subject to targeted conversion QA rather than silent normalization.
5. No child identity, parent identity, parent-child relationship, duplicate merge, Dario-line bridge, or canonical wiki update should be promoted from this staged draft.

## Evidence Checked

- Staged identity analysis named above.
- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

The source image visibly places entry 172 on page 58 as a Pulgar/Arriagada registration: child `Jose del Carmen Segundo Pulgar Arriagada`, sex male, birth on 8 March 1888 at about 3 p.m., place `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`. The assigned chunk and source packet agree with that row-level reading.

The staged identity analysis correctly treats the problem as a conversion-control conflict. It does not promote a merge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, Dario/Dario Pulgar Arriagada, or existing Jose/Juana parent candidates.

## Scores

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a direct contemporary source, but the image is handwritten and requires careful row-level reading. |
| conversion_confidence_score | 0.38 | Assigned chunk/source packet and current converted Markdown materially disagree for the same entry number. |
| evidence_quantity_score | 0.62 | One direct source image plus derivative chunk/source packet; no independent corroborating record reviewed for identity bridges. |
| agreement_score | 0.44 | Source image, chunk, and source packet agree with each other, but the controlling converted Markdown disagrees. |
| identity_confidence_score | 0.54 | Moderate confidence for the Pulgar/Arriagada row as visible in the image; low confidence for canonical person attachment. |
| claim_probability | 0.60 | The Pulgar/Arriagada row is probably the visible entry in the referenced image, but derivative conflict blocks proof finality. |
| relevance_level | high | Directly controls Pulgar/Arriagada identity and relationship claims for entry 172. |
| relevance_confidence | 0.96 | The reviewed materials all concern the assigned entry 172 conflict. |
| canonical_readiness | hold_for_conversion_qa | Canonical promotion must wait for targeted conversion QA and then separate claim review. |

## Claim Probability Judgment

The staged draft's central claim is supported as a proof judgment: this is a real row-level conversion conflict, and the correct action is hold for conversion QA. The visible source leans toward the Pulgar/Arriagada row, but the converted file currently asserts a different family. That disagreement prevents canonical use of the identity, birth, parent, or relationship claims until the conversion layer is corrected or otherwise certified.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, source packet, and current converted Markdown. The QA note should explicitly certify the controlling entry-172 row and transcribe the father field only to the visible extent, preserving uncertainty if the suffix after `Pulgar` is not clear. After QA, run separate proof review for any child identity, birth fact, parent claim, relationship claim, or Dario-line identity bridge before canonical promotion.
