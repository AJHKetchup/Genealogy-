---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260525202828220
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
review_status: revise
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The referenced source image and chunk support entry 172 as a Pulgar/Arriagada birth registration, but the referenced converted Markdown transcribes a different entry 172 row for the same source file.
- The staged identity-analysis draft needs revision before reuse because its summary of the converted Markdown is stale. It says the converted file reads `José Francisco`, father `Oswaldo Gomez`, and mother `Rosario de la Cruz de la Maza`; the current referenced converted file reads `José Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- The assigned converted Markdown is not reliable evidence for this entry until targeted conversion QA resolves the row/file-assignment conflict. It conflicts with the source image on child name, parents, birth date, place, and surrounding entries.
- The staged draft's broader Dario-line and canonical-wiki comparisons are not supported by the reviewed source layer. The referenced entry does not name Dario, Arturo, Smith, Dario Jose, or any later professional, property, passenger, or family-linking context.
- The father-field ending after `Pulgar` remains unresolved at proof-review level. The visible source supports `Jose del Carmen Pulgar` with an additional final mark or suffix, but the exact reading should remain under QA as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525171911545.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525171911545.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image visibly shows entry `172` on page 58.
- The source image supports the child as `Jose del Carmen Segundo Pulgar Arriagada`, male.
- The source image supports registration on `Siete de Abril de mil ochocientos ochenta i ocho`.
- The source image supports birth on `Ocho de Marzo de mil ochocientos ochenta i ocho`, at about `a las tres de la tarde`, place `Calle de Valdivia`.
- The source image supports father `Jose del Carmen Pulgar` with an uncertain ending mark/suffix and mother `Juana Arriagada de Pulgar`.
- The source image supports informant `Ernesto Herrera L.`, present at the birth, age `Veintiseis años`, profession `Empleado`, residence `Calle de Valdivia`.
- The chunk and source packet substantially agree with the visible source image for the Pulgar/Arriagada row.

## Scored Judgment

| Metric | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Direct civil birth-register image; handwriting and image quality leave limited ambiguity in some fields. |
| conversion_confidence_score | 0.48 | Chunk/source packet agree with the image, but the assigned converted Markdown is materially wrong for entry 172. |
| evidence_quantity_score | 0.60 | One direct source image plus derivative chunk/source packet; sufficient for local row assessment, insufficient for broader identity bridges. |
| agreement_score | 0.58 | Source image, chunk, and source packet agree on the Pulgar row; converted Markdown and part of the staged draft disagree. |
| identity_confidence_score | 0.74 | Good confidence for the child and parents within this single registration; low confidence for any cross-record identity conclusion. |
| claim_probability | 0.84 | Entry 172 in the source image is probably the Pulgar/Arriagada registration represented by the chunk, not the current converted-file row. |
| relevance_level | high | Pulgar and Arriagada names make the record family-relevant if the conversion is corrected. |
| relevance_confidence | 0.82 | Relevance is strong for the Pulgar/Arriagada source packet, but not for any Dario-line attachment. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until the converted Markdown/chunk/source packet conflict is reconciled and father-field QA is certified. |

## Claim Probability Notes

- Pulgar/Arriagada row identity for entry 172: `0.84`.
- Current converted-file row as correct for this source image: `0.08`.
- Same-person or duplicate-person bridge between the Pulgar/Arriagada child and the converted-file Burgos/de la Cruz row: `0.01`.
- Direct Dario-line identity bridge from this entry alone: `0.03`.
- Father field exactly as `Jose del Carmen Pulgar S.`: `0.62`.
- Father field as `Jose del Carmen Pulgar` with unresolved suffix/mark: `0.78`.

## Next Action

Revise the staged identity-analysis note so it describes the current converted Markdown conflict accurately, then run targeted conversion QA against the source image. After the converted Markdown is corrected or explicitly superseded and the father-field ending is certified, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent-candidate merge, or Dario-line comparison.
