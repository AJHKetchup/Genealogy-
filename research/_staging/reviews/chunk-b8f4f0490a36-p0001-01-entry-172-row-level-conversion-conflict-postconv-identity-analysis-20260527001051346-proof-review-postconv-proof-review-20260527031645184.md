---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527031645184
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527001051346.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527001051346.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_control_update
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The current converted Markdown is not reliable for this physical source image. It records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the visible source image, assigned chunk, source packet, and targeted QA note identify physical entry `172` as the Pulgar/Arriagada row.
2. Canonical promotion from the current converted Markdown should remain blocked until conversion control resolves or explicitly preserves the row-level conflict. The image-reviewed Pulgar/Arriagada reading is stronger than the current conversion, but the canonical path should not silently depend on the stale converted text.
3. The father should be reviewed only as `Jose del Carmen Pulgar` for now. The assigned chunk reads `Jose del Carmen Pulgar S.`, and the image shows a possible terminal mark, but the targeted QA correctly does not certify the suffix as definite.
4. This source does not support any Dario-line attachment, Dario identity bridge, or merge between `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`. Those are separate proof questions requiring direct bridging evidence.

## Evidence Review

The source image was checked directly against the staged draft, source packet, targeted QA note, assigned chunk, and converted Markdown. The physical row labeled `172` on page 58 visibly corresponds to a child named `Jose del Carmen Segundo Pulgar Arriagada`, with parents recorded as `Jose del Carmen Pulgar` or possible `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. It does not correspond to the Burgos/de la Cruz entry in the current converted Markdown.

The source is a civil birth register page image, so source quality is high for the event and immediate parent statements. Evidence quantity is moderate because this review uses one direct source image plus derivative local transcriptions and QA notes from the same source cluster, not independent corroborating records.

## Scored Judgment

| Reviewed claim | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|
| Physical entry `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.92 | 0.74 | 0.68 | 0.82 | 0.88 | 0.90 | high | 0.95 | hold_for_conversion_control_update |
| Current converted Markdown Burgos/de la Cruz row controls this source image's entry `172`. | 0.35 | 0.18 | 0.35 | 0.12 | 0.12 | 0.08 | low | 0.88 | not_ready |
| Father can be promoted as `Jose del Carmen Pulgar`, without terminal suffix. | 0.90 | 0.70 | 0.64 | 0.78 | 0.76 | 0.80 | high | 0.90 | hold_for_suffix_limited_review |
| Father can be promoted as definite `Jose del Carmen Pulgar S.`. | 0.82 | 0.56 | 0.50 | 0.45 | 0.52 | 0.42 | medium | 0.82 | not_ready |
| Mother is recorded in this entry as `Juana Arriagada de Pulgar`. | 0.91 | 0.78 | 0.66 | 0.86 | 0.84 | 0.88 | high | 0.93 | hold_for_conversion_control_update |
| Entry 172 supports a Dario Pulgar identity or lineage bridge. | 0.90 | 0.74 | 0.25 | 0.05 | 0.05 | 0.03 | low_anti_conflation | 0.92 | not_ready |
| Entry 172 proves `Juana Arriagada de Pulgar` equals `Juana de Dios Amagada de Pulgar`. | 0.90 | 0.74 | 0.25 | 0.20 | 0.18 | 0.12 | low | 0.84 | not_ready |

## Evidence Strengths

- The visible page image, targeted QA note, source packet, and assigned chunk all support row control for the Pulgar/Arriagada entry.
- The registration number, registration date, child name, sex, birth date/time, birthplace, mother, declarant, and parent-context fields are materially aligned between the image-reviewed QA note and assigned chunk.
- The staged identity analysis properly treats the Burgos/de la Cruz text as a derivative conversion conflict and does not ask to rewrite the source transcription or promote facts directly.
- The staged identity analysis appropriately blocks Dario-line and Juana-variant merge conclusions because the source does not name Dario and does not bridge the Juana variants.

## Next Action

Hold canonical promotion until conversion control accepts or preserves the row-control correction. After that, promote only narrow claims supported by the physical entry 172 row: the child `Jose del Carmen Segundo Pulgar Arriagada`, birth details, mother `Juana Arriagada de Pulgar`, and father bounded as `Jose del Carmen Pulgar` unless a later proof review certifies the terminal suffix. Do not use this source for Dario-line attachment or Juana identity merging.
