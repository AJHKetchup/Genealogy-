---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525171238466
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525123546801.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525123546801.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.84
conversion_confidence_score: 0.43
evidence_quantity_score: 0.52
agreement_score: 0.54
identity_confidence_score: 0.68
claim_probability: 0.72
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: hold_for_conversion_qa
next_action: targeted_conversion_qa_then_rerun_proof_review
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The visible source image and current chunk support entry 172 as a Pulgar/Arriagada birth row, but the assigned converted Markdown records a materially different row for entry 172.
2. The staged identity analysis and source packet summarize the converted-file conflict with stale details. The converted file currently reviewed records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, birth on `veinte de Febrero` at `En Pellin`; it does not currently say `Emilia de la Cruz`, `veinte i seis de Marzo`, or `En esta`.
3. The father field for the Pulgar row remains unresolved for canonical wording. The chunk reads `Jose del Carmen Pulgar S.`, while the source image supports `Jose del Carmen Pulgar` with a final mark or suffix that should remain open pending targeted QA.
4. The staged draft's Dario-line comparison is useful as an anti-conflation warning only. Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, or a later-life bridge, so it cannot support any Dario identity merge or relationship.
5. Existing canonical or staged downstream Pulgar/Juana material is dependent context, not independent corroboration for this review. No canonical promotion, merge, or relationship attachment should be made from this proof note.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.84 | The source is a civil birth-register image, a strong direct source type for a birth row and parent names; legibility is usable, with father-suffix uncertainty. |
| conversion_confidence_score | 0.43 | The chunk aligns with the visible image for the Pulgar/Arriagada row, but the assigned converted Markdown gives a different entry-172 row. |
| evidence_quantity_score | 0.52 | Review used one source image plus the staged draft, conflict draft, source packet, chunk, and converted file; no independent corroborating source was in scope. |
| agreement_score | 0.54 | Image, chunk, and source packet broadly agree on the Pulgar row, while the converted file disagrees and the staged draft misstates some current converted-file details. |
| identity_confidence_score | 0.68 | The probable source-visible entry-172 subject is `Jose del Carmen Segundo Pulgar Arriagada`, but confidence is capped by derivative conflict and father-field uncertainty. |
| claim_probability | 0.72 | The Pulgar/Arriagada row is more probable from the visible source and chunk than the converted-file row, but not ready for canonical use. |
| relevance_level | high | If QA-certified, the entry directly concerns Pulgar/Arriagada child and parent evidence. |
| relevance_confidence | 0.90 | Relevance to Pulgar/Arriagada research is clear; relevance to Dario-line identity claims is only contextual and cautionary. |
| canonical_readiness | hold_for_conversion_qa | Hold all dependent claims, relationships, merges, and identity bridges until conversion QA resolves the row and father field. |

## Evidence Strengths

- The visible source image for register page 58, entry 172 shows a Pulgar/Arriagada row consistent with the chunk: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at Calle de Valdivia.
- The chunk provides a coherent row with father read as `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, parent residence `Calle de Colipi`, and informant `Ernesto Herrera L.`.
- The conflict draft and source packet correctly identify the issue as a row-level conversion or assignment conflict rather than a spelling variant.
- The staged identity analysis correctly recommends holding canonical action and rejecting Dario-line bridge claims from surname overlap alone.

## Review Findings

- Literal support for the child identity is probable from the image and chunk as `Jose del Carmen Segundo Pulgar Arriagada`, but held because the converted Markdown assigns entry 172 to `Jose Francisco`.
- Literal support for the mother claim is probable as `Juana Arriagada de Pulgar`, but should not be used to merge Juana candidates while the row-level conflict remains open.
- Literal support for the father claim is weaker than the child and mother claims because the terminal mark or suffix after `Pulgar` is not settled.
- The staged draft's converted-file summary should be refreshed before reuse. The active converted file's conflicting row is `Jose Francisco` / `Oswaldo Gomez` / `Rosario de la Cruz de la Maza`, not the exact row described in the staged draft.
- There is no source support here for a Dario, Dario Jose, Dario Arturo, Pulgar-Smith, or Alexander John Heinz identity or relationship bridge.

## Next Action

Send the source image, chunk, source packet, conflict draft, staged identity analysis, and converted Markdown to targeted conversion QA for entry 172. QA should decide the controlling entry-172 row, refresh the converted-file conflict description to match the file currently on disk, and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth facts, father claim, mother claim, parent-child relationship, same-person hypothesis, or Pulgar/Dario-line comparison.
