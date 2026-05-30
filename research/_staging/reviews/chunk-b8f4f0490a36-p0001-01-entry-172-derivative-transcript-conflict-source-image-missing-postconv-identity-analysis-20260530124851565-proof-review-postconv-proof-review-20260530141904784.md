---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530141904784
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

This review covers only the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124851565.md`.

## Blockers First

1. Do not promote this item to canonical claims, relationships, person pages, family pages, or identity merges. The expected source image and conversion-job page image are not present, so physical row control for entry `172` cannot be certified from the visible source.
2. The referenced derivative texts materially conflict. The assigned chunk/source packet identify entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted Markdown identifies entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
3. The conflict is identity-bearing, not a spelling or name-normalization issue. Child name, parent set, birth date, birth time, place, and informant differ.
4. The father-field reading `Jose del Carmen Pulgar S.` remains derivative only. The suffix or terminal mark must not be normalized, expanded, or promoted without image-controlled rereading.
5. No Dario-line attachment is supported by this staged draft. None of the checked materials visibly name Dario, Arturo, Smith, a spouse, a child, an occupation bridge, or another independent identifier for a Dario candidate.

## Evidence Strengths

- The staged identity analysis accurately reports the conflict between the assigned chunk/source packet and the converted Markdown.
- The source packet and assigned chunk agree internally on the Pulgar/Arriagada row: entry `172`, registration on `Siete de Abril de mil ochocientos ochenta i ocho`, child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth on `Ocho de Marzo de mil ochocientos ochenta i ocho` at about three in the afternoon on `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The converted Markdown consistently provides the competing Burgos/de la Cruz row for entry `172`: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth on `El seis de Abril de mil ochocientos ochenta i ocho` at ten at night, place `En esta`, and informant `Oswaldo Burgos`.
- The conversion review note directly states that the source image and conversion-job page image were unavailable in that worker run. A fresh path check for this proof review also found both referenced image paths absent.
- The staged draft correctly treats row control as unresolved and recommends holding dependent claims for conversion QA.

## Scored Judgment

| Metric | Score / Judgment |
| --- | --- |
| source_quality_score | 0.78 for the underlying civil birth register type if image-certified; 0.35 for this review because only conflicting derivative transcripts are available |
| conversion_confidence_score | 0.25 overall; the derivative layers disagree on nearly every identity-bearing field and no image reread is available |
| evidence_quantity_score | 0.40; one targeted register entry is represented by two conflicting derivative readings plus a QA note |
| agreement_score | 0.20 overall; chunk and source packet agree with each other, but they materially disagree with the converted Markdown |
| identity_confidence_score | 0.55 for the Pulgar/Arriagada row as a staged derivative candidate; 0.25 for the Burgos/de la Cruz row as the controlling converted-file candidate; 0.02 for any Dario attachment |
| claim_probability | 0.62 that the assigned Pulgar/Arriagada row is the intended family-relevant candidate; 0.24 that the converted Burgos/de la Cruz row controls entry `172`; 0.88 that the task contains a real derivative row-control/provenance conflict; 0.03 or lower for Dario identity claims |
| relevance_level | high if Pulgar/Arriagada row is later certified; low if Burgos/de la Cruz row is later certified |
| relevance_confidence | 0.80 for relevance as a Pulgar-line lead under the Pulgar/Arriagada hypothesis; 0.15 for relevance under the Burgos/de la Cruz hypothesis |
| canonical_readiness | hold_for_conversion_qa / not_ready |

## Review Finding

The staged identity analysis is supported as a cautionary conflict analysis. It should remain staged because it correctly blocks canonical promotion while preserving the competing derivative readings.

The evidence does not support a canonical child identity, parent-child relationship, same-person merge, Dario-line attachment, or father-name normalization. The only well-supported conclusion at this point is that the entry `172` evidence stack has an unresolved derivative transcript conflict requiring image-controlled conversion QA.

## Next Action

Keep this item on `hold_for_conversion_qa`.

The exact next action is to restore or locate the original source image or certified page image for entry `172`, then compare the physical row against the assigned chunk and converted Markdown. The QA result should explicitly decide whether entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row and should bound the father-field reading before any proof-reviewed canonical claim or relationship is considered.
