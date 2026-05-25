---
type: proof_review
status: revise_hold
role: claim_reviewer
worker: postconv-proof-review-20260525165933158
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525123546801.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525123546801.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_page: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

1. Canonical readiness remains `hold_for_conversion_qa`. The source image and current chunk support entry 172 as a Pulgar/Arriagada birth row, while the assigned converted Markdown gives entry 172 as a Gomez/de la Cruz de la Maza row. These cannot both be the controlling transcription for the same row.
2. The staged identity-analysis draft and source packet misstate parts of the current converted-file reading. The reviewed converted Markdown records entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born `En veinte de Febrero... a las diez de la noche`, place `En Pellin`. The draft instead says mother `Emilia de la Cruz`, birth date `veinte i seis de Marzo`, and place `En esta`.
3. The father field in the Pulgar/Arriagada row is not ready for normalized canonical use. The chunk reads `Jose del Carmen Pulgar S.`, and the source image appears compatible with a trailing initial or mark after `Pulgar`; this review does not certify whether the field should be transcribed as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Parent-child relationship claims remain held. The image-supported row is strong enough for a QA target, but not for promoting claims or merging `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar` candidates while the derivative conversion conflict remains unresolved.
5. No Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, later-life event, spouse, or child bridge is named in this entry. Any Dario-line attachment from this record would be a relationship jump based only on surname context.

## Evidence Strengths

- The source image for page 58, entry 172 visibly supports the same broad row described by the chunk: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered `Siete de Abril de mil ochocientos ochenta i ocho`, born `Ocho de Marzo... a las tres de la tarde`, place `Calle de Valdivia`, with father `Jose del Carmen Pulgar [S.?]` and mother `Juana Arriagada de Pulgar`.
- The current chunk gives a coherent civil birth registration row with child, sex, birth date and place, parents, residence, informant, and official signature context.
- The staged draft is appropriately conservative in its main disposition: it treats the item as a row-level conversion or assignment conflict and does not promote canonical claims.
- The draft correctly warns against using the Pulgar/Arriagada surname pattern as a direct Dario-line identity bridge.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.84 | Civil birth register page image is a strong primary source for birth and parent evidence; legibility is good enough for the row but weaker at the father suffix. |
| conversion_confidence_score | 0.43 | The chunk aligns with the visible source image, but the assigned converted Markdown gives a materially different row for entry 172. |
| evidence_quantity_score | 0.56 | Review used the staged draft, source packet, chunk, converted Markdown, and page image; no independent corroborating source was in scope. |
| agreement_score | 0.46 | Source image, chunk, and source packet broadly agree on Pulgar/Arriagada, but the converted Markdown disagrees and the staged draft misquotes parts of that converted reading. |
| identity_confidence_score | 0.68 | Probable that the visible entry 172 is for `Jose del Carmen Segundo Pulgar Arriagada`; confidence is capped by conversion conflict and father-suffix uncertainty. |
| claim_probability | 0.72 | The Pulgar/Arriagada row is more probable from the image and chunk, but the claim is not promotable until conversion QA reconciles the derivative file. |
| relevance_level | high | If QA-certified, the row is directly relevant to Pulgar/Arriagada family evidence. Direct Dario relevance is absent. |
| relevance_confidence | 0.88 | Pulgar and Arriagada are explicit in the image-supported row; broader Dario-line relevance is only contextual. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, merges, or identity bridges until targeted conversion QA resolves row control and father-field transcription. |

## Review Decision

Recommended disposition: `revise_hold`.

The staged draft's hold conclusion is supported, but the description of the converted-file conflict needs revision before reuse. The conflict should be described from the current converted Markdown as `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 20 February 1888 at 10 p.m. in Pellin, not as `Emilia de la Cruz`, 26 March, or `En esta`.

## Next Action

Keep this item out of canonical folders. Send the source image, converted Markdown, current chunk, and source packet to targeted conversion QA. QA should decide whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz de la Maza row, refresh the conflict wording to match the current converted file, and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review after QA before any claim, parent-child relationship, parent merge, or Dario-line comparison is promoted.
