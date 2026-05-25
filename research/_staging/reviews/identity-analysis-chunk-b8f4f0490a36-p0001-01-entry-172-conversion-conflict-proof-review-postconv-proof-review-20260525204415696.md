---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525204415696
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md"
reviewed_conflict_note: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
claim_probability: 0.68
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The staged draft correctly treats entry 172 as a conversion conflict, but the conflict is still active and should not be promoted into claims, relationships, or canonical wiki pages.
- The source image and the assigned chunk support entry 172 on page 58 as a Pulgar/Arriagada birth-registration row for `Jose del Carmen Segundo Pulgar Arriagada`, with father field appearing as `Jose del Carmen Pulgar` plus an unresolved possible suffix/mark, and mother `Juana Arriagada de Pulgar`.
- The currently referenced converted Markdown does not match the image/chunk. It currently records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 1888-04-06 at 10 p.m. in `En esta`.
- The staged draft and conflict/source-packet notes describe a prior or competing converted-file reading as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 1888-02-20 at 10 p.m. in `En Pellin`. That description is not literally supported by the converted Markdown as it exists in the workspace during this review.
- The father field must remain unresolved among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies the source reading. This review does not normalize the name or instruct transcription changes.
- The Dario-line comparisons in the staged draft are anti-conflation guidance only. This source does not visibly name Dario, Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or any other Dario candidate.

## Evidence Strengths

- Source quality is strong for a birth-registration claim because the image is an original civil register spread with entry numbers, registration date, child, birth details, parents, informant, and official signature columns.
- The assigned chunk is aligned with the visible source image for the central family-relevant row: entry 172, registration date 1888-04-07, child `Jose del Carmen Segundo Pulgar Arriagada`, male sex, birth date 1888-03-08 at 3 p.m., place `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and residences on `Calle de Colipi`/`Calle de Valdivia`.
- The staged identity-analysis draft appropriately treats the competing readings as a row-level or file-assignment conflict rather than a spelling variant or identity merge.
- The staged draft correctly preserves the father-ending uncertainty and blocks parent-candidate and Dario-line merges.

## Evidence And Probability Scoring

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil registration image is direct, contemporaneous evidence, but the image is small/low contrast enough that father-ending certification should be handled by targeted QA. |
| conversion_confidence_score | 0.38 | The chunk and image agree on the Pulgar/Arriagada row, but the converted Markdown is materially inconsistent and the staged draft's description of the converted Markdown no longer matches the current file. |
| evidence_quantity_score | 0.62 | One direct source image plus derivative chunk/source packet/conflict notes; no independent corroborating record reviewed for identity beyond this entry. |
| agreement_score | 0.44 | Image and chunk agree, while converted Markdown and derivative descriptions disagree on the same entry number. |
| identity_confidence_score | 0.66 | The entry likely concerns the Pulgar/Arriagada child if the source image/chunk control, but proof remains blocked by conversion-file inconsistency and father-ending uncertainty. |
| claim_probability | 0.68 | Probable that the visible entry 172 is the Pulgar/Arriagada registration, but not promotion-ready until conversion QA reconciles the file conflict. |
| relevance_level | 1.00 | Directly relevant to the staged draft and source packet under review. |
| relevance_confidence | 0.98 | The reviewed image, chunk, source packet, conflict note, and staged draft all point to the same assigned page/chunk task even though their readings conflict. |
| canonical_readiness | 0.10 | Hold; no canonical promotion from this review. |

## Claim-Specific Assessment

| Claim Or Hypothesis | Probability | Review Judgment |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.68 | Supported by source image and chunk, blocked by converted Markdown inconsistency. |
| Father is exactly `Jose del Carmen Pulgar S.`. | 0.45 | Chunk reads this, but source-image father ending needs QA; keep the suffix uncertain. |
| Father is `Jose del Carmen Pulgar` with unresolved suffix/mark. | 0.62 | Best conservative formulation pending QA. |
| Mother is `Juana Arriagada de Pulgar`. | 0.66 | Supported by source image/chunk if Pulgar row controls; still held due to conversion conflict. |
| Converted Markdown's current `Jose Miguel`/`Oswaldo Burgos`/`Concepcion de la Cruz` entry is controlling for this source image. | 0.18 | Current converted text conflicts with the visible image and chunk; likely wrong row, wrong file assignment, or stale conversion output. |
| Any Dario identity bridge is supported by this entry. | 0.02 | No Dario appears in the visible source or reviewed derivatives. |

## Source Reliability And Identity Risk

- Source reliability: high for the register image, medium-low for the current converted Markdown, medium for the chunk because it aligns with the image but still needs father-field QA.
- Conversion risk: high. The converted Markdown disagreement affects child identity, parents, birth date, birth place, and informant context.
- Identity risk: high if the father is merged into an existing `Jose del Carmen Pulgar` candidate without resolving the suffix/mark and comparing spouse, residence, date, and child context.
- Relationship-jump risk: high for parent-child relationships until conversion QA confirms the controlling row.
- Relevance risk: low for this staged draft; high for any attempted Dario bridge because the source contains no Dario evidence.

## Next Action

Keep the staged draft and all dependent claims at `hold_for_conversion_qa`.

Run targeted conversion QA on `CHUNK-b8f4f0490a36-P0001-01` using the source image, current converted Markdown, chunk, source packet, and conflict note. The QA result should decide whether the converted Markdown is stale, misassigned, or otherwise superseded for entry 172, and it should certify the father field only as far as the visible source supports: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
