---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527150455528
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210041275.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210041275.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_quality_score: 0.82
conversion_confidence_score: 0.38
evidence_quantity_score: 0.55
agreement_score: 0.42
identity_confidence_score: 0.58
claim_probability: 0.64
relevance_level: high
relevance_confidence: 0.86
canonical_readiness: hold_for_conversion_qa
created: 2026-05-27
---

# Proof Review: Entry 172 Row Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210041275.md`.

## Blockers First

- Canonical readiness remains `hold_for_conversion_qa`. The referenced converted Markdown assigns entry 172 to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, while the referenced chunk, source packet, and visible source image support a different entry 172 row for `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- The conflict is identity-bearing, not a spelling or same-person variation. It changes the child, parents, birth date, birth time, place, residence, and informant.
- The father field is not promotion-ready. The chunk reads `Jose del Carmen Pulgar S.`, but the final mark or suffix still needs targeted QA before any normalization to `Jose del Carmen Pulgar`.
- Relationship claims must not be promoted from this draft. The evidence is promising for a Pulgar/Arriagada child-parent row, but the derivative-file disagreement prevents canonical attachment.
- No Dario-line bridge is present. The reviewed materials do not name Dario, Arturo, Pulgar-Smith, or any relationship that would attach this entry to a Dario candidate.

## Evidence Strengths

- The source is a civil birth register page, a strong source type for birth identity, parent names, and registration details when the row is correctly identified.
- The page image visibly aligns at a high level with the chunk for entry 172: the row numbered 172 on page 58 names a Pulgar/Arriagada child and Pulgar/Arriagada parents, not the Burgos/de la Cruz family found in the converted Markdown.
- The staged identity analysis correctly treats the problem as a row-level conversion or assignment conflict and recommends hold rather than promotion.
- The source packet accurately preserves the key uncertainty: the Pulgar/Arriagada row may be family-relevant, but the current converted Markdown contradicts it and the father field needs certification.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration is a high-quality source type; image legibility is adequate for row-level identification, though not all handwriting is equally clear. |
| conversion_confidence_score | 0.38 | The chunk and image agree at a high level, but the converted file contradicts the row completely. |
| evidence_quantity_score | 0.55 | One relevant page image plus two derivative transcriptions; useful, but not enough to overcome the conflict without QA. |
| agreement_score | 0.42 | Chunk, packet, and image align against the converted Markdown; agreement is partial because the official converted file is materially inconsistent. |
| identity_confidence_score | 0.58 | Moderate confidence that the family-relevant row is Pulgar/Arriagada, but insufficient for canonical identity attachment. |
| claim_probability | 0.64 | The Pulgar/Arriagada reading is more probable than the Burgos/de la Cruz reading for the visible row 172, but the claim remains uncertified. |
| relevance_level | high | High relevance to Pulgar/Arriagada research if QA confirms the row; low relevance to Dario identity bridging. |
| relevance_confidence | 0.86 | The surnames and parent-child structure are directly relevant to Pulgar/Arriagada research. |
| canonical_readiness | hold_for_conversion_qa | Promotion should wait for targeted conversion QA and a follow-up proof review. |

## Claim Probability

The staged draft's central hold conclusion is supported. The most probable explanation is that the derivative files contain a row or conversion-state mismatch, with the visible source image and chunk supporting a Pulgar/Arriagada entry 172 while the converted Markdown reflects a different row set. Probability for using this draft as canonical evidence now is low because a proof review cannot silently replace the converted transcription.

## Next Action

Run targeted conversion QA on `CHUNK-b8f4f0490a36-P0001-01` against the page image, converted Markdown, chunk, and source packet. QA should certify the controlling entry 172 row and explicitly resolve the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting any child identity, birth fact, parent relationship, parent-pair claim, or Dario-line comparison.
