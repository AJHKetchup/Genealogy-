---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531070406847
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531021526319.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531021526319.md
reviewed_conflict_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531004750573.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source_quality_score: 0.26
conversion_confidence_score: 0.10
evidence_quantity_score: 0.35
agreement_score: 0.16
identity_confidence_score: 0.32
claim_probability: 0.22
relevance_level: high
relevance_confidence: 0.93
canonical_readiness: hold
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Page 5 Identity/Control Conflict

## Blockers First

1. The exact staged draft under review is `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531021526319.md`; it analyzes a page-control conflict, not a promotion-ready identity claim.
2. The assigned chunk and the conversion-job page Markdown preserve different literal page-5 content. The assigned chunk contains the 1979-1982 HABITAT through 1970-1972 CITELCO sequence ending with `EDUCATION`; `page-markdown/page-0005.md` contains 1999-1997 consulting entries beginning with PROFONANPE and TVE.
3. The original source file `raw/sources/CV of Dario Arturo Pulgar.pdf`, the job-local staged PDF, and `page-images/page-0005.jpg` are absent in the current workspace, so physical page control cannot be verified.
4. The chunk manifest contains duplicate entries for `CHUNK-fb0a0000636f-P0005-01`, and current file hashes differ from recorded metadata. Current observed hashes: chunk `D6EA4F611EE03000C11CBBA63246E95B55F8A421FCBC87D0D667E91F5C8D0B8D`; aggregate converted file `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`; conversion-job page Markdown `B87BD19F16275A992482651063C280BFC303BC6B7B0CD30CFBC2843D6D5E692F`.
5. Neither competing page-5 derivative body prints `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Arriagada`, `Smith`, `Jose`, `Juana`, or any family relationship. The Dario association is document metadata/title context only.

## Scored Judgment

| Field | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.26 | The source title/path identify a CV of Dario Arturo Pulgar, but the source PDF and rendered page image needed for direct verification are unavailable. |
| conversion_confidence_score | 0.10 | Page-control disagreement, duplicate chunk manifest entries, absent source controls, and hash drift make the controlling transcription uncertain. |
| evidence_quantity_score | 0.35 | Multiple local derivatives exist, but they are derivative-only and materially conflict. |
| agreement_score | 0.16 | The derivatives agree only that the material is CV-style work history; they disagree on the literal page-5 body. |
| identity_confidence_score | 0.32 | Document metadata supports a broad Dario Arturo Pulgar context, but page-local text does not independently identify him or bridge to any canonical Pulgar person. |
| claim_probability | 0.22 | A promotion-ready identity or occupational claim from this staged draft is unlikely until page control is repaired. |
| relevance_level | high | The CV title and Pulgar metadata make the conflict relevant to Pulgar identity work after QA. |
| relevance_confidence | 0.93 | Relevance is clear even though proof value is blocked. |
| canonical_readiness | hold | No canonical person, relationship, claim, merge, rename, or wiki edit is ready. |

## Evidence Strengths

- The staged draft accurately preserves the page-control problem and does not overstate the disputed page as stable identity proof.
- The assigned chunk is locally present and legible as a derivative transcription of a 1979-1970 CV work-history page.
- The conversion-job page Markdown is locally present and legible as a derivative transcription of a different 1999-1997 CV work-history page.
- The aggregate converted file contains both competing sequences, which supports the draft's warning that the current conversion state is internally misaligned.
- The draft correctly treats Pulgar-Smith, Pulgar-Arriagada, and Jose/Juana relationship possibilities as identity-risk context only, not as established relationships.

## Review Decision

Hold for conversion QA. The reviewed draft is useful as a conflict note, but it does not support promotion of any page-5 occupational fact, identity bridge, or family relationship.

The strongest supported claim is limited to workspace state: conflicting derivative readings for page 5 exist, and the physical controls needed to decide between them are absent. The body text of the disputed page does not itself support normalizing the subject to Dario Arturo Pulgar-Smith or attaching the evidence to any Pulgar-Arriagada or Jose/Juana family cluster.

## Next Action

1. Restore or regenerate authoritative access to `raw/sources/CV of Dario Arturo Pulgar.pdf` or `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg`.
2. Compare physical page 5 against both derivative readings: the 1999-1997 conversion-job page Markdown and the 1979-1970 assigned chunk/current aggregate sequence.
3. Repair or supersede the duplicate manifest rows and reconcile hash drift before using `CHUNK-fb0a0000636f-P0005-01` as evidence.
4. After page control is certified, rerun proof review for surviving occupational claims as document-level CV evidence, then run a separate identity-bridge review before attaching any accepted claim to a canonical person.
