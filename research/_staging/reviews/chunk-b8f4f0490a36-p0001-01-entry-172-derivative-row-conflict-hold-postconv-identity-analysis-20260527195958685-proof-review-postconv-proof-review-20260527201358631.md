---
type: proof_review
status: completed
role: claim_reviewer
worker: "postconv-proof-review-20260527201358631"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
reviewed_conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
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

# Proof Review: Entry 172 Derivative Row Conflict

## Blockers

1. The original image and rendered page image are unavailable in this checkout. `Test-Path` was false for both `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` and `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png`.
2. The derivative witnesses disagree at the row and family level. The assigned chunk/source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the current converted Markdown reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.
3. The father field cannot be normalized for canonical use from this task. The chunk has derivative text `Jose del Carmen Pulgar S.`, but the source image is missing and the staged draft correctly keeps the terminal mark/suffix unresolved.
4. No reviewed file literally names `Dario`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, or `Dario Jose Pulgar-Arriagada` in entry `172`. A Dario-line attachment would be an unsupported identity jump from this evidence set.
5. Canonical promotion remains blocked. This review does not support edits to `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or any other canonical location.

## Evidence Strengths

- The staged draft correctly identifies the controlling problem as a derivative row-control conflict rather than a normal name variant.
- The source class is strong in principle: a civil birth registration, once image-verified, could support birth identity, parent names, residence, and informant details.
- The Pulgar/Arriagada reading is directly supported by the assigned chunk and the held source packet.
- The Burgos/de la Cruz reading is directly supported only by the current converted Markdown and is mutually incompatible with the assigned chunk/source packet.
- The staged draft appropriately treats Dario comparisons as anti-conflation context and does not promote a Dario relationship or same-person claim.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil registration is a high-quality record type, but the image was not available for direct review. |
| conversion_confidence_score | 0.34 | The chunk/source packet and converted Markdown disagree on entry `172` names, parents, and dates. |
| evidence_quantity_score | 0.46 | Multiple local derivatives were available, but they all point back to one unavailable image and one conflicted event. |
| agreement_score | 0.28 | Agreement is low because the main derivatives describe different families for the same entry number. |
| identity_confidence_score | 0.62 | Moderate confidence that the staged analysis frames the conflict accurately; not enough confidence for a canonical identity decision. |
| claim_probability | 0.78 | The most probable claim is procedural: hold the item for conversion QA rather than promotion. |
| relevance_level | high | The conflict directly affects the Pulgar/Arriagada entry-172 identity and relationship candidates. |
| relevance_confidence | 0.91 | The reviewed files explicitly reference this staged draft, source packet, chunk, and converted file. |
| canonical_readiness | hold_for_conversion_qa | Source-image row control and father-field boundary remain unresolved. |

## Claim-Level Review

| Claim or hypothesis | Support | Risk | Claim probability | Canonical readiness |
| --- | --- | --- | ---: | --- |
| Entry `172` is the Pulgar/Arriagada birth row | Assigned chunk and source packet agree on this derivative reading | Current converted Markdown gives a different child and parents; no image available | 0.72 | hold_for_conversion_qa |
| Entry `172` is the Burgos/de la Cruz birth row | Current converted Markdown gives this reading | Conflicts with the assigned chunk/source packet and staged hold analysis | 0.20 | not_ready |
| The father can be canonically recorded as `Jose del Carmen Pulgar S.` | The chunk has this derivative text | Terminal mark/suffix is not image-certified | 0.48 | hold_for_conversion_qa |
| `Juana Arriagada de Pulgar` is the mother if the Pulgar row is confirmed | Chunk/source packet agree on this derivative reading | Blocked by derivative row conflict | 0.70 | hold_for_conversion_qa |
| Entry `172` supports a Dario identity bridge | No literal support in the reviewed evidence | Would require separate Dario-bearing evidence and relationship proof | 0.04 | not_ready |

## Next Action

Keep this staged identity analysis at `hold_for_conversion_qa`. The next action should be targeted row-control QA against the original image or rendered page image, with an explicit decision between the Pulgar/Arriagada and Burgos/de la Cruz readings and an explicit father-field boundary. Do not infer or promote any Dario-line relationship from entry `172` without separate identity-bearing evidence.

No external research was performed. No raw source, converted Markdown, chunk, source packet, staged identity-analysis draft, or canonical wiki page was edited.
