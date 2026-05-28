---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528131540221
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
reviewed_sources:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers the staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md`.

## Blockers First

1. The staged draft correctly identifies a derivative row-control conflict: the converted Markdown gives entry 172 as a Burgos/de la Cruz child, while the chunk and source packet give entry 172 as a Pulgar/Arriagada child.
2. The source image visibly supports the Pulgar/Arriagada row at entry 172, but this proof-review task should not rewrite the converted Markdown or perform source conversion. A targeted conversion-QA/correction note remains required to resolve the derivative conflict.
3. The father field in the Pulgar/Arriagada row is not safe for normalized promotion beyond the visible uncertainty range already stated by the staged draft: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. No Dario, Arturo, Smith, public-role, passenger, or later Pulgar-Arriagada identity bridge is present in this source. Any same-person or family-line bridge to Dario candidates remains unsupported by this row alone.
5. Canonical pages and earlier b8f4-derived notes are not independent evidence for this task because the controlling conversion set is under conflict.

## Evidence Strengths

- Civil birth registration is a high-value source type for a narrow birth-row claim when the row is controlled.
- The chunk, source packet, and source image agree on the family-relevant row: entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. on Calle de Valdivia, with parents read as `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The staged identity-analysis draft keeps interpretation separate from transcription and properly treats the Burgos/de la Cruz reading as a row-control/conversion-control conflict, not as a name variant or same-person problem.
- The draft's `hold_for_conversion_qa` recommendation is supported.

## Scores

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image; direct source for birth-row facts, though image legibility is imperfect in some handwritten fields. |
| conversion_confidence_score | 0.42 | The chunk and source packet align with the source image, but the referenced converted Markdown contradicts them at the row level. |
| evidence_quantity_score | 0.58 | One direct source image plus competing local derivatives; sufficient to identify a conflict, not sufficient for canonical promotion without conversion QA. |
| agreement_score | 0.55 | Image, chunk, and source packet agree on Pulgar/Arriagada, but the current converted Markdown gives a different entry-172 family. |
| identity_confidence_score | 0.60 | Moderate confidence for the row-conflict analysis and Pulgar/Arriagada row candidate; lower for any canonical identity attachment. |
| claim_probability | 0.68 | The claim that this staged draft has correctly identified a row-control conflict is well supported; dependent person/relationship claims remain below promotion threshold. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada birth and parent-candidate review if the row is certified. |
| relevance_confidence | 0.90 | The visible row and the chunk/source packet contain Pulgar and Arriagada names. |
| canonical_readiness | hold | Do not promote until the derivative conflict is resolved by targeted conversion QA. |

## Claim Judgments

| Claim / issue | Probability | Judgment |
| --- | ---: | --- |
| Staged draft accurately identifies a row-level conversion conflict for entry 172. | 0.86 | Supported. |
| Pulgar/Arriagada is the visible entry-172 row in the page image. | 0.82 | Supported as a review observation, but should be formalized by conversion QA before canonical use. |
| Converted Markdown Burgos/de la Cruz entry is the controlling entry 172 for this source image. | 0.12 | Weakly supported here; it conflicts with the image and chunk, but should be handled as conversion QA rather than silently corrected in proof review. |
| `Jose del Carmen Pulgar S.` is the fully certified father reading. | 0.62 | Plausible, but the suffix remains a literal-reading uncertainty. |
| The row proves a bridge to any Dario Pulgar candidate. | 0.03 | Not supported. |

## Next Action

Keep the staged draft on hold/revise for targeted conversion QA. The next worker should compare the source image, converted Markdown, chunk, and source packet, then record which derivative should control entry 172 and certify the father field only to the visible source-supported level. No canonical promotion or Dario-family bridge should be made from this review note.
