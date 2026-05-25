---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525203953502
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

- Revision blocker: the staged identity-analysis draft states that the assigned converted Markdown records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born `En veinte de Febrero...`, place `En Pellin`; the reviewed converted file currently records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril...`, place `En esta`. The staged draft therefore accurately identifies a row-level conflict in principle, but it misquotes the current converted-file conflict details.
- Conversion blocker: the chunk and visible source image support the Pulgar/Arriagada row for entry 172, while the converted file supports a different Oswaldo Burgos/Concepcion de la Cruz row for entry 172. This remains a conversion or file-assignment conflict, not a spelling variant.
- Father-field blocker: the chunk reads the father as `Jose del Carmen Pulgar S.`; the source packet preserves uncertainty as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Do not normalize this father name until targeted conversion QA certifies the final mark or suffix.
- Identity-risk blocker: no Dario individual appears in this entry. Shared Pulgar/Arriagada surname context is not evidence for a Dario bridge, merge, or relationship jump.
- Canonical-readiness blocker: no child identity, birth fact, parent-child relationship, parent merge, or Dario-line comparison from this staged draft is ready for canonical promotion.

## Evidence Strengths

- The source type is a civil birth registration and is directly relevant to the claimed child, birth, and parent facts if the row assignment is confirmed.
- The reviewed chunk gives a complete row for entry 172: `Jose del Carmen Segundo Pulgar Arriagada`, male, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- Direct image review supports the same broad Pulgar/Arriagada row visible on register page 58, entry 172, including the child name, parents, and Calle de Valdivia/Colipi context.
- The source packet correctly flags `conversion_confidence: mixed` and `promotion_recommendation: hold_for_conversion_qa`.

## Scored Judgment

| Dimension | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong source type; image quality is usable but not perfect for final suffix resolution. |
| conversion_confidence_score | 0.38 | Chunk/source-image support conflicts with the assigned converted Markdown, and the staged draft misquotes the converted-file contents. |
| evidence_quantity_score | 0.62 | One direct register row plus derivative chunk/source-packet evidence; no independent corroborating record reviewed for this task. |
| agreement_score | 0.42 | Source image and chunk agree broadly, but converted Markdown and staged conflict details disagree materially. |
| identity_confidence_score | 0.66 | Pulgar/Arriagada identity is plausible from the image/chunk, but the controlling conversion/file assignment is unresolved. |
| claim_probability | 0.64 | More likely than not that the intended row is the Pulgar/Arriagada entry, but not proof-ready until QA reconciles the converted file. |
| relevance_level | high | The row is directly relevant to the child and parent identity claims under review. |
| relevance_confidence | 0.94 | The staged draft, chunk, source packet, and image all concern register page 58, entry 172. |
| canonical_readiness | 0.10 | Hold. Requires targeted conversion QA and a corrected conflict summary before promotion review. |

## Claim-Level Assessment

| Claim Or Hypothesis | Probability | Readiness | Notes |
| --- | ---: | --- | --- |
| Entry 172 is the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.64 | Hold | Supported by chunk and visible source image; blocked by converted-file disagreement. |
| Father is `Jose del Carmen Pulgar S.`. | 0.52 | Hold | Chunk supports this reading, but source packet correctly preserves suffix uncertainty. |
| Father is a normalized `Jose del Carmen Pulgar` without suffix. | 0.45 | Hold | Plausible base-name reading, but normalization would overstep the reviewed evidence. |
| Mother is `Juana Arriagada de Pulgar`. | 0.64 | Hold | Supported by chunk and visible row; blocked only by controlling row conflict. |
| Assigned converted Markdown row is controlling for entry 172. | 0.28 | Hold | Converted file has a coherent but different row; requires QA to determine whether it is a wrong conversion, wrong page, or wrong file assignment. |
| Any Dario identity is directly supported or bridged by this entry. | 0.01 | Not ready | No Dario appears in the reviewed source context. |

## Relationship And Conflict Review

- Child-parent relationships for `Jose del Carmen Segundo Pulgar Arriagada` to `Jose del Carmen Pulgar S./[?]` and `Juana Arriagada de Pulgar` are relevant but must remain staged only.
- The conflict is material: the child, parents, birth date, birth place, and informant context differ between the Pulgar/Arriagada row and the converted Markdown row.
- The staged identity-analysis draft's anti-conflation guidance is appropriate: no Dario merge or bridge should be inferred from this entry.
- The staged identity-analysis draft should be revised or superseded to reflect the current converted Markdown's actual conflicting row details before any future proof promotion.

## Next Action

Keep this staged identity-analysis draft and all dependent claims at `hold_for_conversion_qa`. Run targeted conversion QA against the source image, converted Markdown, chunk, and source packet to decide the controlling entry-172 row and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review using the corrected conflict details.
