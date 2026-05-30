---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530225216120
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_conversion_job_page: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
source_quality_score: 0.35
conversion_confidence_score: 0.15
evidence_quantity_score: 0.40
agreement_score: 0.10
identity_confidence_score: 0.45
claim_probability: 0.30
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Page-Control Conflict for CHUNK-fb0a0000636f-P0005-01

This review covers staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md`.

## Blockers First

1. Page control is unresolved. The assigned chunk reads page 5 as the `1979 - 1982` HABITAT through `1970 - 1972` CITELCO work-history page, while the conversion job page markdown for page 5 reads the page as `1999` PROFONANPE/TVE and `1998 - 1999` Arca/Klohn/SNC Lavalin work-history text.
2. The source packet reports hash drift between the chunk-recorded converted SHA-256 and the observed converted SHA-256.
3. The chunk manifest contains duplicate entries for `CHUNK-fb0a0000636f-P0005-01` with different character counts and hashes, so the chunk manifest cannot be treated as clean page-control evidence.
4. `raw/sources/CV of Dario Arturo Pulgar.pdf` is not present in this checkout, and `page-images/page-0005.jpg` is also absent. I could not verify the physical source page or image.
5. The page-local text in both competing derivative readings does not name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, parents, spouse, children, or other kinship. Identity remains document-level/contextual, not page-local.

## Evidence Strengths

- The source packet and metadata consistently identify the document title/source as `CV of Dario Arturo Pulgar`.
- The assigned chunk and aggregate converted file contain coherent CV work-history text for HABITAT, National Film Board of Canada, Chile Films, and CITELCO.
- The conversion job page markdown contains coherent CV work-history text for PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The staged draft accurately preserves the conversion/page-control conflict and recommends hold rather than canonical promotion.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.35 | The underlying source is a named CV, but the PDF/page image is unavailable for direct review. |
| conversion_confidence_score | 0.15 | Competing derivative transcripts, hash drift, duplicate manifest entries, and missing page image make conversion control very weak. |
| evidence_quantity_score | 0.40 | There is enough derivative text to identify the nature of the dispute, but not enough controlled evidence to resolve it. |
| agreement_score | 0.10 | The assigned chunk and conversion job page markdown materially disagree about page 5. |
| identity_confidence_score | 0.45 | Document-level metadata supports `Dario Arturo Pulgar`; page-local identity evidence is absent. |
| claim_probability | 0.30 | The claim that this draft is not ready and must be held is strongly supported, but any substantive work-history or identity claim from page 5 remains low-probability until page control is repaired. |
| relevance_level | high | The source title and Pulgar identity context make this relevant to the family research workspace. |
| relevance_confidence | 0.85 | Relevance is high even though promotion is blocked. |
| canonical_readiness | not_ready | No canonical claim, relationship, merge, or identity bridge should be promoted from this page-control state. |

## Identity And Relationship Risk

- Same-person risk: moderate. `Dario Arturo Pulgar` may relate to canonical `Dario Arturo Pulgar-Smith`, but this page does not provide the `Smith` name form or a family bridge.
- Conflation risk: high if this is merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, or Jose/Juana parent-candidate clusters.
- Relationship jumps: unsupported. No relationship claim appears in the reviewed page-local text.
- Conflict handling: the staged draft properly treats this as a derivative transcription/page-control conflict rather than a resolved identity fact.

## Next Action

Hold for conversion QA. Restore or confirm the source PDF or `page-0005.jpg`, reconcile the duplicate manifest entries and hash drift, then decide which derivative text controls physical page 5. After page control is certified, run a separate identity-bridge review before attaching the accepted CV subject to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana cluster.

No raw sources, converted Markdown, chunks, source packets, staged drafts, or canonical wiki pages were edited.
