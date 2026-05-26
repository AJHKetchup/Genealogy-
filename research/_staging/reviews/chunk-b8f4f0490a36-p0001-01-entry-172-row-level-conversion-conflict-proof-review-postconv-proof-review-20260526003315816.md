---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526003315816"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md"
output_area: "research/_staging/reviews/"
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

Review of staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md`.

## Blockers First

1. The controlling conversion remains inconsistent. The current converted Markdown reads entry 172 as a Burgos/de la Cruz birth, while the chunk, source packet, and visible page image support a Pulgar/Arriagada row for page 58, entry 172.
2. Canonical promotion is blocked until conversion QA updates or explicitly supersedes the conflicting converted Markdown. The disagreement changes the child, parents, birth date, birthplace, and informant.
3. The father-field suffix/trailing mark after `Jose del Carmen Pulgar` remains insufficiently certified from this review. It should not be normalized silently to `Jose del Carmen Pulgar S.` or dropped without targeted transcription QA.
4. No identity bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada is supported by this entry. The staged draft correctly treats those as anti-conflation context only.

## Evidence Checked

- Staged identity analysis: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525234359762.md`.
- Staged conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image shows page 58, row 172 as the Pulgar/Arriagada entry, not the Burgos/de la Cruz entry in the current converted Markdown.
- The assigned chunk and source packet agree on the main Pulgar/Arriagada facts: child `Jose del Carmen Segundo Pulgar Arriagada`, male; birth on 8 March 1888 at 3 p.m.; birthplace `Calle de Valdivia`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- The staged identity analysis correctly frames the issue as a row-level conversion-control conflict rather than a same-person merge, name variant, or relationship proof.
- The draft correctly blocks promotion of child identity, birth facts, parent claims, parent-child relationships, and Dario-related identity bridges.

## Scoring

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong source for the event, but this review did not create a corrected source transcription. |
| conversion_confidence_score | 0.42 | The page image and chunk support Pulgar/Arriagada, but the current converted Markdown materially conflicts. |
| evidence_quantity_score | 0.62 | One direct register image plus derivative chunk/source-packet support; no independent corroborating record checked. |
| agreement_score | 0.48 | Image, chunk, and packet agree against the converted Markdown; derivative artifacts are not in full agreement. |
| identity_confidence_score | 0.58 | Moderate confidence for the Pulgar/Arriagada row itself; low confidence for attaching it to any canonical person beyond the row. |
| claim_probability | 0.64 | The claim that entry 172 should be handled as Pulgar/Arriagada is more likely than the converted Burgos/de la Cruz reading, but still blocked by conversion QA. |
| relevance_level | high | Directly controls whether Pulgar/Arriagada birth, parent, and relationship claims can be extracted. |
| relevance_confidence | 0.97 | The row is directly family-relevant if QA certifies the Pulgar/Arriagada reading. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until conversion QA resolves the row and father-field reading. |

## Claim Probability Notes

The visible image, source packet, and chunk make the Pulgar/Arriagada reading the stronger working hypothesis for page 58, entry 172. The current converted Markdown appears to describe a different register spread or row sequence and cannot be used as canonical support for Pulgar claims in its present state.

This review therefore supports the staged draft's hold recommendation. It does not certify the father suffix, does not create a canonical child identity, and does not attach this row to any Dario Pulgar candidate.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the page image, the current converted Markdown, and the assigned chunk. The QA note should decide the controlling entry-172 transcription and separately certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, create separate proof reviews for child identity, birth facts, parent names, and parent-child relationships before any canonical promotion.
