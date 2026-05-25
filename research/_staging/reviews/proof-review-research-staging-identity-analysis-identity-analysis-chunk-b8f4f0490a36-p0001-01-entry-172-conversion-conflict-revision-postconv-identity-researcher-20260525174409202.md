---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260525203301917
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525174409202.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525171911545.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
created: 2026-05-25
source_quality_score: 0.86
conversion_confidence_score: 0.38
evidence_quantity_score: 0.62
agreement_score: 0.44
identity_confidence_score: 0.58
claim_probability: 0.68
relevance_level: high
relevance_confidence: 0.82
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Analysis Conversion Conflict

## Blockers

- The assigned converted Markdown does not agree with the chunk, source packet, or visible source image for entry 172. It currently describes entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, whereas the chunk/source packet and source image support a Pulgar/Arriagada row. This is a derivative-transcription or file-assignment conflict and blocks canonical promotion.
- The staged identity analysis also cites a converted-file contradiction involving `José Francisco`, `Oswaldo Gomez`, and `Rosario de la Cruz de la Maza`; that exact reading is not present in the currently reviewed converted Markdown. The underlying blocker remains valid, but the review note should not treat the Gomez/de la Cruz wording as the current converted-file text.
- The father field in the Pulgar/Arriagada row is still not fully certified. The chunk reads `Jose del Carmen Pulgar S.`, and the source image is compatible with a final mark or suffix after `Pulgar`, but this review should not normalize it away.
- No Dario-line identity bridge is supported by this record. The visible entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario, Arturo, Smith, or a later professional/property context.
- Canonical readiness is `hold_for_conversion_qa`. Do not promote child identity, birth facts, parent-child relationships, parent merges, or Dario-line attachments until the converted Markdown is reconciled against the source image and chunk.

## Evidence Strengths

- The source image is a civil birth register page, a strong source type for birth registration, parent names, registration date, birth date, and place when the row is correctly identified.
- The assigned chunk and source packet agree that entry 172 is a Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, registered on 7 April 1888 and born on 8 March 1888 at `Calle de Valdivia`.
- Visual inspection of the source image supports the broad Pulgar/Arriagada reading for entry 172 and contradicts the currently assigned converted Markdown's Burgos/de la Cruz row.
- The staged identity analysis correctly treats this as a conversion conflict rather than as a same-person, duplicate-person, or spelling-variant problem.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is direct evidence for the event, though handwriting and row-level legibility keep it below perfect. |
| conversion_confidence_score | 0.38 | The chunk/source packet and image align broadly, but the assigned converted Markdown gives a different entry 172. |
| evidence_quantity_score | 0.62 | Review used the staged draft, source packet, chunk, converted file, and source image; no independent corroborating source was reviewed. |
| agreement_score | 0.44 | Chunk, source packet, and image agree against the converted Markdown; derivative layers are materially inconsistent. |
| identity_confidence_score | 0.58 | The Pulgar/Arriagada child identity is plausible from the image-backed chunk, but the record cannot yet support broader identity merges. |
| claim_probability | 0.68 | The reviewed evidence favors the Pulgar/Arriagada entry-172 hypothesis, but conversion QA is required before relying on it canonically. |
| relevance_level | high | `Pulgar` and `Arriagada` are family-relevant terms, and the record may affect child/parent candidate evidence. |
| relevance_confidence | 0.82 | Family relevance is clear if the Pulgar row is the controlling row; relevance to any Dario-line person remains low. |
| canonical_readiness | hold_for_conversion_qa | Reconcile the converted Markdown, chunk, and source image before promotion. |

## Claim Judgment

The staged identity analysis is substantially supported as a review of a conversion conflict. Its main conclusion, that entry 172 cannot be canonically promoted until row-level QA is complete, is correct.

The Pulgar/Arriagada reading is more probable than the current converted Markdown reading because the source image and chunk both support the Pulgar row. However, this proof review is not a conversion rewrite task. The visible source should be used by conversion QA to certify the controlling row and the father-field ending after `Pulgar`.

The Dario-related hypotheses should remain negative or lead-only. This entry does not provide a literal Dario name or a relationship bridge to a canonical Dario Pulgar identity cluster.

## Next Action

Run targeted conversion QA on `CHUNK-b8f4f0490a36-P0001-01` against the source image. Reconcile the assigned converted Markdown with the chunk/source packet, certify whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`, and then rerun proof review before any canonical promotion.
