---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525202146121
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
reviewed_sources:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

- Hold for conversion QA. The source image and assigned chunk support entry 172 as the Pulgar/Arriagada registration, but the assigned converted Markdown gives a different entry-172 family cluster. This is a controlling row/file-assignment conflict, not a name variant.
- The staged identity analysis accurately identifies the need to hold, but it misstates the current converted Markdown conflict. The staged draft says the converted Markdown records `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 20 February 1888 at `En Pellin`; the reviewed converted file instead records entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at `En esta`.
- The father's exact ending remains unresolved. The chunk reads `Jose del Carmen Pulgar S.` and the image visibly supports `Jose del Carmen Pulgar` with a possible suffix/mark, but this reviewer does not certify whether the final mark is `S.`, another suffix, or non-name notation.
- No canonical promotion should occur for child identity, birth facts, parent-child relationships, parent duplicate candidates, or any Dario-line bridge until targeted conversion QA reconciles the image, chunk, converted Markdown, and source-packet statements.
- The staged analysis cites existing wiki stubs as context. Those pages are not needed to prove this claim and should not be treated as source authority for promotion.

## Evidence Strengths

- The source image for page 58, entry 172 visibly supports a child named `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registered 7 April 1888.
- The assigned chunk matches the visible row: birth date `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and residence details on Calle de Colipi/Valdivia.
- The source packet correctly flags `conversion_confidence: mixed` and recommends `hold_for_conversion_qa`.
- The staged identity analysis correctly treats the conflict as material and rejects any Dario identity bridge from this entry.

## Scoring

| Dimension | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a strong direct source for the event, but the available image is a photographed two-page spread with handwriting and row alignment challenges. |
| conversion_confidence_score | 0.42 | Chunk and image agree on the Pulgar/Arriagada row, while the current converted Markdown assigns entry 172 to a different family cluster. |
| evidence_quantity_score | 0.70 | One direct source image plus chunk/source-packet derivatives; enough to identify the conflict, not enough to promote. |
| agreement_score | 0.46 | Source image, chunk, and source packet broadly agree; converted Markdown conflicts, and the staged draft misquotes that converted conflict. |
| identity_confidence_score | 0.66 | The Pulgar/Arriagada identity is likely for the visible row, but row/file-assignment and father-suffix uncertainty prevent proof-ready identity linkage. |
| claim_probability | 0.68 | Probable that entry 172 is the Pulgar/Arriagada birth registration if the image/chunk controls. Probability remains limited by derivative conflict. |
| relevance_level | 1.00 | Directly relevant to the staged draft's identity-conflict claim. |
| relevance_confidence | 0.98 | The reviewed files and page image are the exact sources referenced by the staged draft. |
| canonical_readiness | 0.10 | Hold. Requires targeted conversion QA and renewed proof review before promotion. |

## Claim Judgment

The staged draft's main proof conclusion is supportable as a hold: entry 172 has a material conversion conflict and should not be promoted. The strongest current reading is the Pulgar/Arriagada row visible in the source image and transcribed in the chunk, but the assigned converted Markdown still conflicts with that row and must be reconciled.

The staged draft should not be used as a literal final authority for the competing converted-reading details because it names a different converted cluster than the current converted Markdown actually contains. That discrepancy strengthens the need for QA and lowers agreement/conversion confidence.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned converted Markdown, assigned chunk, and source packet. QA should decide whether entry 172 is controlled by the Pulgar/Arriagada row or whether the converted Markdown/chunk assignment is wrong, and should certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review for identity, birth facts, and parent-child relationships.
