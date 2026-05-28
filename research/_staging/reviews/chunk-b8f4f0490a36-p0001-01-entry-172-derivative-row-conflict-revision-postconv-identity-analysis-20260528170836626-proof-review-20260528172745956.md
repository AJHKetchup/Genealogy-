---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528172745956
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-identity-analysis-20260528170836626.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-identity-analysis-20260528170836626.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260528133324374.md"
conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-evidence-extraction-20260528133324374.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
source_quality_score: 0.86
conversion_confidence_score: 0.34
evidence_quantity_score: 0.62
agreement_score: 0.42
identity_confidence_score: 0.74
claim_probability: 0.76
relevance_level: high
relevance_confidence: 0.95
canonical_readiness: blocked
review_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Row Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-identity-analysis-20260528170836626.md`.
- Canonical readiness is `blocked`. The assigned converted Markdown records entry `172` as a Burgos/de la Cruz birth, while the assigned chunk, source packet, conflict note, and visible source image support physical entry `172` as a Pulgar/Arriagada birth registration.
- This review may affirm the row-control conflict but must not promote a child identity, parent-child relationship, father suffix, same-person merge, Dario-line attachment, or wiki update.
- The father should remain no stronger than `Jose del Carmen Pulgar` for proof purposes. The chunk transcribes `Jose del Carmen Pulgar S.`, but the source packet explicitly does not certify the terminal `S.` and the image does not make that suffix reliable enough for normalization.
- Same-person claims connecting the entry 172 child to any Dario, Arturo, Pulgar-Smith, or later Pulgar-Arriagada candidate are unsupported by this source.

## Evidence Strengths

- The source is a civil birth register image for Los Angeles, La Laja, Chile, dated 1888, with a clearly organized table and physical row numbers.
- The visible image shows entry `172` on page 58 as the middle row of the left page; the row contains `Jose del Carmen Segundo Pulgar Arriagada`, not the Burgos/de la Cruz child in the converted Markdown.
- The assigned chunk and source packet agree on the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m., birth place Calle de Valdivia, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and declarant `Ernesto Herrera L.`.
- The staged identity-analysis draft accurately keeps the evidence in hold status and correctly treats the problem as a derivative row-control conflict rather than a normal identity-variant issue.

## Probability And Evidence Scoring

| item | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil register image is a strong original-style source for birth registration facts, though image resolution and handwriting limit some suffix-level certainty. |
| conversion_confidence_score | 0.34 | The assigned converted Markdown is materially inconsistent with the image-reviewed row, assigned chunk, and source packet. |
| evidence_quantity_score | 0.62 | One source image plus derivative chunk/source packet is enough to identify the row conflict, but not enough to resolve broader identity bridges or suffix normalization. |
| agreement_score | 0.42 | Source image, chunk, source packet, and conflict note agree with each other, but the controlling converted Markdown disagrees sharply. |
| identity_confidence_score | 0.74 | The Pulgar/Arriagada child identity within the visible row is likely, but identity use remains bounded to this row until conversion QA resolves control. |
| claim_probability | 0.76 | Physical entry `172` is probably the Pulgar/Arriagada registration, but promotion remains blocked because the conversion derivative says otherwise. |
| relevance_level | high | Pulgar and Arriagada names are directly relevant to the staged family context. |
| relevance_confidence | 0.95 | Relevance is clear even though canonical use is blocked. |
| canonical_readiness | blocked | Requires targeted conversion QA and then rerun proof review before any canonical claim or relationship promotion. |

## Claim-Level Judgment

| claim or hypothesis | judgment | claim_probability | canonical_readiness |
| --- | --- | ---: | --- |
| Physical entry `172` is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by visible image, chunk, and source packet, but in conflict with converted Markdown. | 0.76 | blocked |
| Entry `172` is the Burgos/de la Cruz row from the converted Markdown. | Not supported by the visible source image for this assigned page/row; preserved only as the derivative conflict reading. | 0.18 | blocked |
| Father is `Jose del Carmen Pulgar`. | Plausible row reading if Pulgar row controls. | 0.70 | blocked |
| Father is `Jose del Carmen Pulgar S.` or an expanded Segundo-style father name. | Not certified. | 0.35 | blocked |
| Mother is `Juana Arriagada de Pulgar`. | Plausible row reading if Pulgar row controls. | 0.70 | blocked |
| Child is the same person as any Dario, Arturo, Pulgar-Smith, or later Pulgar-Arriagada candidate. | Unsupported relationship or identity jump. | 0.03 | blocked |

## Identity And Relationship Risk

- Identity risk is high for downstream use because the same entry number has two incompatible derivative readings.
- Relationship risk is high for parent-child promotion until conversion QA certifies the controlling row.
- The current evidence should not be used to merge `Jose del Carmen Segundo Pulgar Arriagada` with any Dario candidate or to merge `Juana Arriagada de Pulgar` with similarly named Juana candidates from other entries.
- The draft's existing hold recommendation is proportionate and should stand.

## Next Action

Run targeted conversion QA against the exact image, converted Markdown, and chunk for physical entry `172`. The QA result should certify which row controls, explain why the converted Markdown and chunk diverge, and state whether the father field is only `Jose del Carmen Pulgar` or whether any terminal suffix is visibly supported. After that, rerun proof review before considering any canonical promotion.
