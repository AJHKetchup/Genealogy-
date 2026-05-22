---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/conflicts/CHUNK-3d3ab761209f-P0001-01-conflict-candidates.md
staged_draft: research/_staging/conflicts/CHUNK-3d3ab761209f-P0001-01-conflict-candidates.md
reviewer: postconv-proof-review-20260522010752563
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: conflict candidates for CHUNK-3d3ab761209f-P0001-01

## Blockers

- Raw source image is unavailable at the source path named by the staged draft and manifest: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`. `raw/sources` currently contains only `.gitkeep`.
- The manifest page image is also unavailable at `raw/codex-conversion-jobs/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513/page-images/page-0001.png`; the conversion job directory currently contains `manifest.json`, `README.md`, `page-markdown`, and `work-orders`, but no `page-images` directory.
- Because no visible source image is available, the image-dependent candidates cannot be resolved: record 514 witness surname `Utiera`, record 514 street name `Sanegueso`, record 515 `Neira` emendation text, and the bottom-crop completeness concern remain holds.
- The negative-evidence candidate for record 514 father unknown is directly supported by the converted file and chunk, but it should not be used by itself to reject a later father claim unless the later claim is reviewed against its own source strength and identity context.

## Scores

- source_quality_score: 0.80
- conversion_confidence_score: 0.72
- evidence_quantity_score: 0.70
- agreement_score: 0.94
- identity_confidence_score: 0.62
- claim_probability: 0.76
- relevance_level: high
- relevance_confidence: 0.88
- canonical_readiness: hold

## Candidate Judgments

| Candidate id | Judgment | Claim probability | Canonical readiness | Rationale |
| --- | --- | ---: | --- | --- |
| conflict-514-father-unknown | supported as staged negative evidence | 0.86 | hold | The converted file and chunk both state record 514's father field as `Se ignora`. This is strong literal support for an unknown father as recorded at registration, but not a final disproof of any later father attribution. |
| qa-514-witness-utiera | hold | 0.45 | hold | The converted file explicitly flags `Utiera` as a difficult witness surname reading. Without the image, the surname cannot be verified or normalized. |
| qa-514-street-sanegueso | hold | 0.60 | hold | The converted file reads `Calle Sanegueso` and says the handwriting is clear but the spelling is unusual. Image review is still needed before place normalization or canonical use. |
| qa-515-neira-emendation | hold | 0.68 | hold | The converted file and chunk include the emendation note `Neira=emendado= / vale= / Emilio Larenas / O. de R. C.`, but image review is required before relying on this for canonical surname correction. |
| qa-page-cropped | supported as conversion QA limitation | 0.72 | hold | The converted file's completeness audit says the page is cropped at the bottom while three complete records are visible. This is relevant source-packet QA, but the crop cannot be independently checked without the image. |

## Evidence Strengths

- The staged draft, converted file, chunk, and manifest all agree on the source identity, chunk id, page number, document type, and register entries 513-515.
- Record 514's father field is consistently transcribed as `Se ignora`, and the mother/compareciente is consistently transcribed as Mercedes Riquelme.
- The staged draft correctly preserves uncertainty instead of silently normalizing difficult readings for `Utiera`, `Sanegueso`, and the record 515 emendation.
- The candidate set does not promote a relationship jump. It frames the unknown-father entry as potential conflict or negative evidence against later claims, which is the appropriate evidentiary posture.

## Review Judgment

The staged conflict/QA draft is internally supported by the converted Markdown and the assigned chunk. The strongest item is the record 514 unknown-father note, which is directly represented in the conversion and is relevant negative evidence for later father assignments involving Juan Bautista Riquelme Aviles.

The review cannot reach canonical readiness because the raw and rendered page images are unavailable. The image-dependent QA items should remain holds, and no witness, street, surname emendation, or page-crop conclusion should be promoted beyond the current converted-text evidence.

## Next Action

Restore or regenerate the source/page image, then visually verify record 514's father field, witness surname, and street name; record 515's `Neira` emendation; and the bottom crop. After image review, promote only the verified negative-evidence conflict note and preserve unresolved readings as QA limitations.
