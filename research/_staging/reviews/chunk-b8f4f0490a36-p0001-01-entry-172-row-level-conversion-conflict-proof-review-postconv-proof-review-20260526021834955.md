---
type: proof_review
status: draft
role: claim_reviewer
worker: "postconv-proof-review-20260526021834955"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014144513.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014144513.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
created: "2026-05-26"
source_quality_score: 0.88
conversion_confidence_score: 0.42
evidence_quantity_score: 0.62
agreement_score: 0.38
identity_confidence_score: 0.70
claim_probability: 0.72
relevance_level: high
relevance_confidence: 0.94
canonical_readiness: 0.08
disposition: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

1. Row-control conflict remains unresolved. The staged identity analysis, source packet, assigned chunk, and visible page image support entry 172 as a Pulgar/Arriagada row, while the referenced converted Markdown records entry 172 as a Burgos/de la Cruz row.
2. The converted Markdown cannot be used as controlling support for the Pulgar/Arriagada claim set because it names a different child, parents, birth date, place, and informant for the same entry number.
3. The father field is not fully certified. The visible source supports the father beginning `Jose del Carmen Pulgar`, and the chunk transcribes `Jose del Carmen Pulgar S.`, but this proof review should not harden the trailing suffix beyond the visible support already flagged for targeted QA.
4. The staged draft does not support any merge or attachment to Dario candidates. Shared Pulgar/Arriagada surname context is relevant for anti-conflation only, not same-person proof.
5. Existing Jose/Juana wiki clusters are identity-risk context only. This draft does not prove that `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person, nor that every `Jose del Carmen Pulgar` reference is the same father.

## Evidence Strengths

- The source is a civil birth register page, a strong original-source type for birth, parent, residence, and informant claims when the row is controlled correctly.
- The source packet directly reports image-reviewed support for entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, son of a father beginning `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- The assigned chunk consistently transcribes entry 172 as the Pulgar/Arriagada birth row: registration on 7 April 1888, birth on 8 March 1888 about 3 p.m. at Calle de Valdivia, parents resident at Calle de Colipi, and informant `Ernesto Herrera L.`.
- Visual review of the referenced image agrees with the source packet and chunk at the row-control level: page 58, entry 172 is visibly the Pulgar/Arriagada row, not the Burgos/de la Cruz row in the converted Markdown.
- The staged draft correctly treats the conflict as a hold rather than promoting a canonical claim set.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration is high-quality direct evidence, reduced slightly by image legibility and need for certified row-control QA. |
| conversion_confidence_score | 0.42 | The chunk is coherent and image-aligned, but the converted Markdown materially contradicts it for the same entry number. |
| evidence_quantity_score | 0.62 | One original register image plus one chunk and one source packet support the Pulgar row; no independent corroborating source is supplied. |
| agreement_score | 0.38 | Agreement is strong among chunk, source packet, staged draft, and image, but weak across the conversion artifact set because the converted Markdown conflicts. |
| identity_confidence_score | 0.70 | Probable identity of the entry-172 child as `Jose del Carmen Segundo Pulgar Arriagada`, held below promotion level by conversion conflict and father-suffix uncertainty. |
| claim_probability | 0.72 | The Pulgar/Arriagada row is more probable than the Burgos/de la Cruz row for the visible image, but not yet canonical-ready. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada parent-child research if row QA certifies it. |
| relevance_confidence | 0.94 | The names and family terms are visibly and textually tied to the Pulgar/Arriagada cluster. |
| canonical_readiness | 0.08 | Hold. Do not promote until targeted conversion QA reconciles the converted Markdown and certifies the father-field reading. |

## Claim-Level Review

| Candidate claim | Probability | Review disposition |
| --- | ---: | --- |
| Entry 172 on the visible page is the Pulgar/Arriagada birth row. | 0.72 | Hold for conversion QA; supported by image, chunk, and source packet against converted Markdown. |
| Child is `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | Hold; likely visible and chunk-supported, but dependent on row-control QA. |
| Father is `Jose del Carmen Pulgar S.`. | 0.55 | Revise/hold; father begins `Jose del Carmen Pulgar`, but trailing suffix requires certification. |
| Mother is `Juana Arriagada de Pulgar`. | 0.72 | Hold; likely supported if Pulgar row is certified. |
| Informant is `Ernesto Herrera L.` and present at birth. | 0.68 | Hold; chunk and image support, but tied to row-control QA. |
| Entry-172 child is a Dario candidate. | 0.04 | Do not promote; no given-name, kinship, spouse, child, chronology, or document-subject bridge is supplied here. |
| Jose/Juana parent candidates are duplicate/variant identities. | 0.25 | Do not promote; needs separate identity proof after row-control QA. |

## Next Action

Run targeted conversion QA on the source image, converted Markdown, and assigned chunk to certify which row controls entry 172 and to record the father field only to the visible extent. After QA, rerun proof review for the child identity, birth facts, father, mother, informant, and any parent-identity comparisons. No canonical promotion, merge, rename, or Dario attachment should be made from this staged draft.
