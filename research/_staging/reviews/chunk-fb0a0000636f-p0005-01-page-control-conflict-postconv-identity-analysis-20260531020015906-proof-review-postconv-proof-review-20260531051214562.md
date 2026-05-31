---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531051214562
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

1. Do not promote page-5 occupational claims from this staged draft. The assigned chunk preserves a 1979-1970 work-history page, while the conversion-job page Markdown for page 5 preserves a different 1999-1997 consulting-work page.
2. Do not use this item for a same-person merge or family relationship. The page-5 body in the checked derivatives does not state `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Smith`, `Arriagada`, parents, spouse, children, or Alexander John Heinz.
3. The source PDF and authoritative page image were not locally available for visual verification. `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent, and the manifest-listed `page-images/page-0005.jpg` is absent under the conversion job tree.
4. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts and hashes. This supports a derivative-integrity blocker, not a resolved page transcription.

## Evidence Strengths

- The staged draft accurately identifies the main control conflict: the assigned chunk contains `1979 - 1982` HABITAT/Nairobi through `1970 - 1972` CITELCO/Santiago and ends with `EDUCATION`.
- The conversion-job page Markdown for page 5 independently contains the competing `1999` PROFONANPE/Peru through `1997-1998` SNC Lavalin Agriculture/Maracaibo text.
- The source packet correctly reports that the recorded source title/path identifies a document-level CV subject as `Dario Arturo Pulgar`, while page 5 itself does not independently bridge that subject to a canonical person.
- The staged draft's hold/block recommendation is supported by the available local derivatives and metadata.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 4/10 |
| conversion_confidence_score | 1/10 |
| evidence_quantity_score | 2/10 for identity/relationship claims; 5/10 for the existence of a local derivative conflict |
| agreement_score | 2/10 between assigned chunk, aggregate converted file, conversion-job page Markdown, and manifests |
| identity_confidence_score | 5/10 for document-level `Dario Arturo Pulgar` only from title/path context; 1/10 for any merge to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada` |
| claim_probability | 0.95 that a page-control/derivative-integrity conflict exists; 0.35 that either competing page-5 occupational transcription controls the physical page; 0.01 for any family relationship claim |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | blocked |

## Review Finding

The staged identity/conflict analysis is supported as a blocked proof judgment. The local evidence is strong enough to say that page-control and derivative integrity are compromised, but not strong enough to decide which transcription controls physical page 5. The conversion-job manifest records an image path and source PDF hash, but the checked files needed for visual verification are absent locally.

No page-5 text checked here supplies an independent identity bridge beyond document title/path context. Name-overlap or family-context matching must remain outside this page-5 claim until a separate identity-bridge review can use direct identifiers.

## Next Action

Keep this item on hold for conversion QA. Restore or re-render the authoritative page-5 image/source PDF, reconcile duplicate chunk metadata and hashes, then re-review the controlling page-5 transcription before staging any occupational claim. After page control is repaired, handle any link from the CV subject to canonical Pulgar identities in a separate identity-bridge proof review.
