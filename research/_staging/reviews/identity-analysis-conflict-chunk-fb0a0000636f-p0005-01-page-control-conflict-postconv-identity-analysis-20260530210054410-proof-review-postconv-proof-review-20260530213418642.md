---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210054410.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210054410.md
reviewer: postconv-proof-review-20260530213418642
review_date: 2026-05-30
canonical_readiness: hold
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers

- Page-control conflict confirmed: the referenced chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` transcribes 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries, while the referenced conversion job page Markdown `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` transcribes 1999, 1998-1999, and 1997-1998 entries.
- Page image unavailable at the manifest path `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg`, so I could not visually adjudicate which transcript controls page 5.
- Chunk manifest instability confirmed: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json` lists `CHUNK-fb0a0000636f-P0005-01` twice with different character counts and SHA-256 values.
- The page text reviewed does not itself name `Dario Arturo Pulgar` or prove identity with canonical `Dario Arturo Pulgar-Smith`; attribution remains document-level from the CV title and local metadata.
- The reviewed evidence contains no kinship statement. It does not support parent, spouse, child, sibling, grandparent, merge, or relationship-conflict claims.

## Scores

- source_quality_score: 0.58
- conversion_confidence_score: 0.25
- evidence_quantity_score: 0.42
- agreement_score: 0.18
- identity_confidence_score: 0.55
- claim_probability: 0.30
- relevance_level: high
- relevance_confidence: 0.92
- canonical_readiness: hold

## Evidence Strengths

- The staged draft accurately identifies the controlling problem as a derivative transcription/page-control conflict rather than a genealogical conclusion.
- The source packet `research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md` correctly flags conversion confidence as blocked and recommends holding for conversion QA.
- The chunk and source packet agree with each other on the 1979-1970 work-history sequence, so that transcript is internally coherent as a candidate.
- The conversion job manifest and page Markdown agree that page 5 should have a page Markdown file at `page-markdown/page-0005.md`, and that file is internally coherent as a competing candidate.
- The aggregate converted file contains both the 1999/1998 material and the 1979-1970 material, supporting the staged concern that derivative outputs need reconciliation before any claim is promoted.

## Review Judgment

The staged identity/conflict analysis is supported as a hold recommendation. No page-5 occupational claim should be promoted from this draft until source-prep or conversion QA determines whether page 5 is controlled by the 1999/1998 conversion job page Markdown, the 1979-1970 chunk text, or a repaired derivative output.

The document-level CV title provides some support that the broader source concerns Dario Arturo Pulgar, but this page-control review does not establish that the CV subject is the same person as canonical `Dario Arturo Pulgar-Smith`. It also gives no basis to merge Pulgar-line candidates or resolve Jose/Juana relationship clusters.

## Next Action

Hold for conversion QA. Restore or re-render the authoritative page 5 image, reconcile `page-markdown/page-0005.md`, the aggregate converted file, and the duplicate chunk manifest entries, then rerun proof review on any surviving page-5 claims. Keep this draft out of canonical claims, relationships, and wiki pages until that reconciliation is complete.
