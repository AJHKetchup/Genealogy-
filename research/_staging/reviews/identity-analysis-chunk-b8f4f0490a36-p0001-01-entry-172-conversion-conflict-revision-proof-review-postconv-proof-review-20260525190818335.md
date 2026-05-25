---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525190818335
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

- The reviewed staged draft is `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525093246706.md`.
- The draft's core blocker is supported: the assigned converted Markdown and assigned chunk give materially different entry-172 readings.
- The converted Markdown records entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 in `En esta`.
- The chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at `Calle de Valdivia`.
- The staged source packet partly misquotes the converted Markdown conflict as `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born 26 March 1888. That mismatch is a review-level blocker for relying on the packet's conflict wording, even though the underlying row-level conflict remains real.
- The source image visually aligns much more closely with the chunk's Pulgar/Arriagada row than with the converted Markdown row, but this proof review should not rewrite the source transcription. A targeted conversion QA note should certify the controlling literal reading.
- Do not promote any child identity, birth claim, parent-child relationship, Jose/Juana merge, father-name normalization, or Dario-line linkage from this draft while the derivative evidence chain remains inconsistent.

## Evidence Strengths

- The source type is a civil birth register, a strong source class for birth identity, parent names, date, place, and informant details when the transcription is stable.
- The chunk gives a coherent single-row Pulgar/Arriagada reading for entry 172, including child, sex, registration date, birth date/time, birth place, parents, residences, informant, and official signature context.
- The source packet correctly preserves the chunk's Pulgar/Arriagada reading and correctly recommends `hold_for_conversion_qa`.
- The staged identity analysis is cautious on identity risk. It treats the Pulgar/Arriagada and Burgos/de la Cruz rows as separate readings, rejects a same-person/duplicate theory, and blocks Dario-line linkage by surname alone.
- The father suffix after `Pulgar` remains a legitimate literal-reading uncertainty. The draft appropriately keeps `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` open pending QA.

## Scored Judgment

| Metric | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration is a high-quality source type, but current use is impaired by conflicting derivative transcriptions. |
| conversion_confidence_score | 0.42 | The chunk and source image appear mutually plausible for the Pulgar/Arriagada row, but the converted Markdown is materially different and the source packet misstates that converted-file conflict. |
| evidence_quantity_score | 0.55 | One source image plus one chunk and one source packet support the review; no independent corroborating source is present. |
| agreement_score | 0.40 | Chunk/source packet agree on the Pulgar/Arriagada claim, but converted Markdown disagrees and the packet's description of that disagreement is inaccurate. |
| identity_confidence_score | 0.62 | The Pulgar/Arriagada row is internally coherent in the chunk and source image, but not ready as an identity conclusion until QA resolves the chain. |
| claim_probability | 0.66 | Probable that entry 172 in the visible source is the Pulgar/Arriagada row, but probability is held below promotion level because this review is not a conversion correction. |
| relevance_level | high | If certified, the row is directly relevant to Pulgar/Arriagada birth and parent-candidate work. |
| relevance_confidence | 0.86 | The names `Pulgar` and `Arriagada` are directly visible in the chunk and appear in the page image. |
| canonical_readiness | hold_for_conversion_qa | No canonical promotion should occur before targeted conversion QA and a fresh proof review. |

## Claim Probability And Identity Risk

- Pulgar/Arriagada entry-172 birth claim: probable but held; current probability 0.66.
- Parent-child relationship to `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`: plausible within the chunk; current probability 0.62 because the father suffix and row-control issue remain unresolved.
- Same-person theory between the Pulgar/Arriagada row and the converted Markdown Burgos/de la Cruz row: unsupported; current probability 0.02.
- Dario-line bridge from this entry to any `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada` candidate: unsupported; current probability 0.04.

## Next Action

Create or route a targeted conversion QA task against the source image, converted Markdown, chunk, and source packet. The QA note should identify the controlling entry-172 row and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, identity merge, or Dario-line comparison is promoted.
