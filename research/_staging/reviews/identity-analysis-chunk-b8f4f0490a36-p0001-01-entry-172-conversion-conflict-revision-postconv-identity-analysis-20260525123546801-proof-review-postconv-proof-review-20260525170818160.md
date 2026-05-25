---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525170818160
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525123546801.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525123546801.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
created: 2026-05-25
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The staged draft correctly treats this as a row-level conversion conflict and should not be promoted to canonical claims, relationships, or wiki pages.
- The referenced converted file and referenced chunk materially disagree for entry 172. The chunk gives a Pulgar/Arriagada birth row; the assembled converted file gives `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born in `Pellin`.
- The staged draft and source packet partly misdescribe the converted-file side of the conflict as `Emilia de la Cruz`, with different date/place details. That stale conflict description must be corrected by conversion QA or a revised staging pass before canonical use.
- The father-name ending after `Jose del Carmen Pulgar` remains uncertain. The chunk reads `Jose del Carmen Pulgar S.`, but proof review should preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted QA records the visible-source reading.
- Do not attach this entry to any Dario/Pulgar-Smith/Dario Pulgar Arriagada candidate. The source row reviewed here does not name Dario or supply a later-life identity bridge.

## Evidence Strengths

- The raw source image was present and visually reviewed. It supports page 58, entry 172 as the Pulgar/Arriagada row rather than the Gomez/de la Cruz/Maza row in the assembled converted Markdown.
- The referenced chunk agrees with the visible image on the main identity cluster: child `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source type is a civil birth register image, a strong primary source class for birth event, declared parent, residence, and informant facts when the row is correctly assigned and transcribed.
- The staged draft appropriately identifies high identity and relationship risk from derivative-transcript disagreement and keeps the analysis on hold.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image, primary for the event and declared parents. |
| conversion_confidence_score | 0.38 | Source image/chunk support one row; assembled converted Markdown supports a different row; father suffix unresolved. |
| evidence_quantity_score | 0.58 | One direct source image plus derivative chunk/source packet; no independent corroborating record reviewed. |
| agreement_score | 0.34 | High disagreement between converted file, chunk, and some staged/source-packet conflict wording. |
| identity_confidence_score | 0.72 | Pulgar/Arriagada child identity is visually and chunk-supported, but derivative conflict blocks canonical confidence. |
| claim_probability | 0.69 | Probable that entry 172 is the Pulgar/Arriagada row, subject to conversion QA reconciliation. |
| relevance_level | 0.95 | Highly relevant to Pulgar/Arriagada research if certified. |
| relevance_confidence | 0.86 | Relevance is clear from names in the image/chunk; Dario-line relevance remains only contextual, not probative. |
| canonical_readiness | 0.05 | Hold only; no promotion until targeted conversion QA resolves row assignment and father-field reading. |

## Claim Judgment

The staged identity analysis is supported as a hold note, not as canonical proof. The visible source image and assigned chunk support the Pulgar/Arriagada identity cluster, but the derivative evidence package is internally unstable because the assembled converted Markdown records a different entry 172 family and the staged/source-packet wording does not accurately match the current converted file.

The child identity and parent-child relationships should remain plausible image-supported leads only. The evidence is strong enough to justify targeted QA, but not strong enough for canonical promotion, merge decisions, or relationship assertions.

## Next Action

Send to targeted conversion QA. Reconcile the source image, assembled converted Markdown, chunk, and source packet for page 58 entry 172; correct the stale description of the converted-file conflict; and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review for the child identity, birth facts, father claim, mother claim, parent-child relationships, and any Pulgar-line comparison before promotion.
