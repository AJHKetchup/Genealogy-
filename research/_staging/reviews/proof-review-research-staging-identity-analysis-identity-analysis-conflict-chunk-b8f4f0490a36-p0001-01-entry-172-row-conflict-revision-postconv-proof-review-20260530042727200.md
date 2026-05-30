---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530042656221
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
created: 2026-05-30
---

# Proof Review: Entry 172 Row Conflict Revision

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The assigned chunk/source packet and current converted Markdown give incompatible entry-172 row identities.
2. The assigned chunk and source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, at `Calle de Valdivia`.
3. The current converted Markdown reads entry `172` as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, at `En esta`.
4. The referenced source image path was not available under `raw/sources/` at review time, so this review cannot visually certify which derivative row controls.
5. The father field `Jose del Carmen Pulgar S.` cannot be normalized to `Jose del Carmen Pulgar` without targeted image QA.
6. No available reviewed context for this task names Dario, Arturo, Smith, a Dario child, spouse, or any bridge to a Dario-line identity. Any Dario attachment remains unsupported.

## Evidence Strengths

- The staged draft accurately treats the issue as a severe row-level conversion conflict, not a same-person variant or ordinary spelling issue.
- The assigned chunk and source packet agree internally on the Pulgar/Arriagada reading and preserve a coherent civil birth-registration row.
- The current converted Markdown is internally coherent for a different Burgos/de la Cruz row, which strengthens the conclusion that this is a row-control or conversion-assignment conflict.
- A Chilean civil birth register would be a strong source for birth identity and stated parentage after the controlling row is certified.
- The staged draft correctly keeps Dario-line relevance as anti-conflation context only.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 7/10 for the underlying civil birth-register source type; 4/10 for this review because the page image was unavailable for direct visual verification |
| conversion_confidence_score | 3/10 |
| evidence_quantity_score | 4/10 |
| agreement_score | 2/10 between the converted Markdown and chunk/source packet for entry `172`; 8/10 between the chunk and source packet only |
| identity_confidence_score | 5/10 for the held Pulgar/Arriagada candidate row; 2/10 for exact father-field normalization; 1/10 for any Dario-line bridge |
| claim_probability | 0.62 that the assigned staged target is the Pulgar/Arriagada row; 0.12 for canonical promotion now; 0.03 for Dario-line identity relevance |
| relevance_level | high for Pulgar/Arriagada parent-candidate review; low for Dario identity attachment |
| relevance_confidence | 0.90 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

Hold the staged draft. The draft's main proof judgment is supported by the available derivative evidence: entry `172` is not promotion-ready because the conversion chain disagrees on child name, parents, birth date, birth time, birth place, residence context, and informant.

Do not promote a child identity, birth fact, parent-child relationship, parent-pair clue, parent merge, or Dario-line attachment from this draft. Do not revise the source transcription toward the Pulgar reading or the Burgos reading without visual source QA.

## Next Action

Run targeted conversion QA against the actual source image, current converted Markdown, assigned chunk, and source packet. The QA note must decide the controlling physical row for entry `172` and, if the Pulgar/Arriagada row controls, certify the father field only as far as visible: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review after QA before any canonical promotion.
