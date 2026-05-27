---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527045646995
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030521948.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030521948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.91
conversion_confidence_score: 0.44
evidence_quantity_score: 0.72
agreement_score: 0.54
identity_confidence_score: 0.78
claim_probability: 0.84
relevance_level: high
relevance_confidence: 0.95
canonical_readiness_score: 0.12
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Canonical promotion is blocked by a material derivative conflict. The current converted Markdown assigns entry `172` to `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the assigned chunk, source packet, QA note, and direct image inspection place physical row `172` on the Pulgar/Arriagada registration.
- The father field is not fully settled. The chunk reads `Jose del Carmen Pulgar S.`, but the source packet and QA note certify only `Jose del Carmen Pulgar`; the visible image supports the Pulgar reading but does not make the terminal mark reliable enough for promotion as a suffix.
- No relationship bridge to any Dario/Darío, Arturo, Smith, or later Pulgar-Arriagada identity is supported by this row. The entry names a child `Jose del Carmen Segundo Pulgar Arriagada` and his parents, but it does not prove identity with or descent to any Dario cluster.
- Parent identity beyond this row remains unproved. `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` may be useful candidate parents, but this source alone does not merge them with same- or similar-named wiki stubs.

## Evidence Strengths

- The source is a civil birth register image for Los Angeles, Chile, 1888, and is a strong source type for birth, parentage, registration date, birth date, sex, and informant claims.
- Direct page-image inspection confirms that register page 58, physical row `172`, reads across as `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; birth on `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; birthplace `Calle de Valdivia`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- The assigned chunk agrees with the image-reviewed Pulgar/Arriagada row for the child, mother, date/time, place, and informant.
- The source packet and QA note correctly preserve the conflict with the current converted Markdown rather than silently rewriting the converted text.

## Scoring

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.91 | Civil registration image, directly relevant and visible; strong for the local birth-row facts. |
| conversion_confidence_score | 0.44 | Low-moderate overall because the chunk and image QA agree with each other, but the current converted Markdown materially disagrees. |
| evidence_quantity_score | 0.72 | One primary image plus chunk, source packet, and QA note; enough for row-control review, not enough for broader identity merges. |
| agreement_score | 0.54 | Strong agreement among image, chunk, packet, and QA note; severe disagreement with the converted Markdown lowers total agreement. |
| identity_confidence_score | 0.78 | Moderately high that physical entry `172` is the Pulgar/Arriagada child; low for any identity beyond this row. |
| claim_probability | 0.84 | The row-control claim is likely correct: entry `172` on the visible source image is the Pulgar/Arriagada registration, not the Burgos/de la Cruz entry. |
| relevance_level | high | High relevance to Pulgar/Arriagada research and high risk of bad canonical attachment if promoted prematurely. |
| relevance_confidence | 0.95 | The names Pulgar and Arriagada are directly present in the row. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical claims, relationships, or page edits until conversion-control resolves or supersedes the conflicting converted Markdown. |

## Proof Judgment

Accept the staged draft's main row-control finding as probable: the visible physical row numbered `172` is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, not the Burgos/de la Cruz `José Miguel` entry currently present in the converted Markdown.

Hold all canonical promotion. The supported local claim is row-control and transcription-risk assessment only. Do not promote the father suffix `S.`, do not merge parent candidates, and do not connect this child or parents to any Dario/Darío or Arturo identity from this evidence.

## Next Action

Send this item to conversion-control for reconciliation of the converted Markdown against the source image and assigned chunk. After the derivative conflict is resolved, a separate proof review can evaluate promoted birth and parentage claims using the corrected conversion layer and, if needed, a focused crop for the father-field terminal mark.
