---
type: proof_review
status: completed
role: claim_reviewer
worker: "postconv-proof-review-20260527201140294"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
reviewed_conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.82
conversion_confidence_score: 0.34
evidence_quantity_score: 0.46
agreement_score: 0.28
identity_confidence_score: 0.62
claim_probability: 0.78
relevance_level: high
relevance_confidence: 0.91
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Row Conflict Identity Analysis

## Blockers

1. The source image named in the manifest and derivatives is absent from this checkout, and the rendered page image path is also absent. I could not independently inspect physical entry `172`.
2. The reviewed derivatives remain materially incompatible. The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the current converted Markdown reads entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
3. The father field is not ready for canonical normalization. The available chunk text supports only the derivative reading `Jose del Carmen Pulgar S.`, while the staged draft correctly treats the terminal mark/suffix as unresolved for promotion.
4. No reviewed item for this task literally names `Dario`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, or `Dario Jose Pulgar-Arriagada` in entry `172`. Any Dario bridge would be an external identity inference and is not supported here.
5. Canonical promotion is blocked. The staged draft should not be promoted to claims, relationships, person pages, family pages, or other canonical locations until row-control QA resolves which derivative transcript controls entry `172`.

## Evidence Strengths

- The staged draft accurately identifies the central conflict: the assigned chunk/source packet and the current converted Markdown cannot both describe the same entry `172`.
- The source type is strong in principle. A civil birth registration, if verified against the image, could support a child identity, birth event, parent names, parental residence, and informant details.
- The Pulgar/Arriagada reading has direct derivative support from both the assigned chunk and the held source packet.
- The Burgos/de la Cruz reading has direct derivative support from the current converted Markdown, but conflicts with the assigned chunk, source packet, and the staged hold analysis.
- The staged draft properly avoids converting the Dario comparison into a relationship claim and correctly recommends `hold_for_conversion_qa`.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration is a high-quality source class, but the original image was unavailable for this review. |
| conversion_confidence_score | 0.34 | Conversion confidence is low because local derivatives disagree on entry `172` at the row/family level. |
| evidence_quantity_score | 0.46 | There are multiple local derivatives, but only one source event and no independently viewable image in this task context. |
| agreement_score | 0.28 | Agreement is poor between the assigned chunk/source packet and current converted Markdown. |
| identity_confidence_score | 0.62 | Moderate confidence that the staged analysis correctly frames the conflict; lower confidence for any specific canonical identity. |
| claim_probability | 0.78 | High probability that the correct review outcome is hold for conversion QA, not promotion. |
| relevance_level | high | The conflict directly affects Pulgar/Arriagada identity and relationship staging. |
| relevance_confidence | 0.91 | The reviewed files explicitly concern entry `172` and the Pulgar/Arriagada row-control problem. |
| canonical_readiness | hold_for_conversion_qa | Row control, source-image verification, and father-field boundary remain unresolved. |

## Claim-Level Findings

| Claim or hypothesis | Support | Risk | Probability | Readiness |
| --- | --- | --- | ---: | --- |
| Entry `172` may be the Pulgar/Arriagada birth row | Supported by assigned chunk and held source packet | Current converted Markdown gives a mutually exclusive Burgos/de la Cruz row; image unavailable | 0.72 | hold_for_conversion_qa |
| Entry `172` may be the Burgos/de la Cruz birth row | Supported by current converted Markdown | Conflicts with assigned chunk/source packet and staged row-control concern | 0.20 | not_ready |
| Father can be used canonically as `Jose del Carmen Pulgar S.` | Literal derivative support in chunk | Suffix/terminal mark not image-certified; staged draft flags unresolved boundary | 0.48 | hold_for_conversion_qa |
| Mother candidate `Juana Arriagada de Pulgar` is relevant if Pulgar row is confirmed | Supported by chunk/source packet | Blocked by row-control conflict and no image review in this task | 0.70 | hold_for_conversion_qa |
| Entry `172` supports a Dario-line identity bridge | No literal Dario support in reviewed files | Would be a surname/family-context inference only | 0.04 | not_ready |

## Verification Notes

- `Test-Path` returned false for `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.
- `Test-Path` returned false for `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`.
- The manifest exists and points to the same missing source/page-image paths.
- No external research was performed.
- No raw source, converted Markdown, chunk, source packet, staged identity analysis, or canonical wiki page was edited.

## Next Action

Keep the staged identity analysis at `hold_for_conversion_qa`. The next useful action is targeted row-control QA using the original image or rendered page image, with an explicit decision between the Pulgar/Arriagada and Burgos/de la Cruz entry-172 readings and an explicit father-field boundary for `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain marked form. Do not attach this entry to any Dario identity without separate Dario-bearing evidence.
