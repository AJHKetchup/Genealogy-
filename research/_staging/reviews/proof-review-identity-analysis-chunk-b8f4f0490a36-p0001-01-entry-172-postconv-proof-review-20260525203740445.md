---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525203740445
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
reviewed:
  - research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525171911545.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525171911545.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.82
conversion_confidence_score: 0.32
evidence_quantity_score: 0.46
agreement_score: 0.28
identity_confidence_score: 0.56
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.78
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Proof Review: Entry 172 Identity Analysis

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The chunk/source packet and the source image support a Pulgar/Arriagada birth-registration reading for entry 172, but the assigned converted Markdown contains a different entry-172 transcription. This is a row-level or conversion-file conflict, not a normal name variation.
- The staged identity-analysis draft repeats an older or conflicting summary of the converted Markdown as `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born in `Pellin`. The current converted file reviewed here instead reads entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, place `En esta`. The exact opposing converted-row details therefore need QA correction before promotion.
- The father field in the Pulgar/Arriagada row is not proof-ready as a normalized identity. The chunk reads `Jose del Carmen Pulgar S.` and the page image appears consistent with a Pulgar father field, but the suffix after `Pulgar` remains too uncertain for canonical normalization from this review alone.
- No Dario-line identity bridge is supported. The reviewed source layers do not name Dario, Arturo, Smith, Dario Jose, or any later-life Dario context.
- Parent-child and same-person conclusions are blocked. `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar S.`, and `Juana Arriagada de Pulgar` may be the relevant row if the chunk/image reading is certified, but the converted-file conflict prevents canonical promotion now.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a direct contemporary source, but this review used only targeted visual checking of the cited page. |
| conversion_confidence_score | 0.32 | The derivative transcriptions disagree materially on the child, parents, birth date, place, and informant for entry 172. |
| evidence_quantity_score | 0.46 | There is one direct register image plus derivative chunk/source-packet evidence, but no independent corroborating source for identity bridging. |
| agreement_score | 0.28 | Chunk, source packet, and visible image lean Pulgar/Arriagada; converted Markdown disagrees and the staged draft misstates the current converted-file details. |
| identity_confidence_score | 0.56 | Confidence that entry 172 is the Pulgar/Arriagada row is moderate, but confidence in any canonical person merge or parent-child promotion remains low. |
| claim_probability | 0.62 | The Pulgar/Arriagada claim is more probable than the converted Markdown reading after image comparison, but not promotion-ready because the conversion conflict is unresolved. |
| relevance_level | high | If certified, the Pulgar/Arriagada row is family-relevant and directly names Pulgar/Arriagada candidates. |
| relevance_confidence | 0.78 | Relevance is strong for Pulgar/Arriagada research, but weak for Dario-line bridging without additional evidence. |
| canonical_readiness | hold_for_conversion_qa | Requires targeted conversion QA and a rerun proof review. |

## Evidence Strengths

- The chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered `Siete de Abril de mil ochocientos ochenta i ocho`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`.
- The chunk/source packet agree on the mother as `Juana Arriagada de Pulgar` and the informant as `Ernesto Herrera L.`, age `Veintiseis años`, profession `Empleado`, domicile `Calle de Valdivia`.
- The source image visibly shows entry 172 on page 58 with a Pulgar/Arriagada-looking child and parent row, so the chunk reading has real visual support. This supports hold-and-QA rather than rejection.
- The staged identity-analysis draft correctly treats the conflict as non-promotable and correctly rejects same-person or duplicate-person treatment between the Pulgar/Arriagada row and the unrelated converted-row reading.

## Claim Judgment

The best current hypothesis is that entry 172 is probably the Pulgar/Arriagada registration represented by the chunk, not the row represented in the current converted Markdown. However, proof review cannot convert that probability into canonical facts while the assigned converted file remains inconsistent and the father-name ending is unresolved.

This draft should not support a canonical claim for child identity, birth event, parents, or Dario-line relationship. It can support only a staged QA note that asks whether entry 172 should be certified as the Pulgar/Arriagada row and how the father field should be represented.

## Next Action

Run targeted conversion QA against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, the assigned converted Markdown, and `CHUNK-b8f4f0490a36-P0001-01`. QA should reconcile why the converted file currently carries a different entry-172 row and should certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical promotion.
