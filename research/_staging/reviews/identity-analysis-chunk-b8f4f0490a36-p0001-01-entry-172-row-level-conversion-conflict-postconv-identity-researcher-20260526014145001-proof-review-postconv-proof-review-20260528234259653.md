---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260528234259653
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
review_output: "research/_staging/reviews/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001-proof-review-postconv-proof-review-20260528234259653.md"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness is `hold`. The staged draft correctly identifies a row-level conflict between the current converted Markdown and the assigned chunk/source packet for entry 172.
- The current converted Markdown records entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. This is not supported by the visible source image for the entry-172 row reviewed here.
- The visible source image and assigned chunk support a Pulgar/Arriagada entry-172 row, but the father field still has a narrow suffix/extent uncertainty after `Jose del Carmen Pulgar`. It should remain certified only as `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` until targeted conversion QA resolves the mark.
- The entry does not name Dario, Arturo, Smith, Pulgar-Smith, or any passenger-list identity. No Dario-line identity bridge, merge, relationship, or name-variant claim is ready from this item.
- Existing canonical pages must not be updated from this review. This review is limited to the staged identity-analysis draft and referenced verification materials.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md`.
- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image visibly places entry `172` on page 58 and supports the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registration date 7 April 1888, birth date 8 March 1888, birth time about 3 p.m., and place `Calle de Valdivia`.
- The source image supports mother `Juana Arriagada de Pulgar` and informant `Ernesto Herrera L.`, present at the birth, age 26, employee, domiciled at Calle de Valdivia.
- The assigned chunk and source packet agree with the source image on the row-level identity, dates, parents, residence cluster, and informant.
- The staged identity-analysis draft correctly keeps interpretation separate from transcription and correctly treats Dario-line relevance as indirect or unsupported.

## Scored Judgment

| Category | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a direct, contemporary source for entry-172 birth-registration facts; image is readable enough for row control. |
| conversion_confidence_score | 0.55 | The assigned chunk aligns with the image, but the current converted Markdown is materially wrong for the same entry number. |
| evidence_quantity_score | 0.62 | One direct register image plus local converted/chunk derivatives; enough for row-control review, not enough for broader identity linking. |
| agreement_score | 0.58 | Source image, chunk, source packet, and staged conflict draft agree on Pulgar/Arriagada; current converted Markdown strongly disagrees. |
| identity_confidence_score | 0.66 | Confidence is good for the entry-172 child/mother/informant cluster, lower for the exact father suffix and any same-person linkage beyond the row. |
| claim_probability | 0.74 | Probability that the visible entry-172 row is the Pulgar/Arriagada row is high, but claim promotion remains blocked by the active converted-file conflict. |
| relevance_level | high_for_pulgar_arriagada; low_for_dario_identity | The item is directly relevant to Pulgar/Arriagada birth-registration staging and only weak family-context evidence for Dario-line research. |
| relevance_confidence | 0.86 | Relevance judgment is well supported by visible names and by the absence of any Dario/Arturo/Smith identifiers. |
| canonical_readiness | hold | No canonical action until conversion QA reconciles the converted Markdown with the source image/chunk and certifies the father-field extent. |

## Claim Probability Notes

- `Jose del Carmen Segundo Pulgar Arriagada` as the child in visible entry 172: 0.82.
- Registration date 7 April 1888: 0.86.
- Birth date 8 March 1888, about 3 p.m., Calle de Valdivia: 0.80.
- Mother `Juana Arriagada de Pulgar`: 0.82.
- Informant `Ernesto Herrera L.` present at birth: 0.78.
- Father `Jose del Carmen Pulgar` with possible suffix/mark after surname: 0.72 for the base name, 0.55 for exact suffix `S.`.
- Current converted Markdown's Burgos/de la Cruz row as the correct row for this source image entry 172: 0.05.
- Any Dario-line identity or relationship claim from entry 172 alone: 0.02.

## Review Decision

Hold the staged draft. The draft's central conclusion is supported: this is a serious row-level conversion conflict and no canonical claim should be promoted from the entry until conversion QA resolves the controlling artifact.

The proof review slightly strengthens the Pulgar/Arriagada side because the source image itself visibly supports that row for entry 172. However, this review does not authorize editing the converted Markdown or canonical wiki pages.

## Next Action

Run targeted conversion QA against the source image, assigned chunk, and current converted Markdown for entry 172 only. QA should correct or supersede the current Burgos/de la Cruz converted reading if confirmed, and should certify the father field only to the visible extent. After QA, rerun proof review before creating or updating any canonical child, parent, relationship, merge, name-variant, or Dario-line claim.
