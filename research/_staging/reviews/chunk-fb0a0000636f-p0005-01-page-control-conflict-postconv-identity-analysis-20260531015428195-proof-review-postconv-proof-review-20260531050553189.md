---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531050514645
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531015428195.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531015428195.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531010209483.md"
conflict_draft: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531010209483.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Page Control Conflict

## Blockers First

1. The staged draft is supported as a hold. Page control remains unresolved: the assigned chunk preserves a 1979-1970 work-history page, while the conversion-job page Markdown for page 5 preserves a different 1999-1997 consulting-work page.
2. The recorded source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent locally, and no local `page-0005.jpg`, `page-0005.jpeg`, or `page-0005.png` was found under the conversion-job tree. I could not verify either derivative against the physical page.
3. The aggregate converted file contains both conflicting sequences, so it confirms derivative conflict but does not identify which text controls physical page 5.
4. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` for the same chunk path with different metadata. This independently blocks treating the current chunk mapping as stable.
5. No reviewed page-5 derivative text supports a family relationship, a parent/child/spouse claim, or a same-person merge to `Dario Arturo Pulgar-Smith`, `Dario Pulgar Arriagada`, or `Dario Jose Pulgar-Arriagada`.

## Evidence Strengths

- The staged draft accurately identifies the core conversion problem and keeps canonical readiness on hold.
- The assigned chunk literally contains the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries, ending at `EDUCATION`.
- The conversion-job page Markdown literally contains the competing 1999 PROFONANPE and Television Trust for the Environment entries, plus 1998-1999 Arca Consulting/European Commission, 1997-1998 Klohn Crippen Consultants, and SNC Lavalin Agriculture entries.
- The source packet and conflict draft both preserve the same caution: the CV title/path identify the document subject as `Dario Arturo Pulgar`, but the page body does not independently restate the subject's full name and the physical page is not controlled.
- The draft appropriately separates document-title identity from broader canonical identity attachment.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 3/10 because the underlying source is a potentially useful CV, but the original PDF and page image are unavailable for review. |
| conversion_confidence_score | 2/10 because the chunk and page Markdown disagree materially and the manifest has duplicate page-5 entries. |
| evidence_quantity_score | 4/10 because there are multiple derivative texts, but they are contradictory derivatives rather than independent corroborating sources. |
| agreement_score | 2/10 for physical page-5 control; 8/10 that a page-control conflict exists. |
| identity_confidence_score | 5.5/10 for document-level `Dario Arturo Pulgar` from title/path context only; 2/10 or lower for any same-person merge to Pulgar-Smith or Pulgar-Arriagada candidates. |
| claim_probability | 0.90 that the staged item correctly identifies a page-control conflict; 0.49 that any specific page-5 work-history claim is currently safe to use; 0.10 or lower for relationship claims from this evidence. |
| relevance_level | high |
| relevance_confidence | 0.98 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged identity/conflict analysis is supported as a proof-review hold. Its central claim is not that either occupational sequence is proven, but that the page-5 evidence is unsafe because the derivative page bodies conflict and the controlling source image/PDF is unavailable.

Do not promote occupation, chronology, travel, education-heading, identity-merge, name-variant, or relationship claims from this staged draft. The only high-probability claim is the procedural one: this item needs conversion/source QA before genealogical proof work can continue.

## Next Action

Restore or regenerate authoritative access to the original PDF or rendered physical page 5, reconcile the duplicate chunk manifest and hash drift, and certify which page-5 transcription controls. After that, rerun proof review on the surviving literal claims. Any attachment to `Dario Arturo Pulgar-Smith` or Pulgar-Arriagada candidates should remain a separate identity-bridge review.
