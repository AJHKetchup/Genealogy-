---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260526022456172
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: "2026-05-26"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Row-control blocker remains active. The staged identity analysis, conflict draft, source packet, chunk, and visible page image support entry 172 as a Pulgar/Arriagada row, while the current converted Markdown records a materially different Burgos/de la Cruz row for entry 172.
2. Father-name certification is not complete. The source image and chunk support a father field beginning `Jose del Carmen Pulgar`; the suffix or trailing mark should remain unresolved among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA.
3. Identity and relationship promotion are blocked. This source is not ready for child identity, parent-child relationships, parent merges, Dario-line comparisons, or canonical facts while the controlling row and father suffix remain under QA.
4. The Dario candidate hypothesis is unsupported by this entry. The visible and staged evidence names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada.

## Evidence Strengths

- The source is a civil birth-registration image for Los Angeles, Chile, 1888, and is directly relevant to the asserted entry number.
- The chunk and source packet agree that entry 172 names child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, birth on 8 March 1888 at about 3 p.m., and place `Calle de Valdivia`.
- Direct image review supports the Pulgar/Arriagada row on page 58, entry 172. This makes the converted Markdown's Burgos/de la Cruz reading a conversion-control conflict, not an equal identity variant.
- The staged identity analysis correctly treats the Pulgar/Arriagada hypothesis as likely but not canonical-ready, and correctly rejects any Dario merge or attachment from this entry.

## Scored Judgment

| Metric | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong source for birth registration details, though proof is constrained by the conversion conflict. |
| conversion_confidence_score | 0.46 | Chunk and image agree on Pulgar/Arriagada, but the current converted Markdown contains a different row for entry 172. |
| evidence_quantity_score | 0.64 | One direct source image plus chunk, source packet, and conflict draft; no independent corroborating source reviewed for identity merges. |
| agreement_score | 0.72 | Staged draft, chunk, source packet, conflict draft, and image agree against the converted Markdown outlier. |
| identity_confidence_score | 0.76 | Probable that the row-level subject is `Jose del Carmen Segundo Pulgar Arriagada`; reduced by pending conversion QA and father suffix uncertainty. |
| claim_probability | 0.74 | The claim that entry 172 is the Pulgar/Arriagada row is probable on reviewed local evidence, but held pending targeted QA. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada birth and parentage candidates; relevant to Dario only as an anti-conflation checkpoint. |
| relevance_confidence | 0.91 | Pulgar and Arriagada are visible in the entry-172 row and repeated in the staged evidence. |
| canonical_readiness | hold | Not ready for canonical promotion until targeted conversion QA certifies row control and father-field reading. |

## Claim-Level Findings

| Claim Or Hypothesis | Probability | Review Disposition |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.74 | Hold for targeted conversion QA; likely, but not proof-complete. |
| Entry 172 is the Burgos/de la Cruz row recorded in the current converted Markdown. | 0.16 | Revise/hold as a conversion outlier; not supported by the reviewed image, chunk, source packet, or conflict draft. |
| Father is exactly `Jose del Carmen Pulgar S.`. | 0.58 | Hold. The beginning `Jose del Carmen Pulgar` is supported, but the suffix needs certification. |
| Mother is `Juana Arriagada de Pulgar`. | 0.78 | Probable after row-control QA; not canonical-ready before QA. |
| Child is the same person as any Dario candidate. | 0.04 | Do not promote. This source does not provide the necessary identity bridge. |
| Jose/Juana parent candidates are duplicates or variants of other canonical clusters. | 0.30 | Hold for separate identity proof after row-control QA; this entry alone does not prove a merge. |

## Source Reliability And Risk

- Source reliability: strong for the existence and content of a birth-register row once row control is certified.
- Conversion reliability: mixed. The chunk is consistent with direct image review, but the current converted Markdown is materially inconsistent.
- Identity risk: high if promoted prematurely, because the row conflict changes child, parents, birth date, birthplace, residence, and informant.
- Relationship risk: high for parent-child assertions and parent merges until the row and father suffix are certified.
- Relevance risk: low for Pulgar/Arriagada relevance, high for any attempted Dario attachment.

## Next Action

Run targeted conversion QA for the source image, converted Markdown, and chunk to certify the controlling entry-172 row and father-field reading. After QA, rerun proof review for the child identity, birth facts, father, mother, and informant. Do not promote this staged draft to canonical claims, relationships, wiki people, wiki families, or Dario-line identity work before that QA result exists.
