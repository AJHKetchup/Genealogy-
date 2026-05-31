---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531050734135
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020015906.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020015906.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531010209483.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
source_quality_score: 0.28
conversion_confidence_score: 0.10
evidence_quantity_score: 0.36
agreement_score: 0.18
identity_confidence_score: 0.33
claim_probability: 0.24
relevance_level: high
relevance_confidence: 0.93
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa_then_identity_bridge
---

# Proof Review: Page 5 Control Conflict

## Blockers First

1. The staged draft's central blocker is supported: the assigned chunk and conversion-job page markdown do not agree on the page-5 body. The assigned chunk contains 1979-1982 HABITAT through 1970-1972 CITELCO and an `EDUCATION` heading; the conversion-job page markdown contains 1999-1997 consulting entries beginning with PROFONANPE.
2. The recorded raw source PDF at `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent. The conversion-job manifest also references `page-images/page-0005.jpg` and a locally staged source PDF, but both checked paths are absent.
3. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting `chars` and `sha256` values. This prevents treating the chunk manifest as clean page-control evidence.
4. Neither competing page-5 derivative body independently names the CV subject. Only metadata/source IDs include `Dario Arturo Pulgar`.
5. No reviewed page-5 derivative states `Smith`, `Arriagada`, `Jose`, `Juana`, parents, spouse, children, or a relationship to Alexander John Heinz. Any relationship or same-person bridge is unsupported from this page.

## Scored Judgment

| Field | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.28 | The document title/path identify a CV of Dario Arturo Pulgar, but the original source and referenced page image are unavailable for direct verification. |
| conversion_confidence_score | 0.10 | Page-control conflict, duplicate chunk metadata, absent image, and absent source block reliance on either derivative as the controlling transcription. |
| evidence_quantity_score | 0.36 | There are several local derivative texts and manifests, but only derivative evidence is available and it conflicts. |
| agreement_score | 0.18 | The chunk and job page markdown agree only that the material is CV-style work history; they disagree on the literal page content. |
| identity_confidence_score | 0.33 | Metadata supports a document-level Dario Arturo Pulgar association, but page 5 itself provides no independent identity bridge to Dario Arturo Pulgar-Smith or other Pulgar candidates. |
| claim_probability | 0.24 | The broad claim that this staged draft identifies a promotion-ready page-5 identity/work-history claim is low because physical page control is unresolved. |
| relevance_level | high | A CV titled for Dario Arturo Pulgar is relevant to Pulgar identity analysis once page control is repaired. |
| relevance_confidence | 0.93 | Relevance is clear from the source title/path and Pulgar matching terms, even though proof value is blocked. |
| canonical_readiness | blocked | No canonical claim, relationship, merge, rename, or wiki update is ready. |

## Evidence Strengths

- The staged draft accurately reports the two competing derivative readings and correctly treats the disagreement as a page-control conflict rather than as a resolved biographical conflict.
- The assigned chunk is internally legible and complete as a derivative transcription of a 1979-1970 professional-history page.
- The conversion-job page markdown is also internally legible as a derivative transcription of a different 1999-1997 professional-history page.
- The source packet's warning about duplicate manifest metadata is supported by the chunk manifest entries for the same chunk ID.

## Review Decision

Hold. The staged draft is reliable as a conflict note, but not as support for a canonical identity, relationship, or occupational claim.

The only claim with strong local derivative support is that conflicting derivative page-5 texts exist in this workspace. The assigned chunk's literal text exists locally, but whether that text controls physical page 5 cannot be verified without the missing page image or source PDF.

## Next Action

1. Restore or regenerate the authoritative source/page image for physical page 5.
2. Reconcile the chunk manifest duplication and hash drift before using `CHUNK-fb0a0000636f-P0005-01` as evidence.
3. After page-control QA, run a separate identity-bridge review for the full CV cluster before attaching the CV subject to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or any Jose/Juana parent candidate.
