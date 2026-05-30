---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530103701682
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527065100628.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527065100628.md
review_status: hold
canonical_readiness: hold_for_conversion_qa_and_identity_bridge
source_quality_score: 0.52
conversion_confidence_score: 0.28
evidence_quantity_score: 0.46
agreement_score: 0.34
identity_confidence_score: 0.58
claim_probability: 0.56
relevance_level: high
relevance_confidence: 0.95
---

# Proof Review: identity-analysis-conflict-chunk-fb0a0000636f-p0004-01

## Blockers

- The staged draft under review is exactly `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527065100628.md`.
- Canonical readiness remains `hold_for_conversion_qa_and_identity_bridge`. Do not promote page-4 work-history facts, relationship claims, person merges, or name normalizations from this draft.
- Current converted page 4 in `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md` contains 2000 IBRD / Bolivia, Peru and 1999-2000 Antamina / Huarmey, Peru entries, while the referenced chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md` contains 1982-1989 FAO/CIDA/WIF/independent consultant entries.
- The chunk manifest lists `CHUNK-fb0a0000636f-P0004-01` twice for the same page/path with different character counts and hashes. The current chunk SHA-256 is `c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15`, matching neither manifest value.
- The current converted-file SHA-256 is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`, not the converted hash recorded in the chunk front matter.
- The expected page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg` is not present, so physical page control could not be visually resolved in this review.
- Page-body text in the derivative chunk does not literally state `Dario Arturo Pulgar`, `Pulgar-Smith`, `Smith`, `Arriagada`, parents, spouse, children, grandchildren, or any kinship relationship.

## Evidence Strengths

- The staged draft correctly treats the strongest supported conclusion as document-level attribution only: the source title/path and local metadata identify the PDF as `CV of Dario Arturo Pulgar`.
- The draft appropriately distinguishes page-level work-history evidence from identity proof. The body of the referenced chunk is a work-history continuation and contains no standalone personal-name or relationship bridge.
- The draft's anti-conflation analysis is supported: this page does not justify merging `Dario Arturo Pulgar` with `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, `Dario Pulgar A.`, or Jose/Juana parent candidates.
- The draft's recommended hold is consistent with the source packet and conversion review note, both of which identify unresolved page-control and manifest/hash conflicts.

## Scored Judgment

| field | score | judgment |
|---|---:|---|
| source_quality_score | 0.52 | A CV can be useful for occupational chronology, but the reviewed page evidence is derivative and not currently tied to a verified physical page image. |
| conversion_confidence_score | 0.28 | Low because converted page 4 and the chunk disagree, expected page image is missing, and hashes/manifests are inconsistent. |
| evidence_quantity_score | 0.46 | Multiple local metadata layers exist, but page-body evidence is unnamed and relationship evidence is absent. |
| agreement_score | 0.34 | Draft/source packet agree on holding the evidence, but converted page 4 conflicts with the chunk's 1982-1989 text. |
| identity_confidence_score | 0.58 | Probable document-level CV subject attribution to Dario Arturo Pulgar; not enough for canonical Pulgar-Smith identity attachment. |
| claim_probability | 0.56 | The held identity-analysis conclusions are plausible as cautions, but dependent page-4 factual claims are not currently proof-ready. |
| relevance_level | high | The draft directly addresses the assigned page identity and manifest QA conflict. |
| relevance_confidence | 0.95 | All reviewed files are the exact staged draft and its referenced conversion/chunk/source-packet context. |
| canonical_readiness | hold_for_conversion_qa_and_identity_bridge | No canonical promotion, merge, relationship attachment, or name normalization should occur. |

## Claim Review

- Hypothesis that the page belongs to document-level CV subject `Dario Arturo Pulgar`: `hold`, probability `0.60`. Metadata supports the PDF subject, but the page-body text is unnamed and page-control conflict prevents promotion.
- Hypothesis that the CV subject is the same person as canonical `Dario Arturo Pulgar-Smith`: `hold`, probability `0.45`. Distinctive name overlap may be useful for follow-up, but this page does not state `Smith` or any family bridge.
- Hypothesis that the CV subject is the same as Pulgar-Arriagada / Dario Pulgar A. candidates: `revise_or_reject_for_this_source`, probability `0.08`. This page supplies no `Arriagada`, `Jose`, medical-surgeon, expropriation, or lineage evidence.
- Hypothesis that Jose/Juana parent candidates connect to this CV subject: `unsupported_from_this_page`, probability `0.03`. No parentage or kinship language appears in the reviewed page evidence.

## Next Action

Keep this staged identity analysis on hold. The next work should be source-prep/conversion QA: restore or regenerate page-4 page control, reconcile duplicate manifest entries and hashes, determine which physical page contains the 1982-1989 text, then rerun proof review on refreshed staged evidence before any canonical use.
