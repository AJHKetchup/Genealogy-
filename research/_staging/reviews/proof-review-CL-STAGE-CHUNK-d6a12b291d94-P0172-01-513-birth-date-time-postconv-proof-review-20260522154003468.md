---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260522154003468
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-date-time.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-date-time.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_requested: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
reviewed_chunk_available: unavailable_at_requested_path
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
claim_type: event
subject_claimed: Tulio Cesar Luis Jose
predicate_claimed: birth_date_time
object_claimed: "22 June 1889, 4:20 a.m."
source_quality_score: 0.92
conversion_confidence_score: 0.20
evidence_quantity_score: 0.35
agreement_score: 0.05
identity_confidence_score: 0.10
claim_probability: 0.08
relevance_level: medium
relevance_confidence: 0.45
canonical_readiness: hold
---

# Proof Review: CL-STAGE-CHUNK-d6a12b291d94-P0172-01-513-birth-date-time

## Blockers

- The staged claim is not literally supported as written. It claims entry 513 birth date/time for `Tulio Cesar Luis Jose`, but the visible source image's entry 513 child field appears to be a masculine Pulgar-family child with a name line beginning `Pulgar Ama...` and a later given-name line beginning `Jose ...`; the visible `Tulio...` material is in the lower visible row associated with a different entry, not entry 513.
- The staged object `22 June 1889, 4:20 a.m.` is not supported by the reviewed conversion layers or the source image. The source image for entry 513 appears closer to `Junio veinte i dos ... a las cuatro i media ... tarde`, while the assembled converted file instead reads entry 513 as `El mismo veinte dos ... a las cuatro de la mañana`. Neither supports the exact staged time `4:20 a.m.`.
- The staged literal-support block (`Fecha. Junio veinte i dos ... a las cuatro i veinte de la mañana`) does not match the assembled converted file's entry 513 text and is not confirmed by the visible image.
- The referenced chunk path in the staged draft and source packet is unavailable at the requested location, so the claim cannot be verified against its cited chunk.
- The source packet for this staged set has internal disagreement: its literal support says entry 513 includes `Tulio Cesar Luis Jose`, but the same physical page image places the visible Tulio row below entry 514 and not in entry 513. This is a conversion/claim-extraction mismatch, not a promotable proof basis.

## Evidence Strengths

- The source itself is a strong, direct civil birth register page from Los Anjeles/Los Angeles, La Laja, Chile, with visible entries 513, 514, and part of 515.
- Entry 513 is visible on the source image and contains a birth-date/time column, so a corrected birth-date/time claim may be recoverable after targeted conversion QA.
- The reviewed image supports that entry 513 is a birth registration on page 172 and that its birth-date/time field includes `Junio veinte i dos`; however, the exact time and subject identity require correction before canonical use.

## Scored Judgment

- `source_quality_score`: 0.92. A contemporaneous civil birth register is direct evidence for a birth event.
- `conversion_confidence_score`: 0.20. The staged draft, source packet, assembled converted file, and visible image materially disagree.
- `evidence_quantity_score`: 0.35. There is one direct source page, but the cited chunk is unavailable and the derivative readings conflict.
- `agreement_score`: 0.05. The exact subject and exact time are unsupported; only a broad `Junio veinte i dos` component has partial image support.
- `identity_confidence_score`: 0.10. `Tulio Cesar Luis Jose` is not established as the entry 513 child by the reviewed evidence.
- `claim_probability`: 0.08. Very low probability that the exact staged claim is correct.
- `relevance_level`: medium. The source page is relevant to birth-date/time claims on this register page, but the staged subject-entry pairing appears wrong.
- `relevance_confidence`: 0.45. Relevance is reduced by the apparent row/entry mismatch and missing chunk.
- `canonical_readiness`: hold. Do not promote this claim.

## Next Action

Hold for conversion QA. Reconcile the source image, converted file, and missing/stale chunk reference for entry 513, specifically the child identity and the birth time phrase. If the Tulio row is intended, revise the claim to the correct entry number and only use wording visibly supported by that row or by a corrected conversion.
