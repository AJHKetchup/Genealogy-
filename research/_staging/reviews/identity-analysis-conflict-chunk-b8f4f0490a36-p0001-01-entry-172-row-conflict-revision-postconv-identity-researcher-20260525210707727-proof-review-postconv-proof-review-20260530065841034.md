---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530065841034
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md
reviewed_status: hold
source_quality_score: 0.82
conversion_confidence_score: 0.30
evidence_quantity_score: 0.58
agreement_score: 0.34
identity_confidence_score: 0.60
claim_probability: 0.88
relevance_level: high
relevance_confidence: 0.97
canonical_readiness: hold_for_conversion_qa
created: 2026-05-30
---

# Proof Review: Entry 172 Row Conflict Revision

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The staged draft's central conclusion is supported: the assigned chunk and source packet describe entry 172 as a Pulgar/Arriagada birth row, while the referenced converted Markdown describes entry 172 as a Burgos/de la Cruz row.
2. The conflict is row-level and material. The two derivative readings disagree on child name, parents, birth date, birth time, birthplace, informant, and official context; this cannot be treated as a spelling variant or minor transcription uncertainty.
3. The cited page image path, `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, was not available locally during this review. I therefore did not certify the visible source image or the father-field suffix.
4. The father reading remains blocked at the exact literal level. The available chunk reads `Jose del Carmen Pulgar S.`, but the review cannot decide between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` without targeted image QA.
5. No Dario-line attachment is supported. The reviewed materials do not name Dario, Arturo, Smith, Dario Jose, or Dario Pulgar Arriagada, and they provide no direct bridge from this entry to any Dario identity cluster.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image path was checked but did not resolve locally: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | A civil birth register image would be a strong primary source, but the original image was unavailable locally for this review, so scoring relies on derivative files. |
| conversion_confidence_score | 0.30 | The chunk/source packet and converted Markdown materially disagree for the same entry number; conversion confidence must remain low until row-control QA. |
| evidence_quantity_score | 0.58 | There are multiple derivative artifacts documenting the conflict, but no available local source image verification in this review. |
| agreement_score | 0.34 | The chunk, source packet, conflict draft, and staged identity analysis agree with one another; the current converted Markdown directly conflicts. |
| identity_confidence_score | 0.60 | The Pulgar/Arriagada identity reading is coherent within the assigned chunk, but identity confidence is capped by row-control conflict and father-field uncertainty. |
| claim_probability | 0.88 | The claim that this staged draft should remain on hold for conversion QA is strongly supported by the derivative-file conflict. |
| relevance_level | high | The row directly concerns Pulgar/Arriagada identity and parent-child candidates if the row is certified. |
| relevance_confidence | 0.97 | The assigned draft and referenced files all concern entry 172 and its Pulgar/Arriagada versus Burgos/de la Cruz conflict. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, merges, or wiki updates from this staged draft before targeted row-control QA and renewed proof review. |

## Evidence Strengths

- The staged draft accurately identifies the dispute as a conversion-control problem, not a normal identity-variant problem.
- The source packet preserves both derivative readings and correctly recommends `hold_for_conversion_qa` rather than promotion.
- The conflict draft concisely states the material differences between the Pulgar/Arriagada and Burgos/de la Cruz readings.
- The staged draft properly blocks Dario-line inference and parent merges from surname overlap alone.

## Next Action

Run targeted conversion QA using the original source image, the assigned chunk, the current converted Markdown, and the source packet. The QA note should certify the controlling physical row for entry 172 and record the father field only to the visible level of certainty. After that, rerun proof review before any canonical claim, relationship, identity merge, or wiki update.
