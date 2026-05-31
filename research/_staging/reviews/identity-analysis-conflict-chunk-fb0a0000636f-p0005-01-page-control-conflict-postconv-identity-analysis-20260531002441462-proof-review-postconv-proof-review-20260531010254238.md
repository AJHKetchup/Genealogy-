---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260531010254238
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002441462.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002441462.md
review_status: hold
canonical_readiness: not_ready
claim_probability: 0.49
created_at: 2026-05-31T01:02:54Z
---

# Proof Review: CV Page 5 Control Conflict

## Blockers First

- The exact staged draft reviewed is `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002441462.md`.
- Page control is unresolved. The assigned chunk preserves a 1979-1970 work-history page headed by HABITAT, NFB, Chile Films, and CITELCO; the conversion-job `page-markdown/page-0005.md` preserves a different 1999-1997 consulting-work page headed by PROFONANPE, TVE, Arca Consulting, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The referenced source packet reports missing local page imagery for page 5, duplicate manifest entries for `CHUNK-fb0a0000636f-P0005-01`, and stale versus observed hash differences. Local checks also found no `page-images/page-0005.jpg` or `extracted-images/page-0005.jpg`.
- Neither competing page-5 derivative independently names the person in the body text or states any parent, spouse, child, grandchild, household, or relationship claim.
- The draft's hold recommendation is supported. No occupational, place, identity-merge, relationship, or canonical wiki claim should be promoted from this item until conversion QA establishes the controlling physical page.

## Evidence Strengths

- The source title and metadata consistently identify the larger document as `CV of Dario Arturo Pulgar`.
- Both derivative text blocks are coherent CV-style professional chronology and are internally readable.
- The assigned chunk directly supports the existence of a derivative transcription containing the 1979-1970 HABITAT/NFB/Chile Films/CITELCO entries.
- The conversion-job page Markdown directly supports the existence of a competing derivative transcription labeled page 5 containing the 1999-1997 PROFONANPE/TVE/Arca/Klohn/SNC Lavalin entries.
- The staged identity analysis appropriately treats this as a conversion/page-control conflict before treating it as a person-identity conflict.

## Scoring

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.55 | A CV can be useful for self-presented occupational chronology, but this review only verifies conflicting derivatives, not a visible controlling page image. |
| conversion_confidence_score | 0.18 | Page image is unavailable locally, derivative page-5 text conflicts, chunk manifest has duplicate entries, and recorded hashes do not match observed hashes. |
| evidence_quantity_score | 0.40 | Several local derivatives and packets were reviewed, but all depend on unresolved page control. |
| agreement_score | 0.20 | Metadata agrees on page 5 and document identity, but the substantive page transcription disagrees materially. |
| identity_confidence_score | 0.50 | Moderate only for document-level attribution to the CV title subject; low for any canonical person attachment or name-variant merge. |
| claim_probability | 0.49 | It is plausible both text blocks belong somewhere in the CV, but the exact physical page-5 claim is unproved. |
| relevance_level | high | The reviewed files directly address the assigned page-control conflict. |
| relevance_confidence | 0.98 | The staged draft, source packet, chunk, page Markdown, converted aggregate, and manifests all refer to the same CV/page-5 control problem. |
| canonical_readiness | 0.03 | Not ready for canonical claims, relationships, merges, person-page updates, or page-specific occupational facts. |

## Review Judgment

Decision: `hold_for_conversion_qa`; `canonical_readiness: not_ready`.

The identity-analysis draft is materially supported as a warning note, not as promotable proof. It correctly avoids making a family relationship or same-person conclusion from page 5. The strongest supported claim is only that local derivatives for the CV page conflict and require conversion/source QA.

## Next Action

Conversion QA should restore or regenerate the authoritative page-5 image from the source PDF, compare it against both derivative transcriptions, reconcile duplicate chunk-manifest and hash drift, then rerun proof review only for the surviving page-5 work-history claims. A separate identity-bridge review is still required before attaching document-level `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith` or separating/merging him with any Pulgar-Arriagada candidate.
