---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211859579.md
worker: postconv-proof-review-20260530221648876
staged_draft_reviewed: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211859579.md
review_status: hold
canonical_readiness: not_ready
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers

- Page-control conflict is confirmed. The assigned chunk and source packet identify page 5 as 1979-1982 through 1970-1972 work-history content, while the conversion job page Markdown identifies page 5 as 1999, 1998-1999, and 1997-1998 work-history content.
- Manifest/provenance conflict is confirmed. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for the same chunk path and page number with different character counts and different hashes.
- Aggregate converted-file conflict is confirmed. The aggregate converted Markdown contains both the 1999/1998 content and the 1979-1970 content in the same converted file.
- Page-image verification is blocked. The conversion job manifest names `page-images/page-0005.jpg`, but that file is not present at the manifest path in this workspace, so the visible source image cannot be checked for control.
- Identity support remains document-level only. The reviewed page derivatives do not repeat `Dario Arturo Pulgar` in the page body; the subject attachment relies on the PDF title, conversion job title, source packet metadata, and document continuity.
- Relationship support is absent. The reviewed evidence states work-history entries only and does not state a parent, spouse, child, household, or kinship relationship.
- Canonical attachment is not supported. This evidence cannot presently attach page-5 occupational claims to a canonical person page or resolve any Pulgar-line same-person/variant question.

## Evidence Scores

| field | score | rationale |
|---|---:|---|
| source_quality_score | 0.62 | A CV is a relevant first-person or self-presented source for work history, but current review is limited to derivative files and unavailable page image. |
| conversion_confidence_score | 0.22 | Multiple derivatives disagree and the page image is missing at the manifest path. |
| evidence_quantity_score | 0.48 | There are several local derivative witnesses, but they conflict on the controlling page text. |
| agreement_score | 0.18 | Chunk/source packet agree with each other, page Markdown disagrees, and the aggregate file contains both streams. |
| identity_confidence_score | 0.52 | Document-level metadata consistently points to Dario Arturo Pulgar, but page-local identity text is absent. |
| claim_probability | 0.30 | The only claim safely supported is that a serious page-control/provenance conflict exists; no occupational claim from page 5 is promotion-ready. |
| relevance_level | high | The evidence directly concerns the assigned staged draft and its page-control conflict. |
| relevance_confidence | 0.96 | All reviewed files are cited by the staged draft or its referenced source packet/manifests. |
| canonical_readiness | 0.03 | Not ready for canonical claims, relationships, identity merges, or wiki attachment. |

## Evidence Strengths

- The staged draft's main conclusion is supported: this is a conversion/provenance dispute, not a promotable genealogical claim.
- The source packet accurately warns that conversion confidence is blocked and that promotion should wait for page-control QA.
- The chunk and source packet are internally consistent for the 1979-1970 work-history sequence.
- The conversion job page Markdown is internally consistent for the 1999/1998 work-history sequence.
- The conversion job manifest supports that page 5 was intended to have an image and page Markdown path, even though the actual image file is missing locally.
- The staged draft correctly avoids promoting relationship claims or resolving Pulgar identity conflicts from this page.

## Review Judgment

Decision: `hold_for_conversion_qa`.

The staged draft is substantially supported as a warning/control analysis. Its recommendation not to promote is correct. The only revision pressure is factual precision around the page image: the manifest records a `page-0005.jpg` path, but the file is absent at that path during this review. Therefore, this proof review cannot decide whether the 1999/1998 page Markdown or the 1979-1970 chunk/source-packet text controls actual page 5.

No source transcription changes are recommended from this review. No canonical claim, relationship, or identity merge should be made from this staged draft.

## Next Action

1. Keep the staged item on hold.
2. Restore or regenerate the authoritative page-5 image through the conversion-QA workflow, without editing this review note.
3. Compare the visible page 5 against both derivative text streams.
4. Repair the duplicate chunk manifest entries and regenerate stale derivatives as needed.
5. Rerun proof review after page control is certified.

