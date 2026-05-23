---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522235742855
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-birth-date-place.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-birth-date-place.md
review_status: complete
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 514 Birth Date And Place

## Blockers

- Hold before canonical promotion: the staged draft is not literally supported as written. It gives the birth date/time/place as `1889-07-23 at 10:00 a.m.; Calle Saneguin`, but direct image review of entry 514 appears closer to `Junio veinte i tres ... a las nueve de la manana`, with the street beginning `Calle de Sane...` or similar. This review does not substitute a corrected transcription; it flags the mismatch for conversion QA.
- Hold before canonical promotion: the referenced derivative transcript and current source packet conflict with the visible source for entry 514. The converted file/chunk gives `El mismo veinte tres ... a las diez de la manana` and `Calle Saneguin`, while the source packet already notes image-reviewed disagreement on entry 514, including a street reading closer to `Calle San...`/`Calle Sanegueso`.
- Hold before canonical promotion: the claim subject is identity-unstable. The staged draft uses `entry 514 child identity unresolved`, and the source packet reports material disagreement in the child-name and parent fields. The birth date/place claim is registration-scoped and directly relevant, but it should not be attached to a resolved person until conversion QA reconciles entry 514.

## Evidence Strengths

- The source image is available and matches the assigned source path, page 172, and row 514 in an 1889 Los Anjeles/La Laja civil birth register.
- The `Fecha i lugar del nacimiento` column for entry 514 is visible in the image, so the evidence is directly relevant to a birth date/time/place claim for that registration.
- The staged draft, source packet, converted file, and chunk all point to the same bdb chunk and source image, so the verification context is now available even though the literal reading remains disputed.

## Scores

| Metric | Score | Rationale |
| :--- | :--- | :--- |
| source_quality_score | 0.86 | Original civil birth-register page image is a direct source for the event, but handwriting, contrast, and image crop make this specific field difficult. |
| conversion_confidence_score | 0.30 | The converted/chunk transcription conflicts with the visible image and with the packet's image-QA notes for entry 514 date/time/place. |
| evidence_quantity_score | 0.55 | One direct source page supports the existence of the field, but there is no independent corroboration for the exact date/time/street reading. |
| agreement_score | 0.20 | Derivative transcript, staged claim, packet QA, and visible source do not agree on the exact birth date/time/place wording. |
| identity_confidence_score | 0.35 | The row number 514 is clear, but the child identity and parent fields remain disputed, limiting person-level linkage confidence. |
| claim_probability | 0.18 | Low probability that the staged claim is correct as written because the visible image appears to contradict both the stated month/time and the street spelling. |
| relevance_level | direct | The cited row and column directly concern entry 514 birth date/time/place. |
| relevance_confidence | 0.92 | The row alignment and field location are clear enough to confirm that this is the correct field for the claim. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until targeted QA resolves entry 514's birth date/time and street-name transcription. |

## Judgment

The claim should be held for conversion QA, not promoted. The source is strong and directly relevant, but the staged wording is too dependent on a disputed derivative transcript. Direct image review supports the presence of an entry 514 birth date/time/place field but does not support the exact claim text `1889-07-23 at 10:00 a.m.; Calle Saneguin` with enough confidence for canonical use.

## Next Action

Run targeted conversion QA on entry 514's `Fecha i lugar del nacimiento` field, especially the month, hour, and street-name spelling. After QA, revise the staged claim to a registration-scoped reading that preserves uncertainty rather than promoting the current text.
