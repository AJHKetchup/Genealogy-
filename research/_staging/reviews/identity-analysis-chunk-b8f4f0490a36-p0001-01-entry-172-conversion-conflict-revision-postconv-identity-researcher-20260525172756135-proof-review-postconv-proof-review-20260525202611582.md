---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260525202611582
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md
review_status: revise
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The visible source image and assigned chunk support entry 172 as a Pulgar/Arriagada birth registration, but the assigned converted Markdown still transcribes a materially different entry 172 row for the same source file.
- The staged identity-analysis draft should be revised before reuse because it says the assigned converted Markdown records `Jose Francisco`, father `Oswaldo Gomez`, and mother `Rosario de la Cruz de la Maza`; the current referenced converted file instead records `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- The converted Markdown conflict is row-level, not a spelling or identity variant. The competing readings differ on child name, father, mother, birth date, birth place, and surrounding page context.
- The father-field ending after `Jose del Carmen Pulgar` remains unresolved. Keep the QA alternatives open as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- The Dario-line discussion in the staged draft is only anti-conflation context. Entry 172 does not name Dario, Arturo, Smith, Dario Jose, or any later professional/passenger/legal identity cluster.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image visibly supports entry `172` on page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, male.
- The source image and chunk support registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- The source image and chunk support birth date/place as `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `a las tres de la tarde`, at `Calle de Valdivia`.
- The source image and chunk support father `Jose del Carmen Pulgar` with an uncertain ending or suffix, and mother `Juana Arriagada de Pulgar`.
- The source image and chunk support informant `Ernesto Herrera L.`, present at the birth, age `Veintiseis años`, profession `Empleado`, residence `Calle de Valdivia`.
- The chunk and source packet agree with the visible source image for the Pulgar/Arriagada row and correctly flag the converted Markdown as conflicting.

## Scored Judgment

| Metric | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth-register image is a direct contemporary source for birth and parent-name evidence, though row-level handwriting and image sharpness leave limited father-suffix ambiguity. |
| conversion_confidence_score | 0.48 | Chunk/source packet agree with the image, but the assigned converted Markdown is materially different and the staged draft also misstates the current converted-file reading. |
| evidence_quantity_score | 0.60 | One direct source image plus derivative chunk, converted file, conflict draft, and source packet; enough for row assessment, not enough for cross-record identity bridges. |
| agreement_score | 0.56 | Source image, chunk, and source packet align on the Pulgar row; assigned converted Markdown and part of the staged identity-analysis summary disagree. |
| identity_confidence_score | 0.74 | Good confidence for the single-record Pulgar/Arriagada child-parent cluster, but low confidence for any merge, duplicate-person, or Dario-line conclusion. |
| claim_probability | 0.84 | Entry 172 in the visible source image is probably the Pulgar/Arriagada birth registration, not the row currently represented in the assigned converted Markdown. |
| relevance_level | high | Pulgar and Arriagada names make the source directly family-relevant once the conversion conflict is resolved. |
| relevance_confidence | 0.82 | Relevance is strong for the Pulgar/Arriagada source packet and weak for Dario-line attachment. |
| canonical_readiness | hold_for_conversion_qa | Hold all promotion until conversion QA reconciles the converted Markdown/chunk/source packet conflict and certifies the father-field ending. |

## Claim Probability Notes

- Pulgar/Arriagada row identity for entry 172: `0.84`.
- Current converted-file row as correct for this source image: `0.08`.
- Same-person bridge between the Pulgar/Arriagada child and the converted-file Burgos/de la Cruz row: `0.01`.
- Direct Dario-line identity bridge from this entry alone: `0.03`.
- Father field exactly as `Jose del Carmen Pulgar S.`: `0.62`.
- Father field as `Jose del Carmen Pulgar` with unresolved suffix/mark: `0.78`.

## Next Action

Revise the staged identity-analysis draft to state the current converted Markdown conflict accurately, then run targeted conversion QA against the source image, converted Markdown, chunk, and source packet. After the derivative conflict is corrected or superseded and the father-field ending is certified, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent-candidate merge, or Dario-line comparison.
