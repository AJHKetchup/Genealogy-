---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527223142088
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-proof-review-revision-hold-postconv-evidence-extraction-20260527221841108.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-proof-review-revision-hold-postconv-evidence-extraction-20260527221841108.md"
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-proof-review-revision-hold-postconv-evidence-extraction-20260527221841108.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 513 Pulgar Child

## Blockers First

1. Do not promote the candidate identity as `Dario Jose Pulgar Arriagada`. The visible source may support a reading in that direction, but the reviewed derivative texts disagree on the child name and maternal surname, and the row-level transcription has not been conversion-QA certified.
2. Do not create or attach canonical parent-child relationships from this draft. The father/declarant and mother fields appear relevant to the Pulgar family, but the exact child identity and mother surname remain identity-controlling conflicts.
3. Do not use either derivative transcript alone for canonical extraction. The converted Markdown reads `Isolina del Carmen / Jose` and `Juana de Dios Amador de Pulgar`; the chunk reads `Pulgar Amagada / Jose Luis` and `Juana de Dios Amagada de Pulgar`; the staged packet reports image-reviewed notes favoring `Pulgar Arriagada / Dario Jose` and `Juana de Dios Arriagada de Pulgar`.
4. The birth date and time also conflict between the converted file and chunk, so event claims should remain held with the identity claim.

## Evidence Strengths

- The original source is a civil birth-register image for Los Angeles, Chile, register page 172, entry 513, a primary source type for birth registration facts.
- Entry 513 is visibly a Pulgar-family row: `Jose del Carmen Pulgar` as father and `Jose del C. Pulgar` as father/declarant are substantially supported by the page image, with `Calle Colon` also visible in the residence/birth-place context.
- The sex field for entry 513 is visibly masculine, agreeing with the staged draft's caution that the record may concern a male Pulgar child.
- The source packet correctly preserves the conversion conflict and recommends `hold_for_conversion_qa` rather than treating the image-reviewed candidate reading as certified transcription.
- Row boundaries for entry 513 versus entries 514 and 515 appear stable enough that this is an entry-specific problem, not a broad page-row mismatch.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 3/10 |
| evidence_quantity_score | 4/10 |
| agreement_score | 3/10 overall; 7/10 for the narrow Pulgar-family/father/declarant elements |
| identity_confidence_score | 5/10 for a male Pulgar child in entry 513; 3.5/10 for exact identity as `Dario Jose Pulgar Arriagada`; 2/10 for relying on `Jose Luis`, `Isolina del Carmen / Jose`, `Amador`, or `Amagada` without QA |
| claim_probability | 0.80 that entry 513 is a Pulgar-family birth registration involving father/declarant `Jose del Carmen Pulgar`; 0.65 that the child is male and born/residing in the Calle Colon context; 0.45 that the exact child identity is `Dario Jose Pulgar Arriagada`; 0.25 or lower for the conflicting derivative readings as canonical identity claims |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supportable as a hold note. It should not be promoted as a corrected identity claim, but it accurately flags that the converted Markdown, assigned chunk, and image-reviewed reading disagree on the fields that control identity and relationship construction.

The visible page gives enough support to keep entry 513 in the Pulgar research workflow and to request targeted QA of the child name, birth date/time, mother surname, and official signature. It does not yet give enough reviewed, agreed transcription support to attach the child to an existing Dario/Pulgar identity cluster or to create canonical parent-child links.

## Next Action

Send entry 513 to targeted conversion QA with the question framed as verification only: double-check the child name, surname sequence, birth date/time, mother surname, and official signature against the visible image. Keep this identity analysis and all related event/relationship claims on hold until the corrected row-level transcription is certified and a fresh proof review scores the atomic claims.
