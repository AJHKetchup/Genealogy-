---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525203040235
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525172756135.md"
reviewed_files:
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
canonical_readiness: hold
next_action: targeted_conversion_qa_then_revised_proof_review
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

- Conversion-control blocker: the visible source image and the assigned chunk broadly support entry 172 as a Pulgar/Arriagada row, but the current assigned converted Markdown is a conflicting derivative transcription for the same source image and entry range. It records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born April 6, 1888, in `En esta`.
- Draft-integrity blocker: the staged identity-analysis draft says the assigned converted Markdown records a different Gomez/de la Cruz de la Maza/Pellin row. That description is not what the current converted Markdown contains. The draft is directionally right that there is a row-level conversion conflict, but it should not be treated as a stable proof statement until the derivative-file history is reconciled.
- Father-field blocker: the source image supports a Pulgar father for the row, but the final mark or suffix after `Jose del Carmen Pulgar` remains insufficiently certified for canonical use. Do not normalize it to `Jose del Carmen Pulgar S.` or remove the possible suffix without targeted QA.
- Relationship blocker: child-parent claims for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar [?]`, and `Juana Arriagada de Pulgar` are plausible from the image/chunk, but they remain held because the controlling conversion layer is inconsistent.
- Identity-risk blocker: this draft gives no direct support for any Dario identity bridge. Shared Pulgar/Arriagada surname context is only a later review prompt, not relationship or same-person evidence.

## Evidence Strengths

- The source is a civil birth register image for Los Angeles, Chile, with register page 58 and entry 172 visible. This is a high-quality source type for birth, parent, registration-date, and residence claims once transcription is settled.
- The visible entry 172 row broadly aligns with the chunk reading: child `Jose del Carmen Segundo Pulgar Arriagada`, male; registration date April 7, 1888; birth date March 8, 1888; place `Calle de Valdivia`; father in the `Jose del Carmen Pulgar` form with unresolved ending; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- The staged draft appropriately treats the situation as a hold for conversion QA and warns against Dario-line conflation.
- The source packet preserves the right hard boundary: it stages the Pulgar/Arriagada row while explicitly flagging conversion confidence as mixed.

## Scores

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil registration image is directly relevant and visible; image quality is usable but not perfect for small suffix marks. |
| conversion_confidence_score | 0.38 | Chunk and image broadly agree, but the current converted Markdown conflicts and the staged draft describes a third derivative reading. |
| evidence_quantity_score | 0.54 | One direct source image plus derivative chunk/source-packet support; no independent corroborating source reviewed for this task. |
| agreement_score | 0.42 | Source image and chunk agree on the Pulgar/Arriagada cluster, while converted Markdown and staged-draft derivative description disagree. |
| identity_confidence_score | 0.62 | The child and parents are plausible for this row, but exact father form and conversion control remain unresolved. |
| claim_probability | 0.64 | Probability that entry 172 is the Pulgar/Arriagada birth row is moderate-high from the image/chunk, but not promotion-ready. |
| relevance_level | high | The staged draft directly concerns this entry and its identity conflict. |
| relevance_confidence | 0.96 | The reviewed files are the exact referenced staged draft, source image, chunk, source packet, conflict note, and converted file. |
| canonical_readiness | 0.10 | Hold. Do not promote claims or relationships until conversion QA resolves the controlling transcription. |

## Claim Judgment

The central staged conclusion, `hold_for_conversion_qa`, is supported. The proof review should not promote the Pulgar/Arriagada child identity, birth facts, parent-child relationships, parent identity candidates, or any Dario-line comparison from this draft.

The Pulgar/Arriagada row has real image-level support, so the staged draft should not be rejected as invented. However, the current converted Markdown is materially incompatible with the image/chunk for entry 172, and the staged identity-analysis draft's statement about the converted Markdown appears stale or based on a prior derivative state. That makes this a revise/hold item rather than canonical-ready proof.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, chunk, source packet, and conflict note. The QA note should explicitly decide the controlling entry-172 transcription and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review for the child identity, birth facts, parent-child relationships, and parent-candidate identity risks.
