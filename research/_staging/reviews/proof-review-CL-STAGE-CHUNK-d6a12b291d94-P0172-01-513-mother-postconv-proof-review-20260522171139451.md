---
type: proof_review
status: draft
role: claim_reviewer
worker: postconv-proof-review-20260522171139451
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-mother.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-mother.md
claim_type: identity
subject: Juana de Dios Amagada de Pulgar
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
chunk_id: CHUNK-d6a12b291d94-P0172-01
page_reference: page 172; entry 513
source_quality_score: 0.86
conversion_confidence_score: 0.48
evidence_quantity_score: 0.55
agreement_score: 0.34
identity_confidence_score: 0.52
claim_probability: 0.50
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 513 Mother

## Blockers

- The staged draft's referenced chunk path is unavailable in this workspace. A related page chunk exists under a different path, but this review does not treat that as a silent replacement for the missing referenced chunk.
- The derivative texts conflict materially. The staged claim and one available chunk read the mother as `Juana de Dios Amagada de Pulgar`; the assembled converted file reads `Juana de Dios Amador de Pulgar`.
- The source image supports the entry 513 mother line beginning `Juana de Dios` and ending `de Pulgar`, with `Chilena`, `Labores de su sexo`, and `Calle Colon`, but the intervening maternal surname is not clear enough for canonical spelling.
- The staged object says this person is the mother of `Tulio Cesar Luis Jose`. The visible image and derivative files do not agree on the entry 513 child name, and the reviewed image does not support promoting that exact child identity wording from this claim.

## Evidence Strengths

- The source is a contemporary civil birth register page for Los Anjeles/La Laja, 1889, with entry number 513 visible.
- The relevant row is internally coherent for the Pulgar household: father/declarant `Jose del Carmen Pulgar`, mother `Juana de Dios ... de Pulgar`, Chilean nationality, household/labors occupation, and `Calle Colon` domicile.
- The mother attributes other than the surname spelling are directly relevant and visibly located in the entry 513 parent column.

## Scored Judgment

| Factor | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil register image is a strong source type for a birth entry, though image contrast and handwriting reduce certainty for names. |
| conversion_confidence_score | 0.48 | Available derivative transcripts disagree on entry 513 names, dates, and the mother's surname. |
| evidence_quantity_score | 0.55 | One direct register entry supports a mother field, but only one image/transcription set is available and the key surname is contested. |
| agreement_score | 0.34 | Staged draft, available chunk, converted Markdown, source packet, and image review are not aligned on the child name or mother surname. |
| identity_confidence_score | 0.52 | `Juana de Dios ... de Pulgar` is likely the mother in entry 513, but `Amagada` is not secure and the linked child identity is unstable. |
| claim_probability | 0.50 | The broad mother-row claim is plausible; the exact staged identity string and mother-of-child wording are not promotion-ready. |
| relevance_level | high | The claim directly concerns the mother field in entry 513. |
| relevance_confidence | 0.90 | The reviewed evidence is the same register page and row cited by the staged draft. |
| canonical_readiness | hold_for_conversion_qa | Requires targeted image/conversion review before canonical promotion. |

## Review Decision

`hold_for_conversion_qa`. Do not promote the staged claim as written. A safer revised evidence statement would preserve only what the visible source supports: entry 513 names the mother as `Juana de Dios [surname uncertain] de Pulgar`, Chilean, occupied in household/labors, domiciled at `Calle Colon`; the exact maternal surname and exact child name require targeted review.

## Next Action

Request targeted conversion QA on entry 513's child-name field and mother-surname line, preferably from a focused crop of the parent/name columns. Keep the staged claim out of canonical claim, relationship, and person/family pages until the image-sensitive names are reconciled.
