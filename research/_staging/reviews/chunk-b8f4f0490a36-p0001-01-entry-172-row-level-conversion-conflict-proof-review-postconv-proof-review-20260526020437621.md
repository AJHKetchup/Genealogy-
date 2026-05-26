---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526020437621
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
reviewed_conflict: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: "2026-05-26"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Row-control remains unresolved. The referenced converted Markdown records entry 172 as a Burgos/de la Cruz birth row, while the referenced chunk, source packet, conflict note, and page image support entry 172 as a Pulgar/Arriagada birth row.
2. The conflict changes the child, parents, birth date, birth place, informant, and family relevance. No child identity, birth fact, parent-child relationship, or merge decision should be promoted from this staged draft while this conflict remains open.
3. The father field is not fully certified. The visible source and source packet support the beginning `Jose del Carmen Pulgar`; the chunk reads `Jose del Carmen Pulgar S.`, but the trailing mark/suffix should remain unresolved pending targeted conversion QA.
4. The Dario-line comparison is unsupported for promotion. The entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada.
5. Parent-identity jumps are not ready. The staged draft may flag Jose/Juana candidate clusters for later comparison, but this entry does not prove a merge between `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`, or between same-named Jose del Carmen Pulgar candidates.

## Evidence Strengths

- The source is a civil birth-registration page, a strong source type for birth identity and parentage if the controlling row is certified.
- The source packet and chunk agree that entry 172 on page 58 is a Pulgar/Arriagada row naming child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- Local image inspection supports that row 172 on page 58 is visually aligned with the Pulgar/Arriagada reading, not the Burgos/de la Cruz reading in the converted Markdown.
- The staged identity analysis handles the conflict conservatively: it recommends holding canonical use, preserves father-name uncertainty, and rejects Dario attachment from this entry.

## Scored Judgment

| Metric | Score / Level | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a high-quality source for this kind of claim, once row control is settled. |
| conversion_confidence_score | 0.42 | Confidence is materially reduced because the canonical converted Markdown and chunk disagree on the same entry number. |
| evidence_quantity_score | 0.62 | There is one source image plus derived local transcriptions/notes; useful, but not independent corroboration. |
| agreement_score | 0.48 | Chunk, source packet, conflict note, and image review agree with each other, but the converted Markdown is directly contradictory. |
| identity_confidence_score | 0.70 | The Pulgar/Arriagada row identity is probable for the visible row, but not safe for canonical use until conversion QA certifies row control. |
| claim_probability | 0.72 | Probable that the correct entry-172 row is Pulgar/Arriagada; probability is held below high confidence due to the converted-file conflict. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parentage if certified; also relevant as an anti-conflation checkpoint. |
| relevance_confidence | 0.86 | Relevance is clear for the Pulgar/Arriagada family, but no relevance bridge to Dario candidates is proven. |
| canonical_readiness | hold_for_conversion_qa | Not ready for promotion, merge, relationship assertion, or Dario-line comparison. |

## Review Findings

The staged draft is literally supported in its main review posture: it correctly identifies a row-level conversion conflict and recommends holding canonical use. The converted file does record a Burgos/de la Cruz entry 172, while the chunk and source packet record a Pulgar/Arriagada entry 172. The page image supports the existence of a Pulgar/Arriagada row numbered 172 on page 58, so the draft's concern is not speculative.

The staged draft should remain a hold rather than a promotion source. The strongest claim available at this stage is not "entry 172 proves this child and these parents for canonical use"; it is "local conversion artifacts conflict, and targeted conversion QA must decide which row controls entry 172." The draft's Dario and parent-cluster warnings are appropriate as guardrails, but they are not independently proven identity conclusions.

## Next Action

Run targeted conversion QA against the source image, converted Markdown, and chunk to certify the controlling row for entry 172 and the father field to the visible extent only. After QA, rerun proof review before any claim, relationship, person-page merge, parent merge, or Dario-line comparison is promoted.
