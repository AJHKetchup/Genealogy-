---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526135422631
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md
reviewed: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- **Canonical readiness:** `hold_for_conversion_qa`. Do not promote any child identity, birth event, parent-child relationship, parent merge, or Dario-line bridge from this staged draft.
- The staged draft correctly identifies a material conflict between derivative artifacts: the converted Markdown gives entry `172` as a Burgos/de la Cruz birth of `José Miguel`, while the chunk and held source packet give entry `172` as a Pulgar/Arriagada birth of `Jose del Carmen Segundo Pulgar Arriagada`.
- The conflict is larger than a single name field. The two readings disagree on child name, sex label, birth date and time, birth place, father, mother, informant, page officer/signature context, and surrounding entries.
- The source image visually supports the Pulgar/Arriagada row for entry `172` at a broad level, but this review is not a conversion-correction task and does not authorize editing the converted Markdown or canonical pages.
- The father field remains uncertified. Preserve the alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA resolves the handwriting.
- No reviewed evidence in this task supports linking this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.

## Evidence Checked

- Staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md`.
- Conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md`.
- Held source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| Claim / Issue | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| A row-control/conversion conflict exists for entry `172`. | 0.88 | 0.32 | 0.82 | 0.18 | 0.82 | 0.94 | high | 0.96 | hold_for_conversion_qa |
| Entry `172` is the Pulgar/Arriagada birth of `Jose del Carmen Segundo Pulgar Arriagada`. | 0.88 | 0.48 | 0.70 | 0.62 | 0.76 | 0.78 | high | 0.90 | hold_for_conversion_qa |
| Entry `172` is the Burgos/de la Cruz birth of `José Miguel`. | 0.88 | 0.18 | 0.35 | 0.12 | 0.22 | 0.12 | low | 0.75 | hold/revise_after_qa |
| `Jose del Carmen Pulgar S.` is the father as written in the entry. | 0.88 | 0.45 | 0.58 | 0.55 | 0.60 | 0.62 | high | 0.84 | hold_for_father_field_qa |
| `Juana Arriagada de Pulgar` is the mother if the Pulgar row controls. | 0.88 | 0.50 | 0.64 | 0.62 | 0.74 | 0.76 | high | 0.88 | hold_for_conversion_qa |
| This record supports a Dario-line bridge or same-person claim. | 0.88 | 0.45 | 0.12 | 0.05 | 0.03 | 0.02 | low | 0.92 | not_ready |

## Evidence Strengths

- The civil birth register image is a high-quality source type for birth identity and parent-child evidence when the row is correctly controlled.
- The chunk, held source packet, and visible source image agree at the broad row level for entry `172`: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar...`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and Calle de Valdivia/Calle de Colipi context.
- The staged identity-analysis draft appropriately treats the conflict as a hold condition and avoids promoting a canonical identity or relationship.
- The draft correctly rejects Dario-line attachment from this evidence because no Dario/Arturo/Smith bridge appears in the reviewed materials.

## Review Notes

- Literal support is present for a Pulgar/Arriagada reading in the chunk and in the visible source image, but the canonical workflow is blocked because the current converted Markdown does not match that reading.
- The converted Markdown appears to represent a different set of rows than the chunk/source image for entries `171` through `176`; this increases the likelihood of a stale or mismatched conversion artifact rather than a mere transcription variant.
- Source reliability is high, but derivative reliability is mixed. The source image and chunk are stronger for this review than the converted Markdown, yet the conflict must be resolved by conversion QA before promotion.
- Claim confidence should remain below promotion threshold until QA certifies the controlling row and the father-field reading.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. Targeted conversion QA should compare the source image, converted Markdown, chunk, and held source packet for `CHUNK-b8f4f0490a36-P0001-01`; certify whether entry `172` is the Pulgar/Arriagada row; and resolve the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical promotion.
