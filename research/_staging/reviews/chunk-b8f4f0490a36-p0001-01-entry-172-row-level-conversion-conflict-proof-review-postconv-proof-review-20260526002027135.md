---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526002027135"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md"
reviewed_output_area: "research/_staging/reviews/"
canonical_readiness: "hold_for_conversion_qa"
promotion_recommendation: "hold"
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

Review of staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md`.

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The visible source image and assigned chunk support the Pulgar/Arriagada row for entry 172, but the current converted Markdown gives a materially different Burgos/de la Cruz row for entry 172.
2. The conflict changes the child, parents, birth date, birthplace, and informant. This is a conversion-control problem, not a same-person or name-variant problem.
3. The father field is not fully proof-certified from the current staged materials. The visible source supports a father beginning `Jose del Carmen Pulgar`, but the trailing mark/suffix remains uncertain and should not be normalized as `S.` without targeted conversion QA.
4. No Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada identity bridge is supported by this source. The staged draft correctly treats those comparisons as anti-conflation context, not proof.
5. No child identity, birth fact, parent claim, parent-child relationship, parent merge, or canonical wiki update should be promoted from this staged draft until the conversion conflict is resolved.

## Evidence Checked

- Staged identity/conflict analysis: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md`.
- Referenced assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

The source image shows page 58, row 172 as a Pulgar/Arriagada birth registration. The child field visibly reads as `Jose del Carmen Segundo Pulgar Arriagada`; the sex field is `Hombre`; the birth date field reads `Ocho de Marzo...`; the mother field reads `Juana Arriagada de Pulgar`; and the compareciente field reads `Ernesto Herrera L.` with `Presente al nacimiento`. This agrees with the assigned chunk and source packet.

The current converted Markdown is internally coherent as a different transcription, but it does not match the visible row 172 on the referenced image. It records `José Miguel`, father/informant `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, which are not the visible Pulgar/Arriagada row.

The staged identity analysis is therefore well supported in its main judgment: hold the item because derivative files disagree and because the conversion artifact must be corrected or superseded before claims are made canonical.

## Scores

| Dimension | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong original/near-original source for the row contents. |
| conversion_confidence_score | 0.42 | The assigned chunk aligns with the image, but the canonical converted Markdown materially conflicts with both. |
| evidence_quantity_score | 0.64 | One source image plus derivative chunk/source packet are enough to identify the conflict, but not enough to promote identity bridges. |
| agreement_score | 0.48 | Source image, chunk, and source packet agree; converted Markdown disagrees on every material field for entry 172. |
| identity_confidence_score | 0.52 | Moderate confidence that the row is Pulgar/Arriagada; low confidence for attaching the people to canonical identities. |
| claim_probability | 0.61 | The Pulgar/Arriagada row is more likely the correct row 172 reading than the converted Markdown row, but the claim remains blocked by conversion QA. |
| relevance_level | 0.98 | Directly relevant to Pulgar/Arriagada birth, parent, and relationship claims from entry 172. |
| relevance_confidence | 0.96 | The row includes the exact Pulgar and Arriagada names under review. |
| canonical_readiness | 0.08 | Hold for conversion QA; not ready for canonical claims or relationships. |

## Claim Probability And Identity Risk

| Claim or hypothesis | Probability | Identity risk | Review judgment |
| --- | ---: | --- | --- |
| Entry 172 on the visible source image is the Pulgar/Arriagada row described by the chunk/source packet. | 0.72 | Medium | Supported enough to flag conversion error/control conflict; still needs targeted QA for corrected transcription. |
| The current converted Markdown's Burgos/de la Cruz entry controls this staged Pulgar/Arriagada task. | 0.12 | High | Not supported by the visible referenced image for row 172. |
| The child in the Pulgar/Arriagada row is `Jose del Carmen Segundo Pulgar Arriagada`. | 0.68 | Medium | Visibly and derivatively supported, but should remain staged until conversion control is resolved. |
| The father should be recorded exactly as `Jose del Carmen Pulgar S.`. | 0.45 | High | The name beginning is supported; the trailing element is not sufficiently certified in this review. |
| The mother is `Juana Arriagada de Pulgar`. | 0.70 | Medium | Supported for the row, but not yet a canonical identity bridge to any other Juana candidate. |
| This row supports any Dario Pulgar identity bridge. | 0.03 | High | Not supported; surname/family context only. |

## Required Boundary Between Verification And Transcription

This review verifies that the staged draft correctly identifies a row-level conflict and recommends hold. It does not amend the converted Markdown, chunk, source packet, or canonical pages. The father-field reading should be double-checked in a conversion QA task; it should not be silently changed or normalized from this proof review.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image and converted Markdown. The QA output should explicitly decide the controlling entry-172 transcription and certify the father field exactly as visible. After QA, rerun separate proof review for child identity, birth facts, father claim, mother claim, and parent-child relationship before any canonical promotion.
