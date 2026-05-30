---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530044358225
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_page_markdown: "raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-markdown/page-0001.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
referenced_prior_review: "research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-proof-review-postconv-proof-review-20260525204415696.md"
source_image_status: "unavailable_at_referenced_paths"
canonical_readiness: hold_for_conversion_qa
claim_probability: 0.56
created: 2026-05-30
---

# Proof Review: Entry 172 Row Conflict Revision

This review covers only the staged draft `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md`.

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The staged draft correctly keeps the entry on hold because the assigned chunk/source packet and current converted Markdown disagree on the controlling row for entry 172.
- The referenced source image was not available at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, and the manifest image path `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` is also absent. This review therefore cannot independently certify the visible handwriting.
- The assigned chunk reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The current converted file and page Markdown read entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- These readings are incompatible row identities, not spelling variants. No child identity, parent identity, birth fact, or parent-child relationship should be promoted from this review.
- The father field in the Pulgar/Arriagada reading must remain unresolved at proof precision. This review cannot instruct a change to `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` without visible-source QA.
- No Dario-line attachment is supported. The reviewed draft and references do not name Dario, Arturo, Smith, Dario Jose, Dario J., or any bridge tying this entry to a Dario candidate.

## Evidence Strengths

- The staged draft accurately identifies a material row-level conflict and treats it as a hold condition rather than a merge or promotion problem.
- The assigned chunk and revised source packet agree with each other on a coherent Pulgar/Arriagada birth-registration row for entry 172.
- The current converted Markdown and job page Markdown agree with each other on a different Burgos/de la Cruz row for entry 172, confirming that the conflict is current in the workspace and not merely a stale note.
- The draft's anti-conflation guidance is sound: existing Jose, Juana, and Dario candidates should not be attached or merged based on this conflicted entry.

## Evidence And Probability Scoring

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.70 | Civil birth registers are high-quality direct sources in principle, but the source image is unavailable for this review, so the score is capped. |
| conversion_confidence_score | 0.25 | The chunk/source packet and converted Markdown/page Markdown materially disagree on child, parents, birth date, place, and informant context. |
| evidence_quantity_score | 0.46 | One source package is represented by multiple derivatives, but there is no available image verification and no independent corroborating source reviewed here. |
| agreement_score | 0.36 | Agreement exists within each derivative pair, but the pairs conflict with each other at row level. |
| identity_confidence_score | 0.52 | The Pulgar/Arriagada row may be the family-relevant row, but identity confidence is limited by missing source-image verification and current conversion conflict. |
| claim_probability | 0.56 | Probable enough to preserve as a candidate, not strong enough for canonical claim or relationship promotion. |
| relevance_level | high | Directly relevant to the staged identity-conflict draft and Pulgar/Arriagada candidate row; only anti-conflation relevance for Dario candidates. |
| relevance_confidence | 0.94 | All reviewed files point to the same assigned chunk/task even though their transcriptions conflict. |
| canonical_readiness | hold_for_conversion_qa | Hold pending targeted conversion QA against the actual page image. |

## Claim-Specific Assessment

| Claim Or Hypothesis | Probability | Review Judgment |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth-registration row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.56 | Supported by the assigned chunk/source packet; blocked by conflicting converted Markdown and unavailable image. |
| Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.32 | Supported by current converted Markdown/page Markdown; conflicts with the assigned chunk/source packet and staged family-relevant packet. |
| `Jose del Carmen Pulgar S.` is the exact father-field reading. | 0.40 | Chunk supports this reading, but visible-source certification is unavailable. |
| `Juana Arriagada de Pulgar` is the mother in the controlling row. | 0.55 | Supported if the chunk/source packet control; still held because row control is unresolved. |
| This entry supports any Dario identity bridge. | 0.02 | No reviewed text names or bridges any Dario candidate. |

## Next Action

Keep the staged draft and dependent claims at `hold_for_conversion_qa`.

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` only after the actual source/page image is available. The QA note should decide the controlling entry-172 row and certify the father field only as far as the visible source supports: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting child identity, birth facts, parent identities, relationships, Jose/Juana merges, or any Dario-line comparison.
