---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260525232021368"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230105907.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230105907.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged draft is correctly treated as a conversion-control conflict, but canonical use remains blocked because the referenced converted Markdown assigns entry 172 to `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, while the chunk and visible source image assign entry 172 to `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- The current converted file is not reliable for entry 172 row facts until targeted conversion QA replaces or explicitly explains the conflicting Burgos/de la Cruz reading.
- Parent-child relationships, parent identity merges, child identity claims, birth facts, and Dario/Pulgar comparison claims should remain held. The record does not name Dario, Arturo, Smith, Pulgar-Smith, Dario Jose, or a later descendant bridge.
- The father suffix should remain guarded as `Jose del Carmen Pulgar S.` from the chunk/source image reading, with no expansion of `S.` unless a later QA note certifies it.

## Scores

| Metric | Score | Review Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is a strong primary source type, and the page image is available. |
| conversion_confidence_score | 0.40 | The chunk matches the image on the controlling row, but the current converted Markdown materially conflicts with it. |
| evidence_quantity_score | 0.64 | One directly relevant civil-register image plus two derivative readings; quantity is limited and the derivatives disagree. |
| agreement_score | 0.46 | Staged draft, source packet, chunk, and source image agree on the Pulgar/Arriagada row, but the converted file disagrees on every main identity field. |
| identity_confidence_score | 0.58 | The image supports the Pulgar/Arriagada entry-172 identity more strongly than the converted file, but the conversion-control conflict prevents certification. |
| claim_probability | 0.78 | Probability that entry 172 on page 58 is the Pulgar/Arriagada row after visual review; not high enough for promotion while the canonical converted file remains inconsistent. |
| relevance_level | direct | The staged draft directly addresses the assigned entry-172 row conflict. |
| relevance_confidence | 0.99 | All reviewed files point to the same entry number, page, and conflict. |
| canonical_readiness | hold | Do not promote until conversion QA resolves the converted-file conflict and certifies the father field. |

## Evidence Strengths

- The source image visibly places entry `172` on page 58 in the Pulgar/Arriagada row position. The visible row supports the child name `Jose del Carmen Segundo Pulgar Arriagada`, male sex, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date `Ocho de Marzo`, birth place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The chunk and source packet are consistent with that visible source-image reading.
- The staged identity-analysis draft accurately frames the Burgos/de la Cruz text as a row-control conversion conflict rather than a name variant or duplicate-person hypothesis.
- The anti-conflation warnings are appropriate: the entry is relevant to Pulgar/Arriagada family research only as a held lead and provides no direct Dario-line identity proof.

## Review Judgment

The staged draft is supported as a hold/revise conflict analysis. The Pulgar/Arriagada reading has stronger literal support than the Burgos/de la Cruz reading because it is visible in the source image and matches the chunk/source packet. However, the proof-review outcome must remain `hold` because the referenced converted Markdown, which is part of the source chain, still records a different entry-172 family.

No canonical child identity, birth event, parent-child relationship, parent merge, or Dario-line comparison should be promoted from this staged draft.

## Next Action

Run targeted conversion QA for the source image, converted Markdown, chunk, and source packet. The QA note should certify the controlling entry-172 row and update or flag the converted Markdown conflict. After that, rerun proof review on the accepted row facts and any proposed Pulgar/Arriagada relationship claims.
