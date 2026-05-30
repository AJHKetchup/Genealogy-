---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530232814400
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md
review_status: hold
canonical_readiness: not_ready
source_quality_score: 0.46
conversion_confidence_score: 0.20
evidence_quantity_score: 0.42
agreement_score: 0.30
identity_confidence_score: 0.68
claim_probability: 0.58
relevance_level: high
relevance_confidence: 0.88
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers First

- Page-control conflict is literal and unresolved. The assigned chunk and aggregate converted file contain the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO sequence, while the conversion job page Markdown for page 5 contains 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen/SNC Lavalin entries.
- Visual proof cannot be completed from the available files. `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is absent in this checkout.
- Metadata control is unstable. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice with different character counts and hashes, and the source packet records a converted-file hash mismatch between recorded and observed content.
- Page-local identity support is limited. The page body does not repeat `Dario Arturo Pulgar`; attribution to that person comes from the source title and document-level CV context.
- No relationship claim is supported. The reviewed materials for this staged draft contain no parent, spouse, child, sibling, household, descendant, or other kinship statement.

## Evidence Strengths

- The staged identity/conflict analysis accurately describes the competing derivative readings and correctly treats the issue as a conversion/page-control conflict rather than a resolved genealogical identity conflict.
- The assigned chunk and the aggregate converted file agree with each other on the older work-history sequence ending with `EDUCATION`.
- The source packet correctly limits potential use to work-history claims after conversion QA and explicitly excludes family-relationship promotion.
- Relevance to the Pulgar line is high at the document level because the source is titled `CV of Dario Arturo Pulgar`, but that relevance does not overcome the page-control and page-local identity limits.

## Scored Judgment

| Metric | Score / value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.46 | Named CV PDF source, but proof review is derivative-only because the page image is unavailable. |
| conversion_confidence_score | 0.20 | Low due to missing page image, duplicate manifest entries, hash mismatch, and conflicting page-5 derivatives. |
| evidence_quantity_score | 0.42 | Substantial work-history text exists, but it is one disputed page with no visual confirmation. |
| agreement_score | 0.30 | Chunk and assembled conversion agree, but the job page Markdown materially disagrees. |
| identity_confidence_score | 0.68 | Moderate for document-level `Dario Arturo Pulgar`; insufficient for any canonical merge or broader identity bridge. |
| claim_probability | 0.58 | The assigned chunk may be correct, but cannot be preferred over page Markdown until page control is certified. |
| relevance_level | high | Relevant to Pulgar CV work-history and possible later comparison. |
| relevance_confidence | 0.88 | Document title and source-packet context support relevance despite page-local identity limits. |
| canonical_readiness | not_ready | Do not promote claims, relationships, identity merges, or wiki updates from this staged draft. |

## Review Decision

Hold for conversion QA. The staged draft is supported as a page-control conflict analysis, but the underlying evidence is not ready for canonical use. The current record should not be revised into a specific work-history claim, identity merge, name-variant promotion, or relationship claim.

## Next Action

Restore or regenerate the page 5 image, repair the duplicate manifest state, resolve the converted-file hash mismatch, and certify which page-5 transcription controls. After that, rerun visual proof review against the certified page text before any separate identity-bridge review or canonical promotion.
