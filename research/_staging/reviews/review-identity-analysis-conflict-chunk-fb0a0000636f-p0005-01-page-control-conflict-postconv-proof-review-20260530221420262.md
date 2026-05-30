---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530221420262
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md
review_status: hold
canonical_readiness: not_ready
---

# Proof Review: Page-Control Conflict For CHUNK-fb0a0000636f-P0005-01

## Blockers

- Page-control conflict is confirmed. The assigned chunk and source packet support 1979-1970 work-history entries, while the referenced conversion job page Markdown for page 5 supports 1999/1998 entries.
- The referenced job manifest points to `page-images/page-0005.jpg`, but the `page-images` directory is absent under the conversion job folder checked during review. The authoritative rendered page image was therefore unavailable from the referenced path.
- The chunk manifest lists duplicate `CHUNK-fb0a0000636f-P0005-01` entries with different character counts and hashes, so the chunk identity is not stable enough for canonical use.
- Page 5 body text, in either competing derivative transcription, does not itself name Dario Arturo Pulgar or provide a parent, spouse, child, sibling, household, birth, death, or other kinship bridge.
- No occupational, identity, or relationship claim from this staged draft should be promoted until conversion QA determines which page-5 transcription controls.

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

Scoring rationale: the source is a named CV packet with internally legible derivative text, but the controlling page transcription is unresolved. Evidence quantity is moderate for work-history content and weak for identity or genealogy. Agreement is low because the page-level derivatives disagree materially. Identity confidence is limited to document-level attribution, not page-local proof.

## Evidence Strengths

- The staged draft accurately identifies the conflict as a conversion/provenance problem rather than a genealogical relationship conflict.
- The assigned chunk and source packet agree with each other on the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- The conversion job page Markdown and job manifest agree with each other that page 5 is associated with the 1999/1998 professional entries.
- The staged draft correctly maintains uncertainty around canonical attachment to `Dario Arturo Pulgar-Smith` because page-local identity and relationship bridges are absent.

## Literal Support Check

Reviewed allowed referenced files:

- `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md`
- `research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md`
- `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`
- `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`
- `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`
- `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/manifest.json`
- `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json`

The 1979-1970 work-history sequence is literally present in the assigned chunk and source packet. The 1999/1998 sequence is literally present in the conversion job page Markdown for page 5. The aggregate converted file contains both sequences in the same broader converted-file context, which supports the staged draft's concern but does not resolve page control.

## Identity And Relationship Risk

- Identity risk: high if the CV page is attached to a canonical person by name/title alone.
- Relationship risk: low for this page as a direct relationship source, because no family relationship is stated.
- Claim risk: high for occupational claims until page-control QA resolves which transcription belongs to page 5.
- Conflict type: derivative transcription/page-control conflict, not a resolved identity or family-relationship conflict.

## Next Action

Hold. Send to conversion QA/source-prep control review to restore or locate the authoritative page-5 image, reconcile the duplicate chunk-manifest records, and determine whether the 1999/1998 page Markdown or the 1979-1970 chunk text controls page 5. Rerun proof review after page control is certified. Do not promote this staged draft to `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or any canonical folder.
