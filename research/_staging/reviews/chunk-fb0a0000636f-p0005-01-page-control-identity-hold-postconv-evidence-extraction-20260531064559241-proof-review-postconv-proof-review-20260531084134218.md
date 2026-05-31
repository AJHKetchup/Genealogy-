---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531084134218
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
canonical_readiness: blocked
---

# Proof Review: Page-Control Identity Hold

## Blockers First

1. Keep this item on hold. The assigned chunk and the page-0005 conversion do not describe the same page content. The chunk contains the 1979-1970 HABITAT/NFB/Chile Films/CITELCO work-history page ending at `EDUCATION`, while the page-0005 conversion and rough Docling discovery contain the 1999-1997 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin page.
2. Do not promote any claim from this staged draft to canonical files. The source PDF and manifest-listed page image for page 5 are not available at the referenced local paths, so the physical page cannot be visually verified in this review.
3. Treat the chunk manifest as unreliable for this item until conversion QA reruns. It records duplicate `CHUNK-fb0a0000636f-P0005-01` entries with different character counts and different hashes, and the current local file hashes do not match the manifest values.
4. Do not attach this page to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, Jose del Carmen Pulgar, Juana Arriagada de Pulgar, or any family relationship. The reviewed page materials do not state those identity bridges or relationships.

## Evidence Strengths

- The staged draft correctly identifies a page-control conflict between the assigned chunk and the page-0005 conversion context.
- The converted file, page-0005 job Markdown, and rough Docling discovery agree with each other on the 1999-1997 consulting-work content.
- The assigned chunk is internally coherent as a CV work-history page, but it appears to correspond to a different page/control position than the page-0005 conversion context.
- The source title provides a document-continuity hypothesis for `Dario Arturo Pulgar`, but the page body does not independently repeat the subject name or provide a family bridge.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 4/10 for the CV as a potential self-authored career source, reduced because the source PDF and page image are unavailable locally for this review |
| conversion_confidence_score | 2/10 for the assigned page-5 chunk/control; 6/10 for the page-0005 conversion text as unverified but internally consistent with rough Docling |
| evidence_quantity_score | 2/10 for identity or relationship claims; 5/10 for the narrow observation that conflicting local page-control artifacts exist |
| agreement_score | 2/10 between assigned chunk and page-0005 conversion context; 7/10 between page-0005 conversion Markdown and rough Docling discovery |
| identity_confidence_score | 2/10 for attaching the assigned chunk to any canonical person; 4/10 for the limited document-continuity hypothesis that the CV source concerns `Dario Arturo Pulgar` |
| claim_probability | 0.85 that a page-control/chunking conflict exists; 0.25 that the assigned chunk is valid evidence for physical page 5; 0.15 or lower for any canonical identity merge or family relationship claim |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | blocked |

## Review Finding

The staged draft is supported as a hold recommendation. The review confirms the page-control conflict using only the referenced local conversion artifacts: the assigned chunk does not agree with the page-0005 conversion Markdown or rough Docling discovery. The conflict is compounded by missing local source/page-image files and stale or inconsistent hash metadata. Because the physical page cannot be checked and the chunk identity is unstable, the work-history details should not be used as canonical evidence.

The only supported conclusion is procedural: this item requires conversion QA and page-control repair before any genealogical claim can be evaluated. The reviewed materials do not support identity merges, name normalization beyond the source-title hypothesis, parent/spouse/child relationships, or attachment to canonical family pages.

## Next Action

Run conversion QA for this source packet after restoring or regenerating the rendered page image and source PDF at the manifest paths. Rebuild the chunk manifest so `CHUNK-fb0a0000636f-P0005-01` maps to one physical page and one stable hash, then rerun proof review before considering any canonical claim.
