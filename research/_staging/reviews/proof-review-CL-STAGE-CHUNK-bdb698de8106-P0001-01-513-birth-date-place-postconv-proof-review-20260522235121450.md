---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522235121450
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md
reviewed_source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
review_date: 2026-05-22
status: hold
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.86
conversion_confidence_score: 0.36
evidence_quantity_score: 0.58
agreement_score: 0.43
identity_confidence_score: 0.32
claim_probability: 0.47
relevance_level: direct
relevance_confidence: 0.90
---

# Proof Review: CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place

## Blockers

- Hold for conversion QA. The staged draft claims the converted transcript says entry 513 birth date/time/place is `1889-07-22 at 4:00 a.m.; Calle Colon`, but direct image review does not safely support the date/time wording as staged.
- The visible entry 513 birth-date field appears to begin with `Junio veinte i dos`, not the staged `Julio veintidos`/`El mismo veinte dos`; the time line includes `a las cuatro`, but the minute and a.m./p.m. reading remains disputed.
- The source packet flags material image-review conflicts for entry 513, including the child identity. This birth event must not be attached to any canonical child until the row transcription is reconciled.
- `Calle Colon` is visible in the entry 513 birth-place field and is also present in the converted file and chunk, but the combined date/time/place claim is not canonical-ready while the date/time and identity conflicts remain unresolved.

## Evidence Strengths

- The source is a contemporaneous civil birth register page for Los Angeles/Los Anjeles, La Laja, Chile, and entry 513 is visible on register page 172.
- The claim concerns a dedicated `Fecha i lugar del nacimiento` column, so the source is directly relevant to a birth date/time/place claim if the entry is accurately transcribed.
- The converted file, chunk, source packet, and visible image all point to the same source page and entry number.
- The place component `Calle Colon` has cross-layer support: it appears in the converted transcript, chunk, and visible source image for entry 513.

## Scored Judgment

| source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
|---:|---:|---:|---:|---:|---:|---|---:|---|
| 0.86 | 0.36 | 0.58 | 0.43 | 0.32 | 0.47 | direct | 0.90 | hold_for_conversion_qa |

The source quality is strong, but the derivative conversion is weak for this exact claim because the staged literal support, source-packet QA notes, and visible source image do not agree on the date/time field. Evidence quantity is limited to one direct entry plus derivative transcription layers, and those layers are currently in conflict. Identity confidence is low because the source packet explicitly keeps the entry 513 child identity unresolved.

No relationship jump is made by this claim. The principal risks are conversion accuracy and identity attachment. The claim is directly relevant to entry 513, but the exact staged statement has only moderate-low probability as written; the isolated `Calle Colon` place reading is stronger than the combined `1889-07-22 at 4:00 a.m.` date/time/place statement.

## Next Action

Send to targeted conversion QA/image reread before promotion. QA should reconcile entry 513's child identity and the birth-date/time field directly against the restored page image, then revise or replace the staged claim from the corrected transcription. Retain `Calle Colon` only as a provisional entry-513 place reading until that QA pass is complete.
