---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260527120509086
task_id: proof-review:research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md
staged_draft: research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md
review_status: hold
canonical_readiness: not_ready
source_quality_score: 0.62
conversion_confidence_score: 0.30
evidence_quantity_score: 0.42
agreement_score: 0.28
identity_confidence_score: 0.46
claim_probability: 0.20
relevance_level: high
relevance_confidence: 0.95
---

# Proof Review: CHUNK-fb0a0000636f-P0004-01 Identity And Manifest QA

## Blockers

- Page-control blocker: the rendered page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg` visibly supports the current converted page-4 text for `2000 / International Bank for Reconstruction and Development (IBRD)` and `1999 - 2000 / Antamina Mining Company`, not the referenced chunk/source-packet text for 1988-1989, 1988, 1986-1987, and 1982-1985.
- Manifest blocker: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json` lists `CHUNK-fb0a0000636f-P0004-01` twice for the same page, path, and part, with different character counts and manifest hashes.
- File-integrity blocker: the current SHA-256 of `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md` is `c8536868c8f59d4340eb31173302f11866a5475823353b2409109b0574980f15`, which does not match either duplicate manifest hash for this chunk path.
- Claim-control blocker: the staged analysis correctly treats the 1982-1989 employment claims as not promotion-ready from page 4 because the page image and the first page-4 section of the converted file support different text.
- Identity blocker: page 4 itself does not name Dario Arturo Pulgar. The subject attribution is document-level from the source title and conversion metadata, not page-local identity proof.
- Relationship/merge blocker: the reviewed evidence does not bridge `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, Jose del Carmen Pulgar, any Juana candidate, or any parent/child/spouse relationship.

## Evidence Strengths

- The staged draft's core hold conclusion is supported. The visible page image agrees with the first converted page-4 section and conflicts with the referenced chunk/source packet.
- The referenced chunk and source packet are internally readable and consistently preserve the 1982-1989 entries, so the issue is not transcription legibility inside that derivative chunk; it is page-control and manifest integrity.
- The source title and converted file title consistently identify the document as a CV of Dario Arturo Pulgar, supporting a moderate document-level subject hypothesis.
- The staged draft appropriately avoids a canonical merge or relationship jump and keeps the result as identity/conflict hold analysis.

## Scored Judgment

| field | score | judgment |
|---|---:|---|
| source_quality_score | 0.62 | A CV can directly support career claims, but this review only reached a contested page/chunk control state. |
| conversion_confidence_score | 0.30 | Text is legible, but duplicate chunk identity, mismatched hashes, and page-image disagreement make conversion/page control unreliable. |
| evidence_quantity_score | 0.42 | There is enough local evidence to support a hold decision, not enough to promote the staged employment or identity-bridge claims. |
| agreement_score | 0.28 | Page image and current converted page-4 text agree with each other; chunk/source packet disagree with them under the same chunk id. |
| identity_confidence_score | 0.46 | Document-level attribution to Dario Arturo Pulgar is plausible, but page-local naming and canonical bridge evidence are absent. |
| claim_probability | 0.20 | Low for the staged 1982-1989 claims as page-4 claims until source-prep QA reconciles the physical page and chunk records. |
| relevance_level | high | The evidence directly controls whether this staged draft can proceed. |
| relevance_confidence | 0.95 | The reviewed files are exactly the staged draft's cited control files. |
| canonical_readiness | not_ready | Do not promote to canonical claims, relationships, or wiki pages. |

## Review Notes

- Literal support for the 1982-1989 employment text exists in the current referenced chunk file and source packet.
- Literal support for that same text as page 4 is not reliable because the visible page-4 image shows the 2000/1999-2000 work-history entries instead.
- The staged draft's stronger claims about not merging Pulgar-line candidates are appropriate as a cautionary hold, but they should remain non-canonical because this page does not provide family or identity-bridge data.
- No external research was performed, and no raw sources, converted Markdown, chunks, source packets, claims, relationships, or canonical wiki files were edited.

## Next Action

Hold for targeted source-prep/conversion QA. Reconcile the duplicate `CHUNK-fb0a0000636f-P0004-01` manifest entries, determine which physical page contains the 1982-1989 CV entries, regenerate any affected source packets or staged claims through the source-prep workflow, and rerun proof review before any canonical promotion or identity merge.
