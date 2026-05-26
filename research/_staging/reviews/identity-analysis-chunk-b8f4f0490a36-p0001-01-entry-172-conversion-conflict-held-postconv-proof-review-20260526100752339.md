---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526100752339
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md
reviewed_sources:
  - research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.84
conversion_confidence_score: 0.36
evidence_quantity_score: 0.68
agreement_score: 0.42
identity_confidence_score: 0.66
claim_probability: 0.58
relevance_level: high
relevance_confidence: 0.92
canonical_readiness: hold
created: 2026-05-26
---

# Proof Review: Entry 172 Conversion Conflict

## Blockers First

- Canonical readiness is `hold`. The staged identity analysis correctly identifies an unresolved row-control conflict: the current converted Markdown gives entry `172` as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the current chunk, source packet, conflict note, and visible page image support a different entry `172` for `Jose del Carmen Segundo Pulgar Arriagada`.
- This is not a spelling variation or identity merge question. The competing readings change the child, parents, birth date/time, birth place, informant, residence details, and downstream relationships.
- The father field in the Pulgar row remains partly uncertain. The image and chunk support `Jose del Carmen Pulgar` followed by a possible terminal `S.` or mark, but this proof review should not normalize that field to a canonical person.
- No Dario-line bridge is supported here. The reviewed evidence does not name Dario, Arturo, Smith, a spouse, descendants, adult chronology, or any identity-continuity facts.

## Scores

| Dimension | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.84 | Civil birth register image is a strong source type for birth and parent-name evidence, but the row is small and handwriting remains visually constrained. |
| conversion_confidence_score | 0.36 | The chunk and converted Markdown disagree on the literal row for the same entry number; targeted conversion QA is required. |
| evidence_quantity_score | 0.68 | One primary register image plus derivative chunk, source packet, conflict note, and converted file were reviewed, but all evidence concerns one source image. |
| agreement_score | 0.42 | Chunk, packet, conflict note, and image align on the Pulgar row; converted Markdown directly conflicts. |
| identity_confidence_score | 0.66 | The Pulgar child/parent reading is plausible from the image and chunk, but row-control and father-field uncertainty prevent stronger identity confidence. |
| claim_probability | 0.58 | More likely than not that the staged conflict is real and that the Pulgar row is visible for entry 172, but the derivative conflict keeps the claim below promotion level. |
| relevance_level | high | Pulgar and Arriagada are family-relevant names in the assigned packet. |
| relevance_confidence | 0.92 | The relevance is direct if the Pulgar row controls; relevance drops only if conversion QA rejects that row. |
| canonical_readiness | hold | Do not promote identity, birth, parent-child relationship, parent identity, or Dario-line claims from this staged draft. |

## Evidence Strengths

- The reviewed page image visibly places entry `172` on page `58` with the Pulgar/Arriagada row described by the chunk: child `Jose del Carmen Segundo Pulgar Arriagada`, birth on `Ocho de Marzo de mil ochocientos ochenta i ocho`, father beginning `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet accurately preserves the key uncertainty: the father field appears to contain `Jose del Carmen Pulgar` with an uncertified ending, possibly `S.`.
- The staged identity analysis does not over-promote the evidence. Its hold recommendation is supported by the literal conflict between the converted Markdown and the chunk/image.

## Review Judgment

The staged draft is supported as a conflict analysis, not as a ready canonical identity claim. The strongest supported claim is that entry `172` has a material derivative-transcription conflict requiring conversion QA. A conditional Pulgar/Arriagada birth claim is plausible, but it is not ready for canonical promotion while the assigned converted Markdown still records the same entry number as a Burgos/de la Cruz birth.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. Targeted QA should compare the page image, converted Markdown, chunk, and source packet; decide the controlling transcription for entry `172`; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting any identity, birth fact, parent-child relationship, parent merge, or Dario-line bridge.
