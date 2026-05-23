---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260523190852354
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-bdb698de8106-p0001-01-identity-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-bdb698de8106-p0001-01-identity-candidates.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_expected: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_chunk_available: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
review_status: hold
canonical_readiness: hold
created_at: 2026-05-23T19:08:52Z
---

# Proof Review: bdb698de8106 Identity Candidates

## Blockers

- Canonical readiness is `hold`. Do not promote this staged identity analysis to canonical claims, relationships, wiki people, wiki families, or any Dario/Pulgar identity page.
- The staged draft's cited chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is still unavailable in this workspace. An alternate chunk exists under the certificate-no-513-codex chunk directory, but it carries `CHUNK-3d3ab761209f-P0001-01`, not the assigned `CHUNK-bdb698de8106-P0001-01`. This keeps citation lineage unstable.
- Entry 513 child identity is not settled. The converted file reads `Tulio Cesar Luis José`; the available alternate chunk reads `Pulgar Amagada / José Luis`; the source packet says visible image review found a Pulgar-surname child field with unresolved lines and final `José`. The image supports a Pulgar-line child field, but not a proof-ready normalized child name from this review alone.
- Entry 513 mother surname remains a material uncertainty. The converted file reads `Juana de Dios Amagada de Pulgar`, and the image appears closer to `Amagada` than to the staged draft's older `Amador` conflict wording, but this review should not silently normalize the surname or convert it to `Arriagada`.
- Entries 514 and 515 show broader page-level derivative conflicts. The converted file gives entry 514 father `Belisario Riquelme` and entry 515 father `Pedro Pablo Leiva`; the source packet and visible image support holding those readings because the image appears closer to entry 514 father `Se ignora` and entry 515 father/declarant `Pedro Pablo Neira`.
- The source page does not name Dario. Any link to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` is a research lead only, not a supported identity or relationship claim.

## Evidence Strengths

- Source quality is strong in type: a civil birth-register page is direct evidence for registrations, date/place fields, parents, declarants, and sex when the relevant cells are legible.
- Source identity is well supported. The source image, converted file, and source packet all identify register page 172 of the 1889 Los Anjeles/La Laja birth register with entries 513, 514, and 515 visible.
- Entry 513 has useful but incomplete support for a Pulgar father/declarant cluster: `José del Carmen Pulgar` / `José del C. Pulgar`, father role, agriculturist occupation, and Calle Colon domicile are visible or consistently derivative-supported.
- The staged draft's central judgment is supported: this is a conflict-analysis packet and should remain held pending targeted conversion QA.

## Scored Judgment

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil register image is a strong source type, though handwriting, contrast, and cropping reduce certainty for some cells. |
| conversion_confidence_score | 0.34 | The converted file and available chunk disagree on key names, dates/times, father fields, and entry completeness. |
| evidence_quantity_score | 0.58 | One direct page image plus derivative conversion, alternate chunk, source packet, and prior local QA notes are enough to identify conflicts but not settle exact identities. |
| agreement_score | 0.36 | Good agreement on source/page and some entry 513 father/declarant context; poor agreement on child names, mother surname, and entries 514-515. |
| identity_confidence_score | 0.28 | Registration-page identity is clear; exact person identities and same-person matches are not yet reliable. |
| claim_probability | 0.30 | Low probability for any exact identity-candidate claim beyond a general registration-scoped Pulgar/Riquelme/Neira candidate set. |
| relevance_level | high | The checked materials directly concern the assigned staged identity-analysis draft and its cited page. |
| relevance_confidence | 0.96 | The task id, staged draft, source packet, converted file, available related chunk, and source image all align with the assignment. |
| canonical_readiness | hold | Hold all canonical promotion and all Dario/Pulgar identity linkage until conversion QA resolves literal readings. |

## Identity Risk And Relationship Review

- Identity risk is high for entry 513 because the disputed fields are the exact fields needed to decide whether the record concerns an existing Pulgar/Amagada/Arriagada cluster.
- Parent-child relationship risk is high. `José del Carmen Pulgar` appears strongly supported as father/declarant, but the child name and mother surname are not stable enough for promotion.
- Relationship jumps to any Dario identity are unsupported by this source. Surname, locality, and broad Pulgar-line context do not establish same-person identity, ancestry, or descendant relationships.
- Conflict severity is high because promoting one derivative layer would likely encode wrong or premature names for at least entry 513 and could also affect entries 514 and 515.

## Next Action

Keep the staged draft on hold and run targeted conversion QA against the restored source image. The QA pass should reconcile the missing assigned chunk path, confirm entry 513 child full name, birth date/time, father/declarant, mother surname, and official signature, then confirm entry 514 and entry 515 person fields before any renewed identity proof review or canonical comparison.
