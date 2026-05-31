---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531051655931
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020015906.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020015906.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531010209483.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: blocked
---

# Proof Review: CV Page 5 Page-Control Conflict

## Blockers First

1. Canonical promotion is blocked. The assigned chunk and the conversion-job page Markdown give different page-5 readings: the chunk has 1979-1970 work-history entries ending at `EDUCATION`, while `page-markdown/page-0005.md` has 1999-1997 consulting entries.
2. The original source PDF is absent at `raw/sources/CV of Dario Arturo Pulgar.pdf`, and the conversion-job staged source PDF is also absent at the manifest's `local_staged_source_file` path.
3. The manifest references `page-images/page-0005.jpg`, but no `page-images` directory exists under the conversion job tree, so the physical page image cannot be checked in this review.
4. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts and recorded hashes. Current local file hashes do not match the recorded converted/chunk hashes in the chunk front matter.
5. The aggregate converted file contains both competing readings in different positions, so it does not resolve which transcription controls physical page 5.
6. Page 5 supplies no direct family relationship, parent, spouse, child, `Smith`, `Jose`, `Juana`, `Arriagada`, or Alexander John Heinz bridge. Any same-person or relationship conclusion must remain outside this page-5 proof.

## Evidence Strengths

- The staged draft accurately identifies the page-control problem and correctly recommends hold/block rather than promotion.
- The assigned chunk clearly contains the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- The conversion-job page Markdown clearly contains the competing 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting, 1997-1998 Klohn Crippen, and SNC Lavalin entries.
- The source packet correctly reports high uncertainty, absent recorded source PDF, duplicate chunk metadata, and hash drift.
- The source title/path and job metadata make the broader document relevant to a `Dario Arturo Pulgar` CV cluster, but that is document-level context rather than independent page-5 identity proof.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 4/10 |
| conversion_confidence_score | 1/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 |
| identity_confidence_score | 5/10 for document-level `Dario Arturo Pulgar` context from title/path; 2/10 for same as `Dario Arturo Pulgar-Smith`; 1/10 for `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or Jose/Juana parent attachment |
| claim_probability | 0.95 that a local derivative conflict exists; 0.30 that the assigned-chunk 1979-1970 text controls physical page 5; 0.30 that the job page Markdown 1999-1997 text controls physical page 5; 0.05 for any family relationship claim from page 5 |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | blocked |

## Review Finding

The staged draft is supported in its main conclusion: this is a page-control and derivative-integrity conflict, not promotion-ready identity or relationship evidence. The available files prove that two incompatible page-5 derivative readings exist, while the source PDF and page image needed to adjudicate them are unavailable locally.

One point should be tightened if this draft is revised: the aggregate converted file is not a clean witness for only the 1979-1970 reading. It contains the 1999-1997 text near the earlier page-5 position and the 1979-1970 text later, which increases the likelihood of duplicate or shifted page assembly rather than resolving the conflict.

## Next Action

Hold this item for conversion QA. Restore or regenerate the source PDF/page image, reconcile the duplicate chunk manifest entries, recompute the converted and chunk hashes, and certify the controlling page-5 transcription before any work-history claim is promoted. Run a separate identity-bridge proof review only after page control is repaired.
