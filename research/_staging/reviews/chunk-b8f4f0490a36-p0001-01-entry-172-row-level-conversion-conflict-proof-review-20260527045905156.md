---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527045905156
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030052086.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030052086.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.90
conversion_confidence_score: 0.44
evidence_quantity_score: 0.72
agreement_score: 0.58
identity_confidence_score: 0.76
claim_probability: 0.82
relevance_level: high
relevance_confidence: 0.96
canonical_readiness: hold_for_conversion_qa
canonical_readiness_score: 0.12
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The physical source image, assigned chunk, source packet, and targeted QA note support entry `172` as the Pulgar/Arriagada row, while the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. This is a material row-control conflict, not a minor transcription variant.
- The converted Markdown cannot be used as-is for a promoted entry-172 claim. It appears to describe a different or stale page set from the image and chunk used for this task.
- The father field should remain bounded to `Jose del Carmen Pulgar` for promotion purposes. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the image and QA packet do not certify the terminal mark as part of the name.
- No relationship bridge is proved from this row to any Dario, Dario Arturo, Dario Jose, or later Pulgar-Arriagada identity. The row names `Jose del Carmen Segundo Pulgar Arriagada` as the child and provides parent fields only for this birth registration.
- `Juana Arriagada de Pulgar` should not be merged with `Juana de Dios Amagada de Pulgar` or other Juana variants from this evidence alone.

## Evidence Strengths

- The civil birth-register image is a high-quality source type for the immediate birth, parent-name, registration-date, birth-date, residence, and informant claims.
- The visible row number `172` on page 58 aligns with the Pulgar/Arriagada row. Reading across the row supports child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date/time `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, birth place `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The assigned chunk, source packet, and targeted QA note agree on the main Pulgar/Arriagada identity and conflict-control issue. Their only meaningful internal divergence is the father's terminal mark or suffix.
- The staged identity-analysis draft correctly keeps the Burgos/de la Cruz derivative text separate from the Pulgar/Arriagada row and correctly recommends no canonical promotion while the conversion conflict remains unresolved.

## Scored Judgment

| Metric | Score / Level | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.90 | Original civil registration image directly supports the local event and relationships, subject to handwriting limits. |
| conversion_confidence_score | 0.44 | Mixed derivative state: the chunk matches the image-reviewed row, but the converted file materially conflicts. |
| evidence_quantity_score | 0.72 | One direct source image plus chunk, source packet, and QA note are enough for row-control review, but not for wider identity merges. |
| agreement_score | 0.58 | Strong agreement among image, chunk, packet, and QA for the Pulgar/Arriagada row; severe disagreement with the converted Markdown. |
| identity_confidence_score | 0.76 | Moderate-high for the local row identity; low for any broader same-person or lineage bridge. |
| claim_probability | 0.82 | The claim that physical entry 172 is the Pulgar/Arriagada birth registration is probable. |
| relevance_level | high | Highly relevant to Pulgar/Arriagada research and high risk if attached to the wrong canonical persons. |
| relevance_confidence | 0.96 | Direct name and family relevance is clear. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until conversion-control reconciles or supersedes the conflicting converted Markdown. |

## Claim Review

- Supported with hold: physical row `172` on page 58 is the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. Probability: 0.82.
- Revise boundary: father should be carried only as `Jose del Carmen Pulgar` unless a focused review certifies the terminal `S.` or another suffix. Probability for certified suffix from current evidence: 0.30.
- Reject for this source: entry `172` in the physical image is `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. That reading is present in the converted file but is not supported by the source image assigned to this task. Probability for this image/row: 0.05.
- Hold/reject broader identity jumps: no claim tying this row to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada is supported by this row alone. Probability: 0.06.

## Next Action

Send this item back to conversion-control with a hold recommendation. The converted Markdown should be reconciled against the source image and assigned chunk before any claim, relationship, parent merge, or canonical wiki update is promoted. A separate focused review should resolve the father-field terminal mark if that suffix is needed.
