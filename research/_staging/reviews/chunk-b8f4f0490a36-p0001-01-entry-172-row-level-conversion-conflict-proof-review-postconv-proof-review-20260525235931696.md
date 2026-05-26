---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525235931696
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
reviewed_sources:
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
created: 2026-05-25
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. **Converted-file conflict:** the staged draft's blocker is real. The assigned chunk/source packet and source image read entry 172 as a Pulgar/Arriagada birth-registration row, while the referenced converted Markdown reads entry 172 as a Burgos/de la Cruz row. These are not compatible variants of one identity.
2. **Canonical-readiness blocker:** no child identity, birth fact, parent-child relationship, parent identity merge, or Dario-related bridge should be promoted from this draft until the conversion-control conflict is resolved in the conversion layer.
3. **Father-field blocker:** the source image and chunk support the base father reading `Jose del Carmen Pulgar`; the final mark or suffix after `Pulgar` is not strong enough for me to certify as a settled canonical form beyond the staged uncertainty already stated.
4. **Identity-risk blocker:** the entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario. Any direct Dario attachment from this entry would be an unsupported relationship jump.

## Evidence Scores

- source_quality_score: 0.86
- conversion_confidence_score: 0.38
- evidence_quantity_score: 0.72
- agreement_score: 0.42
- identity_confidence_score: 0.68 for the Pulgar/Arriagada row as the visible entry-172 row; 0.05 for any Dario identity attachment
- claim_probability: 0.78 that entry 172 on the visible page is the Pulgar/Arriagada row; 0.35 that the exact father form includes a meaningful suffix after `Pulgar`; 0.05 for a direct Dario bridge
- relevance_level: high for Pulgar/Arriagada family reconstruction; low for direct Dario proof
- relevance_confidence: 0.84 for Pulgar/Arriagada relevance; 0.20 for Dario relevance
- canonical_readiness: hold

## Evidence Strengths

- The source packet and assigned chunk consistently transcribe entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The page image visibly supports the chunk/source-packet row placement: entry 172 is on page 58 beneath entry 171, and the child, parent, mother, and informant fields align with the Pulgar/Arriagada reading rather than the Burgos/de la Cruz converted-file reading.
- The conflict candidate accurately characterizes the mismatch as row-level conversion conflict rather than a same-person or name-variant problem.
- The staged identity analysis correctly keeps Dario hypotheses separate and recommends no Dario attachment from this entry.

## Weaknesses And Risk

- The referenced converted Markdown remains materially inconsistent with the assigned chunk and image for entry 172, so downstream claim promotion would be premature even though the image favors the chunk.
- The father suffix or terminal mark after `Jose del Carmen Pulgar` remains uncertain. The proof should not force `S.` into a canonical name unless targeted conversion QA certifies that visible reading.
- Relationship conclusions are vulnerable to a row-control correction workflow. If the converted Markdown is not corrected or superseded, claim consumers could attach facts to the wrong entry family.

## Judgment

The staged draft is supported as a conflict analysis and should remain at `hold_for_conversion_qa`. The Pulgar/Arriagada row has meaningful visual and chunk support, but the conversion conflict prevents canonical readiness. The draft's caution against merging Jose/Juana candidates or attaching this entry to any Dario identity is well supported.

## Next Action

Run targeted conversion QA for this exact source image, chunk, and converted Markdown. QA should decide the controlling entry-172 row and record the father field only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that correction or certification exists, rerun proof review for any child birth facts, parent-child relationships, or Pulgar/Arriagada identity merges.
