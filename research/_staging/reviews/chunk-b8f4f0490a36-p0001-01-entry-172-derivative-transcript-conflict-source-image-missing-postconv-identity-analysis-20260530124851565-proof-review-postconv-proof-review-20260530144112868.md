---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530144112868
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Transcript Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md`.

## Blockers First

1. Do not promote this item to canonical claims, relationships, merges, or wiki pages. The expected source image and conversion-job page image are absent in this workspace, so physical row control for entry `172` cannot be independently certified.
2. The assigned chunk/source packet and current converted Markdown materially conflict. The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted Markdown reads entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
3. The conflict is identity-bearing, not a spelling or formatting variant. Child name, parent set, birth date/time/place, and informant differ.
4. The father suffix or terminal mark in `Jose del Carmen Pulgar S.` remains derivative-only. It must not be normalized or expanded without visible-source support.
5. No Dario-line attachment is supported by this staged draft. The reviewed evidence does not name Dario, Arturo, Smith, a spouse, child, occupation bridge, later residence, or other same-person connector.

## Evidence Strengths

- The assigned chunk and source packet agree internally on the Pulgar/Arriagada reading for entry `172`: registration date `Siete de Abril de mil ochocientos ochenta i ocho`; child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; birth `Ocho de Marzo de mil ochocientos ochenta i ocho`, about three in the afternoon, `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- The converted Markdown clearly preserves the competing Burgos/de la Cruz reading for entry `172`: child `Jose Miguel`; birth `El seis de Abril de mil ochocientos ochenta i ocho`, about ten at night, `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.
- The prior conversion review correctly identifies the source-image and page-image absence and recommends `hold_for_conversion_qa`.
- If later image QA certifies the Pulgar/Arriagada row, the civil birth register would be relevant evidence for a narrow birth-registration and parent-child claim. That relevance is conditional on row-control resolution.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 7/10 for the underlying civil birth register type; 3/10 for this reviewed derivative-only state |
| conversion_confidence_score | 3/10 |
| evidence_quantity_score | 4/10 |
| agreement_score | 3/10 overall; 8/10 within the assigned chunk/source-packet pair only |
| identity_confidence_score | 5/10 for a Pulgar/Arriagada candidate row; 2/10 for a Burgos/de la Cruz controlling-row alternative; 0.5/10 for any Dario identity attachment |
| claim_probability | 0.60 that the assigned Pulgar/Arriagada row is the intended staged evidence; 0.25 that the converted Burgos/de la Cruz row controls entry `172`; 0.85 that a derivative row/provenance mismatch exists; 0.03 or lower for Dario same-person relevance |
| relevance_level | high if the Pulgar/Arriagada row is certified; low if the Burgos/de la Cruz row is certified |
| relevance_confidence | 0.70 for conditional Pulgar-line relevance; 0.20 for current canonical relevance |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged identity analysis is supported as a hold judgment. It accurately treats the evidence as an unresolved derivative-transcript conflict and does not supply enough verified source control for canonical promotion.

The assigned chunk and source packet can support only a staged, conditional Pulgar/Arriagada candidate. The current converted Markdown supplies a directly conflicting Burgos/de la Cruz candidate for the same entry number. Because neither available derivative layer can be checked against the missing image here, proof cannot select one as the canonical reading.

## Next Action

Keep this draft on `hold_for_conversion_qa`. A conversion-QA worker must restore or locate the original source image or certified page image and reread physical entry `172` against both derivative texts. After that, proof review should score only the certified literal readings for child name, birth event, father, mother, informant, and any parent-child relationship. No Dario-line comparison, merge, or relationship claim should proceed from this item without separate identity-bridge evidence.
