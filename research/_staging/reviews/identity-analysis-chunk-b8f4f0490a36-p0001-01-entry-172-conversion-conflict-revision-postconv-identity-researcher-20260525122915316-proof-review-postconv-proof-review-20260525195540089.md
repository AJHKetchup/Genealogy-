---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260525195540089
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525122915316.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525122915316.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The staged identity analysis is supported as a conflict/hold note, not as a claim package ready for canonical promotion.
2. The referenced chunk and visible source image support entry 172 as the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, father read in the chunk as `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
3. The referenced converted Markdown does not support the Pulgar/Arriagada row. In the file reviewed for this task, entry 172 reads as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril... a las diez de la noche`, place `En esta`.
4. The staged draft/source packet describe the converted-file conflict as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born `veinte i seis de Marzo`. That description is not literal support from the current referenced converted file and should be revised or superseded during conversion QA.
5. The father ending after `Jose del Carmen Pulgar` remains unresolved for canonical purposes. Do not normalize `Jose del Carmen Pulgar S.` into `Jose del Carmen Pulgar`, and do not merge parent candidates from this draft alone.
6. No Dario identity cluster is named in entry 172. This draft gives no source-supported bridge to `Dario`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or similar Pulgar/Arriagada Dario candidates.

## Evidence Strengths

- The page image was visually checked and supports the broad chunk reading for page 58, entry 172: a Pulgar/Arriagada birth row, not the Burgos/de la Cruz row in the converted Markdown.
- The referenced chunk gives a coherent row-level transcription for entry 172: registration date 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; birth 8 March 1888 at 3 p.m.; place `Calle de Valdivia`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- The staged draft correctly identifies the controlling issue as a row-level conversion/file-assignment conflict and correctly recommends holding dependent identity, parent-child, and merge claims.
- The source packet preserves the key uncertainty: the conflict between converted Markdown and chunk plus the exact father-name ending.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a strong primary source, and the image was available for review. |
| conversion_confidence_score | 0.42 | Image and chunk align on the Pulgar/Arriagada row, but the referenced converted Markdown assigns entry 172 to a materially different family. |
| evidence_quantity_score | 0.58 | One primary image plus one aligned chunk support the Pulgar/Arriagada reading; the assembled converted Markdown conflicts. |
| agreement_score | 0.44 | Chunk/source packet/image agree broadly, but converted Markdown and stale conflict wording disagree materially. |
| identity_confidence_score | 0.67 | Probable that the visible entry 172 is for `Jose del Carmen Segundo Pulgar Arriagada`, capped by derivative conflict and father-suffix uncertainty. |
| claim_probability | 0.68 | Pulgar/Arriagada reading is probable from image plus chunk, but not proof-ready until conversion QA reconciles the package. |
| relevance_level | high | Directly concerns entry 172 and the Pulgar/Arriagada parent-child evidence under review. |
| relevance_confidence | 0.95 | The reviewed files all reference the same chunk id, page reference, and source image, despite internal transcript conflict. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, parent merges, or Dario comparisons from this draft. |

## Claim Probability Detail

| Claim or Hypothesis | Probability | Review Judgment |
| --- | ---: | --- |
| Entry 172 is the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.68 | Supported by chunk and visible image; held because converted Markdown conflicts. |
| Father is exactly `Jose del Carmen Pulgar S.` | 0.55 | Chunk reads this way, but suffix needs targeted image QA before canonical normalization. |
| Mother is `Juana Arriagada de Pulgar`. | 0.66 | Supported by chunk and visible image; held because the derivative package is unstable. |
| Entry 172 is the converted-file `Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz` row. | 0.18 | Literally present in converted Markdown, but contradicted by source image and chunk for this packet. |
| Entry 172 is the draft-described `Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz` row. | 0.10 | Present in staged/source-packet wording, but not in the current referenced converted file or chunk reviewed here. |
| This entry bridges any Dario Pulgar identity cluster. | 0.02 | No Dario is named; shared surnames alone are not relationship or identity proof. |

## Next Action

Send this item to targeted conversion QA before any canonical use. QA should reconcile the source image, referenced converted Markdown, referenced chunk, conflict draft, and source packet for `CHUNK-b8f4f0490a36-P0001-01`; decide which row is the controlling entry 172; correct the stale converted-file conflict description; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review for the child identity, birth facts, parent-child relationships, parent candidate merges, and any Dario-line anti-conflation note.
