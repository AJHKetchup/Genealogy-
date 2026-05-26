---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526100317893
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md
reviewed: 2026-05-26
canonical_readiness: hold_for_conversion_qa
claim_probability: 0.86
---

# Proof Review: Entry 172 Conversion Conflict

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. Do not promote any child identity, birth fact, parent-child relationship, parent identity merge, or Dario-line bridge from this draft.
- The current converted Markdown and the assigned chunk disagree at the row level for the same entry number. The converted file records entry `172` as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the chunk records entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The source image visibly supports the Pulgar/Arriagada row for page 58, entry `172`, but the father field ending remains uncertain enough that this review should not certify whether the father is exactly `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing wiki pages and other staged Dario/Pulgar identity contexts are not independent proof for this row. They must not be used to bootstrap a merge, relationship, or same-person conclusion.

## Evidence Checked

- Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md`.
- Referenced converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| Review Item | Score / Value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth-register image is a strong original-source class for birth, parent, informant, date, and place claims. |
| conversion_confidence_score | 0.38 | Current derivative artifacts conflict sharply; the chunk aligns with the visible page image, but the converted Markdown is materially wrong for entry `172`. |
| evidence_quantity_score | 0.62 | One source image plus derivative chunk/source packet support the conflict finding; this is enough for a hold judgment, not enough for canonical promotion while conversion QA remains open. |
| agreement_score | 0.42 | Source image, chunk, source packet, and conflict draft agree on Pulgar/Arriagada; the converted Markdown disagrees on every identity-bearing field. |
| identity_confidence_score | 0.66 | The identity analysis correctly treats the Pulgar child and Burgos child as incompatible rows, but cannot certify final identity facts until the conversion row conflict is resolved. |
| claim_probability | 0.86 | High probability that the staged draft's main claim is correct: this is a row-level conversion conflict requiring QA hold. |
| relevance_level | high | Pulgar and Arriagada names are directly relevant if the visible row controls. |
| relevance_confidence | 0.90 | Relevance is clear for Pulgar/Arriagada review, but not for any Dario-line merge or attachment. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical folders, relationship promotion, or identity merge. |

## Evidence Strengths

- The source image shows entry `172` on page 58 with the child name beginning `Jose del Carmen Segundo Pulgar Arriagada`, birth date `Ocho de Marzo`, location `Calle de Valdivia`, father beginning `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The assigned chunk and held source packet are materially consistent with that visible Pulgar/Arriagada row.
- The staged identity analysis correctly characterizes the issue as a derivative row-control conflict rather than a spelling variant, ordinary uncertainty, or same-person question.
- The draft appropriately blocks normalization of the uncertain father field and blocks any attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

## Conflicts And Risks

- Literal support conflict: the current converted Markdown does not support the Pulgar/Arriagada claims; it appears to represent a different row or an earlier erroneous conversion.
- Identity risk: promoting both readings would create incompatible child, parent, birth-date, birth-place, and informant facts for the same entry number.
- Relationship jump risk: the Pulgar child, father, and mother may be staged as candidates only; no parent-child relationship should be canonical until conversion QA certifies the controlling transcription.
- Dario-line risk: there is no direct support in this reviewed evidence for a same-person claim involving any Dario Pulgar identity.

## Next Action

Keep the staged identity analysis on hold and route `CHUNK-b8f4f0490a36-P0001-01` to targeted conversion QA. QA should reconcile the source image, assigned chunk, held source packet, and current converted Markdown, then certify the controlling row and father-field ending before any proof-reviewed promotion is attempted.
