---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530214450128
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold
---

# Proof Review: Page 5 Derivative Transcription Conflict

## Blockers First

1. Do not promote any occupational claim from this staged draft. The assigned chunk/source packet transcribe page 5 as 1979-1970 work-history entries, while the conversion job page Markdown for page 5 transcribes 1999/1998 entries.
2. The authoritative page image was not available for visual control. The job manifest records `page-images/page-0005.jpg`, but the `page-images` directory is absent in the checked conversion-job folder, so the conflicting derivative readings cannot be resolved here.
3. The chunk manifest lists duplicate `CHUNK-fb0a0000636f-P0005-01` records for page 5 with different character counts and different SHA-256 hashes, creating a provenance/control blocker.
4. No page-local text in either derivative page-5 body names `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or any Jose/Juana parent candidate. Subject attribution is document-level only.
5. No reviewed text in this task states a parent, spouse, child, sibling, grandchild, household, or other kinship relationship. Relationship claims and same-person merges remain unsupported.

## Evidence Strengths

- The staged draft correctly identifies the conflict as a derivative transcription/page-control problem rather than a genealogical fact conflict.
- The source packet and assigned chunk agree internally on the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- The conversion job page Markdown for page 5 clearly contains a different sequence beginning with 1999, 1998-1999, and 1997-1998 entries.
- The aggregate converted file contains both a 1999/1998 section and a later 1979-1970 section in the same converted-file context, supporting the staged draft's warning that stale or duplicated derivative output may be present.
- The document title/source path supports `Dario Arturo Pulgar` only as a document-level subject label pending page-control and identity-bridge review.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 5/10 for the CV as a document-level occupational source; not visually controllable for page 5 in this review |
| conversion_confidence_score | 2/10 because page 5 has contradictory derivative transcriptions and no available page image |
| evidence_quantity_score | 3/10 for occupational chronology only; 0/10 for kinship evidence |
| agreement_score | 2/10 across derivatives for page 5; 7/10 within the chunk/source-packet pair alone |
| identity_confidence_score | 5/10 for document-level `Dario Arturo Pulgar`; 2/10 for attachment to `Dario Arturo Pulgar-Smith`; 1/10 for any Jose/Juana parent-candidate relationship |
| claim_probability | 0.25 for any specific page-5 occupational claim as currently staged; 0.60 for document-level subject attribution; 0.10 or lower for relationship claims |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold / not_ready |

## Review Finding

The staged draft is supported as a hold. Its central warning is confirmed: the assigned chunk and source packet cannot be treated as controlling page 5 while the page Markdown gives a materially different page-5 transcription and the recorded page image is unavailable.

The draft is appropriately conservative on identity and relationship risk. This review found no literal support in the checked page-5 derivatives for a relationship claim, a same-person merge, or expansion from document-level `Dario Arturo Pulgar` to any canonical Pulgar-line profile.

## Next Action

Hold for conversion QA. Restore or locate the authoritative `page-0005.jpg` or inspect the source PDF page through the controlled conversion workflow, decide which derivative text controls page 5, repair duplicate/stale chunk manifest records, then rerun proof review before any occupational claim or identity attachment is promoted.
