---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527220553845
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-image-reviewed-conflict-note-postconv-evidence-extraction-20260527200921254.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-image-reviewed-conflict-note-postconv-evidence-extraction-20260527200921254.md"
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-image-reviewed-hold-postconv-evidence-extraction-20260527200921254.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
canonical_readiness: hold
---

# Proof Review: Entry 513 Pulgar Conflict Note

## Blockers First

1. Do not promote this draft to canonical claims or relationships. The draft is a conflict note, and the referenced converted Markdown and assigned chunk materially disagree with each other and with the page image for the child name, birth date/time, mother surname, and official signature.
2. The staged draft's image-reviewed child-name statement needs revision or QA certification before any atomic claim is created. The visible source supports `Pulgar Arria...` and a given-name sequence that appears closer to `Jose Dario` than `Dario Jose`; the exact surname ending and given-name order should remain uncertified until targeted conversion QA confirms it.
3. The derivative converted file is not reliable for entry 513. It reads the child as `Isolina del Carmen / Jose`, the mother as `Juana de Dios Amador de Pulgar`, and the official as `Emilio Lininger`, none of which should be used for canonical identity construction without correction.
4. The assigned chunk is also not fully reliable for entry 513. It preserves some row context but reads the child as `Pulgar Amagada / Jose Luis`, the birth date as June 26, and the mother surname as `Amagada`, conflicting with the page image.

## Evidence Strengths

- The original source is a civil birth register page, a strong source type for birth, parentage, residence, declarant, and registration facts when the row is accurately read.
- The page image clearly places entry `513` in the first row of page 172 and shows father/declarant `Jose del Carmen Pulgar` or abbreviated `Jose del C. Pulgar`, male sex, residence at Calle Colon, and a mother named `Juana de Dios ... de Pulgar`.
- The page image supports the staged draft's central procedural conclusion: entry 513 should remain held for conversion QA because both derivative transcriptions contain serious row-level errors.
- The source packet correctly frames entries 514 and 515 as row-boundary context only and does not use them to supply entry 513 facts.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 3/10 for current derivative conversion/chunk readings; 6/10 for the source packet's image-reviewed row summary pending QA |
| evidence_quantity_score | 4/10 |
| agreement_score | 2/10 across converted file, chunk, and source packet; 7/10 between source packet's broad conflict diagnosis and visible image |
| identity_confidence_score | 6/10 for a Pulgar child of Jose del Carmen Pulgar and Juana de Dios Arriagada-or-similar de Pulgar; 4/10 for the exact name `Dario Jose Pulgar Arriagada` as written in the staged draft |
| claim_probability | 0.85 that entry 513 concerns a male Pulgar child born to Jose del Carmen Pulgar and Juana de Dios Arriagada-or-similar de Pulgar; 0.55 for the exact child-name/order `Dario Jose Pulgar Arriagada`; 0.90 that current derivative transcriptions are unsuitable for canonical promotion |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a conversion-conflict warning and hold recommendation. It should not be treated as a verified identity claim. The page image supports the high-level conflict diagnosis and supports a Pulgar-family relevance lead, but the exact child name and name order in the staged draft are not sufficiently secure for canonical use.

The strongest supported action is to keep this draft staged and route entry 513 for targeted row-level conversion QA. Any downstream atomic birth, parent-child, or same-person claim should be generated only after that QA pass certifies the literal row transcription from the image.

## Next Action

Hold. Request targeted conversion QA for entry 513, with special attention to the child surname, given-name order, birth date, mother surname, and official signature. After QA, rerun proof review on atomic claims rather than this conflict note.
