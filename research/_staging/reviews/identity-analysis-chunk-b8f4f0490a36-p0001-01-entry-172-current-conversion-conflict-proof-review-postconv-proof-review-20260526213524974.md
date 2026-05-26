---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526213524974
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173036167.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173036167.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
created: 2026-05-26
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- Canonical readiness is blocked by a material row-level conflict. The staged draft, source packet, assigned chunk, and visible source image support entry `172` as a Pulgar/Arriagada birth registration; the current converted Markdown instead gives entry `172` as a Burgos/de la Cruz birth registration.
- The conflict is not a name variant or same-person problem. It changes the child, parents, birth date, birth place, informant, residences, and relationship candidates.
- The father reading is not fully certified. The visible source and chunk support at least `Jose del Carmen Pulgar`; the trailing character or mark after `Pulgar` remains unresolved and should not be normalized or expanded.
- No canonical claim, relationship, merge, or wiki update should be made from this draft until targeted conversion QA resolves why the current converted Markdown disagrees with the source image and chunk.

## Evidence Strengths

- The visible source image shows page 58, entry `172`, with a Pulgar/Arriagada row. It is consistent with the assigned chunk's row for `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888 at about 3 p.m. at Calle de Valdivia.
- The assigned chunk and source packet agree on the core Pulgar/Arriagada details: child `Jose del Carmen Segundo Pulgar Arriagada`, father at least `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The current converted Markdown is internally coherent but appears to describe a different image or row set: entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The staged identity analysis correctly treats this as a conversion-control conflict and preserves uncertainty rather than promoting a relationship or identity merge.

## Scored Judgment

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a high-value original source for birth and parent statements, but this review relies on one page image and does not resolve the conversion pipeline mismatch. |
| conversion_confidence_score | 0.42 | Image, chunk, and source packet agree on Pulgar/Arriagada, but the current converted Markdown is materially different, so the conversion set is not stable. |
| evidence_quantity_score | 0.58 | There is one direct source image plus two derivative local transcriptions supporting the Pulgar row; no independent second record is present. |
| agreement_score | 0.54 | Strong agreement among image, chunk, source packet, and staged analysis; severe disagreement with the current converted Markdown keeps the overall score moderate. |
| identity_confidence_score | 0.70 | The source-local child identity is probable if the image/chunk controls. Confidence is capped by the unresolved conversion conflict and father suffix uncertainty. |
| claim_probability | 0.72 | Entry `172` probably supports a Pulgar/Arriagada birth registration because the visible image aligns with the chunk, but the converted Markdown conflict prevents promotion-grade certainty. |
| relevance_level | high | Pulgar and Arriagada are directly named and are family-relevant terms in the staged packet. |
| relevance_confidence | 0.91 | Relevance is clear if this row controls; uncertainty concerns conversion control, not whether the names are relevant. |
| canonical_readiness | 0.08 | Hold for targeted conversion QA; do not promote claims or relationships yet. |

## Claim-Level Review

| claim | support | probability | review |
| --- | --- | ---: | --- |
| Entry 172 is the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by visible image, assigned chunk, and source packet; contradicted by current converted Markdown. | 0.72 | Hold for conversion QA. |
| Birth occurred 8 March 1888 at about 3 p.m. at Calle de Valdivia. | Supported by image/chunk/source packet under the Pulgar-row reading. | 0.70 | Hold; likely valid if Pulgar row is confirmed controlling. |
| Father was `Jose del Carmen Pulgar S.` | Chunk gives this reading; image supports at least `Jose del Carmen Pulgar` but trailing mark is not fully certified. | 0.60 | Revise/hold to visible extent only until father field QA. |
| Mother was `Juana Arriagada de Pulgar`. | Supported by image/chunk/source packet under the Pulgar-row reading. | 0.70 | Hold; likely valid if Pulgar row is confirmed controlling. |
| Informant was `Ernesto Herrera L.`, present at the birth. | Supported by image/chunk/source packet under the Pulgar-row reading. | 0.69 | Hold; likely valid if Pulgar row is confirmed controlling. |
| Pulgar/Arriagada row and Burgos/de la Cruz row are same-person or variant identities. | No literal support. | 0.02 | Reject as an identity explanation. Treat as conversion/source control conflict. |
| This entry attaches to Dario-line candidates. | No literal support in this source. | 0.01 | Do not attach without a separate proof-reviewed bridge. |

## Identity And Relationship Risk

- Identity risk is high if the Burgos/de la Cruz converted row and Pulgar/Arriagada image row are both treated as entry `172` facts.
- Relationship risk is severe because the father-child and mother-child claims change completely depending on which row controls.
- Merge risk is moderate for similarly named Pulgar/Juana candidates in other staged or canonical materials, but this draft supplies no independent bridge for those merges.
- Dario-line relevance remains only a protection warning. The entry does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or passenger Dario candidates.

## Next Action

Run targeted conversion QA against the source image, current converted Markdown, assigned chunk, and source packet for page 58 entry `172`. If QA confirms the image/chunk controls, revise the converted Markdown through the normal conversion QA workflow and rerun proof review on the reconciled row, especially the father field after `Pulgar`. Until then, keep this draft at `hold_for_conversion_qa` and do not promote any canonical claims or relationships.
