---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525162738001
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

1. Canonical promotion remains blocked by a material row-level conversion conflict. The chunk, source packet, and visible source image support entry 172 as a Pulgar/Arriagada row, while the current converted Markdown records entry 172 as `Jose Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`.
2. The staged identity analysis and conflict draft describe the converted-file conflict as `Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz`, but the reviewed converted file currently says `Jose Miguel` / `Oswaldo Bunster` / `Amelia de la Maza`. This does not remove the blocker; it means the conflict description itself needs QA refresh before reuse.
3. The exact father-name ending is still not ready for canonical use. The reviewed chunk reads `Jose del Carmen Pulgar S.`, but the source packet correctly preserves possible QA outcomes of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Parent-child relationship claims should remain held. The visible source and chunk support a likely child-parent cluster, but the derivative transcript disagreement must be resolved before canonical attachment to `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar`.
5. No Dario, Arturo, Smith, Dario Jose, Dario/Darío Pulgar Arriagada, passenger, occupational, Geneva, property, or later-life identity bridge is supported by this entry. Those hypotheses should remain anti-conflation checks only.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.84 | The source image is a civil birth register, a strong source class for birth and parent-name evidence. Image legibility is usable but not perfect at the father suffix. |
| conversion_confidence_score | 0.44 | The chunk/source-packet reading broadly matches the visible source image, but the assigned converted Markdown is a different row cluster. |
| evidence_quantity_score | 0.50 | Review used one source image, one chunk, one converted file, one source packet, one conflict draft, and the staged analysis; no independent corroborating record was in scope. |
| agreement_score | 0.52 | Source image, chunk, and source packet agree on the Pulgar/Arriagada row, but the converted file disagrees materially and the staged draft misstates the current converted-file row. |
| identity_confidence_score | 0.66 | The likely entry-172 subject is `Jose del Carmen Segundo Pulgar Arriagada`, but identity confidence is capped by conversion conflict and father-suffix uncertainty. |
| claim_probability | 0.70 | The claim that entry 172 is the Pulgar/Arriagada birth registration is probable from the source image and chunk, but not ready for canonical use. |
| relevance_level | high | If confirmed, the entry directly concerns Pulgar/Arriagada parent-child evidence. |
| relevance_confidence | 0.90 | Family-line relevance is clear from the names in the source image and chunk, even though broader Dario-line relevance is unsupported. |
| canonical_readiness | hold_for_conversion_qa | Keep all dependent claims, relationships, merges, and identity bridges out of canonical folders until targeted conversion QA resolves the row and father field. |

## Evidence Strengths

- The visible source image for page 58, entry 172 supports a Pulgar/Arriagada row rather than the current converted Markdown's `Jose Miguel` / `Oswaldo Bunster` / `Amelia de la Maza` row.
- The chunk provides a coherent civil-register entry with registration date, child name and sex, birth date and place, father, mother, parent residence, informant, and official signature.
- The source packet correctly treats the derivative disagreement as a conversion QA blocker and avoids forcing the father suffix into a canonical form.
- The staged identity analysis is appropriately conservative in its final recommendation: it keeps the item at `hold_for_conversion_qa` and does not promote Dario-related identity bridges from surname context.

## Review Findings

- Literal support for child identity: supported at review level by source image and chunk as `Jose del Carmen Segundo Pulgar Arriagada`, male, entry 172; held because the converted Markdown disagrees.
- Literal support for birth details: supported at review level as 8 March 1888, 3 p.m., Calle de Valdivia; held pending conversion QA.
- Literal support for father: supported at review level as `Jose del Carmen Pulgar` with unresolved final mark or suffix; not ready for normalized identity or relationship promotion.
- Literal support for mother: supported at review level as `Juana Arriagada de Pulgar`; insufficient by itself for merging with other Juana candidates.
- Literal support for Dario/Arturo/Smith-related identity claims: absent. This entry should not be used as a bridge to those identities without another identity-bearing source.

## Next Action

Keep the staged identity analysis at `hold_for_conversion_qa`. Send the source image, chunk, source packet, and converted Markdown to targeted conversion QA for entry 172. QA should identify the controlling entry-172 row, refresh the conflict description to match the current converted file if needed, and explicitly record whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review after QA before any canonical claim, relationship, parent merge, or wider Dario-line comparison is promoted.
