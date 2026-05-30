---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530110954151
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527065926865.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527065926865.md
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

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527065926865.md`.
- Canonical readiness is `hold_for_conversion_qa_and_identity_bridge`. Do not promote occupational facts, relationship claims, person merges, or name normalizations from this staged draft.
- The current converted file's first page-4 section contains 2000 IBRD / Bolivia, Peru and 1999-2000 Antamina / Huarmey, Peru entries, while the referenced chunk contains 1982-1989 FAO/CIDA/WIF/independent consultant entries.
- The converted file later repeats the 1982-1989 text after page-6 material, so page continuity and page identity are not stable enough for canonical use.
- The chunk manifest lists `CHUNK-fb0a0000636f-P0004-01` twice for the same path/page with different character counts and hashes: `4572` / `5e6aed90f2420572473987255df4bbec4de8750bd2f9701a9b71b2896f27a43f` and `3985` / `504f69374f1d289f20e70388a7653b8f8673e10ae649490cb6df74fe04fc3112`.
- The current on-disk chunk SHA-256 is `c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15`, matching neither manifest value.
- The current converted-file SHA-256 is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`, not the converted hash recorded in the chunk front matter.
- The expected page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg` is not present, so physical page control could not be visually resolved.
- The referenced chunk body does not literally name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, `Arriagada`, `Jose`, `Juana`, any parent, spouse, child, grandchild, or household relationship.

## Evidence Strengths

- The staged draft correctly treats subject attribution as document-level only. The source path, source packet, converted-file title, and chunk front matter all point to `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The referenced chunk text is internally readable typed CV work-history material for FAO in Ndola, CIDA in Ethiopia, Worldview International Foundation in Rome, and independent communications consulting for CIDA.
- The staged draft's anti-conflation caution is supported: this page does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario Pulgar A.`, or Jose/Juana parent connections.
- The hold recommendation agrees with the source packet's QA note that page-control and manifest/hash conflicts remain unresolved.

## Scored Judgment

| field | score | judgment |
|---|---:|---|
| source_quality_score | 0.52 | A CV is useful for occupational chronology, but this reviewed evidence is derivative and not currently tied to a verified physical page image. |
| conversion_confidence_score | 0.28 | Low because converted page 4 and the chunk disagree, the expected page image is missing, and manifest/hash values conflict. |
| evidence_quantity_score | 0.46 | Several local metadata layers support document-level attribution, but the page body is unnamed and relationship evidence is absent. |
| agreement_score | 0.34 | The staged draft and source packet agree on holding the evidence, but converted page 4 conflicts with the referenced chunk text. |
| identity_confidence_score | 0.58 | Document-level attribution to `Dario Arturo Pulgar` is plausible; canonical `Pulgar-Smith` attachment is not proved here. |
| claim_probability | 0.56 | The staged draft's cautionary identity analysis is plausible, but dependent page-4 factual claims are not proof-ready. |
| relevance_level | high | The review directly addresses the assigned staged identity-analysis draft and its referenced conversion/chunk/source-packet context. |
| relevance_confidence | 0.95 | All checked files are the exact staged draft or directly referenced local support files. |
| canonical_readiness | hold_for_conversion_qa_and_identity_bridge | No canonical promotion, merge, relationship attachment, or name normalization should occur. |

## Claim Review

- Document-level CV subject is `Dario Arturo Pulgar`: `hold`, probability `0.60`. Metadata supports this, but the page-body text is unnamed and page-control is unresolved.
- Same person as canonical `Dario Arturo Pulgar-Smith`: `hold`, probability `0.45`. Name overlap may justify follow-up, but this page does not state `Smith` or provide a family bridge.
- Same person as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario Pulgar A.`: `revise_or_reject_for_this_source`, probability `0.08`. This page lacks the variant names, roles, places, or lineage bridge needed for that attachment.
- Relationship to Jose/Juana parent candidates: `unsupported_from_this_page`, probability `0.03`. No parentage, spouse, child, household, or kinship statement appears in the reviewed evidence.

## Next Action

Keep this staged identity analysis on hold. The next action is targeted source-prep/conversion QA: restore or regenerate page-4 page control, reconcile duplicate manifest entries and hashes, determine which physical page contains the 1982-1989 text, and rerun proof review before any canonical use.
