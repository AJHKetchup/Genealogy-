---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530215422568
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md
review_status: hold
canonical_readiness: not_ready
claim_probability: 0.20
source_quality_score: 0.55
conversion_confidence_score: 0.20
evidence_quantity_score: 0.45
agreement_score: 0.25
identity_confidence_score: 0.50
relevance_level: high
relevance_confidence: 0.95
---

# Proof Review: Page-Control Conflict, CHUNK-fb0a0000636f-P0005-01

## Blockers

- Source-control blocker: the named source file `raw/sources/CV of Dario Arturo Pulgar.pdf` was not present in this workspace during review, and the conversion-job page image `page-images/page-0005.jpg` was also absent. I could not inspect the visible source page.
- Conversion-control blocker: the assigned chunk and source packet transcribe page 5 as 1979-1970 work-history content, while the conversion-job page Markdown for page 5 transcribes 1999/1998 content. Both cannot control the same page.
- Manifest blocker: the chunk manifest lists duplicate `CHUNK-fb0a0000636f-P0005-01` records with different char counts and hashes, so the derivative chain is not stable enough for claim promotion.
- Claim-support blocker: the staged draft correctly treats this as a derivative transcription/provenance conflict, not as a proved occupational fact set.
- Identity blocker: the reviewed page-level derivative text does not name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or any parent/relationship candidates. Subject attribution is document-title context only.
- Relationship blocker: the reviewed evidence contains no birth, death, parent, spouse, child, sibling, household, or other kinship statement.

## Scores

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.55 | A CV can be useful for occupational chronology, but the authoritative PDF/page image was unavailable for this review. |
| conversion_confidence_score | 0.20 | Derivative outputs materially disagree, the page image is absent, and the chunk manifest is internally duplicated. |
| evidence_quantity_score | 0.45 | Several local derivatives were available, but they are conflicting derivatives rather than independent corroborating evidence. |
| agreement_score | 0.25 | The chunk/source packet agree with each other, but they disagree with the page Markdown and unstable manifest state. |
| identity_confidence_score | 0.50 | Document-level title context points to Dario Arturo Pulgar, but page-level text does not independently identify him. |
| claim_probability | 0.20 | Low probability that any page-5 occupational claim is promotion-ready before source-control QA. |
| relevance_level | high | The staged draft directly concerns the assigned page-control conflict. |
| relevance_confidence | 0.95 | All reviewed files are directly referenced by the staged draft or its immediate evidence chain. |
| canonical_readiness | not_ready | Hold for conversion/source-control QA; do not promote or attach to canonical pages. |

## Evidence Strengths

- The staged draft is well supported in its central procedural conclusion: a page-control conflict exists and should block promotion.
- The source packet and assigned chunk consistently support the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO sequence.
- The conversion-job page Markdown consistently supports a different 1999/1998 page-5 work-history sequence.
- The job manifest references page 5 and its intended `page-markdown/page-0005.md`, while the chunk manifest documents the duplicate page-5 chunk state. These files explain why the derivative chain is unsafe.

## Review Judgment

The staged draft's hold recommendation is supported. The draft should not be promoted as occupational evidence, identity evidence, relationship evidence, or canonical conflict resolution. It is useful only as a staging note documenting a conversion/provenance blocker.

I did not find literal support for resolving whether the controlling page-5 source text is the 1999/1998 sequence or the 1979-1970 sequence. I also did not find page-local evidence that proves the CV subject is canonical `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada candidate.

## Next Action

Hold for conversion QA. Restore or re-render the authoritative page-5 image/source page, compare it against both derivative transcriptions, repair the stale or duplicated chunk/manifest state through the source-prep workflow, and rerun proof review before any claim promotion or canonical attachment.
