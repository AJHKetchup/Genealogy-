---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530223136610
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211859579.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211859579.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold
---

# Proof Review: Page-Control Conflict For CV Page 5

## Blockers First

1. Do not promote either page-5 work-history transcription. The assigned chunk/source packet support 1979-1982 through 1970-1972 entries, while the conversion job page Markdown for page 5 supports 1999, 1998-1999, and 1997-1998 entries.
2. The page image cannot currently resolve the conflict. The conversion job manifest declares `page-images/page-0005.jpg`, but that file is not present at the declared path in the workspace.
3. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for the same chunk path and page number with different character counts and hashes.
4. The page body does not repeat `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, parent names, spouse, child, birth, death, or household facts. Subject attachment rests only on document-level CV metadata.
5. No relationship or same-person claim is supported by this staged draft. It cannot resolve Pulgar-Smith, Pulgar-Arriagada, Jose, or Juana identity clusters.

## Evidence Strengths

- The staged draft accurately identifies the controlling issue as conversion/provenance conflict rather than a genealogical fact conflict.
- The source packet, assigned chunk, and aggregate converted file contain internally legible 1979-1970 CV work-history text.
- The conversion job manifest maps page 5 to `page-markdown/page-0005.md`, and that page Markdown contains internally legible 1999/1998 CV work-history text.
- The source title and job metadata consistently identify the broader document as `CV of Dario Arturo Pulgar`, but this is document-level context, not page-local identity proof.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 5/10 |
| conversion_confidence_score | 2/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 |
| identity_confidence_score | 4/10 for document-level attribution to `Dario Arturo Pulgar`; 1/10 for any same-person or relationship conclusion |
| claim_probability | 0.50 that one of the two derivative transcriptions belongs to the intended CV page 5; 0.05 for promoting either exact page-5 claim before image/PDF QA; 0.05 for any kinship claim |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold; not ready for canonical claims, relationships, person pages, or identity merges |

## Review Finding

The staged analysis is supported as a hold. Literal support exists inside each derivative stream, but the streams disagree about what page 5 contains, and the declared page image is unavailable for visual arbitration. Because the visible controlling source page could not be checked, no reviewer should choose the 1999/1998 text or the 1979-1970 text as canonical page-5 evidence.

The CV title supports only a cautious document-level association with `Dario Arturo Pulgar`. It does not prove that the CV subject is `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or any other Pulgar candidate, and it does not state a Jose/Juana parent relationship.

## Next Action

Keep this item on `hold_for_conversion_qa`. Restore or regenerate the page-5 image/PDF-derived page control, repair the duplicate manifest/chunk state, then rerun proof review. After page control is certified, run a separate identity-bridge review before attaching any surviving CV work-history claims to a canonical person.
