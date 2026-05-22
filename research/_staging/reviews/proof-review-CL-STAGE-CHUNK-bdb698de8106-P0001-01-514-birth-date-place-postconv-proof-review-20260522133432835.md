---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522133432835
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-birth-date-place.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-514-birth-date-place.md
review_status: complete
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 514 Birth Date And Place

## Blockers

- Hold before canonical promotion: the staged claim is not literally supported as written. It claims `1889-07-23 at 10:00 a.m.; Calle Saneguin`, but the visible source image for entry 514 appears to read `Junio veinte i tres ... a las nueve de la mañana` and a street closer to `Calle Sanegueso`.
- Hold before canonical promotion: the staged draft's subject `Riquelme Juan Teodoro` is not supported by the verification context. The image and corrected chunk layer point to entry 514's child as `Riquelme ... Juan Bautista`; the bdb converted file instead reads `Rigoberto Juan Bautista`. This claim should not be used for identity linkage until conversion QA resolves the child-name field.
- Hold before canonical promotion: the referenced chunk path in the staged draft and source packet, `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, is unavailable. The existing chunk in that folder is `page-0172-chunk-01.md`, with chunk id `CHUNK-0554d5747bd2-P0172-01`.
- Hold before canonical promotion: derivative transcripts conflict materially. The bdb converted file reads entry 514's place as `Calle Paneque`, while the corrected chunk layer and direct image review support a different street reading, probably `Calle Sanegueso`. Do not normalize or quote the street name until conversion QA.

## Evidence Strengths

- The source identity is strong: the staged draft, source packet, converted file, and source image all refer to page 172 of an 1889 Los Anjeles/La Laja civil birth register containing entry 514.
- The claim is relevant to entry 514 because the source image has a visible `Fecha i lugar del nacimiento` column in the row aligned with registration number 514.
- The visible image directly supports that entry 514 contains a birth date/time and place field, even though the exact date, time, and street spelling in the staged draft are not supported as written.

## Scores

| Metric | Score | Rationale |
| :--- | :--- | :--- |
| source_quality_score | 0.82 | Original register page image is a direct civil birth-register source, but the page is a difficult monochrome image with some crop/contrast issues. |
| conversion_confidence_score | 0.32 | The referenced derivatives conflict on entry 514, and the staged draft cites an unavailable chunk path. |
| evidence_quantity_score | 0.55 | One direct source page is available and relevant, but there is no corroborating independent source for this atomic birth date/place claim. |
| agreement_score | 0.18 | The staged claim disagrees with both the visible source image and at least one corrected chunk layer for date/time/place. |
| identity_confidence_score | 0.25 | Entry 514 identity is unstable across derivatives; `Juan Teodoro` is not supported in the checked evidence. |
| claim_probability | 0.12 | Low probability that the staged claim is correct as written, especially for month, hour, and street spelling. |
| relevance_level | direct | The source row is directly about entry 514's birth date and place. |
| relevance_confidence | 0.90 | The field being reviewed is clearly visible in the correct row and column. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until conversion QA reconciles the image with the conflicting derivative transcripts. |

## Judgment

The claim should be revised or held, not promoted. The image appears to support a birth date/time of June 23, 1889, at nine in the morning, and a place closer to `Calle Sanegueso`; however, this review does not edit the source transcription or canonicalize that reading. The safe action is to return this staged claim for conversion QA focused on entry 514's child name, birth date/time, and street-name spelling.

## Next Action

Run targeted conversion QA against the source image for entry 514's `Fecha i lugar del nacimiento` field. After QA, replace this staged claim with an image-supported, registration-scoped birth date/time/place claim before any canonical promotion.
