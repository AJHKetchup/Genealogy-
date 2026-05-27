---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md
worker: postconv-proof-review-20260527115129079
staged_draft: research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md
review_status: hold
canonical_readiness: not_ready
promotion_recommendation: do_not_promote
---

# Proof Review: Page Identity And Manifest QA

## Blockers

- Page-control blocker: the existing page image for page 4 shows the 2000 IBRD and 1999-2000 Antamina entries, not the 1988-1989, 1988, 1986-1987, and 1982-1985 entries preserved in the referenced chunk and source packet.
- Manifest blocker: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json` lists `CHUNK-fb0a0000636f-P0004-01` twice with the same page, part, and path but different `chars` and `sha256` values.
- Current chunk hash blocker: the current `page-0004-chunk-01.md` file hashes to `C8536868C8F59D4340EB31173302F11866A5475823353B2409109B0574980F15`, which matches neither manifest hash for the duplicate page-4 entries.
- Claim-support blocker: employment claims for the 1982-1989 roles may be real CV text, but they are not proven as page-4 claims while the rendered page-4 image supports different content.
- Identity blocker: the page body does not name Dario Arturo Pulgar. Subject attribution comes from the source title/document-level context only.
- Relationship blocker: the reviewed evidence contains no parent, spouse, child, grandparent, or other kinship relationship. It cannot bridge the CV subject to any canonical Pulgar-line person.

## Evidence Strengths

- The source is a local curriculum vitae titled `CV of Dario Arturo Pulgar`, so document-level subject attribution to Dario Arturo Pulgar is plausible.
- The page image is clear typed text and directly supports the current converted page-4 section with 2000 IBRD and 1999-2000 Antamina entries.
- The referenced chunk and source packet are internally readable and consistently preserve 1982-1989 employment entries.
- The staged identity analysis correctly treats the issue as a conversion/page-control hold rather than a genealogical conflict ready for promotion.

## Scored Judgment

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.72 | A CV is a useful authored career source, but this review has only page-level derivative and image context, not independent corroboration. |
| conversion_confidence_score | 0.30 | Text is legible, but page/chunk control is unreliable because image, converted file sectioning, chunk file, and manifest metadata disagree. |
| evidence_quantity_score | 0.45 | Several local control files were available, but all material is from one source packet/conversion family. |
| agreement_score | 0.25 | Page image agrees with the first converted page-4 section, while referenced chunk/source packet and duplicate manifest state disagree. |
| identity_confidence_score | 0.55 | The source title supports Dario Arturo Pulgar as document subject, but the page body does not name him and no canonical bridge is present. |
| claim_probability | 0.20 | Low for promoting the 1982-1989 entries as page-4 claims; the visible page 4 supports different entries. |
| relevance_level | 0.95 | Directly relevant to whether this staged conflict and associated employment claims can proceed. |
| relevance_confidence | 0.95 | The reviewed files are the exact staged draft references and local control files. |
| canonical_readiness | 0.05 | Not ready for canonical claims, relationships, or identity merge/attachment. |

## Review Finding

Hold the staged draft. The draft's core conclusion is supported: this is a page identity and manifest-control problem, not a promotion-ready biographical claim. The 1982-1989 employment text should not be rejected as impossible, because it appears in the referenced chunk/source packet and later in the converted file body. However, it should not be promoted from `CHUNK-fb0a0000636f-P0004-01` as page-4 evidence because the rendered page-4 image visibly supports the 2000/1999-2000 material instead.

No relationship claim is supported. No same-person claim connecting `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith` or other Pulgar-line candidates is supported by this page.

## Next Action

Run targeted source-prep/conversion QA to reconcile `CHUNK-fb0a0000636f-P0004-01`, the duplicate manifest entries, the current chunk hash, and the physical page image. After page-control is corrected, regenerate or refresh affected source packets/staged claims through the normal workflow and rerun proof review. Do not promote this staged draft to canonical folders.
