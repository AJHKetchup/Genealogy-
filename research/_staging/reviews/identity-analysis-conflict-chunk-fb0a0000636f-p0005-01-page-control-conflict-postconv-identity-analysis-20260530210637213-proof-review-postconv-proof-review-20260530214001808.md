---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530214001808
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold
---

# Proof Review: Page 5 Control Conflict

## Blockers First

1. Hold all claims from this staged draft. The assigned chunk and source packet support a 1979-1970 work-history page, while the conversion job page Markdown for the same page number supports a different 1999/1998 work-history page.
2. The visible page-control source could not be checked from the referenced local page image because `page-images/page-0005.jpg` is missing, even though the job manifest lists it.
3. The referenced source PDF path `raw/sources/CV of Dario Arturo Pulgar.pdf` is also unavailable in this workspace, and the job manifest's staged `source/` directory is absent. This prevents authoritative visual/source-page verification.
4. The chunk manifest contains duplicate records for `CHUNK-fb0a0000636f-P0005-01` with different character counts and hashes, so the derivative provenance is unstable.
5. Do not attach either page-5 work-history sequence to canonical `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana candidate from this draft. The reviewed page-level derivatives do not state a birth, death, parent, spouse, child, household, or identity bridge.

## Evidence Strengths

- The staged draft correctly identifies this as a conversion/provenance conflict rather than a genealogical relationship conflict.
- The source packet and assigned chunk agree internally on the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO sequence.
- The conversion job page Markdown and the aggregate converted file also contain a page-5 section with 1999/1998 entries, confirming that a materially different page-5 derivative exists.
- The job manifest names page 5, `page-markdown/page-0005.md`, and `page-images/page-0005.jpg`, which gives a clear next QA target even though the page image is missing locally.
- The staged draft's caution about identity and relationship promotion is supported: none of the reviewed derivative page-5 bodies repeats `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, parent candidates, spouse, children, or other kinship facts.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 5/10 for the CV as a source type, but 2/10 for this review because the referenced source PDF/page image is unavailable |
| conversion_confidence_score | 2/10 |
| evidence_quantity_score | 4/10 for detecting the derivative conflict; 1/10 for any genealogical identity or relationship claim |
| agreement_score | 2/10 across page-5 derivatives; 7/10 within the 1979-1970 chunk/source-packet pair only |
| identity_confidence_score | 4/10 for document-level subject attribution to `Dario Arturo Pulgar`; 1/10 for attachment to `Dario Arturo Pulgar-Smith` or Pulgar-Arriagada/Jose/Juana candidates |
| claim_probability | 0.85 that a derivative page-control conflict exists; 0.25 that either page-5 work-history sequence is promotion-ready now; 0.10 for any relationship claim |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold, not ready |

## Review Finding

The staged analysis is supported as a hold. The proof-reviewable fact is the derivative conflict itself: two local derivative paths assign incompatible work-history content to page 5, and the manifest/chunk provenance is inconsistent.

The occupational contents should not be promoted from either derivative text until the authoritative page image or source PDF page is restored and compared. The identity discussion should remain cautious and non-canonical because the reviewed page-level evidence does not supply a page-local name or relationship bridge.

## Next Action

Restore or regenerate the referenced page image/source-page control, then rerun conversion QA to decide whether page 5 is the 1999/1998 text or the 1979-1970 text. After derivative repair, rerun proof review before staging any occupational claim, and run a separate identity-bridge review before attaching any surviving CV claim to a canonical person.
