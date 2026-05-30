---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530032920647
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205450696.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205450696.md
reviewed:
  - research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205450696.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-markdown/page-0001.md
  - research/_staging/tasks/conversion-review-note-chunk-b8f4f0490a36-p0001-01-entry-172-image-reread.md
source_quality_score: 0.76
conversion_confidence_score: 0.30
evidence_quantity_score: 0.45
agreement_score: 0.38
identity_confidence_score: 0.50
claim_probability: 0.60
relevance_level: high_for_pulgar_arriagada_conflict_low_for_dario_identity
relevance_confidence: 0.82
canonical_readiness: hold_for_conversion_qa
created: 2026-05-30
---

# Proof Review: Entry 172 Row Conflict

This review covers only the staged draft `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205450696.md`.

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The assigned chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted Markdown and conversion-job page Markdown identify entry 172 as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The referenced source image path `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` was not available in this workspace pass. I could not independently certify the visible row from the image.
- The Pulgar/Arriagada reading is supported by the assigned chunk, source packet, and prior image-reread note, but it is not supported by the current converted Markdown or page Markdown. This is a row/source-assignment conflict, not a spelling variation.
- The father field remains unresolved at proof precision. The assigned chunk reads `Jose del Carmen Pulgar S.`, while the image-reread note says the field is readable as `Jose del Carmen Pulgar` and that a final `S.` is not clearly visible.
- No child identity, parent identity, child-parent relationship, parent-pair clue, Dario-line bridge, or canonical merge should be promoted from this draft until targeted conversion QA identifies the controlling row and certifies the father field.

## Evidence Strengths

- The staged draft accurately preserves the core conflict and does not over-promote the Pulgar/Arriagada row.
- The source type, if the image is recovered and confirmed, is strong: a civil birth registration is direct evidence for a birth event and named parents.
- The source packet and assigned chunk agree internally on the Pulgar/Arriagada row: registration date 7 April 1888, birth date 8 March 1888 at 3 p.m., birthplace Calle de Valdivia, child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The converted Markdown and conversion-job page Markdown agree internally on a different entry 172: child `Jose Miguel`, birth date 6 April 1888 at 10 p.m., father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.
- The prior image-reread note favors the Pulgar/Arriagada row for the child, mother, event details, informant, and official, while explicitly preserving the father-name suffix uncertainty.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.76 | Civil birth registration is high-quality direct evidence, but the image was unavailable for this review pass. |
| conversion_confidence_score | 0.30 | The converted Markdown and page Markdown conflict materially with the assigned chunk and source packet. |
| evidence_quantity_score | 0.45 | There are multiple derivative artifacts, but only one underlying source image and it could not be inspected here. |
| agreement_score | 0.38 | Evidence clusters agree within themselves but disagree across the controlling row. |
| identity_confidence_score | 0.50 | The Pulgar/Arriagada identity is plausible and locally supported, but the row conflict and father suffix block identity attachment. |
| claim_probability | 0.60 | The staged hold analysis is more likely than not correct because it matches the source packet, chunk, and prior image-reread note, but it remains unready for promotion. |
| relevance_level | high_for_pulgar_arriagada_conflict_low_for_dario_identity | Relevant to Pulgar/Arriagada parent and child claims; no literal Dario, Arturo, Smith, passenger, medical, or later-life bridge appears in the reviewed row evidence. |
| relevance_confidence | 0.82 | The relevance boundary is clear even though the row assignment remains unresolved. |
| canonical_readiness | hold_for_conversion_qa | Targeted QA must reconcile the row before canonical use. |

## Claim Probability

The staged draft's main claim should stand as a hold-level conflict analysis with `claim_probability: 0.60`. The probability that entry 172 is the Pulgar/Arriagada row is higher than the probability that it is the Burgos/de la Cruz row because the source packet, assigned chunk, and prior image-reread note align on Pulgar/Arriagada. That probability is not high enough for promotion because the current converted Markdown and page Markdown give a wholly different row and the cited image was not available for direct verification in this pass.

## Next Action

Run targeted conversion QA against the actual source image and the existing derivative files. The QA result should decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and if Pulgar/Arriagada controls, certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, relationship, or identity merge is promoted.
