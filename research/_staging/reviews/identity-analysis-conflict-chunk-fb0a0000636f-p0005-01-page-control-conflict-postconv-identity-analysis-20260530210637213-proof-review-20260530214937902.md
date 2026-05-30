---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530214937902
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md"
conflict_draft: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: not_ready
---

# Proof Review: Page 5 CV Control Conflict

## Blockers First

1. Hold all claims from this staged draft. The referenced chunk/source packet and the conversion job page Markdown give materially different literal text for page 5: the chunk supports 1979-1970 work-history entries, while `page-markdown/page-0005.md` supports 1999/1998 work-history entries.
2. The page image needed to settle control was not available at the manifest path during this review. The job manifest names `page-images/page-0005.jpg`, but the checked job directory contains the page Markdown and work order files, not that image.
3. The chunk manifest lists duplicate `CHUNK-fb0a0000636f-P0005-01` records with different character counts and hashes. That makes the derivative chain unreliable until conversion QA repairs or certifies the page mapping.
4. No relationship claim is supported. The checked page-5 derivative texts do not state a birth, death, parent, spouse, child, sibling, household, or other kinship relationship.
5. No same-person merge or canonical attachment is supported from this draft. The subject attribution to `Dario Arturo Pulgar` is document-level from the CV title/source metadata; the page body itself does not repeat `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or any Pulgar-Arriagada/Jose/Juana candidate name.

## Evidence Strengths

- The staged draft accurately identifies the conflict as a derivative transcription/page-control problem rather than a genealogical fact conflict.
- The source packet and referenced chunk agree internally on the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO sequence.
- The conversion job page Markdown is internally legible and separately supports a different 1999/1998 sequence for page 5.
- The source title and conversion job title consistently identify the broader document as a CV of `Dario Arturo Pulgar`, but that is only document-level context and not a page-local identity bridge.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 5/10 |
| conversion_confidence_score | 2/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 overall; 7/10 within the chunk/source-packet pair only |
| identity_confidence_score | 5/10 for document-level `Dario Arturo Pulgar` attribution; 2/10 for canonical `Dario Arturo Pulgar-Smith` attachment; 1/10 for any Pulgar-line relationship claim |
| claim_probability | 0.20 for promoting any page-5 occupational claim now; 0.55 that the broader source is a CV for `Dario Arturo Pulgar`; 0.10 for any relationship claim |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | not_ready; hold for conversion QA and separate identity-bridge review |

## Review Finding

The staged draft is supported as a hold recommendation. Its main conclusion is reliable: the current derivatives cannot both be accepted as the controlling page-5 transcription, and no claim should be promoted from either text until the authoritative page image or source page is checked through the conversion-QA workflow.

This review does not revise any literal transcription. It only confirms that the available derivative evidence is conflicting and insufficient for canonical claims, same-person merges, or relationship conclusions.

## Next Action

Run conversion QA/source-prep repair for page 5: restore or regenerate the page image if needed, compare the visible source page against the two competing derivative texts, repair the duplicate chunk-manifest records, and rerun proof review after page control is certified. Keep this staged draft and all downstream occupational, identity, and relationship claims on hold until then.
