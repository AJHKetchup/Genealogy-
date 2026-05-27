---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260527021402830
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

1. Canonical promotion is blocked by a material conversion conflict. The current converted Markdown identifies entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the source image, assigned chunk, source packet, and targeted QA note support physical entry `172` as the Pulgar/Arriagada row.
2. The father suffix remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, but the visible source supports only the bounded father reading `Jose del Carmen Pulgar`; the possible suffix should stay in notes only.
3. No Dario-line identity bridge is supported. The reviewed entry does not name Dario, Arturo, Smith, a spouse, descendant, or another direct bridge to the Dario clusters.
4. No merge is supported between `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`. This source names only `Juana Arriagada de Pulgar`.

## Evidence Scores

| Judgment area | Score | Notes |
|---|---:|---|
| source_quality_score | 0.90 | Civil birth register image is direct evidence for the recorded birth row. |
| conversion_confidence_score | 0.68 | The chunk and targeted QA align with the visible image, but the converted Markdown is materially mismatched. |
| evidence_quantity_score | 0.72 | One direct register row was reviewed, with supporting chunk, source packet, QA note, and visual image check. |
| agreement_score | 0.74 | Source image, chunk, packet, and QA agree on Pulgar/Arriagada; the converted Markdown sharply disagrees. |
| identity_confidence_score | 0.83 | Strong for the bounded child identity in physical entry 172; low for any broader merge. |
| claim_probability | 0.84 | Physical entry 172 probably records `Jose del Carmen Segundo Pulgar Arriagada` with the stated birth details and parents. |
| relevance_level | high | Direct Pulgar/Arriagada family evidence and anti-conflation context. |
| relevance_confidence | 0.92 | The reviewed row directly names the Pulgar/Arriagada child and parents. |
| canonical_readiness | hold | Keep staged until conversion-control resolves or explicitly preserves the derivative row mismatch. |

## Reviewed Support

The source image visibly supports the assigned chunk and targeted QA note for page 58, entry `172`. The supported bounded reading is:

- registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- child: `Jose del Carmen Segundo Pulgar Arriagada`
- sex: `Hombre`
- birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`
- birth place: `Calle de Valdivia`
- father: `Jose del Carmen Pulgar`
- mother: `Juana Arriagada de Pulgar`
- declarant: `Ernesto Herrera L.`, present at the birth

The staged draft is supported where it treats the Burgos/de la Cruz converted Markdown as a derivative conversion mismatch instead of controlling evidence for physical entry `172`.

## Evidence Strengths

- The source image places entry `172` in the middle row of register page 58 with Pulgar/Arriagada names.
- The assigned chunk matches the image on the main child, date, place, parent, and declarant fields.
- The targeted QA note properly separates the certified father reading from the unresolved possible suffix.
- The staged draft correctly rejects unsupported relationship jumps, parent-candidate merges, and Dario-line identity attachments.

## Next Action

Hold canonical promotion. Route the converted Markdown mismatch to conversion-control or another scoped correction path. After row-control reconciliation, promote only narrow Entry 172 claims for `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` without suffix, and mother `Juana Arriagada de Pulgar`; do not promote a Dario bridge or Juana identity merge from this record.
