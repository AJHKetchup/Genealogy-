---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526100535225
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526085239273.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526085239273.md"
canonical_readiness: hold
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.85
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

- The staged draft correctly identifies a controlling row-level conversion conflict. The assigned chunk and source packet present entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, while the current converted Markdown presents entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The source image visually supports the Pulgar/Arriagada row at page 58, entry 172, but the converted Markdown remains materially inconsistent and cannot be used as clean support until conversion QA resolves the mismatch.
- The father field is not fully certified. The chunk reads `Jose del Carmen Pulgar S.`, and the source packet flags the terminal `S.` or mark as needing targeted QA.
- Parent-child claims, father-name normalization, and any Dario-line bridge must remain held. The reviewed evidence supports a Pulgar/Arriagada candidate row, not a same-person or relationship bridge to any Dario candidate.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526085239273.md`
- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Evidence Assessment

The civil birth register image is a high-quality source type for identity, birth, and parent-name evidence. In the visible image, entry 172 on page 58 aligns with the Pulgar/Arriagada reading in the assigned chunk: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at Calle de Valdivia, with father beginning `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.

The staged draft's hold recommendation is supported. Its main limitation is not the source type but the derivative-text state: the current converted Markdown has a different row set and gives a Burgos/de la Cruz family for entry 172. That disagreement is severe enough to block canonical promotion even though the image and chunk favor the Pulgar/Arriagada row.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth register image is a strong primary source for the event if the row is certified. |
| conversion_confidence_score | 0.38 | Assigned chunk and image align, but the current converted Markdown conflicts at the row level. |
| evidence_quantity_score | 0.55 | One relevant register image plus derivative chunk/source-packet review; no independent corroborating source reviewed. |
| agreement_score | 0.42 | Chunk/source packet/image agree on Pulgar/Arriagada, but converted Markdown gives an incompatible family. |
| identity_confidence_score | 0.64 | The entry-172 Pulgar/Arriagada identity is plausible and visually supported, but held by conversion conflict. |
| claim_probability | 0.62 | More likely than the Burgos/de la Cruz derivative reading under the reviewed evidence, but not promotable. |
| relevance_level | high | If certified, the row is directly relevant to Pulgar/Arriagada family reconstruction. |
| relevance_confidence | 0.85 | The names `Pulgar` and `Arriagada` are directly present in the chunk and visible row. |
| canonical_readiness | hold | Targeted conversion QA and follow-up proof review are required before promotion. |

## Claim-Level Review

| Claim Or Finding | Probability | Review Judgment |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row. | 0.62 | Hold; supported by image/chunk/source packet, blocked by converted-file conflict. |
| Entry 172 is the Burgos/de la Cruz row in the current converted Markdown. | 0.20 | Revise/hold; present in derivative text but contradicted by the assigned image-aligned chunk. |
| `Jose del Carmen Segundo Pulgar Arriagada` is child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. | 0.54 | Conditional hold; depends on QA certifying the row and father field. |
| `Jose del Carmen Pulgar S.` should be normalized to `Jose del Carmen Pulgar`. | 0.35 | Hold; the visible source supports the beginning of the name but not a silent normalization of the terminal mark. |
| Entry 172 supports a Dario-line same-person or direct relationship bridge. | 0.05 | Not supported by the reviewed evidence. |

## Evidence Strengths

- The staged draft accurately treats the disagreement as a row-level conversion conflict rather than a spelling variant.
- The assigned chunk, source packet, and source image all support the existence of a Pulgar/Arriagada entry 172 candidate.
- The staged draft appropriately avoids promotion, merge, parentage normalization, and Dario-line attachment while the conversion conflict remains unresolved.

## Next Action

Run targeted conversion QA on the source image and derivative Markdown for page 58, entry 172. QA should explicitly decide the controlling row and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting any identity, birth, parentage, or relationship claim.
