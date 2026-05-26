---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526213943560
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173036167.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173036167.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
created: 2026-05-26
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- The staged draft is not ready for canonical promotion because its referenced converted Markdown and referenced chunk disagree on the controlling entry-172 row.
- The chunk, source packet, and visible source image support entry `172` on page 58 as a Pulgar/Arriagada birth registration. The converted Markdown instead records entry `172` as a Burgos/de la Cruz birth registration. These cannot be treated as variants of one person or family.
- The father field is not fully certified. The source image and chunk support at least `Jose del Carmen Pulgar`; the trailing mark after `Pulgar` remains uncertain and should not be expanded or normalized without targeted conversion QA.
- The claim is relevant to the Pulgar/Arriagada family cluster, but all dependent identity and relationship claims must remain held until conversion QA reconciles the converted file with the source image and chunk.

## Evidence Strengths

- The source image was checked directly. Page 58 row `172` visibly aligns with the Pulgar/Arriagada reading, including child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and birth details on 8 March 1888 at Calle de Valdivia.
- The assigned chunk gives a coherent literal table for entries 171-176 and records entry `172` as the Pulgar/Arriagada row.
- The source packet explicitly flags the same conversion conflict and preserves the needed uncertainty around the father's trailing letter or mark.
- The staged draft correctly treats this as a row-control/conversion problem rather than a same-person merge problem.

## Scored Judgment

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong original source for the event, but the visible image is a photographed two-page spread with some small handwriting. |
| conversion_confidence_score | 0.38 | The chunk is consistent with the image, but the canonical converted Markdown currently transcribes a materially different row for entry 172. |
| evidence_quantity_score | 0.62 | One original source image plus derivative chunk/source-packet agreement; no independent corroborating record in this review scope. |
| agreement_score | 0.54 | Source image, chunk, source packet, and staged draft agree on Pulgar/Arriagada, while the converted Markdown directly conflicts. |
| identity_confidence_score | 0.70 | Probable source-local identity for `Jose del Carmen Segundo Pulgar Arriagada` if the image/chunk row controls; capped by conversion conflict and father-field uncertainty. |
| claim_probability | 0.68 | The Pulgar/Arriagada reading is more likely for the visible entry-172 row than the converted Markdown reading, but the workflow needs conversion QA before promotion. |
| relevance_level | high | The row directly names Pulgar and Arriagada persons and is family-relevant. |
| relevance_confidence | 0.86 | Relevance is clear if the Pulgar/Arriagada row controls; uncertainty is about conversion control, not topical relevance. |
| canonical_readiness | 0.08 | Hold. Do not promote facts, relationships, merges, or wiki edits until the converted-file conflict is resolved and proof review is rerun. |

## Claim-Level Review

| claim | review judgment | probability | canonical readiness |
| --- | --- | ---: | ---: |
| Entry 172 records child `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by image/chunk/source packet; contradicted by current converted Markdown. | 0.70 | 0.10 |
| Child was born 8 March 1888 at about 3 p.m. at Calle de Valdivia. | Supported by image/chunk/source packet; held because row control is not conversion-stable. | 0.68 | 0.10 |
| Father is `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`. | Base name supported; trailing mark uncertain. Preserve uncertainty. | 0.62 | 0.06 |
| Mother is `Juana Arriagada de Pulgar`. | Supported by image/chunk/source packet if Pulgar row controls. | 0.69 | 0.10 |
| Informant is `Ernesto Herrera L.`, present at birth. | Supported by image/chunk/source packet if Pulgar row controls. | 0.67 | 0.10 |
| Pulgar/Arriagada row and Burgos/de la Cruz row are the same identity cluster. | Not supported; details are materially incompatible. | 0.02 | 0.00 |

## Identity And Relationship Risk

- Identity risk is high if the converted Markdown is used without QA, because it assigns entry `172` to a different child and parent set.
- Relationship-jump risk is high for any child-parent relationship promotion from this record before row-control QA.
- Same-person merge risk remains high for attaching this entry to Dario-line candidates or to other Jose/Juana Pulgar records without a separate bridge. This review found no source-local evidence naming Dario or proving a later-life identity bridge.
- Conflict severity is severe because the disagreement changes the child, father, mother, birth date, birth place, informant, and downstream family relevance.

## Next Action

Run targeted conversion QA against the source image, chunk, source packet, and converted Markdown for page 58 entry `172`. If QA confirms the Pulgar/Arriagada row, update or supersede the conflicting conversion and rerun proof review with the father field preserved only to the visible extent. Until then, keep this staged draft at `hold_for_conversion_qa` and do not promote it to canonical claims, relationships, or wiki pages.
