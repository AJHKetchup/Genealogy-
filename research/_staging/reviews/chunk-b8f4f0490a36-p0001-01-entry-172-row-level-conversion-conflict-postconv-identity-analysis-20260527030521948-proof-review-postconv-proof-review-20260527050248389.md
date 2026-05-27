---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260527050121740
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030521948.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030521948.md
reviewed_status: hold_for_conversion_qa
source_quality_score: 0.89
conversion_confidence_score: 0.43
evidence_quantity_score: 0.66
agreement_score: 0.58
identity_confidence_score: 0.79
claim_probability: 0.87
relevance_level: high
relevance_confidence: 0.98
canonical_readiness: hold_for_conversion_qa
created: 2026-05-27
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The page image, assigned chunk, source packet, and targeted QA note support physical entry `172` as the Pulgar/Arriagada row, but the current converted Markdown still records entry `172` as a Burgos/de la Cruz row.
2. The disagreement is material. It changes the child, parents, birth date/time, birthplace/residence context, informant, and official-signature context; this cannot be treated as a name variant.
3. The father field remains bounded. The image and QA note support `Jose del Carmen Pulgar`; the chunk's terminal `S.` is plausible but not certified here, so it should not be promoted as part of the name without focused conversion QA.
4. No relationship or identity bridge to Dario, Arturo, Smith, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` is supported by this row. Any Dario linkage remains a separate proof problem.
5. Parent-candidate merges are not ready. This row can identify parent candidates named `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, but it does not prove that they are identical to every same-named or similar canonical/staged person.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030521948.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md`.
- Targeted conversion QA note: `research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| metric | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.89 | The cited source is a civil birth-register image with direct row evidence. Image quality is adequate for row identity, but handwriting and scale leave the father suffix unresolved. |
| conversion_confidence_score | 0.43 | The assigned chunk agrees with the visible Pulgar/Arriagada row, but the canonical converted Markdown materially disagrees for the same entry number. |
| evidence_quantity_score | 0.66 | One primary image plus the chunk, source packet, and QA note are enough to judge the conflict and row-control probability, but not enough for canonical promotion. |
| agreement_score | 0.58 | Image, chunk, source packet, QA note, and staged analysis align on the Pulgar/Arriagada row; the current converted file is the major dissenting derivative. |
| identity_confidence_score | 0.79 | Local identity confidence is moderate-high for entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`; broader same-person or lineage claims remain low. |
| claim_probability | 0.87 | The staged draft's central claim that this is a row-level conversion conflict is strongly supported. |
| relevance_level | high | The item is directly relevant to Pulgar/Arriagada family identity and has high risk of wrong canonical attachment if mishandled. |
| relevance_confidence | 0.98 | All reviewed files concern the same entry-number conflict and source image. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, identity merges, or wiki edits until conversion-control reconciles the converted Markdown and father-field uncertainty. |

## Evidence Strengths

- The page image visibly shows physical row `172` on page 58 as the row containing `Jose del Carmen Segundo Pulgar Arriagada`, with Pulgar/Arriagada parentage and informant `Ernesto Herrera L.`.
- The assigned chunk, source packet, QA note, and staged identity analysis consistently preserve the Pulgar/Arriagada row-control reading.
- The staged draft correctly treats the Burgos/de la Cruz text in the converted Markdown as a conversion-control conflict, not as competing evidence for the same child.
- The draft appropriately blocks Dario-related identity bridges and parent-candidate merges until separate proof exists.

## Next Action

Hold this staged draft for conversion QA. Conversion-control should reconcile or supersede the current converted Markdown so entry `172` matches the physical row, and should resolve whether the father field is only `Jose del Carmen Pulgar` or includes a certified terminal suffix. After that, rerun proof review before any canonical claim, relationship, person merge, or wiki update.
