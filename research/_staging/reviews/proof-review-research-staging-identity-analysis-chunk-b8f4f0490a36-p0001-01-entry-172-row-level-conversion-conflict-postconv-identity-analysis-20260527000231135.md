---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260527020446886
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000231135.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527000231135.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260526232323475.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260526232323475.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical promotion remains blocked by a material row-control conflict between the current converted Markdown and the image-reviewed row. The converted file records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the source image, assigned chunk, source packet, and targeted QA note support physical entry `172` as the Pulgar/Arriagada birth registration.
2. The father field is not ready for a suffix-level claim. The chunk reads `Jose del Carmen Pulgar S.`, but the source image shows only an ambiguous trailing mark after `Pulgar`; I accept `Jose del Carmen Pulgar` and hold the possible `S.`.
3. The staged draft correctly rejects Dario-line identity or lineage attachment. This record does not name Dario, Arturo, Smith, a spouse, descendant, or any direct bridge to the Dario clusters.
4. The staged draft correctly keeps `Juana Arriagada de Pulgar` separate from `Juana de Dios Amagada de Pulgar`. This source names only `Juana Arriagada de Pulgar`.

## Evidence Scores

| Judgment area | Score | Notes |
|---|---:|---|
| source_quality_score | 0.90 | Civil birth register image is a strong original/near-original source for the recorded birth facts. |
| conversion_confidence_score | 0.68 | The assigned chunk and targeted QA align with the image, but the current converted Markdown is materially mismatched. |
| evidence_quantity_score | 0.72 | One direct register row plus chunk, source packet, QA note, and visual check; no independent corroborating source reviewed. |
| agreement_score | 0.74 | Image, chunk, packet, and QA agree on the Pulgar/Arriagada row; converted Markdown sharply disagrees. |
| identity_confidence_score | 0.83 | Strong for the bounded identity of the child named in physical entry 172; weak for broader merges. |
| claim_probability | 0.84 | Physical entry 172 probably records `Jose del Carmen Segundo Pulgar Arriagada`, with the stated parents and birth details. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-candidate work. |
| relevance_confidence | 0.92 | The named child and parents are directly within the Pulgar/Arriagada line under review. |
| canonical_readiness | hold | Use as staged proof context only until conversion-control resolves or explicitly carries the row mismatch. |

## Reviewed Support

The source image and assigned chunk support physical entry `172` on page 58 as:

- registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- child: `Jose del Carmen Segundo Pulgar Arriagada`
- sex: `Hombre`
- birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`
- birth place: `Calle de Valdivia`
- father: `Jose del Carmen Pulgar`
- mother: `Juana Arriagada de Pulgar`
- declarant: `Ernesto Herrera L.`, present at birth

The source packet and targeted QA note accurately summarize this row. The staged identity analysis is literally supported where it treats the converted Markdown's Burgos/de la Cruz entry as a derivative conversion conflict rather than as controlling evidence for this physical row.

## Identity And Relationship Risk

The child identity claim is probable when limited to the image-reviewed entry. Parent relationship claims are probable but should remain gated by conversion reconciliation. The father suffix must not be promoted. The mother reading is stronger, but should not be merged with other Juana candidates from surrounding family context.

The Dario hypotheses are appropriately scored as not supported. The record supplies only a surname-level future lead, not an identity bridge.

## Evidence Strengths

- The source image visibly places entry `172` in the middle row of page 58 with the Pulgar/Arriagada names.
- The assigned chunk gives a detailed row transcription that agrees with the source image on the main child, date, place, parent, and declarant fields.
- The targeted QA note correctly identifies the current converted Markdown as stale, row-shifted, or otherwise mismatched for this source identity.
- The staged draft keeps uncertainty separated from interpretation and avoids unsupported parent merges or Dario-line jumps.

## Next Action

Hold canonical promotion. Send this item to conversion-control or a scoped correction workflow so the stale converted Markdown conflict is resolved or explicitly preserved as a known derivative mismatch. After that, promote only narrow Entry 172 claims for `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` without suffix, and mother `Juana Arriagada de Pulgar`; do not promote any Dario bridge or Juana identity merge from this record.
