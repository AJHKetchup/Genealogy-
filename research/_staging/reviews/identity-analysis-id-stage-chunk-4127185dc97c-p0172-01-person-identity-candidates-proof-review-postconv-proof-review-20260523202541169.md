---
type: proof_review
status: reviewed
role: claim_reviewer
worker: postconv-proof-review-20260523202541169
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
referenced_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
canonical_readiness: hold
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Page 172 Identity Candidates

## Blockers First

- The exact staged draft reviewed is `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md`.
- The current referenced chunk exists, but its `chunk_id` is `CHUNK-fb0d63eb2b71-P0172-01`, not the staged/source-packet `CHUNK-4127185dc97c-P0172-01`; the converted SHA in the chunk also differs from the source packet. This metadata mismatch blocks canonical use until reconciled.
- Entry 513 identity remains conversion-sensitive. The current chunk reads child `Isidoro del Carmen Jose`, father/declarant `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, and mother `Juana de Dios Amador`; prior local QA notes and the visible image support a Pulgar-family row but do not settle the child's full name or the mother's surname.
- Entry 514 identity and relationship fields remain conflicted. The current chunk reads child `Rigoberto Juan Bautista`, father `Alejandro Riquelme`, and mother/declarant `Mercedes Riquelme`; local QA notes and the visible image raise a serious father-field conflict, including a possible `se ignora` reading.
- Entry 515 is only partly visible in the page image and remains conflicted. The current chunk reads child `Rosa Elvira del Carmen` and father/declarant `Pedro Pablo Leiva`; prior QA notes and the visible right-column emendation support a competing `Neira` reading.
- No relationship or same-person bridge to any Dario/Pulgar canonical identity is supported by this staged draft. Do not merge or attach page-172 entries to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or any Jose/Juana parent candidate from this review alone.

## Evidence Strengths

- Source quality is high in kind: a civil birth-register page is direct evidence for birth registration facts when accurately transcribed.
- The image, source packet, converted file, and current chunk agree on the page frame: register page 172, year 1889, and entries 513, 514, and 515.
- The page image visibly supports the general table structure and several stable participants or contexts, including entry 513 as a Pulgar-family row, entry 514 as a Riquelme row with Mercedes Riquelme as a key participant, and entry 515 as a row requiring lower-field caution.
- The staged draft correctly recommends `hold_for_conversion_qa`; that recommendation is supported.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil register image is a strong source type, but current proof depends on disputed transcription layers. |
| conversion_confidence_score | 0.32 | Page frame is reliable; identity-critical names, surnames, father fields, dates, and lower entry 515 details remain conflicted. |
| evidence_quantity_score | 0.58 | There is one direct source image plus converted/chunk text and local QA notes, but no settled corrected transcription. |
| agreement_score | 0.36 | Evidence layers agree on page/entry presence but disagree on multiple person and relationship fields. |
| identity_confidence_score | 0.38 | The rows are real, but exact individual identities and parent-child assertions are not proof-ready. |
| claim_probability | 0.46 | Probable that the staged draft identifies the correct page and rows; low-to-moderate probability for exact identity claims as written. |
| relevance_level | direct | The evidence directly concerns the assigned staged identity draft and its cited page. |
| relevance_confidence | 0.99 | The reviewed source packet, chunk, converted file, and image all match the assigned page-172 evidence cluster. |
| canonical_readiness | hold | Conversion QA and metadata reconciliation are required before promotion. |

## Claim-Level Findings

| Claim / Hypothesis | Probability | Finding |
| --- | ---: | --- |
| Entries 513-515 are identity candidates from register page 172 | 0.74 | Supported as page/row candidates only. The page frame is strong, but exact identities are not settled. |
| Entry 513 is a Pulgar-family birth row | 0.66 | Plausible and visually supported at the row level; do not promote child name, maternal surname, or parent-child relationship until a targeted reread settles them. |
| Entry 513 father/declarant is Jose del Carmen Pulgar | 0.68 | Internally supported by the current chunk and visible row, but canonical matching still needs resolved child/mother readings and metadata cleanup. |
| Entry 513 mother is Juana de Dios Amador / Amagada / Arriagada de Pulgar | 0.34 | Mother given names and de Pulgar context are plausible, but the surname remains a blocked reading. Keep variants separate. |
| Entry 514 child and parent relationship readings are settled | 0.24 | Not supported. Father-field conflict is material, and the row should stay on hold. |
| Entry 514 Mercedes Riquelme is a row participant | 0.72 | Supported as a mother/declarant candidate, but relationship scope should not exceed the unsettled row evidence. |
| Entry 515 is a Leiva-row birth | 0.30 | Current chunk supports Leiva, but image/QA conflict with Neira blocks promotion. |
| Entry 515 is a Neira-row birth | 0.52 | Plausible because of visible emendation/QA notes, but not settled enough for canonical use. |
| Any entry links to a Dario/Pulgar canonical identity | 0.04 | Not supported by literal evidence in this staged draft. Treat only as anti-conflation context. |

## Conflicts And Identity Risk

- Identity risk is high for entry 513 if `Amador`, `Amagada`, and `Arriagada` are normalized by family context rather than source reading.
- Relationship risk is high for entry 514 because a named father versus an unknown-father reading would create opposite genealogical conclusions.
- Identity risk is high for entry 515 because `Leiva` versus `Neira` changes the person group and parentage.
- Source reliability is not the problem; conversion confidence and cross-layer agreement are the problem.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`.

Reconcile the metadata first so the source packet, staged draft, converted file, and current chunk use the same current chunk id and converted SHA. Then perform targeted side-by-side image QA for entries 513-515, focusing on entry 513 child name and mother surname, entry 514 father field and child name, and entry 515 Leiva/Neira plus the lower mother field. No canonical promotion, relationship creation, rename, or Dario/Pulgar merge is justified before that pass.
