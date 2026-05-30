---
type: proof_review
status: revise
role: claim_reviewer
worker: postconv-proof-review-20260530064416933
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_conversion_qa_note: "research/_staging/tasks/conversion-review-note-chunk-b8f4f0490a36-p0001-01-entry-172-rowcert-postconv-evidence-extraction-20260527220554472.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: "revise_before_claim_promotion"
---

# Proof Review: Entry 172 Row-Control Identity Analysis

Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md`.

## Blockers

1. The staged draft's main recommendation, `hold_for_conversion_qa`, is now stale against the later local conversion QA note `research/_staging/tasks/conversion-review-note-chunk-b8f4f0490a36-p0001-01-entry-172-rowcert-postconv-evidence-extraction-20260527220554472.md`. That QA note certifies physical entry `172` as the Pulgar/Arriagada row, not the Burgos/de la Cruz row.
2. The staged draft repeats the chunk's father reading `Jose del Carmen Pulgar S.` as a candidate. The conversion QA note explicitly certifies the father field only as `Jose del Carmen Pulgar` and says the suffix after `Pulgar` is not sufficiently visible for promotion.
3. The original source image path recorded in the packet, `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, did not resolve in this checkout during review. I therefore rely on the local derivative files plus the image-reviewed conversion QA note, not on fresh visual inspection.
4. No same-person, parent-merge, or Dario-line bridge claim is supported by this staged draft. Shared Pulgar/Arriagada name context is not enough to attach the row to any Dario Pulgar identity cluster.

## Evidence Strengths

- The assigned chunk and source packet agree that entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with mother `Juana Arriagada de Pulgar` and informant `Ernesto Herrera L.`.
- The conflict draft correctly treats the Burgos/de la Cruz versus Pulgar/Arriagada mismatch as a conversion row-control conflict, not a spelling variant or identity variant.
- The later conversion QA note directly addresses the requested row-control question and preserves a strict father-field boundary: promote only `Jose del Carmen Pulgar` from this source unless a later source-image review supports more.
- The staged draft correctly blocks Dario-line conclusions and parent-candidate merges.

## Scores

| claim reviewed | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| Physical entry 172 is the Pulgar/Arriagada birth row, not the Burgos/de la Cruz row. | 0.86 | 0.72 | 0.74 | 0.70 | 0.76 | 0.82 | high | 0.94 | revise_before_claim_promotion |
| Child name from entry 172 is `Jose del Carmen Segundo Pulgar Arriagada`. | 0.86 | 0.70 | 0.70 | 0.68 | 0.72 | 0.78 | high | 0.94 | revise_before_claim_promotion |
| Mother in entry 172 is `Juana Arriagada de Pulgar`. | 0.86 | 0.70 | 0.70 | 0.68 | 0.72 | 0.78 | high | 0.93 | revise_before_claim_promotion |
| Father in entry 172 should be promoted as `Jose del Carmen Pulgar S.`. | 0.86 | 0.58 | 0.55 | 0.40 | 0.45 | 0.32 | high | 0.86 | hold_for_literal_father_suffix |
| Father in entry 172 can be used literally as `Jose del Carmen Pulgar`. | 0.86 | 0.72 | 0.66 | 0.72 | 0.66 | 0.76 | high | 0.91 | revise_before_claim_promotion |
| This entry supports any Dario Pulgar bridge or identity merge. | 0.70 | 0.70 | 0.20 | 0.20 | 0.03 | 0.02 | low | 0.90 | not_ready |

## Judgment

The staged draft is broadly right about the risk profile, but its final blocker is superseded by later local conversion QA. It should not be promoted as written because it leaves row-control in `hold_for_conversion_qa` and allows an uncertified father suffix as an active candidate.

The appropriate scored outcome is `revise_before_claim_promotion`: prepare a fresh claim or relationship draft from the certified Pulgar/Arriagada row, keep the converted Markdown conflict documented, and limit the father field to `Jose del Carmen Pulgar`.

## Next Action

Revise or replace this identity-analysis draft before any canonical update. The next draft should cite the conversion QA note, state that entry `172` is image-certified as the Pulgar/Arriagada row, avoid promoting `Pulgar S.`, and keep all Dario-line and parent-merge claims out of scope unless supported by separate proof-reviewed evidence.
