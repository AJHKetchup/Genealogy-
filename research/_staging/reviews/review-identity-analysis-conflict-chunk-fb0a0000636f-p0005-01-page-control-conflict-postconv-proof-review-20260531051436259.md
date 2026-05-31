---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260531051436259
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531015428195.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531015428195.md
reviewed_status: hold
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.30
conversion_confidence_score: 0.20
evidence_quantity_score: 0.45
agreement_score: 0.15
identity_confidence_score: 0.55
claim_probability: 0.49
relevance_level: high
relevance_confidence: 0.99
created_at: 2026-05-31T05:14:36Z
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page Control Conflict

## Blockers First

- The staged draft is not ready for canonical promotion because physical page control remains unresolved. The assigned chunk preserves a 1979-1970 work-history page, while the conversion-job page Markdown for page 5 preserves a different 1999-1997 consulting-work page.
- The recorded source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent at the referenced path, and no `page-0005.jpg`, `page-0005.jpeg`, or `page-0005.png` was found under the referenced conversion-job directory during this review.
- The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` with conflicting `chars` and `sha256` values, so the manifest does not provide reliable control for selecting the correct page-5 derivative.
- No reviewed page-5 derivative body independently states a family relationship, a `Pulgar-Smith` identity bridge, or an `Arriagada` identity bridge. Any merge or canonical attachment by name alone would be a relationship/identity jump.

## Evidence Strengths

- The assigned staged identity-analysis draft accurately describes the core conversion conflict and appropriately sets `status: hold` and `canonical_readiness: hold_for_conversion_qa`.
- The referenced source packet accurately reports the assigned chunk's 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries, followed by `EDUCATION`.
- The referenced conversion-job page Markdown accurately contains the competing 1999 PROFONANPE and Television Trust for the Environment entries, plus 1998-1999 Arca Consulting/European Commission, 1997-1998 Klohn Crippen Consultants, and SNC Lavalin Agriculture entries.
- The aggregate converted file contains terms from both competing sequences, which supports treating this as a page-control/conversion QA issue rather than resolved literal evidence for one physical page.

## Scored Judgment

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.30 | The source is a CV derivative with potentially useful biographical detail, but the original PDF is unavailable for review. |
| conversion_confidence_score | 0.20 | Competing page-5 derivatives, absent source/image, and duplicate manifest entries block confidence in page control. |
| evidence_quantity_score | 0.45 | There is enough derivative text to identify the conflict, but not enough controlled evidence to certify page-5 claims. |
| agreement_score | 0.15 | The chunk and conversion-job page Markdown materially disagree on the page body. |
| identity_confidence_score | 0.55 | Moderate only for document-level `Dario Arturo Pulgar` from title/path context; low for canonical same-person attachment. |
| claim_probability | 0.49 | The staged conclusion that this is a hold-level page-control conflict is more probable than either derivative being selected without QA. |
| relevance_level | high | The reviewed files directly concern the assigned staged draft and its referenced page-5 conflict. |
| relevance_confidence | 0.99 | The evidence context is tightly matched to the assigned chunk and page reference. |
| canonical_readiness | hold_for_conversion_qa | Do not promote facts, relationships, name variants, or identity merges until conversion/source QA resolves control. |

## Claim-Level Review

- Supported: the staged draft's main claim that page 5 has a conversion/page-control conflict.
- Supported: the assigned chunk literally contains the 1979-1970 work-history sequence described in the staged draft.
- Supported: the conversion-job page Markdown literally contains the competing 1999-1997 consulting-work sequence described in the staged draft.
- Not supported for promotion: attaching either page-5 work-history sequence to a canonical person while page control is unresolved.
- Not supported by this page-5 evidence: any family relationship claim, parent claim, spouse/child claim, `Dario Arturo Pulgar-Smith` merge, or `Pulgar-Arriagada` merge.

## Next Action

Keep this staged draft on hold. Conversion/source QA should restore the original PDF or an authoritative page-5 image, compare it against both derivative readings, repair or supersede the duplicate manifest/hash state, and certify the controlling physical page-5 transcription. After that, rerun proof review on the surviving literal page-5 claims before any canonical promotion or identity-bridge review.
