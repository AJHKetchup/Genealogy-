---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525050258195
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-474cff632d2f-p0011-01-middle-initial-watch-postconv-identity-analysis-20260525034612325.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-474cff632d2f-p0011-01-middle-initial-watch-postconv-identity-analysis-20260525034612325.md"
canonical_readiness: hold_for_provenance_reconciliation
source_quality_score: 0.82
conversion_confidence_score: 0.90
evidence_quantity_score: 0.42
agreement_score: 0.78
identity_confidence_score: 0.34
claim_probability: 0.88
relevance_level: high
relevance_confidence: 0.94
---

# Proof Review: Darío J. Pulgar Arriagada Middle-Initial Watch

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-474cff632d2f-p0011-01-middle-initial-watch-postconv-identity-analysis-20260525034612325.md`.
- Canonical readiness: `hold_for_provenance_reconciliation`. The staged draft, conflict draft, and source packet cite `CHUNK-474cff632d2f-P0011-01`, but the referenced chunk front matter records `CHUNK-55285fb49aba-P0011-01` and a different `converted_sha256`.
- The visible page supports only a narrow named-person/title-list claim. It does not expand `J.` and does not state age, birth date, parents, spouse, children, residence, death date, or any family relationship.
- Do not use this source alone to merge `Darío J. Pulgar Arriagada` with `Dario Pulgar A.`, `Dario Jose Pulgar-Arriagada`, `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, a 1953 passenger stub, a 2000 expropriation stub, or any Jose/Juana parent candidate.

## Evidence Strengths

- The referenced page image was checked locally at `raw/codex-conversion-jobs/ca753b8b14-anales-de-la-universidad-p0004-0023-anales-de-la-universidad-de-chile-session-of-the-council-of-public-instruction-september-1918-pages-4-23/page-images/page-0011.jpg`.
- The visible page supports the session date `Sesion de 2 de Setiembre de 1918`, the heading `Médicos-Cirujanos:`, and the printed list entry `Darío J. Pulgar Arriagada`.
- The converted chunk transcription agrees with the page image for the narrow name/title-list reading.
- The staged identity analysis correctly treats identity merging as unresolved and recommends against promotion of an identity merge.

## Scoring

| Metric | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Contemporary university/public-instruction session minutes are strong for title-conferral list evidence, but weak for genealogical identity relationships. |
| conversion_confidence_score | 0.90 | Page image and chunk transcription agree for the date, title heading, and name line. |
| evidence_quantity_score | 0.42 | One page, one printed line, no corroborating identifiers in the reviewed context. |
| agreement_score | 0.78 | The narrow literal reading agrees across packet, chunk, and page image; provenance/hash metadata conflicts reduce agreement. |
| identity_confidence_score | 0.34 | The source identifies a named person in a professional list but does not bridge to other Dario Pulgar candidates. |
| claim_probability | 0.88 | High probability for the narrow claim that the 1918 list includes `Darío J. Pulgar Arriagada` under `Médicos-Cirujanos`; low probability for any same-person merge from this evidence alone. |
| relevance_level | high | Highly relevant to Pulgar/Arriagada identity disambiguation and medical-professional context. |
| relevance_confidence | 0.94 | The name and title heading are visible and directly relevant. |
| canonical_readiness | hold_for_provenance_reconciliation | Reconcile chunk id/hash metadata before any canonical claim promotion; do not promote identity merge or relationship claims. |

## Claim Probability By Use

| Proposed use | Probability | Canonical readiness |
| --- | ---: | --- |
| Narrow source-level claim: the 2 September 1918 session list includes `Darío J. Pulgar Arriagada` under `Médicos-Cirujanos` | 0.88 | hold until chunk/hash provenance is reconciled |
| Name-variant claim that `J.` means `Jose` or another expanded middle name | 0.18 | reject for this source |
| Same-person claim with any other Dario Pulgar/Pulgar Arriagada candidate | 0.28 | hold; requires separate bridge evidence |
| Relationship claim to parents, spouse, children, or family cluster | 0.02 | reject for this source |

## Next Action

Revise or reconcile the source packet/conflict draft provenance so the staged `CHUNK-474cff632d2f-P0011-01` citation matches the actual referenced chunk metadata, or explain the converted-hash change in a reviewable way. After that, the narrow title-list appearance claim can be proof-reviewed for canonical claim staging, but all identity merges, middle-name expansions, and relationship claims should remain on hold.
