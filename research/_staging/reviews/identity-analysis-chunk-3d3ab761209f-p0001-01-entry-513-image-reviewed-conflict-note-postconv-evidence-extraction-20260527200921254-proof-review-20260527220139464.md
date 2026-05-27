---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527220139464
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-image-reviewed-conflict-note-postconv-evidence-extraction-20260527200921254.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-3d3ab761209f-p0001-01-entry-513-image-reviewed-conflict-note-postconv-evidence-extraction-20260527200921254.md
source_packet: research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-image-reviewed-hold-postconv-evidence-extraction-20260527200921254.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md
source_quality_score: 0.82
conversion_confidence_score: 0.38
evidence_quantity_score: 0.70
agreement_score: 0.42
identity_confidence_score: 0.66
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: hold
---

# Proof Review: Entry 513 Identity Conflict Note

## Blockers

- Canonical readiness is `hold`. The staged draft is a conflict note and does not provide a QA-certified row transcription suitable for canonical claims or relationships.
- The image-reviewed child name in the staged draft is not fully settled. The visible source supports `Pulgar Arriagada` and a male child, but the given-name order appears more consistent with `Jose Dario` than `Dario Jose`. This should be double-checked by conversion QA before any identity attachment.
- The derivative texts disagree sharply with each other and with the page image. The converted Markdown gives `Isolina del Carmen / Jose`, `Juana de Dios Amador`, and a morning birth time; the chunk gives `Pulgar Amagada / Jose Luis`, `Juana de Dios Amagada`, and a different birth date. Those disagreements lower conversion confidence and agreement scores.
- Relationship proof should remain held. The father and mother fields appear relevant and likely, but the subject identity is not yet stable enough for canonical parent-child linkage.

## Evidence Strengths

- The original page image is a civil birth register page, a direct source for birth, sex, parents, declarant, and registration context.
- The row boundary for entry 513 is visually clear enough to separate it from entries 514 and 515.
- The image visibly supports several family-relevant elements: entry number 513, registration date of 22 July 1889, father `Jose del Carmen Pulgar`, declarant `Jose del C. Pulgar`, mother line consistent with `Juana de Dios Arriagada de Pulgar`, male sex, Calle Colon residence/place context, and official signature consistent with `Emilio Larenas`.
- The staged draft correctly treats the record as a conflict candidate and recommends holding rather than promotion.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Original civil register image is direct evidence, but scan contrast and handwriting limit certainty. |
| conversion_confidence_score | 0.38 | Converted file and chunk contain major disagreements in child name, mother surname, birth date/time, and official signature. |
| evidence_quantity_score | 0.70 | One direct register entry supplies multiple identity fields, but no corroborating independent source is included. |
| agreement_score | 0.42 | Image, chunk, and converted Markdown agree on some Pulgar/father/declarant context but conflict on the subject identity and key dates. |
| identity_confidence_score | 0.66 | A Pulgar-Arriagada child in entry 513 is likely, but the given-name order and derivative conflicts keep identity confidence below promotion level. |
| claim_probability | 0.62 | The conflict note is probably directionally correct as a hold/review item, but its exact `Dario Jose` reading is not yet proven. |
| relevance_level | high | The entry directly concerns a Pulgar child and names Jose del Carmen Pulgar. |
| relevance_confidence | 0.90 | Family relevance is strong despite identity-read uncertainty. |
| canonical_readiness | hold | Needs targeted conversion QA or a certified row-level transcription before canonical use. |

## Next Action

Send entry 513 for targeted conversion QA focused on the child given-name order, child surname, birth date/time, mother surname, and official signature. After QA certification, rerun proof review on atomic claims and parent-child relationship drafts; do not promote this conflict note directly.
