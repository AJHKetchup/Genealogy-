---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003857892.md
worker: postconv-proof-review-20260531040604568
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003857892.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530234356813.md
reviewed_conflict_candidate: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530234356813.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
review_status: complete
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Page 5 CV Control Conflict

## Blockers

- The staged draft under review is exactly `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003857892.md`.
- The core page-control conflict is verified. The assigned chunk and aggregate converted file contain a 1979-1982 through 1970-1972 work-history page, while the conversion-job page Markdown for page 5 contains a 1999 through 1997-1998 consulting-work page.
- The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice with conflicting character counts and SHA-256 values. This prevents treating the chunk metadata as stable page control.
- The source packet reports hash drift between recorded and observed converted/chunk hashes; that concern is consistent with the manifest conflict.
- The page image paths referenced by the job manifest for page 5 were not available at review time: `page-images/page-0005.jpg` and `extracted-images/page-0005.jpg` both tested absent. The physical page therefore was not available in this review to select the controlling derivative transcription.
- Page-local identity is weak. The page body in either derivative does not restate the full name `Dario Arturo Pulgar`; that identity comes from the CV title/source path and document-level context.
- No family relationship appears in either derivative page-5 text. There is no literal support here for parent, spouse, child, grandchild, or Pulgar-Smith/Pulgar-Arriagada identity bridging.

## Evidence Strengths

- The source packet, conflict candidate, assigned chunk, aggregate converted file, page Markdown, and manifests are internally sufficient to verify that a real derivative-text conflict exists.
- The source title and source path consistently identify the document as `CV of Dario Arturo Pulgar`, supporting a limited document-level subject attribution.
- The two competing texts are clear and specific enough to define the conversion QA question: page 5 must be checked against the physical PDF/page image before either occupational chronology is used.
- The identity-analysis draft appropriately treats the conflict as a hold and does not promote the disputed work-history sequence into canonical person or relationship claims.

## Scored Judgment

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.62 | A CV is a relevant identity/work-history source, and the source file has a recorded SHA-256, but this review did not inspect the physical page image/PDF page. |
| conversion_confidence_score | 0.16 | Two local derivatives disagree materially for page 5, manifest entries duplicate the chunk id with conflicting hashes, and the page image was unavailable. |
| evidence_quantity_score | 0.46 | Multiple local derivatives and metadata files were available, but they are conflict evidence rather than settled claim evidence. |
| agreement_score | 0.18 | The derivatives agree on document context but disagree on the actual page-5 content and chronology. |
| identity_confidence_score | 0.55 | Document-level title supports `Dario Arturo Pulgar`; page-local text does not independently name the person or bridge to `Dario Arturo Pulgar-Smith`. |
| claim_probability | 0.30 | The narrow claim that a page-control conflict exists is high, but any occupational or canonical identity claim from page 5 remains low until QA selects a controlling transcription. |
| relevance_level | high | The reviewed evidence directly addresses the assigned page-control and identity-risk question. |
| relevance_confidence | 0.97 | All reviewed files reference the same staged draft, chunk id, source, and page-control dispute. |
| canonical_readiness | hold_for_conversion_qa | Do not promote occupational, identity-bridge, or relationship claims from this page until the physical page is checked and metadata drift is repaired. |

## Claim Review

The staged draft's central judgment is supported: page 5 is not ready for canonical use because the local derivative texts disagree and metadata control is unstable.

The draft's document-level attribution to `Dario Arturo Pulgar` is reasonable as a source-title inference only. It should remain explicitly separate from page-local proof because neither competing page-5 text names the subject.

The draft's caution against attaching the page to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or Jose/Juana parent candidates is supported. This evidence set contains no relationship terms, no surname bridge to Smith or Arriagada, and no independent family identifiers.

The staged draft should not be promoted as a work-history claim. It should remain an identity/control analysis note or be revised only after conversion QA determines whether the controlling page is the 1999-1997 page-markdown text or the 1979-1970 assigned-chunk text.

## Next Action

Hold for targeted conversion QA. Restore or inspect the physical PDF page/image for page 5 of `raw/sources/CV of Dario Arturo Pulgar.pdf`, compare it against both competing local derivatives, repair the duplicate manifest/hash drift, and then rerun claim extraction and identity-bridge proof review before any canonical update.
