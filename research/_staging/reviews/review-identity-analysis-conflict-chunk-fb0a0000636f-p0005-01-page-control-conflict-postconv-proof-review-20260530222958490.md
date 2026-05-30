---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530222913205
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md
review_status: hold
canonical_readiness: not_ready
---

# Proof Review: Page-Control Conflict For CHUNK-fb0a0000636f-P0005-01

## Blockers

- Page-control conflict is confirmed. The assigned chunk and source packet support 1979-1970 work-history entries, while the referenced conversion job page Markdown for page 5 supports 1999/1998 entries.
- The authoritative rendered page image was unavailable at the manifest path `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg`; the file does not currently exist at that path.
- The chunk manifest lists duplicate `CHUNK-fb0a0000636f-P0005-01` records with different character counts and hashes, so the page-level chunk identity is unstable.
- The page body in the competing derivative transcriptions does not repeat `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or any Pulgar-Arriagada/Jose/Juana family candidate.
- This page contains no birth, death, parent, spouse, child, sibling, household, or other kinship evidence. It cannot resolve identity merges or relationship conflicts.
- No occupational, identity, or relationship claim from this staged draft is ready for canonical promotion until conversion QA determines which page-5 transcription controls.

## Evidence Scores

| category | score |
|---|---:|
| source_quality_score | 0.62 |
| conversion_confidence_score | 0.28 |
| evidence_quantity_score | 0.44 |
| agreement_score | 0.22 |
| identity_confidence_score | 0.48 |
| claim_probability | 0.34 |
| relevance_level | high |
| relevance_confidence | 0.94 |
| canonical_readiness | not_ready |

Scoring rationale: the cited source is a named CV packet and both derivative transcriptions are internally legible, but page control is unresolved. Evidence quantity is moderate for work-history text and weak for page-local identity or genealogy. Agreement is low because the derivative files materially disagree about page 5. Identity confidence is limited to document-level attribution from the CV title and job context, not page-local proof.

## Evidence Strengths

- The staged draft correctly treats the issue as a conversion/provenance conflict, not as a resolved genealogical conflict.
- The assigned chunk and source packet agree on the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- The conversion job page Markdown and job manifest agree that page 5 is associated with the 1999/1998 professional entries.
- The aggregate converted file contains both the 1999/1998 sequence and the later 1979-1970 sequence in the broader converted-file context, supporting the staged draft's concern that the derivative outputs are inconsistent.
- The staged draft appropriately keeps `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, Pulgar-Arriagada candidates, and Jose/Juana parent candidates separate or unresolved because this page provides no family bridge.

## Literal Support Check

Reviewed verification context:

- `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md`
- `research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md`
- `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`
- `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`
- `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`
- `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/manifest.json`
- `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json`

Literal support is split. The 1979-1970 work-history sequence is present in the assigned chunk and source packet. The 1999/1998 sequence is present in the conversion job page Markdown for page 5. The missing page image prevents direct verification against the authoritative rendered page during this review.

## Claim And Identity Risk

- Claim risk: high for occupational chronology claims because a wrong page-control decision could attach the wrong work-history entries to page 5.
- Identity risk: high for canonical attachment if the CV subject is linked to `Dario Arturo Pulgar-Smith` or Pulgar-Arriagada candidates by name overlap alone.
- Relationship risk: low as direct relationship evidence because no relationship is stated, but high if used indirectly to merge or separate Pulgar-line people.
- Conversion confidence: low until page image restoration and chunk/page Markdown reconciliation are complete.
- Canonical readiness: `not_ready`.

## Next Action

Hold for conversion QA/source-prep control review. Restore or locate the authoritative page-5 image, reconcile the duplicate chunk-manifest records, and determine whether the 1999/1998 page Markdown or the 1979-1970 assigned chunk controls page 5. Rerun proof review after page control is certified. Do not promote this staged draft to `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or any canonical folder.
