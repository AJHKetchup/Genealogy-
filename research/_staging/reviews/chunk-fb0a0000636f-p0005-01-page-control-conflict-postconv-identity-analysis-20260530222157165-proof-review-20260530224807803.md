---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530224721385
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
reviewed_claim_type: identity_conflict_analysis
canonical_readiness: not_ready
---

# Proof Review: Page-Control Conflict, CV of Dario Arturo Pulgar

This review covers only staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md` and its referenced verification files.

## Blockers First

1. Page control remains unresolved. The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` transcribes the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO work-history entries.
2. The conversion job page Markdown `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` instead transcribes 1999/1998 entries for PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen, and SNC Lavalin Agriculture.
3. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` and the source packet reports recorded converted SHA-256 `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0` versus observed converted SHA-256 `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`.
4. The referenced page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is absent, and the referenced source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent. I could not visually verify the controlling physical page.
5. The reviewed page body does not independently name Dario Arturo Pulgar, Pulgar-Smith, Pulgar-Arriagada, Jose, Juana, Alexander John Heinz, or any kinship relationship. Identity attribution is document-level only.

## Evidence Scores

| Measure | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.35 | CV source identity is plausible from title/path and source packet, but the original PDF is unavailable for direct inspection. |
| conversion_confidence_score | 0.15 | Two derivative page-5 transcriptions conflict, page image is missing, and hash/manifest control is unstable. |
| evidence_quantity_score | 0.30 | There is enough derivative text to identify the conflict, but not enough controlled evidence to promote any page-5 claim. |
| agreement_score | 0.10 | Assigned chunk and conversion job page Markdown materially disagree about page content. |
| identity_confidence_score | 0.45 | Document-level title supports Dario Arturo Pulgar as a working subject, but page-local identity support is absent. |
| claim_probability | 0.20 | The draft's hold/conflict conclusion is well supported; any positive identity/work-history claim from page 5 is low probability until page control is repaired. |
| relevance_level | high | A CV for Dario Arturo Pulgar is relevant to identity/work-history analysis, if controlled. |
| relevance_confidence | 0.85 | Relevance follows from source title and staged packet, despite unresolved page control. |
| canonical_readiness | not_ready | No canonical person, relationship, or work-history promotion should be made from this page-control state. |

## Evidence Strengths

- The staged draft accurately identifies the controlling problem: the chunk and conversion job page Markdown cannot both be the authoritative transcription for physical page 5.
- The source packet preserves the provenance problems instead of smoothing them over: hash drift, duplicate manifest entries, absent page image, and document-level-only identity attribution are all disclosed.
- The draft correctly avoids merging `Dario Arturo Pulgar` with `Dario Arturo Pulgar-Smith`, `Dario Pulgar Arriagada`, or Jose/Juana parent candidates on name overlap alone.
- The draft correctly treats relationship claims as unsupported because no reviewed page-5 text states parents, spouse, child, grandchild, household, or kinship.

## Review Judgment

The staged draft should remain a hold-for-conversion-QA identity/conflict analysis. Its negative/control conclusions are supported by the referenced derivative files and packet. Positive claims about the work history on page 5, the controlling physical page text, or a same-person bridge to any canonical Dario/Pulgar page are not ready.

Canonical readiness is `not_ready`.

## Next Action

Restore or confirm access to the source PDF or `page-0005.jpg`, reconcile the chunk manifest duplicates and converted-file hash drift, and select the controlling page-5 transcription. After that, run a separate proof review for any work-history claim and a separate identity-bridge review before connecting the CV subject to canonical `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana candidate.

No raw sources, converted Markdown, chunks, source packets, staged drafts, canonical wiki pages, claim files, or relationship files were edited.
