---
type: proof_review
status: revise_hold
worker: postconv-proof-review-20260525114552433
role: claim_reviewer
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525092421532.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525092421532.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

- Canonical readiness remains blocked. The assigned converted Markdown and the current chunk are materially different transcriptions of entries 171-176, including a direct conflict for entry 172.
- The staged draft correctly treats this as a row-level/file-assignment conversion conflict and correctly blocks promotion of identity, parent-child relationships, parent merges, and any Dario-line bridge.
- The converted Markdown is not reliable for this Pulgar/Arriagada claim as currently assigned because it gives entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, and a different birth date/place.
- The father-name ending remains a transcription uncertainty for promotion purposes. The chunk/source packet read `Jose del Carmen Pulgar S.`, but a QA note should still certify whether the visible source supports `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No same-person merge or relationship bridge to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada` is supported by this staged draft.

## Evidence Strengths

- The page image visibly supports the chunk/source-packet family-relevant row for entry 172: the child appears as `Jose del Carmen Segundo Pulgar Arriagada`, with parents rendered as `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The chunk and source packet agree with each other on the Pulgar/Arriagada reading, including registration date, birth date/time, birth place, parent names, parent residence, and informant.
- The staged identity analysis is cautious and does not attempt to promote the conflicted derivative evidence, merge identities, or infer a Dario relationship from surname overlap.
- The source type is strong for a birth identity and parent-child event if conversion QA reconciles the derivative conflict.

## Scored Judgment

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is direct evidence for the event, but the proof surface is weakened by conflicting derivative artifacts. |
| conversion_confidence_score | 0.48 | The chunk is visually plausible and source-packet aligned, but the assigned converted Markdown conflicts materially. |
| evidence_quantity_score | 0.55 | One source image plus two agreeing derivative artifacts support the Pulgar reading; no independent corroborating source was reviewed or needed. |
| agreement_score | 0.45 | Chunk, source packet, and image agree, but the assigned converted file disagrees at the row level. |
| identity_confidence_score | 0.62 | The image-supported Pulgar/Arriagada row is stronger than the converted-file reading, but identity use should wait for targeted QA. |
| claim_probability | 0.68 | It is more likely than not that the visible entry 172 on this image is the Pulgar/Arriagada row, but promotion is premature until the conversion assignment conflict is resolved. |
| relevance_level | high | If certified, the row directly concerns a Pulgar/Arriagada birth and parent candidates. |
| relevance_confidence | 0.92 | Family relevance is strong for Pulgar/Arriagada analysis, conditional on conversion QA. |
| canonical_readiness | 0.10 | Hold for conversion QA; no canonical claim, relationship, page update, merge, or Dario bridge should be promoted from this draft now. |

## Claim Review

- Claim that a material conversion conflict exists: supported. The converted Markdown gives a Gomez/de la Cruz entry 172, while the chunk/source packet and visible image give a Pulgar/Arriagada entry 172.
- Claim that entry 172 may support `Jose del Carmen Segundo Pulgar Arriagada`: supported as a high-probability, noncanonical candidate pending conversion QA.
- Claim that `Jose del Carmen Pulgar S.` is the father: supported by the chunk/source packet and visible source at review level, but the exact suffix should remain held until targeted transcription QA certifies it.
- Claim that `Juana Arriagada de Pulgar` is the mother: supported by the chunk/source packet and visible source at review level, but still held because the derivative conflict affects the whole row.
- Claim that this evidence bridges to any Dario candidate: not supported. The staged draft correctly rejects this jump.

## Identity And Relationship Risk

- Same-person risk: moderate for treating the father as an existing `Jose del Carmen Pulgar` without independent proof.
- Duplicate-person risk: high if b8f4-derived wiki snapshots are counted as independent corroboration.
- Relationship-jump risk: high for any Dario-line inference, because the reviewed evidence names no Dario candidate and supplies no lineage bridge.
- Conflict severity: high. The conflict is not a spelling variant; it changes child, parents, dates, residences, informant, and official context.

## Next Action

Run targeted conversion QA against the source image, assigned converted Markdown, and chunk. The QA note should explicitly decide whether the controlling entry 172 for this task is the Pulgar/Arriagada row or the Gomez/de la Cruz row, and should certify the father field without normalizing beyond what is visible. After that, rerun proof review before any canonical claim, relationship, parent merge, or Dario-line comparison is promoted.
