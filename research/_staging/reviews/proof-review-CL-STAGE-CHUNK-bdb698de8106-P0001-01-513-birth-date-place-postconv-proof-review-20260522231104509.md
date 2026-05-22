---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522231104509
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-birth-date-place.md
reviewed_source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
status: hold
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.82
conversion_confidence_score: 0.38
evidence_quantity_score: 0.55
agreement_score: 0.42
identity_confidence_score: 0.35
claim_probability: 0.48
relevance_level: direct
relevance_confidence: 0.90
---

# Proof Review: Entry 513 Birth Date And Place

## Blockers

- The staged draft's literal support says entry 513 was born on `Julio veintidos de mil ochocientos ochenta i nueve, a las cuatro de la mañana`; the visible page image for entry 513 appears to read `Junio veinte i dos` in the birth-date field, not `Julio veintidos`.
- The visible image supports `Calle Colon` in the entry 513 birth-place field, but the date/month conflict is material enough that the combined birth date/place claim should not be promoted.
- The source packet already records material conflicts between the assigned converted/chunk transcript and image-reviewed evidence for record 513, including the child-name field. Identity remains unresolved, so this birth event must not be attached to a canonical child.
- The draft correctly treats the claim as held for conversion QA, but its current object still preserves the converted transcript's disputed date/time. Canonical readiness remains `hold_for_conversion_qa`.

## Evidence Strengths

- Source quality is good: this is a contemporaneous civil birth-register page for Los Angeles, La Laja, Chile, page 172, with entry 513 visible in the image.
- The relevant field is direct evidence for a birth event because the entry has a dedicated `Fecha i lugar del nacimiento` column.
- The image visibly supports a place reading of `Calle Colon` for entry 513. The time line also appears to include `a las cuatro`, consistent with part of the converted transcript, but the surrounding date wording conflicts with the transcript.
- The converted file and chunk consistently contain the same derivative reading, so the conflict is not between derivative files; it is between the derivative transcript and the page image/source-packet QA note.

## Scored Judgment

- `source_quality_score`: 0.82
- `conversion_confidence_score`: 0.38
- `evidence_quantity_score`: 0.55
- `agreement_score`: 0.42
- `identity_confidence_score`: 0.35
- `claim_probability`: 0.48 for the staged combined statement as written; higher for the isolated place `Calle Colon`, lower for the `Julio veintidos` date component.
- `relevance_level`: direct
- `relevance_confidence`: 0.90
- `canonical_readiness`: hold_for_conversion_qa

## Next Action

Send to targeted conversion QA/image reread before any canonical promotion. The next reviewer should reconcile the entry 513 birth-date field against the image, especially `Junio veinte i dos` versus the converted `Julio veintidos`, and keep the child identity unresolved unless the visible source itself supports a stable reading.
