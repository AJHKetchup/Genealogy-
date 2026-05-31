---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531084635884
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
chunk_id: "CHUNK-fb0a0000636f-P0005-01"
canonical_readiness: blocked
---

# Proof Review: Page-Control Identity Hold

## Blockers First

1. Do not promote any page-5 work-history claim from this staged draft. The assigned chunk and the page-5 conversion-job Markdown identify different page bodies: the chunk contains 1979-1970 HABITAT/National Film Board/Chile Films/CITELCO content, while `page-0005.md` contains 1999-1997 PROFONANPE/TVE/Arca Consulting/Klohn Crippen/SNC Lavalin content.
2. Do not attach either page body to a canonical person or family cluster. The checked page material does not itself repeat a subject name and does not state `Pulgar-Smith`, parentage, spouse, children, or any family relationship.
3. Source control is not reviewable to image standard in the current workspace. The referenced source PDF, staged source PDF, and rendered `page-0005.jpg` are absent locally, although the manifest and visual metadata refer to them.
4. The chunk manifest is internally unsafe for promotion: it duplicates `CHUNK-fb0a0000636f-P0005-01` for the same chunk path with incompatible recorded sizes and SHA-256 values. Current observed hashes also do not match the recorded converted/chunk hashes.

## Evidence Strengths

- The staged draft accurately identifies the core page-control conflict between the assigned chunk and the conversion-job page Markdown.
- The referenced converted file contains both content groups in the broader pages 4-9 aggregate, which supports the conclusion that the conflict is a page-control/chunking problem rather than a simple transcription disagreement.
- The source title and manifest title provide weak document-continuity context for a CV of `Dario Arturo Pulgar`, but that is not enough to bridge the page-5 chunk to any canonical identity or relationship.
- The staged draft correctly recommends a hold for identity and relationship use pending conversion QA and a separate identity-bridge review.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 3/10: CV source may be relevant, but the source PDF and rendered page image are unavailable for direct verification. |
| conversion_confidence_score | 1/10 for the assigned page-5 claim set because page-control conflict and missing image prevent certification. |
| evidence_quantity_score | 2/10: only one conflicted CV page/chunk context was reviewed, with no independent identity bridge. |
| agreement_score | 1/10 between assigned chunk and page-5 conversion-job Markdown; 6/10 that the staged draft accurately reports the conflict. |
| identity_confidence_score | 2/10 for document-continuity association with `Dario Arturo Pulgar`; 0.5/10 for `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, Jose/Juana parent candidates, or any family relationship. |
| claim_probability | 0.20 that the assigned chunk is the authoritative physical page 5; 0.70 that there is a real page-control/chunking conflict; 0.10 or lower for any canonical identity merge or relationship claim from this item. |
| relevance_level | high for the Dario Arturo Pulgar CV research cluster, but only as a QA blocker. |
| relevance_confidence | 0.80 that the hold is relevant; 0.20 that the specific chunked work-history facts are ready as evidence. |
| canonical_readiness | blocked; hold for conversion QA and identity-bridge proof review. |

## Review Finding

The staged draft is supported as a proof-review hold. The available conversion artifacts do not establish which text is the authoritative physical page 5, and the absence of the source PDF/page image prevents direct page verification. Because the page body lacks a visible subject name and contains no kinship language, no identity merge or relationship claim is supported.

The boundary between verification context and transcription should remain strict: downstream work may ask conversion QA to determine whether the physical page 5 is the 1999-1997 consulting page or the 1979-1970 work-history page, but this review does not authorize changing names or attaching the content to a canonical person.

## Next Action

Keep this item on hold. Restore or regenerate the rendered page image/source PDF, repair or supersede the duplicate chunk manifest rows and hash drift, and rerun conversion QA. After page control is certified, run a separate identity-bridge proof review before attaching any surviving CV claims to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or any canonical family relationship.
