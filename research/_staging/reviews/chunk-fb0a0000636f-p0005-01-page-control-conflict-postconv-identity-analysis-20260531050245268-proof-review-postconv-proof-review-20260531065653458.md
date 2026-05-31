---
type: proof_review_note
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531065653458
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531050245268.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531050245268.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
review_decision: hold
source_quality_score: 0.25
conversion_confidence_score: 0.15
evidence_quantity_score: 0.25
agreement_score: 0.10
identity_confidence_score: 0.20
claim_probability: 0.25
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: blocked
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers First

1. Canonical promotion remains blocked. The staged draft is supported in identifying an unresolved page-control conflict for page 5.
2. The controlling source cannot be verified from local primary evidence. `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent, and the manifest-expected `page-images/page-0005.jpg` is also absent.
3. The derivative page texts materially disagree. `page-markdown/page-0005.md` and the aggregate converted file's labeled page-5 section preserve 1999-1997 consulting entries, while the assigned chunk preserves 1979-1970 work-history entries ending at `EDUCATION`.
4. Chunk provenance is unstable. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for the same `page-0005-chunk-01.md` path, with different chunk numbers, character counts, and SHA-256 values.
5. Neither derivative page body literally names Dario Arturo Pulgar or any proposed identity variant. Attachment to a person depends only on document title/path continuity.
6. No same-person merge, name normalization, parent/child/spouse relationship, or chronology claim is supportable for canonical use from this page until conversion QA certifies the controlling page and a separate identity-bearing bridge is reviewed.

## Evidence Strengths

- The staged draft accurately reports the central conflict between the page-job Markdown and assigned chunk.
- The converted file and page-job Markdown agree on one page-5 reading: 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen/SNC Lavalin Agriculture.
- The assigned chunk consistently preserves the competing reading: 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, 1970-1972 CITELCO, followed by `EDUCATION`.
- The document path and converted metadata identify the source set as a CV of Dario Arturo Pulgar, making the conflict relevant to identity and chronology work even though the page body itself is not identity-bearing.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 0.25 |
| conversion_confidence_score | 0.15 |
| evidence_quantity_score | 0.25 |
| agreement_score | 0.10 |
| identity_confidence_score | 0.20 |
| claim_probability | 0.25 |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | blocked |

## Review Finding

The staged identity/conflict analysis is supported as a hold. The only proof-reviewed conclusion available now is that page-5 evidence is conflicted and cannot be used for canonical work-history, identity-merge, name-variant, relationship, or chronology claims.

The uncertainty should not be converted into a silent transcription correction. It is acceptable to ask conversion QA to double-check whether the certified page belongs to the Dario Arturo Pulgar CV, but this review cannot choose between the 1999-1997 and 1979-1970 readings without the source PDF or authoritative page image.

## Next Action

Conversion QA should restore or regenerate the authoritative page-5 image or source PDF, compare it against both derivative readings, repair the duplicate chunk manifest/hash drift, and certify the controlling page-5 transcription. After that, rerun proof review on the certified page text before any canonical promotion or identity attachment.
