---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522151013138
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-registration-date.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-registration-date.md
reviewed_at: 2026-05-22
canonical_readiness: hold
claim_probability: 0.94
relevance_level: direct
relevance_confidence: 0.98
source_quality_score: 0.90
conversion_confidence_score: 0.82
evidence_quantity_score: 0.72
agreement_score: 0.84
identity_confidence_score: 0.96
---

# Proof Review: Entry 514 Registration Date

## Blockers

- Canonical readiness is `hold`, not because the specific date claim is weak, but because the staged draft references chunk `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, which is unavailable at that path. The matching manifest in that directory lists `page-0172-chunk-01.md` with a different chunk id.
- The source packet is explicitly marked `hold_for_conversion_qa` and documents material conflicts between derivative transcript layers and the visible image for names, parentage, witnesses, street readings, and record completeness. Those conflicts do not materially undermine this narrow registration-date claim, but they block canonical promotion until the page-level QA issue is resolved.
- The staged draft's `chunk_id` is `CHUNK-bdb698de8106-P0001-01`, while the available related chunks show different IDs (`CHUNK-0554d5747bd2-P0172-01` and `CHUNK-3d3ab761209f-P0001-01`). This is a provenance/traceability problem.

## Evidence Strengths

- The visible source image supports entry `514` in the registration-number column and shows the registration-date cell as `Julio veinte i dos de mil ochocientos ochenta i nueve`, i.e. `1889-07-22`.
- The converted file also transcribes entry `514` with `Julio` / `veintidos` or `veinte i dos` / `de mil ochocientos ochenta i nueve`, matching the staged claim's normalized object `1889-07-22`.
- The claim is an event/date claim tied to a specific register entry, so identity risk is low. The row number alignment is visible and the asserted predicate is confined to the registration date, not to disputed person identity or relationship fields.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth register image is a primary source for registration date, though the image is a derivative scan/crop. |
| conversion_confidence_score | 0.82 | The date reading is visually strong and consistent in derivatives, but the page has active conversion QA concerns and chunk provenance mismatch. |
| evidence_quantity_score | 0.72 | One primary page/entry supports the claim; no independent corroborating source was reviewed. |
| agreement_score | 0.84 | Staged claim, converted file, and visible source agree on the date; broader page fields disagree. |
| identity_confidence_score | 0.96 | Entry number `514` is clearly aligned with the date row; no person-identity inference is required for this claim. |
| claim_probability | 0.94 | The specific assertion that entry 514 was registered on `1889-07-22` is very likely correct. |
| relevance_level | direct | The source field is the exact registration-date field for the claimed entry. |
| relevance_confidence | 0.98 | The reviewed source directly addresses the predicate and object. |
| canonical_readiness | hold | Hold until conversion QA/provenance mismatch is resolved, despite strong narrow support. |

## Next Action

Hold this claim for conversion QA/provenance cleanup. After the source packet and staged draft point to the correct current chunk path and chunk id, this registration-date claim can likely be promoted with high confidence, provided the corrected derivative layer still preserves the visible date reading.
