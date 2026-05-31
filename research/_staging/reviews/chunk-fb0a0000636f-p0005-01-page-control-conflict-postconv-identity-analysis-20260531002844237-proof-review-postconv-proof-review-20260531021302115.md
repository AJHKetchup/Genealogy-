---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002844237.md
worker: postconv-proof-review-20260531021302115
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002844237.md
review_status: hold
canonical_readiness: not_ready
created_at: 2026-05-31T02:13:02Z
---

# Proof Review: CV Page 5 Control Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002844237.md`.
- Direct physical verification is blocked. `raw/sources/CV of Dario Arturo Pulgar.pdf`, the page-5 rendered image, and the page-5 extracted image are absent in this checkout.
- The referenced derivatives disagree on the page-5 body. The assigned chunk contains 1979-1970 HABITAT/NFB/Chile Films/CITELCO work-history text, while `page-markdown/page-0005.md` contains 1999-1997 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin consulting text.
- Provenance is unstable. The source packet reports converted/chunk hash drift, and the chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` for the same path with different character counts and hashes.
- The reviewed page evidence does not state `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, Jose/Juana parentage, Alexander John Heinz, or any family relationship.
- No canonical claim, identity merge, name variant, relationship, occupation, place, or chronology fact from this page is ready for promotion.

## Scores

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.30 | The source is described as a CV titled for Dario Arturo Pulgar, but the source PDF/page image is unavailable for direct review. |
| conversion_confidence_score | 0.20 | Conversion confidence is low because two local derivatives compete and page image/source control is missing. |
| evidence_quantity_score | 0.45 | There are several local derivatives, but they conflict rather than provide cumulative support. |
| agreement_score | 0.25 | Agreement is poor between the assigned chunk/current aggregate conversion and the conversion-job page Markdown. |
| identity_confidence_score | 0.22 | The page supports only a document-title association with Dario Arturo Pulgar, not a canonical same-person bridge. |
| claim_probability | 0.49 | It is plausible that some reviewed work-history text belongs to the CV, but which text controls physical page 5 is unproved. |
| relevance_level | 0.99 | The reviewed evidence directly concerns the assigned staged draft and its referenced local files. |
| relevance_confidence | 0.98 | The staged draft, source packet, chunk, aggregate converted file, page Markdown, and manifest were checked locally. |
| canonical_readiness | 0.05 | Not ready for canonical claims, relationships, identity merges, or wiki updates. |

## Evidence Strengths

- The staged draft correctly treats this as a page-control/conversion conflict before any identity conclusion.
- The source packet explicitly warns that the source title names `Dario Arturo Pulgar`, while the assigned page body does not independently restate the subject's full name.
- The assigned chunk literally supports the existence of the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries within that derivative.
- The conversion-job `page-markdown/page-0005.md` literally supports a different 1999-1997 sequence beginning with PROFONANPE and Television Trust for the Environment.
- The aggregate converted Markdown contains both competing sequences in a chronology that reinforces the need for page-control QA.

## Review Judgment

Decision: `hold_for_conversion_qa`.

The staged draft is supported as a conflict analysis, but not as proof for any canonical genealogical or occupational claim. The available local files support only the narrower claim that page-5 derivative control is unresolved. They do not justify choosing either transcription as the physical page-5 source, and they do not justify attaching document-level `Dario Arturo Pulgar` to any canonical person or family relationship.

## Next Action

Restore or certify the physical source PDF or page-5 image, compare it visually against both competing derivative transcriptions, reconcile the duplicate chunk-manifest/hash issues, and rerun proof review for only the surviving page-5 claims. After page control is fixed, run a separate identity-bridge review before any canonical person attachment or relationship claim.
