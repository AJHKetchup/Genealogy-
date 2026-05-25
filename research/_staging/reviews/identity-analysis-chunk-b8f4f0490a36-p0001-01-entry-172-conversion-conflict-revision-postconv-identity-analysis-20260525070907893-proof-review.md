---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525081927629
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525070907893.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525070907893.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
review_recommendation: hold_for_conversion_qa
canonical_readiness: 0.10
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

1. Canonical promotion is blocked by a material row-level conversion conflict. The staged identity analysis, source packet, chunk, and visible page image support entry 172 as a Pulgar/Arriagada birth registration, while the assigned converted Markdown records a different child and parent pair.
2. The assigned converted Markdown is not reliable for this claim set until conversion QA resolves whether the controlling entry 172 row is the Pulgar/Arriagada row or the Jose Francisco/Gomez row, or whether the converted file assignment is wrong.
3. The father field is not fully proof-ready. The chunk reads `Jose del Carmen Pulgar S.`, while the staged analysis correctly preserves `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as QA outcomes.
4. Parent-child relationships and duplicate-person merges must remain on hold. The draft's caution against attaching Dario, Arturo, Smith, Dario Jose, Dario/Dario Pulgar Arriagada, or entry-513 Juana variants is supported.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth registration image is a direct, identity-bearing source for entry 172, but the page image is small and handwriting-dependent. |
| conversion_confidence_score | 0.42 | The current chunk aligns with the visible Pulgar/Arriagada row, but the assigned converted Markdown materially disagrees. |
| evidence_quantity_score | 0.58 | One source image, one chunk, one source packet, one conflict draft, and the converted Markdown were available; the evidence is narrow but directly relevant. |
| agreement_score | 0.46 | The staged draft, source packet, chunk, and visible image broadly agree; the converted Markdown disagrees on names, parents, dates, and place. |
| identity_confidence_score | 0.64 | The Pulgar/Arriagada child-parent cluster is plausible for this page row, but identity promotion is weakened by the conversion conflict and father-name uncertainty. |
| claim_probability | 0.70 | It is probable that the staged analysis correctly identifies a row-level conflict and correctly recommends hold. |
| relevance_level | high | The row contains Pulgar and Arriagada names and is directly relevant to the local Pulgar-line review. |
| relevance_confidence | 0.92 | The family relevance of the Pulgar/Arriagada row is clear if that row is confirmed as controlling entry 172. |
| canonical_readiness | 0.10 | Not ready for canonical claim, relationship, or identity promotion until conversion QA resolves the row conflict. |

## Evidence Strengths

- The chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source packet accurately identifies the conflict as material rather than a spelling variant and recommends `hold_for_conversion_qa`.
- The visible source image is consistent with the chunk's Pulgar/Arriagada row for entry 172 and does not visibly support changing the child to Dario or attaching a Dario identity from this source alone.
- The staged identity analysis uses appropriate uncertainty boundaries: it preserves unresolved father-name readings, treats parent candidates cautiously, and keeps Dario-line comparisons as anti-conflation checks rather than bridge evidence.

## Review Finding

The staged identity analysis is supportable as a conflict-analysis draft and should remain `hold_for_conversion_qa`. It should not be promoted as proof of a child identity, birth fact, father relationship, mother relationship, or duplicate-person merge. The safest current claim is limited to: local verification found a material conflict between the assigned converted Markdown and the chunk/source-packet/source-image context for entry 172.

## Next Action

Run targeted conversion QA on register page 58, entry 172. The QA note should explicitly decide the controlling source row and record the father field as one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical promotion or parent-candidate merge.
