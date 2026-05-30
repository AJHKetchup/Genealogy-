---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530233252051
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

- Page-control conflict is confirmed. The assigned chunk and aggregate converted file contain the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO sequence, while the conversion job page Markdown for page 5 contains 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen/SNC Lavalin entries.
- Visual proof cannot be completed from this checkout. The job manifest records `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg`, but the file is absent.
- Metadata control is unstable. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice with different character counts and hashes, and the source packet records a converted-file hash mismatch between recorded and observed conversion content.
- Page-local identity support is limited. The reviewed page body does not repeat `Dario Arturo Pulgar`; attribution to that person comes from the source title and document-level CV context.
- No relationship claim is supported. The checked materials name no parents, spouse, children, siblings, household members, descendants, or other kinship links.

## Evidence Strengths

- The staged identity/conflict analysis accurately preserves both competing derivative readings and correctly treats the issue as a conversion/page-control conflict.
- The assigned chunk and aggregate converted file agree with each other on the older work-history sequence and the ending `EDUCATION` heading.
- The source packet correctly limits future use to narrow work-history claims after conversion QA and explicitly excludes family-relationship promotion.
- Relevance to the Pulgar line is high at the document level because the source is titled `CV of Dario Arturo Pulgar`, but that relevance does not resolve page control or prove a canonical identity bridge.

## Scored Judgment

| Metric | Score / value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.46 | Named CV PDF source, but this review is derivative-only because the page image is missing. |
| conversion_confidence_score | 0.20 | Low because page image proof is unavailable, page-5 derivatives conflict, and manifest/hash metadata is unstable. |
| evidence_quantity_score | 0.42 | Substantial work-history text exists, but it is one disputed page with no visual confirmation. |
| agreement_score | 0.30 | Assigned chunk and assembled conversion agree, but the job page Markdown materially disagrees. |
| identity_confidence_score | 0.68 | Moderate for document-level `Dario Arturo Pulgar`; insufficient for any canonical merge, alias, or relationship bridge. |
| claim_probability | 0.58 | The assigned chunk may be correct, but cannot be preferred over page Markdown until page control is certified. |
| relevance_level | high | Relevant to Pulgar CV work-history and possible later identity comparison. |
| relevance_confidence | 0.88 | Document title and source-packet context support relevance despite page-local identity limits. |
| canonical_readiness | not_ready | Do not promote claims, relationships, identity merges, name variants, or wiki updates from this staged draft. |

## Review Decision

Hold for conversion QA. The staged draft is supported as a page-control conflict analysis, but the underlying evidence is not ready for canonical use. No same-person merge, duplicate-person merge, name-variant promotion, relationship promotion, chronology promotion, or canonical wiki update should be made from this draft.

## Next Action

Restore or regenerate `page-images/page-0005.jpg`, repair the duplicate `CHUNK-fb0a0000636f-P0005-01` manifest state, resolve the converted-file hash mismatch, and certify which page-5 transcription controls. After that, rerun visual proof review against the certified page text before any identity-bridge review or canonical promotion.
