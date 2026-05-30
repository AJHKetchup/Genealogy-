---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530221930633
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md
review_status: hold
canonical_readiness: not_ready
created: 2026-05-30
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers

- Page-control blocker: the staged draft is supported in identifying a material derivative conflict. The referenced chunk and source packet for page 5 contain 1979-1970 work-history entries, while the conversion job page Markdown for page 5 contains 1999/1998 work-history entries.
- Authority blocker: the job manifest names `page-images/page-0005.jpg`, but that file is not present at the referenced path in this workspace. I did not resolve the conflict against a visible page image.
- Conversion blocker: the chunk manifest lists duplicate `CHUNK-fb0a0000636f-P0005-01` records with different char counts and hashes, so the chunk provenance is unstable.
- Literal-support blocker: the page-5 body, in either derivative transcription, does not repeat `Dario Arturo Pulgar` or provide page-local identifying facts such as birth, death, parent, spouse, child, household, or other kinship evidence.
- Identity blocker: this staged draft cannot prove that document-level `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada candidate.
- Relationship blocker: no relationship claim is supported by the reviewed page-5 evidence.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md`.
- Source packet: `research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md`.
- Referenced chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`.
- Aggregate converted file: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`.
- Conversion job page Markdown: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`.
- Conversion job manifest and chunk manifest for the referenced page and chunk.

No external research was performed. No raw source, converted Markdown, chunk, packet, or canonical page was edited.

## Evidence Strengths

- The staged draft accurately identifies a genuine conversion/provenance conflict rather than treating the competing work-history entries as reconciled facts.
- The source packet explicitly warns that conversion confidence is blocked and recommends holding promotion pending conversion QA.
- The chunk and source packet agree internally on the 1979-1970 text; the conversion job page Markdown and manifest agree internally on page 5 as the page-Markdown control path.
- The staged draft correctly separates document-level subject attribution from page-local identity proof.

## Scoring

| factor | score | rationale |
|---|---:|---|
| source_quality_score | 0.62 | A CV is a useful authored biographical/professional source, but this review only reached derivative files and a missing declared page image, not a visible controlling page. |
| conversion_confidence_score | 0.25 | Severe page-control conflict, duplicate chunk-manifest records, and missing referenced page image prevent reliance on either page-5 derivative transcription. |
| evidence_quantity_score | 0.45 | Multiple local derivatives were available, but they conflict on the central page text and provide no independent page-local identity or relationship facts. |
| agreement_score | 0.30 | The packet and chunk agree with each other, but they disagree materially with the page Markdown and aggregate converted-file context. |
| identity_confidence_score | 0.55 | Document title and job metadata point to `Dario Arturo Pulgar`; the reviewed page body itself is unnamed. |
| claim_probability | 0.35 | The safest claim is only that a page-control conflict exists. Specific occupational claims from page 5 are not yet probable enough for use. |
| relevance_level | high | The conflict directly controls whether this staged draft can support any page-5 work-history claim. |
| relevance_confidence | 0.95 | All reviewed files are the staged draft's referenced evidence chain for the assigned chunk and page. |
| canonical_readiness | not_ready | Hold for conversion QA before any canonical claim, relationship, identity attachment, or merge decision. |

## Claim-Level Judgment

- Page-control conflict claim: supported. The reviewed derivatives materially disagree about the page-5 transcription.
- 1979-1970 work-history claims: hold. The chunk and packet support the text internally, but page control is unresolved.
- 1999/1998 work-history claims: hold. The page Markdown supports the text internally, but it conflicts with the assigned chunk and packet.
- Document-level subject attribution to `Dario Arturo Pulgar`: plausible but limited. It is supported by source/job title context, not by page-local body text.
- Same-person claim with `Dario Arturo Pulgar-Smith`: not supported by this staged page. Requires a separate identity-bridge review after conversion QA.
- Relationship claims involving Jose/Juana or Pulgar-line candidates: unsupported. The reviewed evidence contains no kinship facts.

## Next Action

Hold this staged draft for conversion QA. The next action is to restore or locate the authoritative page-5 image or inspect the source page through the controlled conversion-QA workflow, then decide whether the 1999/1998 page Markdown or the 1979-1970 chunk/source-packet text controls page 5. After that, rerun proof review before promoting any occupational claim or identity attachment.
