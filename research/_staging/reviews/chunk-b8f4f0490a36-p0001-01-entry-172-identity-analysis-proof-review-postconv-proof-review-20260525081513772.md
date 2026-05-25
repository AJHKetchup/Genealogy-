---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525081513772
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525070907893.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525070907893.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

1. The assigned converted Markdown and the chunk do not agree on entry 172. The chunk and page image support a Pulgar/Arriagada entry, while the converted Markdown records entry 172 as a different child-parent cluster. This is a material row-level conversion conflict, not a minor spelling or normalization issue.
2. The father field is not fully settled for canonical use. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet preserves alternatives around whether the final mark is `S.` or unresolved.
3. Relationship claims are not ready. The source image and chunk support a child-parent cluster, but the conversion conflict must be resolved before attaching the child to canonical parent candidates or using the record in wider identity analysis.
4. The staged draft correctly treats Dario, Arturo, Smith, Dario Jose, Dario/Darío Pulgar Arriagada, Alexander John Heinz, and occupational/passenger/expropriation contexts as unsupported by this entry. No direct identity bridge to those people or contexts appears in the reviewed entry.
5. Do not merge `Juana Arriagada de Pulgar` with similarly named Juana candidates from other staged work based on this review. This entry alone provides only the literal mother name for entry 172.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a strong source type for birth and parent-name claims, but the image is not perfectly sharp at row level. |
| conversion_confidence_score | 0.42 | The current chunk aligns with the visible image for the Pulgar/Arriagada row, but the assigned converted Markdown is materially inconsistent. |
| evidence_quantity_score | 0.48 | One relevant register entry, one chunk, one source packet, and the page image were reviewed; no independent corroborating record was part of this task. |
| agreement_score | 0.46 | Source packet, chunk, and image agree broadly, but the converted Markdown disagrees on the identity-bearing row. |
| identity_confidence_score | 0.64 | Confidence is moderate that the intended entry is `Jose del Carmen Segundo Pulgar Arriagada`; confidence is reduced by the conversion conflict and father-suffix uncertainty. |
| claim_probability | 0.68 | The specific claim that entry 172 records a Pulgar/Arriagada birth is probable from the chunk and image, but not canonical-proof-ready until conversion QA resolves the derivative conflict. |
| relevance_level | high | The entry directly concerns Pulgar and Arriagada names and a parent-child cluster relevant to the local Pulgar-line staging. |
| relevance_confidence | 0.90 | The surname and parent-child content make the family-line relevance clear, even though broader identity bridges are unsupported. |
| canonical_readiness | hold_for_conversion_qa | No promotion or canonical attachment should occur before targeted conversion QA. |

## Evidence Strengths

- The page image visibly shows entry 172 on page 58 as a Pulgar/Arriagada birth entry, matching the chunk's broad identity reading rather than the assigned converted Markdown's `José Francisco` / `Oswaldo Gomez` cluster.
- The chunk gives a coherent civil-registration row: registration date, child name and sex, birth date and place, father, mother, parents' residence, informant, and official signature.
- The source packet accurately flags the conversion conflict and preserves uncertainty around the father field instead of forcing a canonical reading.
- The staged identity analysis is appropriately conservative: it recommends `hold_for_conversion_qa`, separates anti-conflation checks from proof, and does not promote Dario-related bridges from surname context alone.

## Review Findings

- Literal support for child identity: supported at review level by the chunk and visible page image as `Jose del Carmen Segundo Pulgar Arriagada`, male, entry 172, but held from canonical promotion due to derivative conversion conflict.
- Literal support for birth details: supported at review level by the chunk and image as 8 March 1888, 3 p.m., Calle de Valdivia; held pending conversion QA.
- Literal support for father: supported at review level as `Jose del Carmen Pulgar` with a possible final `S.` or unresolved mark; not ready for normalized father identity or relationship attachment.
- Literal support for mother: supported at review level as `Juana Arriagada de Pulgar`; not enough by itself to merge with other Juana candidates.
- Literal support for Dario/Arturo/Smith-related identity claims: absent. This entry should be used only as an anti-conflation or family-line lead until a separate identity-bearing bridge is found.

## Next Action

Keep the staged identity analysis on hold and send the source image, converted Markdown, and chunk to targeted conversion QA for entry 172. QA should decide the controlling row for entry 172 and explicitly record the father-field reading. After QA, rerun proof review for the child identity, birth facts, parent names, and any proposed parent-child relationship claims before any canonical promotion.
