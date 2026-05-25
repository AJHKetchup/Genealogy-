---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260525165423818
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.86
conversion_confidence_score: 0.45
evidence_quantity_score: 0.70
agreement_score: 0.35
identity_confidence_score: 0.78
claim_probability: 0.74
relevance_level: high
relevance_confidence: 0.93
---

# Proof Review: Entry 172 Identity/Conflict Analysis

## Blockers First

1. Canonical readiness remains `hold_for_conversion_qa`. The reviewed converted Markdown and the reviewed chunk describe incompatible entry-172 rows, so no dependent identity claim, parent-child relationship, parent merge, or Dario-line comparison should be promoted.
2. The staged identity-analysis draft correctly identifies a row-level conversion/assignment conflict, but it inaccurately describes the converted Markdown conflict in several places. The converted file reviewed here records entry 172 as `Jose Francisco`, child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`, born `En veinte de Febrero... a las diez de la noche`, place `En Pellin`. It does not record `Emilia de la Cruz`, `veinte i seis de Marzo`, or `En esta`.
3. Because the staged draft repeats that incorrect converted-file description, revise the conflict-detail wording before any later proof package relies on it. This does not change the core hold conclusion.
4. The father-name ending in the Pulgar/Arriagada row remains a field-level uncertainty. The chunk reads `Jose del Carmen Pulgar S.`, but the safe proof posture is to keep the ending unresolved until targeted QA records the visible source-supported form.
5. No Dario identity or relationship bridge is present in the reviewed source context. Any attachment to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada would be a relationship jump.

## Evidence Strengths

- The source class is strong: a civil birth registration page for Los Angeles, Chile, 1888.
- The reviewed source image visibly supports the chunk-level row placement for entry 172 as a Pulgar/Arriagada birth registration on page 58.
- The reviewed chunk gives a coherent literal row for entry 172: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with father read as `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, residence Calle de Colipi, and informant `Ernesto Herrera L.`
- The staged draft's central conclusion is well supported: the problem is a row-level conversion/assignment conflict, not a spelling variant or same-person proof.
- The anti-conflation conclusion is supported. The reviewed materials do not name Dario or provide a later-life bridge.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil registration is a high-value source class, and the source image is available for review. Image readability is sufficient for row-level validation, though fine handwriting still needs targeted field QA. |
| conversion_confidence_score | 0.45 | The chunk and source image agree at row level, but the converted Markdown is materially inconsistent with them and appears to represent a different page/register context. |
| evidence_quantity_score | 0.70 | One source image, one chunk, one converted file, one source packet, and one conflict candidate were reviewed. Quantity is enough to score the conflict, not enough to promote relationships. |
| agreement_score | 0.35 | Agreement is high between source image and chunk for the Pulgar/Arriagada row, but low across all derivative layers because the converted Markdown conflicts and the staged/source-packet conflict description misquotes the converted row. |
| identity_confidence_score | 0.78 | For the visible entry-172 row being Pulgar/Arriagada, confidence is moderately high. For any canonical merge or later identity bridge, confidence remains low. |
| claim_probability | 0.74 | The staged draft's core claim that this should be held for conversion QA is probable. Its specific converted-file details require revision. |
| relevance_level | high | The source directly concerns a Pulgar/Arriagada birth row and therefore is highly relevant to Pulgar-line research if certified. |
| relevance_confidence | 0.93 | The relevance is clear from the visible image and chunk, subject to conversion QA. |
| canonical_readiness | hold_for_conversion_qa | No canonical claim or relationship should be promoted until QA reconciles the chunk/source image with the converted Markdown and resolves the father field. |

## Claim-Level Findings

| Claim / issue reviewed | Judgment | Probability |
| --- | --- | ---: |
| Entry 172, as visible in the source image and chunk, is a Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported at row level, pending targeted conversion QA. | 0.82 |
| The reviewed converted Markdown describes a different entry-172 family. | Supported, but the staged draft states the wrong mother/date/place for that converted row. | 0.95 |
| The father can safely be promoted as `Jose del Carmen Pulgar S.` | Hold. The chunk reads this form, but field-level QA should confirm the ending before promotion. | 0.62 |
| The mother is `Juana Arriagada de Pulgar` under the Pulgar-row hypothesis. | Supported by the chunk and visible source image, but dependent on row QA before canonical use. | 0.80 |
| This entry proves or bridges any Dario identity. | Not supported. | 0.04 |
| The staged draft is ready for canonical promotion. | Not supported. | 0.00 |

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, chunk, and converted Markdown. The QA note should explicitly state that the converted Markdown reviewed here gives `Jose Francisco`, `Oswaldo Gomez`, and `Rosario de la Cruz de la Maza`, then decide whether the converted file is misassigned or the chunk was regenerated from the correct image after the converted-file mismatch. After QA, rerun proof review on the certified row-level claims before any canonical promotion.
