---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527114244875
task_id: proof-review:research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md
staged_draft: research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md
reviewed: 2026-05-27
canonical_readiness: blocked
---

# Proof Review: CHUNK-fb0a0000636f-P0004-01 Page Identity And Manifest QA

## Blockers First

1. The staged identity/conflict analysis is supported as a hold note, but it is not ready for canonical promotion. The referenced page image and the current converted file's page-4 section show 2000 and 1999-2000 work-history entries, while the referenced chunk and source packet show 1988-1989, 1988, 1986-1987, and 1982-1985 entries.
2. The chunk manifest lists `CHUNK-fb0a0000636f-P0004-01` twice with the same page path and page number but different `chars` and `sha256` values. This makes the chunk identity unreliable until source-prep or conversion QA reconciles the manifest.
3. The staged source packet's 1982-1989 occupational claims should not be promoted as page-4 claims. They are supported by the current chunk file, but not by the rendered page-4 image or the page-4 section at the top of the current converted Markdown.
4. Page 4 does not visibly name `Dario Arturo Pulgar`. Subject attribution for this page remains document-level from the source title and conversion metadata, not page-local proof.
5. No reviewed page-4 evidence supports a family relationship, same-person merge, parent/child claim, or bridge to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, Jose, Juana, or any other Pulgar-line candidate.

## Evidence Reviewed

- Staged draft reviewed: `research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md`.
- Staged source packet: `research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md`.
- Referenced chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md`.
- Current converted Markdown: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`.
- Chunk manifest: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json`.
- Rendered page image checked for verification only: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg`.

## Scored Judgment

- `source_quality_score`: 0.66
- `conversion_confidence_score`: 0.34
- `evidence_quantity_score`: 0.58
- `agreement_score`: 0.36
- `identity_confidence_score`: 0.62 for document-level CV subject attribution; 0.20 for page-local identity proof; 0.05 for any same-person or relationship bridge to canonical Pulgar-line people.
- `claim_probability`: 0.90 that the staged draft correctly identifies a page-control/manifest conflict; 0.18 that the source-packet 1982-1989 entries are safely promotable as page-4 claims in the current state.
- `relevance_level`: high
- `relevance_confidence`: 0.96
- `canonical_readiness`: blocked

## Evidence Strengths

The staged draft's central blocker is well supported. The rendered page image visibly aligns with the current converted file's page-4 text: continuation material, `2000` / International Bank for Reconstruction and Development / Bolivia, Peru / Senior Consultant, and `1999 - 2000` / Antamina Mining Company / Huarmey, Peru / Head Community Relations.

The referenced chunk and source packet are internally consistent with each other for the older occupational entries: FAO in Ndola, Zambia in 1988-1989; CIDA in Ethiopia in 1988; Worldview International Foundation in Rome in 1986-1987; and independent communications consultant work for CIDA in 1982-1985. This supports treating the problem as a page-control or manifest integrity conflict, not as a simple transcription typo.

The staged draft properly recommends a hold and does not promote relationship claims. Its caution about relying on the CV title for subject identity is appropriate because the reviewed page body does not repeat the name.

## Review Judgment

This proof review affirms the staged draft's hold-level conclusion. The strongest supported claim is procedural: `CHUNK-fb0a0000636f-P0004-01` has conflicting page-control evidence across the page image/current converted page, the chunk file/source packet, and the manifest.

The occupational text in the chunk may belong elsewhere in the CV sequence, but that cannot be certified from this review without source-prep reconciliation. The page-4 image controls against promotion of the 1982-1989 claims as current page-4 claims.

No canonical fact, relationship, merge, or identity bridge should be created from this staged draft. The draft is useful as a QA hold note only.

## Next Action

Run targeted source-prep/conversion QA for `CHUNK-fb0a0000636f-P0004-01`. The QA step should reconcile the duplicate manifest entries, decide which page number controls the 1982-1989 text, and regenerate affected source packets or staged claims through the proper workflow. After that, rerun proof review before any canonical claim, relationship, merge, or wiki update.
