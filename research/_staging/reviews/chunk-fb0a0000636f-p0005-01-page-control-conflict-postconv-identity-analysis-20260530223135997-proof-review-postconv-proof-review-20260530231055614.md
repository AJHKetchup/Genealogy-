---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530231007762
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
review_status: hold
canonical_readiness: not_ready
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers First

- Page-control blocker: the assigned chunk and the aggregate converted file contain a page-5 section with `1979 - 1982` HABITAT, `1974 - 1978` National Film Board of Canada, `1972 - 1973` Chile Films, and `1970 - 1972` CITELCO entries, but the conversion job `page-markdown/page-0005.md` contains `1999`, `1998 - 1999`, and `1997-1998` entries for PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture. Both derivative readings cannot control the same page.
- Image blocker: the job manifest records `page-images/page-0005.jpg`, but that image is not present in this checkout. I could not perform visual proof against the source page.
- Manifest/hash blocker: the chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice with different character counts and SHA-256 values, and the source packet records a converted-file hash mismatch.
- Identity blocker: the page body itself does not repeat `Dario Arturo Pulgar`; that identity is supplied by source title and document-level CV context only.
- Relationship blocker: the staged draft is correct that this page names no parents, spouse, children, siblings, household members, or descendants. No relationship or same-person merge claim is review-ready from this page.

## Evidence Strengths

- The staged draft accurately preserves the two competing derivative transcriptions and does not silently prefer one as the controlling source.
- The assigned chunk and source packet agree on the 1979-1970 work-history sequence and give readable literal text for those entries.
- The conversion job page Markdown independently gives readable literal text for the competing 1999-1997 sequence.
- The draft correctly treats this as a conversion/provenance conflict rather than a genealogical relationship conflict.
- The recommendation to hold for conversion QA is supported by the available files.

## Scored Judgment

| Field | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.62 | A CV is a relevant document-level source for work-history claims, but this review only had derivative files and no page image. |
| conversion_confidence_score | 0.20 | Low because the page image is missing, page-control is disputed, and chunk metadata is duplicated/conflicting. |
| evidence_quantity_score | 0.45 | There is substantial derivative text, but only one page and no source-image proof. |
| agreement_score | 0.30 | The assigned chunk/source packet agree with one another, but they conflict with the job page Markdown for the same page. |
| identity_confidence_score | 0.68 | Moderate for document-level `Dario Arturo Pulgar`; low for any canonical merge because the page body gives no independent identity bridge. |
| claim_probability | 0.58 | The held page-control conflict is well supported; either work-history sequence remains unproven as controlling page-5 text until QA resolves the derivative conflict. |
| relevance_level | high | The CV page is relevant to Pulgar-line identity/work-history research if page control is repaired. |
| relevance_confidence | 0.88 | High document relevance from title/source context, with no page-local family relationship relevance. |
| canonical_readiness | not_ready | Do not promote work-history, identity-merge, relationship, or chronology claims from this staged draft. |

## Claim Review

| Claim or hypothesis in staged draft | Review outcome | Probability | Notes |
| --- | --- | ---: | --- |
| The staged draft should remain a held page-control conflict for document-level `Dario Arturo Pulgar`. | supported | 0.82 | The derivative conflict, missing image, and duplicated chunk metadata all support hold status. |
| If QA certifies the assigned chunk, page 5 may support 1979-1970 work-history claims for document-level `Dario Arturo Pulgar`. | plausible but held | 0.58 | Literal derivative support exists, but source-image proof and page-control certification are missing. |
| If QA certifies the job page Markdown, page 5 may support 1999-1997 consultant/work-history claims for document-level `Dario Arturo Pulgar`. | plausible but held | 0.42 | Literal derivative support exists in `page-markdown/page-0005.md`, but it conflicts with the assigned chunk. |
| The CV subject is the same person as canonical `Dario Arturo Pulgar-Smith`. | not review-ready | 0.35 | Name overlap and document context may justify future comparison, but this page gives no `Smith`, relationship, vital, or family bridge. |
| This page bridges to `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or canonical `Dario Pulgar Arriagada`. | unsupported | 0.08 | The reviewed page materials do not contain `Jose`, `Arriagada`, parentage, medical/military context, or another bridge. |
| Jose/Juana parent candidates explain this page-5 subject. | unsupported | 0.03 | No Jose/Juana names or parent-child terms appear in the reviewed page materials. |

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. A conversion-QA worker should restore or regenerate `page-images/page-0005.jpg`, repair the duplicate `CHUNK-fb0a0000636f-P0005-01` manifest entries and hash mismatch, and certify whether page 5 is controlled by the 1979-1970 assigned-chunk sequence or the 1999-1997 job page Markdown sequence. After that, run visual proof review before any canonical promotion or identity-bridge work.
