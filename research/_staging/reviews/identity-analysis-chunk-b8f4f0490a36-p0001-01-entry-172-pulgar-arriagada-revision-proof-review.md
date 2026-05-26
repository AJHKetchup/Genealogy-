---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md
reviewer: postconv-proof-review-20260526015453648
review_date: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- Hold for conversion QA: the referenced converted file and chunk disagree at the row level for entry 172. The chunk reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the current converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- Revise the staged analysis before canonical use: its description of the converted-file conflict appears stale. It says the converted Markdown reads `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born `En veinte de Febrero...`, place `En Pellin`; the current referenced converted file instead reads `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril...`, place `En esta`.
- Do not promote identity, birth, or parent-child relationship claims from this staged analysis while the assigned conversion and chunk remain unreconciled. This is a controlling-row conflict, not a spelling or normalization issue.
- Do not attach this record to any Dario identity cluster. The staged analysis is correct that the visible source and derivative texts reviewed here do not name Dario.

## Scores

- source_quality_score: 0.88
- conversion_confidence_score: 0.36
- evidence_quantity_score: 0.62
- agreement_score: 0.44
- identity_confidence_score: 0.74
- claim_probability: 0.78
- relevance_level: high
- relevance_confidence: 0.91
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The original source image is available at the path cited by the staged draft, source packet, converted file, and chunk.
- Visual review of page 58, entry 172 supports the chunk/source-packet identity cluster: child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and a father field beginning `Jose del Carmen Pulgar`.
- The staged analysis correctly identifies the major proof issue: derivative text attached to the same source and entry number is inconsistent with the Pulgar/Arriagada row and requires conversion QA before promotion.
- The civil birth register is a strong primary source type for a birth entry, declared parents, and the compareciente once the row assignment is reconciled.

## Review Judgment

The Pulgar/Arriagada identity cluster is probably supported by the visible source image, but it is not canonically ready because the workspace's assigned derivative conversion still gives a different entry 172. The current conflict lowers conversion confidence and agreement scores even though the source image itself is relevant and appears to support the staged identity direction.

The father field should remain bounded as an uncertain reading after `Jose del Carmen Pulgar` until conversion QA certifies whether the trailing mark is `S.`, another abbreviation, or an unresolved mark. The staged analysis appropriately avoids a Dario bridge; surname and family context alone are insufficient for any Dario merge or relationship jump.

## Next Action

Send this source set to targeted conversion QA. Reconcile `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md` against the source image for page 58, entry 172; correct the staged analysis's stale description of the converted-file conflict if this draft is reused. After QA, rerun proof review before promoting any identity, birth-fact, parent-child, or merge claim.
