---
type: proof_review
role: claim_reviewer
status: complete
worker: postconv-proof-review-20260523114614778
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_at: 2026-05-23
source_quality_score: 0.86
conversion_confidence_score: 0.42
evidence_quantity_score: 0.70
agreement_score: 0.46
identity_confidence_score: 0.38
claim_probability: 0.88
relevance_level: critical
relevance_confidence: 0.96
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Page 172 Identity Candidates

## Blockers

- Canonical readiness is **hold_for_conversion_qa**. The staged identity analysis is well supported as a warning/hold note, but the person identities and parent-child relationships in entries 513-515 are not ready for canonical promotion.
- The staged draft contains stale file-context claims. It says the referenced `page-0172-chunk-01.md` is missing and that `page-0001-chunk-01.md` is available; in the current workspace, `page-0172-chunk-01.md` exists and `page-0001-chunk-01.md` does not. The current chunk id is `CHUNK-fb0d63eb2b71-P0172-01`, not the staged/source-packet id `CHUNK-4127185dc97c-P0172-01`.
- The source packet metadata is also stale against current derivative files: it cites converted sha `4127185dc97c...`, while the current chunk manifest and chunk cite converted sha `fb0d63eb2b71...`. This does not invalidate the page, but it blocks clean claim promotion until the staging records are reconciled.
- Entry 513 remains materially conflicted. The current converted file/chunk read the child as `Isidoro del Carmen Jose`, father `Jose del Carmen Pulgar`, and mother `Juana de Dios Amador`; the visible source image supports a Pulgar child reading and appears closer to `Jose Dani...` for the given names, with the mother's surname not safely settled from this review.
- Entry 514 remains materially conflicted in the father field. The converted file/chunk read father `Alejandro Riquelme`; the visible image and source packet support treating the father field as uncertain and plausibly closer to `se ignora`, while mother/declarant `Mercedes Riquelme` is comparatively better supported.
- Entry 515 remains materially conflicted in surname/parentage. The converted file/chunk read `Pedro Pablo Leiva`; the visible image appears closer to `Pedro Pablo Neira`, and the lower row is partly cut off. No Leiva/Neira person or relationship should be promoted from this draft.
- The draft's Dario/Pulgar comparisons are relevant only as anti-conflation guardrails. This page does not name Dario or Arturo, and it does not prove a bridge to `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.

## Evidence Strengths

- The source itself is strong in type: a civil birth register page image for Los Anjeles/La Laja, page 172, entries 513-515.
- Page identity is well supported. The source image visibly shows `Paj. 172`, the 1889 birth-register heading, and entries 513, 514, and 515.
- The staged draft's main recommendation, `hold_for_conversion_qa`, is supported by the source packet, current converted file, current chunk, and direct image review.
- Some narrow row participants are likely. Entry 513 visibly supports `Jose del Carmen Pulgar` / `Jose del C. Pulgar` as father/declarant at source level, and entry 514 visibly supports `Mercedes Riquelme` as mother/declarant. Those are not enough to promote canonical identities while the child names, parent fields, and staging metadata remain conflicted.

## Scores

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil registration image is direct evidence for the page entries, though the scan is high contrast and some fields are hard to read. |
| conversion_confidence_score | 0.42 | The current conversion/chunk align with each other but conflict with visible image readings and source-packet QA on material identity fields. |
| evidence_quantity_score | 0.70 | One source image, one source packet, the converted file, and the current chunk were reviewed; no external or independent corroborating source was used. |
| agreement_score | 0.46 | Page identity and some participant fields agree, but child names, father fields, surnames, and metadata ids/checksums conflict. |
| identity_confidence_score | 0.38 | Individual identities for entries 513-515 are uncertain; confidence is higher only for the broad page/entry frame. |
| claim_probability | 0.88 | The claim that this staged identity draft should remain on hold for conversion QA is highly probable. |
| relevance_level | critical | The conflicts affect whether people, parents, and identity links could be created or merged. |
| relevance_confidence | 0.96 | The reviewed files and source image are exactly the assigned page-172 evidence set. |
| canonical_readiness | hold_for_conversion_qa | Reconcile conversion/staging metadata and disputed name fields before promotion. |

## Judgment

The staged draft is supportable as a hold/identity-risk analysis, but not as proof of any person identity. The strongest source-level conclusion is that page 172 contains entries 513-515 and that all three require conversion QA before any identity, parentage, duplicate, or relationship claim is promoted.

The staged draft should be revised or superseded on the narrow point that the referenced chunk is unavailable. The current workspace does contain the page-172 chunk, but under a different chunk id and converted checksum than the staged draft/source packet. That metadata drift is itself a blocker.

## Next Action

Keep this staged identity analysis on **hold_for_conversion_qa**. First reconcile the staging metadata to the current `page-0172-chunk-01.md` and converted checksum, then perform field-level conversion QA against the source image for entry 513 child name/mother surname, entry 514 father field, and entry 515 Leiva/Neira surname. After those readings are settled, create or review separate atomic claims before considering any canonical person or relationship promotion.
