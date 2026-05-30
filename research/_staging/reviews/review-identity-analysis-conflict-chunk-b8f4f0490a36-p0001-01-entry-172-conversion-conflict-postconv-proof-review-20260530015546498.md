---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530015546498
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict

## Blockers First

1. Canonical readiness remains `hold_for_conversion_qa`. The converted Markdown and assigned chunk disagree materially on the controlling row for entry `172`.
2. The staged draft correctly identifies a row-level conversion conflict, but it does not exactly match the current converted file. The current converted file reads entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho`; it does not read `Jose Francisco`, `Oswaldo Gomez`, or `Emilia de la Cruz`.
3. The assigned chunk and source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, at `Calle de Valdivia`.
4. The source image path named by the derivatives was not available at review time under `raw/sources/`, so I could not visually certify which derivative row controls. This blocks promotion and exact father-field normalization.
5. No reviewed source in this task names Dario, Arturo, Smith, a Dario child, a spouse, a grandchild, or a bridge to any Dario-line candidate. Do not attach entry `172` to a Dario identity from surname context alone.

## Evidence Strengths

- Civil birth registration would be a high-quality source for birth identity and stated parentage if the row control were visually reconciled.
- The chunk and source packet agree internally on the Pulgar/Arriagada reading for entry `172`.
- The converted file and chunk agree that the page is a Los Angeles birth register page containing entry `172`, but they disagree on nearly every material value for that row.
- The staged draft is directionally sound in treating the issue as a severe derivative-transcription or file-assignment conflict and in blocking canonical promotion.
- The staged draft is also sound in rejecting Dario-line attachment; neither derivative reading includes a Dario identity or relationship bridge.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 7/10 for the underlying civil registration type; 4/10 for this review because the page image was unavailable for direct verification |
| conversion_confidence_score | 3/10 |
| evidence_quantity_score | 4/10 |
| agreement_score | 2/10 between converted Markdown and chunk/source packet for entry `172`; 8/10 between chunk and source packet only |
| identity_confidence_score | 5/10 for a held Pulgar/Arriagada row candidate; 2/10 for father exact-name/suffix; 1/10 for any Dario attachment |
| claim_probability | 0.55 that the Pulgar/Arriagada row is the intended staged target; 0.10 for canonical promotion now; 0.02 for a Dario identity bridge |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft should be held, not promoted. Its main conclusion is supported: the evidence chain contains a material entry-172 row conflict, and the safe proof outcome is conversion QA before any claims, relationships, parent merges, or Dario-line comparisons move forward.

The staged draft also needs a narrow correction if reused: update its description of the assigned converted Markdown to the current literal converted-file values, namely `Jose Miguel`, `Oswaldo Burgos`, and `Concepcion de la Cruz`. The older `Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz` wording is not supported by the current converted file reviewed here.

## Next Action

Run targeted conversion QA against the actual source image and the two derivative readings. The QA note must decide whether physical entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and it must bound the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` if the Pulgar row is confirmed. After that, rerun proof review before promoting any canonical claim or relationship.
