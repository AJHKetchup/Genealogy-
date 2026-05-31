---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531071056597
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531050245268.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531050245268.md
reviewed_at: 2026-05-31
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
source_quality_score: 0.25
conversion_confidence_score: 0.15
evidence_quantity_score: 0.25
agreement_score: 0.10
identity_confidence_score: 0.25
claim_probability: 0.25
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers First

1. The staged draft is correctly blocked by unresolved page control. The referenced conversion-job `page-0005.md` supports a 1999-1997 consulting-work page, while the assigned chunk `page-0005-chunk-01.md` supports a different 1979-1970 work-history page ending at `EDUCATION`.
2. The source PDF at `raw/sources/CV of Dario Arturo Pulgar.pdf` is not present locally, so the review cannot verify either derivative text against the original PDF.
3. The manifest-referenced rendered image `page-images/page-0005.jpg` is also not present locally, despite being listed in the conversion-job manifest. No visible page image was available for source-level verification.
4. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` for the same chunk path with conflicting recorded character counts and SHA-256 values. The current observed converted-file hash is `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`, not the chunk manifest's recorded converted hash `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`. The current observed chunk hash is `D6EA4F611EE03000C11CBBA63246E95B55F8A421FCBC87D0D667E91F5C8D0B8D`, matching neither page-5 manifest row.
5. The page body reviewed does not literally name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar`. Identity attachment depends only on document title/path continuity and is not enough for canonical identity or relationship work.
6. No same-person merge, name normalization, family relationship, or chronology claim is ready for canonical promotion from this staged draft.

## Evidence Strengths

- The staged draft accurately preserves the main conversion conflict instead of selecting a reading unsupported by the available local source controls.
- The conversion-job page Markdown literally supports the draft's description of the 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen/SNC Lavalin Agriculture text.
- The assigned chunk literally supports the draft's description of the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO text.
- The aggregate converted file contains both derivative readings in the same converted document, which supports the draft's warning that page sequencing/control is unreliable.
- The document title and conversion metadata support relevance to a CV titled for `Dario Arturo Pulgar`, but that is document-context evidence, not page-body identity proof.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.25 | The source is potentially strong as a CV, but the original PDF and page image are unavailable locally for this review. |
| conversion_confidence_score | 0.15 | Two derivative page-5 readings conflict, and manifest/hash controls are inconsistent. |
| evidence_quantity_score | 0.25 | There is enough derivative text to identify the conflict, but not enough source-controlled evidence to choose a reading or attach identity claims. |
| agreement_score | 0.10 | Converted page Markdown, chunk text, aggregate converted file, and manifest controls disagree materially. |
| identity_confidence_score | 0.25 | Document title/path points toward `Dario Arturo Pulgar`, but the page body lacks an identity-bearing name. |
| claim_probability | 0.25 | The claim that this page belongs to the CV subject is plausible but unproven until page control is repaired. |
| relevance_level | high | The draft concerns a named CV and potential Dario/Pulgar identity conflicts. |
| relevance_confidence | 0.85 | The conflict is directly relevant to preventing premature canonical identity attachment. |
| canonical_readiness | blocked | Conversion QA and identity-bridge review are required before promotion. |

## Claim And Identity Review

The draft's hold recommendation is supported. Page-5 work-history claims should not be promoted because the available local artifacts do not establish which physical page controls the page-5 transcription.

The draft appropriately treats `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, and `Darío/Dario Pulgar Arriagada` as separate identity hypotheses rather than as proven variants or duplicates. The reviewed page evidence supplies no parent, spouse, child, grandchild, or other kinship relationship claim.

## Next Action

Keep this staged identity analysis on `hold_for_conversion_qa`. Restore or regenerate the authoritative source PDF/page-0005 image, reconcile the duplicate chunk manifest/hash drift, certify the controlling page-5 transcription, then rerun proof review before any canonical claim, relationship, identity bridge, merge, or wiki update.
