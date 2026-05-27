---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527193717013
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md"
reviewed_context:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict Revision

## Blockers

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525211124639.md`.
- The row-level conflict is real and material. The assigned chunk/source packet identify entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown identifies entry 172 as a Burgos/de la Cruz birth row.
- The cited source image path, `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, was not available at the referenced location during this review. I therefore could not independently certify the visible source image or resolve the row assignment.
- The staged draft's hold recommendation is supported. No child identity, birth fact, parent relationship, parent-candidate merge, or Dario-line bridge should be promoted from this proof state.
- The father field remains uncertified. It must not be normalized beyond the visible/QA-supported alternatives already stated in the staged work: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Scored Judgment

| item | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | A civil birth register would be a strong primary source, but the source image was unavailable for this review and the judgment depends on derivative files. |
| conversion_confidence_score | 0.25 | The chunk and converted Markdown disagree on the child, parents, birth date/time, place, and informant for the same entry number. |
| evidence_quantity_score | 0.45 | There are several local derivative artifacts, but they are not independent proofs and the controlling image could not be inspected. |
| agreement_score | 0.10 | The relevant derivative transcripts are in direct row-level disagreement. |
| identity_confidence_score | 0.30 | The Pulgar/Arriagada cluster is coherent inside the chunk/source packet, but identity confidence is blocked by row assignment uncertainty. |
| claim_probability | 0.55 | It is plausible that the staged conflict analysis correctly identifies a Pulgar/Arriagada row conflict, but the underlying entry facts remain unproved without image/QA reconciliation. |
| relevance_level | 0.85 | If the Pulgar/Arriagada row is controlling, the item is highly relevant to Pulgar/Arriagada identity and relationship work. |
| relevance_confidence | 0.65 | Relevance is clear for conflict handling, but lower for genealogical promotion because the row has not been certified. |
| canonical_readiness | 0.00 | Hold for targeted conversion QA; not ready for canonical claims, relationships, identities, or wiki updates. |

## Evidence Strengths

- The staged draft accurately preserves the two competing derivative readings rather than forcing a name correction.
- The assigned chunk and source packet agree with each other on the Pulgar/Arriagada reading: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The converted Markdown clearly conflicts with that reading: `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The staged draft correctly treats this as a conversion/row-control problem, not a spelling variant or same-person identity proof.
- The staged draft correctly blocks any bridge to Dario/Darío Pulgar identities because no reviewed local artifact for this row literally names Dario, Arturo, Smith, or a Dario/Darío variant.

## Review Decision

Hold the staged draft as `hold_for_conversion_qa`.

The conflict analysis is useful and materially supported as a conflict note, but the underlying genealogical claims are not proof-ready. The available evidence supports the proposition that there is a serious row assignment/conversion conflict; it does not support promotion of either the Pulgar/Arriagada facts or the Burgos/de la Cruz facts as settled entry-172 facts.

## Next Action

Run targeted conversion QA against the actual page image and the two derivative readings. The QA note should identify the controlling row for register page 58, entry 172, and certify the father field only to the extent visible. After that, rerun proof review before any canonical promotion or identity/relationship merge.
