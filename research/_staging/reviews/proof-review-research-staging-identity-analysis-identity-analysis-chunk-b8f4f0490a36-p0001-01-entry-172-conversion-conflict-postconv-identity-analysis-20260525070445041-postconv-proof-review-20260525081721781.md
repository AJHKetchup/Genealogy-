---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525081721781
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md"
reviewed_staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md"
review_output: "research/_staging/reviews/proof-review-research-staging-identity-analysis-identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041-postconv-proof-review-20260525081721781.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

1. The assigned converted Markdown and the current chunk conflict at the row level. The source image and current chunk support entry 172 as a Pulgar/Arriagada birth registration, while the assigned converted Markdown currently records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, and place `En esta`.

2. The reviewed staged draft correctly recommends hold, but it describes the assigned converted Markdown as naming mother `Rosario de la Cruz de la Maza`, birth place `Pellin`, and birth date 20 February 1888. That wording is not supported by the converted file currently referenced by the draft, which instead gives `Emilia de la Cruz`, `En esta`, and 26 March 1888.

3. The father-name ending remains unresolved. The source image and current chunk support `Jose del Carmen Pulgar` with an apparent final mark or suffix, but this review does not settle whether the final controlled reading should be `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

4. No Dario-line bridge is visible in this entry. The source image, chunk, converted file, and source packet do not name Dario, Arturo, Smith, Alexander John Heinz, Geneva/ICRC context, passenger context, expropriation context, or a lineage bridge to a Dario canonical person.

## Evidence Strengths

- The underlying source is a civil birth-register image, a strong primary source for the birth row once the controlling transcription is settled.
- The visible source image supports the current chunk's broad row identity for entry 172: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at Calle de Valdivia, with father `Jose del Carmen Pulgar...` and mother `Juana Arriagada de Pulgar`.
- The source packet, conflict note, current chunk, and reviewed staged draft agree that the Pulgar/Arriagada material must remain held for conversion QA.
- The staged draft appropriately treats Dario attachment and entry-513 Jose/Juana comparisons as anti-conflation checks, not as promoted identity conclusions.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Primary civil registration image; good source class, but handwriting/image scale still leaves the father suffix unresolved. |
| conversion_confidence_score | 0.36 | Current chunk aligns with the visible image at the row level, but the assigned converted Markdown is materially different and the staged draft misstates the current converted-file details. |
| evidence_quantity_score | 0.47 | One primary register entry plus derivative staging is enough for a local row hypothesis, not enough for canonical identity or relationship promotion during a conversion conflict. |
| agreement_score | 0.41 | Image/current chunk/source packet agree broadly, while the assigned converted Markdown conflicts with them. |
| identity_confidence_score | 0.72 | The Pulgar/Arriagada row appears to be the visible entry 172, but the derivative conflict and father-ending issue cap identity confidence. |
| claim_probability | 0.75 | Probability that the staged draft's central proof posture is correct: hold the Pulgar/Arriagada identity cluster for conversion QA and do not promote or merge. |
| relevance_level | high | The source-visible row directly concerns a Pulgar/Arriagada family cluster. |
| relevance_confidence | 0.91 | `Pulgar` and `Arriagada` are visible in the source image/current chunk and are repeated in the source packet. |
| canonical_readiness | hold_for_conversion_qa | Canonical promotion is blocked until the converted-file conflict and father-name ending are resolved. |

## Review Judgment

The staged draft is supported in its main recommendation: keep this identity analysis on hold for conversion QA. The strongest supported reading from the visible source image and current chunk is that entry 172 concerns `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar...` and `Juana Arriagada de Pulgar`. The assigned converted Markdown is not reliable controlling evidence for this row as currently written.

The staged draft needs revision before downstream use because its description of the converted Markdown does not match the referenced converted file on disk. That mismatch does not justify promotion; it increases the conversion-risk score and reinforces the hold.

No relationship jump is ready. Parent-child claims are plausible within the source-visible Pulgar/Arriagada row, but they are blocked by conversion conflict and father-suffix uncertainty. No Dario identity, Dario lineage bridge, or entry-513 Juana merge is supported by this entry.

## Next Action

Targeted conversion QA should compare the source image, assigned converted Markdown, and current chunk for page 58, entry 172. It should determine the controlling row, correct or supersede the assigned converted Markdown if needed, and record the father field exactly as source-visible or explicitly uncertain. After that, rerun proof review for child identity, birth facts, parent-child relationships, and Jose/Juana parent-candidate comparison. Keep all canonical promotion and Dario-line attachment blocked until that QA is complete.
