---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260530143222526"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Transcript Conflict

This review covers staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md`.

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`; no claim, relationship, merge, Dario-line attachment, or wiki update is ready from this draft.
- The original source image path `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` and page image path `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` are not present in this workspace, so visible row control cannot be certified here.
- The assigned chunk/source packet and the current converted Markdown materially disagree for entry `172`. This affects child name, parent names, birth date/time/place, and informant/declarant.
- The Pulgar/Arriagada reading is supported only by the assigned chunk and staged source packet. The Burgos/de la Cruz reading is supported by the current converted Markdown. Neither derivative layer can be promoted over the other without image-controlled QA.
- The father reading `Jose del Carmen Pulgar S.` remains bounded as derivative text; the terminal `S.` or mark must not be normalized or expanded without a visible source reread.

## Evidence Strengths

- The staged draft accurately identifies a material conflict rather than treating the disagreement as a name variant.
- The assigned chunk and source packet agree internally that entry `172` reads `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, born `Ocho de Marzo de mil ochocientos ochenta i ocho` at about three in the afternoon at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The current converted Markdown explicitly labels entry `172` as `Jose Miguel`, sex `Varon`, born `El seis de Abril de mil ochocientos ochenta i ocho` at ten at night in `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and declarant `Oswaldo Burgos`.
- The conversion review note correctly documents that source/page image absence prevents independent physical row certification.

## Scoring

| Dimension | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.42 | A civil birth register would normally be strong, but only conflicting derivative text is available in this review context. |
| conversion_confidence_score | 0.32 | The chunk and converted Markdown conflict on core identity fields, and the page image is missing. |
| evidence_quantity_score | 0.48 | Multiple derivative artifacts were available, but they derive from the same unresolved source target and conflict materially. |
| agreement_score | 0.30 | Assigned chunk and source packet agree with each other; current converted Markdown disagrees on the key row. |
| identity_confidence_score | 0.52 for Pulgar/Arriagada row control; 0.24 for Burgos/de la Cruz row control; 0.02 for any Dario attachment | Identity confidence is derivative-only and unresolved. The draft properly rejects Dario attachment. |
| claim_probability | 0.58 that the Pulgar/Arriagada row is the intended staged candidate; 0.24 that the current converted Burgos/de la Cruz row controls entry `172`; 0.88 that two derivative layers have been conflated or misaligned | Probabilities reflect staged-document support, not source-image proof. |
| relevance_level | high if the Pulgar/Arriagada row is later certified; low if the Burgos/de la Cruz row controls | Pulgar-line relevance depends entirely on row-control QA. |
| relevance_confidence | 0.72 for conditional relevance; 0.18 for present canonical use | The family relevance is plausible only under the Pulgar/Arriagada reading and cannot be used canonically now. |
| canonical_readiness | hold_for_conversion_qa | Not ready for promotion, relationship creation, merge, rename, or canonical wiki update. |

## Next Action

Keep the staged draft on hold. The next worker should restore or locate the original source image or certified page image, then compare physical entry `172` against the assigned chunk, source packet, conversion review note, and current converted Markdown. Only after row control is visually certified should proof review score the child, parents, birth event, informant, and any parent-child relationship claims.
