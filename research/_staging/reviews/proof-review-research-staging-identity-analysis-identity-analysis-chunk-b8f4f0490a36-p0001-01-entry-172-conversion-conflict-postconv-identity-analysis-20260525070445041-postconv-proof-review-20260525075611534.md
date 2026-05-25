---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525075611534
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md"
reviewed_staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md"
review_output: "research/_staging/reviews/proof-review-research-staging-identity-analysis-identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041-postconv-proof-review-20260525075611534.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

1. The assigned converted Markdown and the current chunk still disagree at row level. The current chunk and visible source image support entry 172 as a Pulgar/Arriagada birth registration, but the assigned converted Markdown on disk records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, and place `En esta`.

2. The reviewed staged draft correctly treats the item as not canonical-ready, but it repeats an older or mismatched description of the converted Markdown as `Rosario de la Cruz de la Maza` and `Pellin`. That detail is not supported by the assigned converted file currently referenced in the draft.

3. Father-name ending remains unresolved. The source image and chunk support the father as `Jose del Carmen Pulgar` with a possible final mark or suffix, but this review does not resolve whether the controlled reading should be `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

4. No Dario bridge is present. The entry does not name Dario, Arturo, Smith, Dario Jose, Dario Pulgar Arriagada, occupation, passenger context, Geneva/ICRC context, expropriation context, Alexander John Heinz, or a lineage bridge to a Dario canonical page.

## Evidence Strengths

- The source is a civil birth-register image, which is a strong primary source for the recorded birth row once the correct row transcription is settled.
- The source image visibly supports the current chunk's broad row identity for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at Calle de Valdivia, with father `Jose del Carmen Pulgar...` and mother `Juana Arriagada de Pulgar`.
- The current chunk, source packet, and reviewed staged draft agree that dependent identity and relationship claims should remain held for conversion QA.
- The staged draft appropriately separates the local Jose/Juana parent-candidate question from unsupported Dario-line attachment.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Primary civil registration image, but page image quality and handwriting still require targeted QA for the father ending. |
| conversion_confidence_score | 0.38 | Current chunk aligns with the image at the row level, but the assigned converted Markdown records a different entry 172 and the staged draft misstates that converted row's mother/place details. |
| evidence_quantity_score | 0.46 | One primary register entry plus derivative staging; enough for a local row hypothesis, not enough for canonical identity attachment or relationship merge. |
| agreement_score | 0.42 | Source image/current chunk/source packet agree broadly; assigned converted Markdown conflicts materially. |
| identity_confidence_score | 0.72 | The Pulgar/Arriagada row identity is likely for the visible entry 172, but derivative conflict and father suffix uncertainty prevent higher confidence. |
| claim_probability | 0.74 | Probability that the staged draft's central judgment is correct: hold the Pulgar/Arriagada identity cluster for conversion QA rather than promote or merge it. |
| relevance_level | high | The row is directly relevant to the Pulgar/Arriagada family cluster. |
| relevance_confidence | 0.91 | `Pulgar` and `Arriagada` are visible in the source image/current chunk, with no need for external context to establish local relevance. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical promotion until the converted-file conflict and father-name ending are resolved. |

## Review Judgment

The staged draft is substantially supported in its main proof posture: this item should remain on hold, not promoted, because the derivative transcription set is internally inconsistent. The strongest supported hypothesis is that the visible source image and current chunk correspond to a Pulgar/Arriagada entry 172, while the assigned converted Markdown is a wrong-row or wrong-conversion artifact for this task.

The staged draft should be revised before any downstream use because its description of the converted Markdown does not match the converted file currently referenced. This does not make the Pulgar/Arriagada row unsupported; it strengthens the need for conversion QA by showing that multiple derivative descriptions of the conflicting row are unstable.

No relationship jump is ready. The child-parent cluster for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar...`, and `Juana Arriagada de Pulgar` is plausible from the image/current chunk, but not canonical-ready. No same-person or lineage bridge to any Dario identity is supported by this entry.

## Next Action

Targeted conversion QA should compare the source image, current chunk, and assigned converted Markdown for page 58, entry 172. It should confirm the controlling row, correct or supersede the assigned converted Markdown, and record the father field exactly as source-visible or explicitly uncertain. After that, rerun proof review on the child identity, birth facts, parent-child relationships, and any Jose/Juana parent-candidate comparison. Keep all dependent canonical promotion and Dario-line attachment blocked until that QA is complete.
