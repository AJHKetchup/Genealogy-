---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530215911008
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530210637213.md
review_status: hold
canonical_readiness: not_ready
claim_probability: 0.20
source_quality_score: 0.55
conversion_confidence_score: 0.20
evidence_quantity_score: 0.45
agreement_score: 0.25
identity_confidence_score: 0.50
relevance_level: high
relevance_confidence: 0.95
---

# Proof Review: Page-Control Conflict, CHUNK-fb0a0000636f-P0005-01

## Blockers

- Source-visibility blocker: the referenced source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is not present in this workspace, and the manifest-referenced page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is also absent. I could not inspect the visible source page.
- Page-control blocker: the assigned chunk and source packet transcribe page 5 as 1979-1982, 1974-1978, 1972-1973, and 1970-1972 work-history entries, while the conversion-job page Markdown for page 5 transcribes 1999, 1998-1999, and 1997-1998 entries. These cannot both be the controlling transcription for the same page.
- Derivative-chain blocker: the chunk manifest lists duplicate `CHUNK-fb0a0000636f-P0005-01` records with different character counts and SHA-256 hashes, so the chunk identity is unstable.
- Claim-support blocker: no occupational claim from either derivative text stream is promotion-ready until source-prep/conversion QA identifies the controlling page-5 transcription.
- Identity blocker: the page-level derivative text reviewed here does not independently name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, a Pulgar-Arriagada candidate, or Jose/Juana parent candidates. Subject attribution rests on document-level title/context only.
- Relationship blocker: the reviewed materials contain no birth, death, parent, spouse, child, sibling, household, or other kinship statement. They cannot resolve Pulgar-line relationship or same-person conflicts.

## Scores

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.55 | A CV can be useful for occupational chronology, but the source PDF and page image were unavailable for direct visual verification. |
| conversion_confidence_score | 0.20 | The local derivative outputs materially disagree, the page image is missing, and the chunk manifest has duplicate page-5 entries. |
| evidence_quantity_score | 0.45 | Multiple referenced derivatives were available, but they are conflicting derivative artifacts rather than independent corroboration. |
| agreement_score | 0.25 | The chunk and source packet agree with each other, but they disagree with `page-markdown/page-0005.md` and with the unstable manifest chain. |
| identity_confidence_score | 0.50 | Document title/context points to Dario Arturo Pulgar, but the page body does not independently identify him or bridge him to a canonical person. |
| claim_probability | 0.20 | Low probability that any page-5 occupational or identity claim is ready for promotion before page-control QA. |
| relevance_level | high | The staged draft directly addresses the assigned page-control conflict. |
| relevance_confidence | 0.95 | The reviewed files are the staged draft and its immediate referenced evidence chain. |
| canonical_readiness | not_ready | Hold; do not promote, merge, attach, or use for canonical relationship resolution. |

## Evidence Strengths

- The staged draft's central conclusion is supported: this is a conversion/provenance conflict, not a resolved genealogical or occupational fact.
- The assigned chunk and source packet consistently support the 1979-1970 work-history sequence, including HABITAT, National Film Board of Canada, Chile Films, and CITELCO.
- The conversion-job page Markdown consistently supports a different 1999/1998 page-5 sequence, including PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The conversion manifest maps page 5 to `page-markdown/page-0005.md`, while the chunk manifest documents duplicate page-5 chunk entries. This explains why the derivative chain is not safe for claim promotion.

## Review Judgment

The staged draft should remain on hold. Its blockers and `canonical_readiness: not_ready` judgment are supported by the reviewed local evidence.

I found no literal support for choosing the 1999/1998 derivative text over the 1979-1970 derivative text, or vice versa. I also found no page-local support for attaching this evidence to canonical `Dario Arturo Pulgar-Smith`, merging any Pulgar-line candidates, or resolving Jose/Juana relationship conflicts.

## Next Action

Hold for source-prep/conversion QA. Restore or re-render the authoritative source page/page-5 image, compare it against both derivative transcriptions, repair the duplicated/stale chunk manifest state through the conversion workflow, and rerun proof review before any claim promotion or canonical attachment.
