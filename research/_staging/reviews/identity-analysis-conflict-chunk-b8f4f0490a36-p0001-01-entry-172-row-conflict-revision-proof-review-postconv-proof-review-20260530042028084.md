---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530042028084
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_prior_review: "research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-proof-review-postconv-proof-review-20260525204415696.md"
source_quality_score: 0.72
conversion_confidence_score: 0.24
evidence_quantity_score: 0.52
agreement_score: 0.28
identity_confidence_score: 0.48
claim_probability: 0.55
relevance_level: direct
relevance_confidence: 0.96
canonical_readiness: hold_for_conversion_qa
created: 2026-05-30
---

# Proof Review: Entry 172 Row Conflict Revision

This review covers the staged draft `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md`.

## Blockers First

1. Canonical readiness remains `hold_for_conversion_qa`. The staged draft describes a real row-level conflict between the assigned chunk/source packet and the current converted Markdown.
2. The referenced source image is unavailable in this workspace at both recorded paths: `raw/sources/...Entry No. 172;.png` and the manifest page image path `raw/codex-conversion-jobs/.../page-images/page-0001.png`. This proof review therefore cannot visually certify the controlling row or the father-field ending.
3. The assigned chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
4. The current converted Markdown and the conversion job page Markdown read entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
5. These are incompatible row identities, not spelling variants. No child, parent, birth, residence, informant, relationship, or merge claim should be promoted from this draft.
6. The father field cannot be certified as `Jose del Carmen Pulgar S.` from this review. Preserve the staged uncertainty until image-based conversion QA determines whether the visible field supports `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
7. No Dario-line claim is supported here. The reviewed materials do not name Dario, Arturo, Smith, Dario Jose, Dario J., or a relationship bridge to any Dario candidate.

## Evidence Strengths

- The staged draft accurately recognizes the conflict as row control / conversion state conflict rather than a same-person identity problem.
- The source packet and assigned chunk are internally coherent for a Pulgar/Arriagada birth-registration row and preserve the father-field uncertainty.
- The current converted Markdown is internally coherent for a different Burgos/de la Cruz row, which makes the contradiction clear and material.
- The prior proof review reports that it inspected the image and found support for the Pulgar/Arriagada row, but that is derivative review evidence for this task because the image is not presently available for direct inspection.
- The staged draft correctly blocks Dario attachment and treats Dario comparisons as anti-conflation guidance only.

## Evidence And Probability Scoring

| Metric | Score / level | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.72 | Civil birth registration would be high-quality direct evidence, but the image is unavailable in this review environment, so this score is reduced for present verifiability. |
| conversion_confidence_score | 0.24 | The assigned chunk/source packet and current converted Markdown disagree on child, parents, birth date/time, place, and informant context. |
| evidence_quantity_score | 0.52 | One source packet, one chunk, one converted file, and one prior proof review were checked; no direct image check or independent corroborating record was available. |
| agreement_score | 0.28 | Derivatives disagree at row level. Agreement exists only within each competing derivative cluster. |
| identity_confidence_score | 0.48 | The Pulgar/Arriagada reading is plausible from the chunk/source packet and prior review, but identity confidence is capped by missing image access and active conversion conflict. |
| claim_probability | 0.55 | Slightly favors the staged Pulgar/Arriagada hypothesis because multiple staged review artifacts support it, but the current conversion still gives a different row and cannot be ignored. |
| relevance_level | direct | The note directly concerns the assigned staged draft and entry 172 row-control dispute. |
| relevance_confidence | 0.96 | All reviewed materials reference the same chunk id, converted file, and entry number. |
| canonical_readiness | hold_for_conversion_qa | Hold; no canonical claim, relationship, person merge, or Dario bridge should proceed from this review. |

## Claim-Specific Judgment

| Claim or hypothesis | Probability | Review judgment |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth-registration row. | 0.55 | Plausible but not proven in this review; needs image-based QA because the source image is unavailable and current conversion conflicts. |
| Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.30 | Directly supported by the current converted Markdown and job page Markdown, but contradicted by the assigned chunk/source packet and prior review. |
| The conflict reflects stale or misassigned derivative conversion state. | 0.70 | Likely, given incompatible readings attached to the same chunk id and source metadata. |
| Father is exactly `Jose del Carmen Pulgar S.`. | 0.35 | Supported by the chunk text only; cannot be certified without the image. |
| Mother is `Juana Arriagada de Pulgar`. | 0.50 | Supported if the Pulgar/Arriagada row controls; blocked by row conflict. |
| Any Dario identity bridge is supported by this source. | 0.02 | No reviewed material provides a Dario name or relationship bridge. |

## Source Reliability And Risk

- Source reliability: potentially high for the original civil register, but not directly testable here because the image file is missing.
- Derivative reliability: mixed. The chunk/source packet and converted Markdown cannot both describe the same entry 172 row.
- Conversion risk: high. The disagreement changes the person, parents, birth event, place, and relevance to the Pulgar/Arriagada line.
- Identity risk: high if `Jose del Carmen Pulgar S.` is merged into an existing `Jose del Carmen Pulgar` page before the source image is reread.
- Relationship-jump risk: high for parent-child claims until row control is certified.
- Relevance risk: low for reviewing this staged draft, but high for any attempted Dario-line use.

## Next Action

Keep the staged draft and all dependent claims on `hold_for_conversion_qa`.

Run targeted conversion QA with access to the actual page image for `CHUNK-b8f4f0490a36-P0001-01`. The QA note should decide whether the controlling entry 172 row is Pulgar/Arriagada or Burgos/de la Cruz, explain whether the converted Markdown is stale or misassigned, and certify the father field only as far as the visible source supports. After that, rerun proof review before any canonical promotion.
