---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530031800451
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-postconv-identity-analysis-20260525210459114.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-postconv-identity-analysis-20260525210459114.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conflict

## Blockers

- The reviewed staged draft is `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-postconv-identity-analysis-20260525210459114.md`.
- The source image named by the staged draft and source packet was not available at the referenced path during this review, so I could not independently verify the handwriting from the image.
- The assigned chunk and assigned converted Markdown materially disagree for entry 172. The chunk reads the child as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the converted Markdown and page-level conversion job Markdown read the child as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This is not a spelling variant or identity-merge question. The conflict changes the child identity, parent identities, birth details, residence context, and potential family line.
- The staged draft's recommendation to hold for targeted conversion QA is supported. No child identity, parent-child relationship, parent candidate, merge, or Dario-line bridge should be promoted from this evidence.

## Evidence Strengths

- The source type is a civil birth registration, which would normally be strong direct evidence for a birth event and parent-child relationship if the row transcription were controlled.
- The staged draft accurately reports the derivative-file conflict: the chunk/source packet support a Pulgar/Arriagada row, while the converted Markdown supports a Burgos/de la Cruz row for the same entry number.
- The source packet explicitly flags low conversion confidence and requests targeted QA to decide the controlling row and father-field reading.
- The staged draft correctly avoids silently changing the Pulgar/Arriagada reading into Dario or using the surname overlap to bridge Dario-line identities.

## Scores

| factor | score / value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registration is a high-quality source type, but direct image inspection was unavailable in this review. |
| conversion_confidence_score | 0.25 | The assigned chunk conflicts with both the converted Markdown and page-level conversion job Markdown for the same entry number. |
| evidence_quantity_score | 0.45 | There are multiple derivative notes, but they derive from the same source assignment and disagree on the controlling row. |
| agreement_score | 0.20 | Agreement is poor across derivative transcriptions: chunk/source packet versus converted/page Markdown. |
| identity_confidence_score | 0.35 | The Pulgar/Arriagada family cluster may be relevant, but identity confidence is limited until row control is settled. |
| claim_probability | 0.40 | The draft's hold claim is well supported; the underlying Pulgar/Arriagada birth and parent claims are not proof-ready. |
| relevance_level | high | All reviewed files concern the assigned entry 172 conflict and exact staged draft. |
| relevance_confidence | 0.95 | Paths, chunk id, source packet, conflict draft, and page reference align with the assigned task. |
| canonical_readiness | hold_for_conversion_qa | Promotion would risk attaching the wrong child and parents from an unresolved row-level conflict. |

## Claim Review

- Literal support: supported for the existence of a derivative conflict. Not supported for canonical promotion of either the Pulgar/Arriagada or Burgos/de la Cruz row.
- Source reliability: potentially high because the underlying source is a civil registration, but reliability cannot be fully used until the correct row is certified against the image.
- Conversion confidence: low. The chunk and converted/page Markdown are mutually incompatible for entry 172.
- Claim confidence: moderate only for the procedural claim that this item must remain on hold; low for any identity or relationship claim.
- Identity risk: high. Promoting before QA could create a false child-parent relationship and wrong family-line attachment.
- Relationship jumps: blocked. Parent-child assertions and parent-candidate merges require targeted conversion QA first.
- Conflicts: material row-level conversion conflict, plus unresolved father-field reading in the Pulgar/Arriagada hypothesis.
- Relevance: high. The reviewed materials directly match the staged draft and task id.

## Next Action

Keep this staged draft on `hold_for_conversion_qa`. Targeted conversion QA should inspect the source image for page 58, entry 172, decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz, and certify the father field if Pulgar/Arriagada is confirmed. After QA, rerun proof review before any canonical identity, relationship, or Dario-line comparison is promoted.
