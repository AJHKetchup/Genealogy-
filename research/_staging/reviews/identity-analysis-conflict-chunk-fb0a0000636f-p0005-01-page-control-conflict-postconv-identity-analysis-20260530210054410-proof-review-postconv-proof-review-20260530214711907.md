---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530214711907
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210054410.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210054410.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md"
conflict_candidate: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: not_ready
---

# Proof Review: CV Page-Control Conflict

## Blockers First

1. Do not promote page-5 occupational claims from this staged draft. The assigned chunk for page 5 contains 1979-1982, 1974-1978, 1972-1973, and 1970-1972 entries, while the conversion job page Markdown for page 5 contains 1999, 1998-1999, and 1997-1998 entries.
2. Do not treat either derivative transcription as controlling until conversion QA resolves page control. The aggregate converted file contains both the 1999/1998 section and the later 1979-1970 section, and the chunk manifest lists duplicate page-5 chunk ids with different char counts and hashes.
3. I could not visually verify the authoritative page image for page 5. The manifest points to `page-images/page-0005.jpg`, but that file is not present in the checked job directory.
4. Do not attach this page to canonical `Dario Arturo Pulgar-Smith`, merge any Pulgar-line candidates, or make Jose/Juana relationship claims from this evidence. The checked page-level derivative texts do not name a spouse, parent, child, household member, `Smith`, Jose candidate, or Juana candidate.

## Evidence Strengths

- The staged identity/conflict analysis accurately identifies the central provenance problem: multiple local derivative texts disagree about what page 5 contains.
- The staged conflict candidate and source packet independently recommend `hold_for_conversion_qa`, matching the reviewed derivative evidence.
- The source title and job metadata support a document-level attribution to `Dario Arturo Pulgar`, but only as contextual CV attribution. The reviewed page-level texts do not independently repeat the subject's name.
- The 1979-1970 chunk text is internally coherent and legible as a CV work-history page if it is later confirmed as the controlling page. The 1999/1998 page Markdown is also internally coherent and legible if it is confirmed as the controlling page.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 for a CV as contextual occupational evidence; lower for identity/kinship proof because this page-level evidence is derivative and not independently identity-bearing |
| conversion_confidence_score | 3/10 because readable derivative texts exist but page control is unresolved and the rendered page image was unavailable |
| evidence_quantity_score | 3/10 for the narrow page-control issue; 1/10 for identity or relationship claims |
| agreement_score | 2/10 across page-5 derivatives; 8/10 between the staged draft, conflict candidate, and source packet that the item should be held |
| identity_confidence_score | 5/10 for document-level `Dario Arturo Pulgar` attribution; 3/10 for attachment to `Dario Arturo Pulgar-Smith`; 1/10 for Jose/Juana relationship or merge claims |
| claim_probability | 0.90 that a page-control conflict exists; 0.55 that the CV is document-level evidence for Dario Arturo Pulgar; 0.40 or lower for attachment to Dario Arturo Pulgar-Smith from this draft; 0.05 for any kinship claim |
| relevance_level | high for conversion/provenance QA; medium for later occupational evidence; low for relationship proof |
| relevance_confidence | 0.90 for the hold recommendation |
| canonical_readiness | not_ready |

## Review Finding

The staged draft is supported as a hold/revise item, not as promotion-ready evidence. Its main conclusion is well founded: the local derivative record cannot currently establish which text controls page 5, so no page-5 occupational claim should be promoted from either the 1999/1998 page Markdown or the 1979-1970 chunk.

The staged draft's identity caution is also supported for this task. The reviewed files provide document-level naming through the source title and job metadata, but the page-level text itself does not supply a direct identity bridge to `Dario Arturo Pulgar-Smith` and does not support any Jose/Juana parent cluster or Pulgar-line merge.

## Next Action

Hold for source-prep/conversion QA. Restore or regenerate the authoritative rendered page image for page 5, compare it against both derivative transcriptions, repair stale chunk or page Markdown outputs as needed, then rerun proof review on any surviving occupational claims. Keep canonical identity attachment and relationship claims on hold pending separate identity-bearing evidence.
