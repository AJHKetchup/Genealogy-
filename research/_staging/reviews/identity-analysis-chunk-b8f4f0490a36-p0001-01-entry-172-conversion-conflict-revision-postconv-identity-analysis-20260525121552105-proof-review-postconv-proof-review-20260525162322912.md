---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525162322912
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers First

1. The staged identity analysis is correct that promotion must be held, but it misstates the conflicting converted-file row. The referenced converted Markdown records entry 172 as `Jose Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`, born `veinte i seis de Marzo` in `En esta Subdelegacion`; the staged draft instead says `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`.
2. The converted Markdown and the chunk/source packet still identify different entry-172 families. The chunk and visible source image support a Pulgar/Arriagada row for entry 172; the converted file supports a Bunster/de la Maza row. This is a row-level conversion or file-assignment conflict, not a name variant.
3. The exact father-name ending remains insufficiently settled for canonical use. The source packet properly preserves possible QA outcomes for `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain reading.
4. No Dario-line bridge is supported by this entry. The reviewed evidence does not name Dario, Dario Arturo, Dario Jose, Dario/Dario Pulgar Arriagada, Smith, passenger travel, or later identity anchors.
5. Existing derivative wiki or staging context should not be used as independent corroboration while this conversion conflict remains unresolved.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md`.
- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source class is strong: a civil birth registration page is direct evidence for a child birth entry, parent names, registration date, birth date, and residence fields when the row is correctly identified.
- The chunk and source packet are internally coherent for entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Visual inspection of the source image supports the chunk/source-packet family cluster for row 172 more than the converted Markdown's Bunster/de la Maza row.
- The staged identity analysis appropriately refuses same-person merges, parent-child promotion, and Dario-line promotion.

## Scores

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration is a high-quality source type, and the page image is available for verification. |
| conversion_confidence_score | 0.38 | The chunk/source packet and visible image align, but the referenced converted file is materially inconsistent and the staged draft misquotes that inconsistency. |
| evidence_quantity_score | 0.46 | There is one direct source image plus derivative transcripts; there is not an independent corroborating record for the identity bridge or parent merge. |
| agreement_score | 0.42 | Chunk/source packet/image broadly agree on Pulgar/Arriagada, but the converted file disagrees on the controlling row. |
| identity_confidence_score | 0.68 | Probable for the row being a Pulgar/Arriagada registration after visual check, but not ready for canonical identity action until conversion QA resolves the row conflict. |
| claim_probability | 0.68 | The claim that entry 172 is the Pulgar/Arriagada birth registration is more likely than not, but remains held by conflicting conversion evidence. |
| relevance_level | high | If confirmed, the entry directly concerns Pulgar/Arriagada parent-child candidates. |
| relevance_confidence | 0.90 | Pulgar and Arriagada names appear in the chunk/source packet and visible row, so family relevance is high despite canonical unreadiness. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, merges, or Dario-line conclusions until targeted conversion QA supersedes or reconciles the converted file. |

## Review Judgment

Revise-and-hold. The staged draft's overall hold recommendation is supported, but its literal description of the converted-file conflict should be corrected in a future revision. The current evidence supports a probable Pulgar/Arriagada row, not a canonical claim.

## Next Action

Run targeted conversion QA against the source image, converted Markdown, and chunk for entry 172. The QA note should explicitly identify the controlling row and father field, and should correct the converted-file conflict description before any further proof review, canonical claim promotion, parent-child relationship promotion, person merge, or Dario-line comparison.
