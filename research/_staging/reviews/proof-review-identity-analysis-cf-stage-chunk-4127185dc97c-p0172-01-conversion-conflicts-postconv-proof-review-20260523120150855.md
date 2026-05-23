---
type: proof_review
role: claim_reviewer
status: complete
worker: postconv-proof-review-20260523120150855
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
staged_draft: research/_staging/identity-analysis/identity-analysis-cf-stage-chunk-4127185dc97c-p0172-01-conversion-conflicts.md
referenced_conflict_draft: research/_staging/conflicts/CF-STAGE-CHUNK-4127185dc97c-P0172-01-conversion-conflicts.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_at: 2026-05-23
source_quality_score: 0.86
conversion_confidence_score: 0.40
evidence_quantity_score: 0.68
agreement_score: 0.44
identity_confidence_score: 0.36
claim_probability: 0.90
relevance_level: critical
relevance_confidence: 0.97
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Conversion Conflict Identity Analysis

## Blockers

- Canonical readiness is **hold_for_conversion_qa**. The staged identity analysis is supported as a warning/hold judgment, but it does not prove any person identity, parent-child relationship, same-person merge, or Dario/Pulgar lineage bridge.
- The staged draft includes stale file-status evidence. It says the referenced `page-0172-chunk-01.md` was unavailable and that `page-0001-chunk-01.md` was available. In the current workspace, the referenced page-172 chunk exists, and the page-0001 chunk path cited by the staged draft does not exist.
- There is metadata drift. The source packet and conflict draft cite `CHUNK-4127185dc97c-P0172-01`, while the current page-172 chunk front matter identifies `CHUNK-fb0d63eb2b71-P0172-01` and converted sha `fb0d63eb2b71...`. This blocks clean promotion until staging metadata is reconciled.
- Entry 513 remains materially unresolved. The current converted file/chunk read the child as `Isidoro del Carmen Jose`, father/declarant as `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, and mother as `Juana de Dios Amador`; the source packet and visible image support a Pulgar-row concern and do not justify promoting a settled child identity or maternal surname from this draft.
- Entry 514 remains materially unresolved. The current converted file/chunk read father `Alejandro Riquelme`, while the source packet and image-reviewed conflict concern flag the father field as plausibly closer to an unknown-father reading. Mercedes Riquelme is comparatively better supported as mother/declarant context, but not enough to promote the whole family structure.
- Entry 515 remains materially unresolved. The current converted file/chunk read `Pedro Pablo Leiva`, while the source packet and visible image concern point toward `Neira` as a serious competing reading. Do not promote Leiva/Neira identity or parentage claims.
- The Pulgar/Dario comparisons in the staged draft are relevant only as anti-conflation safeguards. This evidence set does not name Dario or Arturo and does not prove a connection to `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or any Pulgar-Arriagada Dario identity.

## Evidence Strengths

- The source class is strong: a civil birth-register page image for Los Anjeles/La Laja, Chile, 1889.
- Page identity is well supported. The source image visibly shows page 172, the 1889 birth-register heading, and entries 513, 514, and 515.
- The staged draft's central recommendation, `hold_for_conversion_qa`, agrees with the source packet, the referenced conflict draft, the converted/chunk derivatives, and direct source-image review.
- Some narrow participant readings are plausible at source level, especially `Jose del Carmen Pulgar` / `Jose del C. Pulgar` in entry 513 and `Mercedes Riquelme` in entry 514. These remain provisional because the surrounding child, parent, and surname fields are disputed.

## Scores

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil registration image is direct evidence, though scan contrast and handwriting make several fields difficult. |
| conversion_confidence_score | 0.40 | The current conversion and chunk agree with each other, but materially conflict with source-packet QA concerns and visible image readings. |
| evidence_quantity_score | 0.68 | Reviewed the staged identity analysis, referenced conflict draft, source packet, converted file, current page-172 chunk, and source image; no external research was used. |
| agreement_score | 0.44 | Agreement is strong for page identity and entry numbers, weak for key names, surnames, father fields, and staging metadata. |
| identity_confidence_score | 0.36 | Individual identities in entries 513-515 remain unsettled; confidence is higher only for the page/entry frame. |
| claim_probability | 0.90 | The claim that this staged draft should remain a conversion-QA hold is highly probable. |
| relevance_level | critical | The conflicts directly affect identity, relationship, duplicate-person risk, and canonical promotion readiness. |
| relevance_confidence | 0.97 | The reviewed files are the exact staged draft and its referenced page-172 evidence set. |
| canonical_readiness | hold_for_conversion_qa | Reconcile metadata and proofread disputed fields against the image before any canonical action. |

## Judgment

The staged draft is literally supported as a conversion-conflict analysis and should remain on hold. It is not adequate proof for canonical person, relationship, duplicate, or lineage claims. Its main weakness is not the hold recommendation, which is sound, but the stale assertion that the referenced page-172 chunk is missing and the continuing mismatch between staged ids/checksums and the current chunk.

The source image supports the broad page context and the need for caution. It does not support resolving the disputed child names, maternal surnames, father fields, or Leiva/Neira question within this review note.

## Next Action

Revise or supersede the staged analysis to reflect the current page-172 chunk and converted checksum, then perform targeted field-level conversion QA from the source image for entry 513 child name and mother surname, entry 514 father field, and entry 515 Leiva/Neira surname. Keep all affected claims out of canonical folders until that QA is complete.
