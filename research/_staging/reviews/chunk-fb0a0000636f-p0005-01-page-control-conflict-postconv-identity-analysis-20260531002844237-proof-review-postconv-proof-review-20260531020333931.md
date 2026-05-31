---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260531020248242
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002844237.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002844237.md
review_status: hold
canonical_readiness: not_ready
created_at: 2026-05-31T02:03:33Z
---

# Proof Review: Page-Control Conflict For CV Page 5

## Blockers First

- Page control is unresolved. The assigned chunk and aggregate converted file contain 1979-1970 work-history text ending at `EDUCATION`, while the conversion-job page Markdown for page 5 contains 1999-1997 consulting-work text.
- The physical source cannot be checked in this checkout. `raw/sources/CV of Dario Arturo Pulgar.pdf`, `page-images/page-0005.jpg`, and `extracted-images/page-0005.jpg` are absent.
- Provenance is unstable. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts and hashes, and the source packet records observed hash drift between recorded and current derivative files.
- The page body does not independently state the full name of the CV subject. The document-level title supplies `Dario Arturo Pulgar`, but neither competing page-5 transcription supports a relationship, parentage, or same-person bridge to a canonical wiki person.
- No occupational, place, chronology, identity, or relationship claim from this staged draft should be promoted until conversion QA certifies which derivative text controls physical page 5.

## Evidence Strengths

- The staged draft accurately identifies a conversion/page-control conflict rather than treating the issue as a resolved identity claim.
- The referenced source packet is consistent with the reviewed derivatives: it reports the same conflict between the assigned chunk/aggregate converted file and `page-markdown/page-0005.md`.
- Literal derivative text is readable in both competing versions. The dispute is not mainly legibility; it is which derivative belongs to physical page 5.
- The document title and source packet provide limited document-level context for `Dario Arturo Pulgar`, but that context is insufficient for canonical same-person attachment.

## Verification Notes

- Reviewed staged draft: `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002844237.md`.
- Reviewed source packet: `research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md`.
- Reviewed assigned chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`.
- Reviewed aggregate converted file: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`.
- Reviewed competing page Markdown: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`.
- Reviewed referenced manifests only to confirm path, page-image, and duplicate chunk metadata concerns.

## Scored Judgment

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.35 | The source is a CV packet with named document-level subject, but the physical PDF and page image are unavailable locally for direct verification. |
| conversion_confidence_score | 0.18 | Competing page-5 derivatives, missing page image/source PDF, duplicate chunk entries, and hash drift make conversion control unsafe. |
| evidence_quantity_score | 0.42 | There are multiple local derivatives and a source packet, but no controlling physical-page evidence. |
| agreement_score | 0.20 | The assigned chunk agrees with the aggregate converted file, but conflicts materially with conversion-job `page-markdown/page-0005.md`. |
| identity_confidence_score | 0.30 | Moderate-low for document-level attribution to the CV subject; low for attachment to any canonical person or name variant. |
| claim_probability | 0.48 | The safest probability is near-balanced because either competing derivative may contain CV material, but page-5 control is not proved. |
| relevance_level | 0.95 | The reviewed evidence directly concerns the assigned staged draft and its referenced files. |
| relevance_confidence | 0.96 | The reviewed files are named in the staged draft/source packet and match the task scope. |
| canonical_readiness | 0.05 | Not ready for promotion, merge, relationship attachment, or canonical fact creation. |

## Identity And Relationship Risk

- Same-person risk is high if `Dario Arturo Pulgar` is attached to a canonical `Dario Arturo Pulgar-Smith` profile from this page alone. This review found no page-level `Smith`, parent, spouse, child, grandchild, date, or residence bridge.
- Duplicate-person risk is high if `Dario Arturo Pulgar`, `Dario Pulgar Arriagada`, `Dario Jose Pulgar-Arriagada`, or related Pulgar-line candidates are merged by name overlap.
- Relationship jumps are unsupported. This draft provides no literal parent-child, spouse, grandchild, household, or kinship statement.

## Next Action

Decision: `hold_for_conversion_qa`; do not promote.

Required next action: restore or locate the authoritative source PDF and page-5 image, visually certify whether physical page 5 is the 1999-1997 page or the 1979-1970 page, then reconcile the chunk manifest/hash metadata. After page control is repaired, rerun proof review only on the surviving page-5 claims and conduct any identity-bridge review separately.
