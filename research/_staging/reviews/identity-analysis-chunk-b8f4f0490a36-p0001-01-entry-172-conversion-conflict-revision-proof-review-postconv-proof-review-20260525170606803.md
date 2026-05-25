---
type: proof_review
status: revise
role: claim_reviewer
worker: postconv-proof-review-20260525170606803
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.82
conversion_confidence_score: 0.38
evidence_quantity_score: 0.62
agreement_score: 0.46
identity_confidence_score: 0.63
claim_probability: 0.63
relevance_level: high
relevance_confidence: 0.92
---

# Proof Review: Entry 172 Identity/Conflict Analysis

## Blockers First

1. The staged draft correctly identifies a row-level conflict and should not be promoted, but it inaccurately summarizes the referenced converted Markdown in several fields. The converted file reviewed here records entry 172 as `José Francisco`, born `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En Pellin`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, and informant `Oswaldo Gomez`; it does not match the staged draft's converted-file summary of a 26 March birth at `En esta` with mother `Emilia de la Cruz`.
2. The current chunk and source packet support entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, but the converted Markdown describes a different child-parent cluster for the same entry number. This remains a conversion or assignment conflict, not a resolved identity claim.
3. The father field for the Pulgar/Arriagada row remains transcription-sensitive. The chunk reads `Jose del Carmen Pulgar S.`, and the source image is consistent with a Pulgar father, but targeted QA is still needed before treating the suffix or final character as certified.
4. No Dario-line attachment is supported by the reviewed entry. The staged draft is correct to block attachment to Dario candidates by surname pattern or Pulgar-line context alone.

## Evidence Strengths

- The reviewed source image visibly supports the broad row identity in the chunk for entry 172: a child named `Jose del Carmen Segundo Pulgar Arriagada`, father in the `Jose del Carmen Pulgar...` form, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The chunk and source packet are internally coherent for the Pulgar/Arriagada reading, including registration date, birth date/time, birth place, parents, residence, and informant.
- The staged identity analysis keeps the key uncertainty in bounds: it treats the matter as `hold_for_conversion_qa`, resists canonical promotion, and separates the Pulgar/Arriagada row from Dario identity hypotheses.
- Civil birth registration is a strong source class for child, parent, date, and place claims once the controlling row is certified.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration image is a strong primary-source class, but handwriting and row assignment require careful QA. |
| conversion_confidence_score | 0.38 | The chunk/source packet and converted Markdown disagree on the entire entry-172 family cluster. |
| evidence_quantity_score | 0.62 | There is enough local evidence to identify the conflict and favor the Pulgar/Arriagada row at broad level, but not enough to promote canonical claims. |
| agreement_score | 0.46 | Source image, chunk, and source packet broadly agree with each other; the referenced converted file materially conflicts. |
| identity_confidence_score | 0.63 | Pulgar/Arriagada row identity is probable from the image/chunk, capped by the conversion conflict and father-field uncertainty. |
| claim_probability | 0.63 | The review supports the staged draft's main probability posture for a held Pulgar/Arriagada hypothesis, but the converted-file details need revision. |
| relevance_level | high | The evidence is directly relevant to Pulgar/Arriagada parent-child candidates and anti-conflation work. |
| relevance_confidence | 0.92 | Relevance is high if the Pulgar/Arriagada row is certified; relevance to Dario candidates remains unsupported. |
| canonical_readiness | hold_for_conversion_qa | No fact, relationship, same-person merge, or Dario bridge is ready for canonical promotion. |

## Review Decision

Revise the staged analysis before any downstream reliance. The conclusion and caution level are sound, but the converted-file comparison must be corrected to the literal converted file reviewed here. Keep all dependent claims at `hold_for_conversion_qa`.

## Next Action

Run targeted conversion QA against the source image, current chunk, and referenced converted Markdown. QA should certify whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz-de-la-Maza row and should record the father field exactly as visible. After QA, rerun proof review on the certified child identity, birth facts, parent identities, and parent-child relationships before any canonical promotion.
