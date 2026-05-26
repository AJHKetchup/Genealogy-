---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526090851423
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045206977.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045206977.md
reviewed_sources:
  - research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.86
conversion_confidence_score: 0.50
evidence_quantity_score: 0.62
agreement_score: 0.58
identity_confidence_score: 0.64
claim_probability: 0.70
relevance_level: high
relevance_confidence: 0.92
canonical_readiness: hold_for_conversion_qa
created: 2026-05-26
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown reads the same entry number as a Burgos/de la Cruz birth row.
- The conflict is material, not a spelling or normalization issue. It changes child identity, sex wording, birth date and time, birth place, father, mother, informant, and downstream relationship candidates.
- The current converted Markdown cannot be used as-is for canonical promotion because it disagrees with the chunk derived from it and with the visible source image at the row level.
- The father field remains a transcription-certification issue. Preserve uncertainty among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies the visible reading.
- No Dario-line identity, merge, bridge, or relationship claim is supported by this entry. The reviewed evidence does not name Dario, Arturo, Smith, or any independent bridge to a Dario Pulgar identity.

## Evidence Strengths

- The source is a contemporaneous civil birth register image, so source quality is high for a birth identity and parent-name claim if the row is correctly transcribed.
- The assigned chunk and source packet agree that entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888 at 3 p.m. at Calle de Valdivia, with father read as `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Visual review of the cited source image supports the Pulgar/Arriagada row more than the Burgos/de la Cruz reading in the current converted Markdown. This review does not replace conversion QA, but it raises the probability that the chunk/source-packet row is the controlling row.
- The identity analysis correctly treats existing wiki stubs as derivative context rather than independent proof.

## Scored Judgment

| Measure | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Direct civil-registration image, contemporaneous with the event, but handwriting and row alignment require care. |
| conversion_confidence_score | 0.50 | The visible image and chunk favor Pulgar/Arriagada, but repository derivatives still conflict. |
| evidence_quantity_score | 0.62 | One direct source image plus derivative transcriptions; no independent corroborating record reviewed. |
| agreement_score | 0.58 | Chunk, source packet, and image broadly agree; converted Markdown disagrees completely for entry 172. |
| identity_confidence_score | 0.64 | Plausible identity for `Jose del Carmen Segundo Pulgar Arriagada` if the chunk row controls, but not ready while conversion conflict remains. |
| claim_probability | 0.70 | Pulgar/Arriagada reading is more probable than the Burgos/de la Cruz reading after visual check, but still blocked by derivative conflict. |
| relevance_level | high | The Pulgar/Arriagada row is directly relevant to Pulgar/Arriagada family research if confirmed. |
| relevance_confidence | 0.92 | Names and relationships in the chunk/source packet are highly relevant; relevance depends on QA confirming row control. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until targeted conversion QA resolves the row and father-field reading. |

## Claim-Level Review

| Claim | Probability | Review Status | Notes |
| --- | ---: | --- | --- |
| Entry 172 is the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | hold | Supported by chunk, source packet, and visual image review; blocked by conflicting converted Markdown. |
| Father is `Jose del Carmen Pulgar S.`. | 0.58 | hold | The father field appears consistent with a Pulgar reading, but the final suffix/mark needs targeted certification. |
| Mother is `Juana Arriagada de Pulgar`. | 0.68 | hold | Supported by chunk/source packet and visually plausible in the image, but dependent on row-control QA. |
| Entry 172 supports a Burgos/de la Cruz child `Jose Miguel`. | 0.18 | revise/hold | Only the current converted Markdown supports this; the cited chunk and visible source image do not appear to support it for entry 172. |
| Entry 172 supports a Dario Pulgar identity bridge. | 0.02 | reject_for_now | No Dario-related name or bridging context appears in the reviewed evidence. |

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, and current chunk. QA should decide the controlling entry 172 row and certify the father-field reading without silently normalizing it. After QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent candidate, or Dario-line comparison.
