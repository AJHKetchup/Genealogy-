---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526090419275
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045206977.md"
reviewed_staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045206977.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- Canonical readiness: `hold_for_conversion_qa`. Do not promote any identity, birth fact, parent-child relationship, parent candidate, or Dario-line bridge from this draft until targeted conversion QA resolves the controlling row.
- The reviewed staged draft is supported as a conflict analysis, but not as a promotable identity proof. The referenced chunk/source packet read entry `172` as a Pulgar/Arriagada birth row, while the current converted Markdown reads entry `172` as a Burgos/de la Cruz birth row.
- This is a row-level conversion conflict, not a spelling or name-variant issue. The disagreement affects child name, sex wording, birth date/time, birth place, father, mother, informant, and relationship candidates.
- The visible source image broadly supports the Pulgar/Arriagada row at entry `172`, but this proof review is not a conversion-QA certification. The father field must remain unresolved among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted QA certifies the reading.
- The draft correctly blocks any merge or bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`; this record does not visibly or derivatively name those identities.

## Scored Judgment

| Review Dimension | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a high-quality source type for birth identity and parentage, but the image is small in the review view and needs targeted row QA for final transcription confidence. |
| conversion_confidence_score | 0.38 | Low for canonical use because the converted Markdown and assigned chunk disagree materially for the same source and entry number. |
| evidence_quantity_score | 0.46 | Evidence is one source image plus derivative transcriptions; no independent corroborating source was reviewed for this task. |
| agreement_score | 0.30 | Chunk, source packet, and visible image broadly agree with Pulgar/Arriagada, but the current converted Markdown directly conflicts. |
| identity_confidence_score | 0.62 | The Pulgar/Arriagada identity is plausible if the chunk controls, but row-control uncertainty blocks proof-level confidence. |
| claim_probability | 0.58 | More likely than not that the staged conflict correctly identifies a real conversion conflict and a plausible Pulgar/Arriagada row, but not enough for promotion. |
| relevance_level | 0.90 | High relevance to Pulgar/Arriagada research if the Pulgar row controls; low relevance to Dario-line merge questions without bridge evidence. |
| relevance_confidence | 0.86 | The family-name relevance is clear in the chunk/source packet and visible image, while identity linkage beyond this birth row is not supported. |
| canonical_readiness | 0.08 | Hold only; no canonical update is ready. |

## Evidence Strengths

- The staged identity analysis accurately reports the core conflict: the assigned chunk/source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the current converted Markdown reads entry `172` as `José Miguel`, with parents `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The source packet explicitly marks conversion confidence as low and recommends `hold_for_conversion_qa`, which matches the proof-review result.
- The visible source image appears broadly consistent with the assigned chunk's Pulgar/Arriagada row for entry `172`, supporting the staged draft's claim that the current converted Markdown conflicts with the assigned chunk/source image.
- The staged draft appropriately treats existing canonical stubs and Dario-related pages as non-confirming derivative context, not independent proof.

## Relationship And Identity Risk

- Parent-child relationships to `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` remain plausible but unpromotable while row-control QA is unresolved.
- The father field has a specific transcription risk; do not normalize or merge the father as `Jose del Carmen Pulgar` without QA certification of the suffix/mark.
- No same-person conclusion is supported between the Pulgar/Arriagada child and any Dario Pulgar identity. Shared surname pattern alone is not probative.
- The Burgos/de la Cruz reading in the current converted Markdown should not be silently discarded by this review; it must be reconciled through conversion QA.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, chunk, and source packet. QA should decide whether entry `172` is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row and certify the father-field reading. After QA, rerun proof review before promoting any claim or relationship from this staged draft.
