---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260525202357764
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
review_status: revise
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The source image and assigned chunk support entry 172 as a Pulgar/Arriagada birth registration, but the assigned converted Markdown still transcribes a different entry 172 row for the same file.
- The staged identity-analysis draft should be revised before reuse because it says the converted Markdown reads `José Francisco`, father `Oswaldo Gomez`, and mother `Rosario de la Cruz de la Maza`; the current referenced converted file instead reads `José Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- The current converted Markdown is not reliable for claims from this source image. It conflicts with the source image on the child name, father, mother, birth date, place, and surrounding entries.
- The draft's Dario-line and canonical-wiki comparisons are not directly supported by the reviewed source layer. Entry 172 does not name Dario, Arturo, Smith, Dario Jose, or any later professional/property/passenger context.
- The father-field ending after `Pulgar` remains lower confidence than the core row identity. The visible source supports `Jose del Carmen Pulgar` and likely an ending mark/suffix, but the exact final reading should stay under QA as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525171911545.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525171911545.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image visibly shows entry `172` on page 58 as a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, male.
- The source image supports registration date `Siete de Abril de mil ochocientos ochenta i ocho`.
- The source image supports birth date/place as `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `a las tres de la tarde`, at `Calle de Valdivia`.
- The source image supports father `Jose del Carmen Pulgar` with an uncertain final mark or suffix, and mother `Juana Arriagada de Pulgar`.
- The source image supports informant `Ernesto Herrera L.`, present at the birth, age `Veintiseis años`, profession `Empleado`, residence `Calle de Valdivia`.
- The chunk and source packet substantially agree with the visible source image for the Pulgar/Arriagada row.

## Scored Judgment

| Metric | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth-register image is a direct contemporary source, though handwriting and image quality leave limited ambiguity in some fields. |
| conversion_confidence_score | 0.48 | Chunk/source-packet conversion agrees with the image, but the assigned converted Markdown is a materially different row and cannot be trusted without repair. |
| evidence_quantity_score | 0.60 | One direct source image plus derivative chunk/source packet; enough for local row assessment, not enough for broader identity bridges. |
| agreement_score | 0.58 | Source image, chunk, and source packet agree on the Pulgar row; assigned converted Markdown and parts of the staged draft disagree. |
| identity_confidence_score | 0.74 | Good confidence for the child and parents within this single birth registration; low confidence for any cross-record identity conclusion. |
| claim_probability | 0.84 | Entry 172 in the source image is probably the Pulgar/Arriagada birth registration, not the row currently in the converted Markdown. |
| relevance_level | high | Pulgar and Arriagada names make the record family-relevant if the conversion is corrected. |
| relevance_confidence | 0.82 | Relevance is strong for the Pulgar/Arriagada source packet, but not for Dario-line attachment. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until the converted Markdown/source packet/chunk conflict is reconciled and father-field QA is certified. |

## Claim Probability Notes

- Pulgar/Arriagada row identity for entry 172: `0.84`.
- Current converted-file row as correct for this source image: `0.08`.
- Same-person or duplicate-person bridge between the Pulgar/Arriagada child and the converted-file Burgos/de la Cruz row: `0.01`.
- Direct Dario-line identity bridge from this entry alone: `0.03`.
- Father field exactly as `Jose del Carmen Pulgar S.`: `0.62`; father field as `Jose del Carmen Pulgar` with unresolved suffix/mark: `0.78`.

## Next Action

Revise the staged identity-analysis note to reflect the current converted Markdown conflict accurately, then run targeted conversion QA against the source image. After the converted Markdown is corrected or superseded and the father-field ending is certified, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent-candidate merge, or Dario-line comparison.
