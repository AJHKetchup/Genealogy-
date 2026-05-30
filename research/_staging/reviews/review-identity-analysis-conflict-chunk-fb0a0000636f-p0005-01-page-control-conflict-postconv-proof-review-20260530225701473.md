---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530225701473
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This review covers staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md`.

## Blockers First

1. Page control is not resolved. The assigned chunk and aggregate converted file contain the 1979-1982 HABITAT through 1970-1972 CITELCO work-history sequence, while `page-markdown/page-0005.md` contains a different 1999/1998 PROFONANPE, TVE, Arca, Klohn Crippen, and SNC Lavalin sequence.
2. The source image and original PDF were not available in this checkout. `page-images/page-0005.jpg` was absent, and `raw/sources/CV of Dario Arturo Pulgar.pdf` was absent, so I could not make a visual page-control determination.
3. Provenance is unstable. The source packet records converted SHA-256 drift from `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0` to `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`.
4. The chunk manifest has duplicate `CHUNK-fb0a0000636f-P0005-01` entries pointing to the same chunk path but with different character counts and hashes.
5. Page-local identity support is weak. The page body does not repeat `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or any family relationship.
6. No canonical claim, identity merge, relationship, or work-history promotion is ready from this draft.

## Evidence Strengths

- The document-level converted file title and source packet identify the source as `CV of Dario Arturo Pulgar`.
- Both competing derivative texts are plausible CV work-history text for the same document set.
- The assigned chunk is internally coherent and supports narrow work-history statements only if later QA proves it is the controlling page 5 transcription.
- The source packet correctly flags the conversion/page-control problem and recommends a hold.

## Scored Judgment

| Dimension | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.42 | A CV can be useful for work-history claims, but the original PDF is missing locally and review was limited to derivative files. |
| conversion_confidence_score | 0.18 | Two derivative page-5 texts disagree, page image/PDF are unavailable, and manifest/hash metadata conflict. |
| evidence_quantity_score | 0.35 | There is enough derivative text to identify the dispute, but not enough verified source control to prove the page claim. |
| agreement_score | 0.20 | The assigned chunk agrees with part of the aggregate converted file but conflicts with the conversion job page Markdown and manifest metadata. |
| identity_confidence_score | 0.45 | Document-level attribution to Dario Arturo Pulgar is plausible from title/context, but page-local identity and canonical-identity bridging are absent. |
| claim_probability | 0.30 | The broad claim that this is disputed CV evidence is well supported; any specific page-5 work-history claim remains low probability until page control is fixed. |
| relevance_level | high | A CV for Dario Arturo Pulgar is highly relevant to identity and biographical work-history review. |
| relevance_confidence | 0.85 | Relevance is clear from the source title and source packet even though page control is blocked. |
| canonical_readiness | not_ready | Hold for conversion QA; no promotion or merge should occur. |

## Claim Review

The staged draft's main recommendation, `hold_for_conversion_qa`, is supported. The derivative evidence proves a real page-control/provenance conflict, not a promotable biographical fact.

The draft's narrow document-level statement that the source is a CV of `Dario Arturo Pulgar` is supported by the derivative source title and packet metadata, but not independently verified against the missing PDF. Treat that as provisional document context.

The draft's caution against merging `Dario Arturo Pulgar` with `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or parent/kinship candidates is appropriate. The reviewed page text contains no page-local full-name variant, parent, spouse, child, grandchild, or other relationship statement.

## Next Action

Hold. Restore or regenerate the page image or source PDF, reconcile the duplicate manifest entries and converted-file hash drift, and determine which transcription controls physical page 5. After that, run a separate identity-bridge review before using this CV page for canonical person identity, relationships, or work-history promotion.

No raw sources, converted Markdown, chunks, source packets, staged drafts, canonical claims, relationships, or wiki pages were edited.
