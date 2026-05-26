---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526140317844
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md
reviewed:
  - research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md
  - research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.88
conversion_confidence_score: 0.38
evidence_quantity_score: 0.62
agreement_score: 0.42
identity_confidence_score: 0.64
claim_probability: 0.72
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: 0.10
created: 2026-05-26
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- Canonical promotion is blocked by a material row-control conflict. The same source image and entry number are represented by two incompatible derivative transcriptions: the current converted Markdown gives a Burgos/de la Cruz entry, while the current chunk, held source packet, and staged conflict draft give a Pulgar/Arriagada entry.
- The conflict changes the child identity, sex wording, birth date and time, birth place, father, mother, informant, and relationship candidates. This is not a spelling-only or accent-only problem.
- The father field in the Pulgar/Arriagada reading is not fully certified. Preserve the alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA resolves the reading.
- No Dario-line identity bridge is supported by this staged draft or by the reviewed source materials. The evidence reviewed here does not name Dario, Dario Arturo, Dario Jose, Smith, Alexander John Heinz, or any explicit downstream relationship bridge.
- Existing wiki pages were not used as proof in this review. The staged draft correctly treats them as context only because Entry 172-derived wiki claims cannot bootstrap this contested row.

## Evidence Strengths

- Source quality is strong: the underlying source is a contemporaneous civil birth register image for Los Angeles, Chile, dated 1888.
- The source image, inspected only for verification context, appears broadly consistent with the chunk's row-level Pulgar/Arriagada reading for entry 172. This supports the staged draft's conclusion that the converted Markdown may be stale or row-mismatched.
- The current chunk and held source packet agree on the Pulgar/Arriagada reading: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on `Ocho de Marzo de mil ochocientos ochenta i ocho`, and informant `Ernesto Herrera L.`
- The current converted Markdown explicitly disagrees, reading entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and birth on `El seis de Abril de mil ochocientos ochenta i ocho`.
- The staged identity analysis is appropriately conservative: it identifies the conflict, avoids promotion, preserves father-field uncertainty, and rejects unsupported Dario-line attachment.

## Scored Judgment

| Measure | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration image is a high-quality source type for birth identity and parentage, though the review did not perform full transcription QA. |
| conversion_confidence_score | 0.38 | Current derivative transcriptions disagree materially for the same entry number and source. |
| evidence_quantity_score | 0.62 | Multiple local artifacts were reviewed, but they are derivative of one source image and one row-control issue. |
| agreement_score | 0.42 | Chunk, source packet, and image context align broadly, but the converted Markdown directly conflicts. |
| identity_confidence_score | 0.64 | Pulgar/Arriagada identity is plausible if the chunk controls, but not ready for canonical identity work while row control remains unresolved. |
| claim_probability | 0.72 | The staged draft's claim that this is a conversion-row conflict and should remain on hold is well supported. |
| relevance_level | high | If confirmed, the Pulgar/Arriagada row is directly relevant to Pulgar/Arriagada family identity and parent-child claims. |
| relevance_confidence | 0.90 | The Pulgar and Arriagada names are explicit in the chunk/source-packet reading. |
| canonical_readiness | 0.10 | The claim should not be promoted until targeted conversion QA certifies the controlling row and father-field text. |

## Claim-Level Assessment

| Claim | Review Judgment | Probability | Canonical Readiness |
| --- | --- | ---: | ---: |
| Entry 172 currently has a row-level conversion conflict. | Supported. The reviewed artifacts preserve incompatible readings for the same source and entry number. | 0.86 | 0.15 |
| Entry 172 is the Pulgar/Arriagada birth of `Jose del Carmen Segundo Pulgar Arriagada`. | Plausible but not promotion-ready. The chunk/source packet and visible image context support it broadly, but conversion QA must certify the row. | 0.68 | 0.10 |
| Entry 172 is the Burgos/de la Cruz birth of `José Miguel`. | Not supported by the current chunk/source packet and visually doubtful from the reviewed image, but it remains present in the converted Markdown and must be resolved by QA. | 0.22 | 0.02 |
| `Jose del Carmen Pulgar S.` can be normalized to `Jose del Carmen Pulgar`. | Hold. The staged draft correctly preserves multiple father-field readings rather than normalizing silently. | 0.52 | 0.08 |
| This record supports a Dario-line same-person or relationship bridge. | Not supported. No reviewed source text supplies the required names, dates, relationships, or life-context bridge. | 0.03 | 0.00 |

## Next Action

Keep the staged identity analysis on `hold_for_conversion_qa`. The next required action is targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`: compare the source image, current converted Markdown, current chunk, and held source packet; certify whether entry 172 is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row; and resolve the father field without forcing a canonical normalization.

After conversion QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent candidate, person merge, or Dario-line bridge.
