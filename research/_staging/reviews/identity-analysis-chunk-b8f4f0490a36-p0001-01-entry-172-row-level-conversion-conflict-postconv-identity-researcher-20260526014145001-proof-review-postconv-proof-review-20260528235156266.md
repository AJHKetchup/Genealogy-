---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260528235156266
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_page: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical conversion blocker: the staged draft correctly identifies a material row-control conflict. The referenced chunk and source packet read entry 172 as a Pulgar/Arriagada birth row, while the referenced converted Markdown reads the same entry number as a Burgos/de la Cruz row.
- Source-transcription boundary blocker: this review can verify that the page image favors the Pulgar/Arriagada row, but it must not edit or replace the converted Markdown. Targeted conversion QA is still required before canonical promotion.
- Father-field precision blocker: the page image and chunk support a father named `Jose del Carmen Pulgar` with an apparent following initial or mark, but proof promotion should preserve uncertainty unless conversion QA certifies the exact visible extent as `Pulgar S.` or another reading.
- Identity-bridge blocker: entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, or any passenger-list candidate. It cannot support Dario-line identity claims or relationship jumps by itself.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md`.
- Conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image visibly places entry 172 on page 58 and shows the child name as `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`.
- The image supports registration on 7 April 1888 and birth on 8 March 1888 at about 3 p.m., with place `Calle de Valdivia`.
- The image supports mother `Juana Arriagada de Pulgar` and compareciente/informant `Ernesto Herrera L.`, present at the birth, age twenty-six, employed, resident at Calle de Valdivia.
- The chunk and source packet align with the visible page image on the controlling Pulgar/Arriagada row. The converted Markdown instead appears to describe a different page or row set for entries 171-176.

## Scoring

| Category | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register page image is a strong contemporary source, though handwriting and image quality leave minor reading uncertainty. |
| conversion_confidence_score | 0.45 | The chunk is well aligned with the image, but the canonical converted Markdown is materially incompatible, so conversion confidence for the workflow remains held. |
| evidence_quantity_score | 0.74 | One direct page image plus aligned chunk/source packet are enough for row-level review, but not for downstream identity bridges. |
| agreement_score | 0.50 | Image, chunk, source packet, conflict draft, and staged draft agree on Pulgar/Arriagada; converted Markdown fully disagrees. |
| identity_confidence_score | 0.62 | The child and parents in the Pulgar/Arriagada row are reasonably identifiable within this record, but father suffix and any cross-record identity are unresolved. |
| claim_probability | 0.78 | Probability that the source page's entry 172 is the Pulgar/Arriagada row is high after image inspection; probability of canonical readiness remains low until conversion QA updates the controlling transcript. |
| relevance_level | high_for_pulgar_arriagada; low_for_dario_identity | Directly relevant to a Pulgar/Arriagada birth-registration cluster; only contextual and weak for Dario-line research. |
| relevance_confidence | 0.86 | Relevance to the Pulgar/Arriagada staged issue is clear from names and row number; relevance to Dario candidates is not source-supported. |
| canonical_readiness | hold | Do not promote claims, relationships, merges, or name variants until conversion QA resolves the converted Markdown conflict and father-field extent. |

## Claim Review

| Claim or hypothesis | Support | Risk | Probability | Review action |
| --- | --- | --- | ---: | --- |
| Entry 172 is for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by image, chunk, and source packet. | Converted Markdown says `Jose Miguel` with different parents. | 0.78 | Hold pending conversion QA; likely revise converted text through proper workflow. |
| Father is `Jose del Carmen Pulgar S.`. | Image supports `Jose del Carmen Pulgar` plus a possible following mark/initial; chunk reads `S.`. | Exact suffix is not fully proof-reviewed from this note alone. | 0.66 | Hold exact suffix; accept only father-name core as visible context. |
| Mother is `Juana Arriagada de Pulgar`. | Supported by image, chunk, and source packet. | Still blocked by converted Markdown conflict. | 0.82 | Hold pending row-control QA. |
| Entry supports Dario-line identity or relationships. | No direct Dario name or relationship appears. | High identity-jump risk if used as bridge evidence. | 0.03 | Reject for direct Dario identity use; retain only as possible family-context evidence after QA. |

## Next Action

Run targeted conversion QA on the referenced page image, converted Markdown, and chunk to resolve the controlling row for entry 172. The QA should certify only the row-level transcription and the father-field extent, then this proof review can be rerun for promotion readiness. Until then, keep canonical_readiness as `hold`.
