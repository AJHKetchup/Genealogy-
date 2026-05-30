---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530232324268
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md
review_status: hold
canonical_readiness: not_ready
claim_probability: 0.58
relevance_level: high
relevance_confidence: 0.88
source_quality_score: 0.46
conversion_confidence_score: 0.20
evidence_quantity_score: 0.42
agreement_score: 0.30
identity_confidence_score: 0.68
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers First

- Page-control conflict remains unresolved. The assigned chunk and aggregate converted file support the 1979-1982 HABITAT, 1974-1978 NFB, 1972-1973 Chile Films, and 1970-1972 CITELCO sequence, while the conversion job page Markdown for page 5 supports 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen/SNC Lavalin entries.
- Visual proof is unavailable. The job manifest records `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg`, but that file is not present in this checkout.
- Metadata control is unstable. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` with different character counts and hashes, and the source packet records a converted-file hash mismatch between chunk metadata and observed converted content.
- The page body does not independently name Dario Arturo Pulgar. The subject attribution is document-level, from the source title and CV context, not a page-local identity statement.
- No relationship claim is supported. The checked materials contain no parent, spouse, child, sibling, household, or descendant language on this page.

## Evidence Strengths

- The staged draft accurately preserves the two competing derivative readings and does not silently choose between them.
- The assigned chunk and aggregate converted file agree with each other on the older work-history sequence ending with `EDUCATION`.
- The conversion job page Markdown is present and internally coherent for a later CV work-history page, but it directly conflicts with the assigned chunk for the controlling page-5 text.
- The source packet correctly limits evidence scope to possible work-history claims after conversion QA and excludes family-relationship promotion.

## Scored Judgment

| Metric | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.46 | The source is a named CV PDF, but review is derivative-only because the page image is missing. |
| conversion_confidence_score | 0.20 | Low due to missing page image, duplicate chunk manifest entries, hash mismatch, and conflicting page-5 derivatives. |
| evidence_quantity_score | 0.42 | There is substantial work-history text, but only one disputed page and no visual confirmation. |
| agreement_score | 0.30 | Chunk and assembled conversion agree with each other, but the job page Markdown materially disagrees. |
| identity_confidence_score | 0.68 | Moderate for document-level `Dario Arturo Pulgar`; low for any canonical merge or expanded identity bridge. |
| claim_probability | 0.58 | The assigned chunk may be correct, but it cannot be preferred over the page Markdown until page control is restored. |
| relevance_level | high | Relevant to Pulgar CV work-history and possible later identity comparison. |
| relevance_confidence | 0.88 | The document title and source packet make the Pulgar-line relevance clear despite page-local identity limits. |
| canonical_readiness | not_ready | Do not promote claims, relationships, identity merges, or wiki updates from this staged draft. |

## Review Decision

Hold for conversion QA. The staged draft is well supported as a page-control conflict analysis, but the underlying evidence is not ready for canonical use. Any work-history claim from page 5 should remain provisional until a conversion-QA worker restores or regenerates `page-0005.jpg`, repairs the duplicate manifest state, resolves the converted-file hash mismatch, and certifies which page-5 transcription controls.

## Next Action

Route to conversion QA. After page control is certified, rerun visual proof review against the restored page image. Only then should a separate identity-bridge review compare the accepted CV subject evidence to any canonical or staged Pulgar identity candidates.
