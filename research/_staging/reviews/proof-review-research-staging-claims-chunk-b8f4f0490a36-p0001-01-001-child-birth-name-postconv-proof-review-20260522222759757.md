---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/chunk-b8f4f0490a36-p0001-01-001-child-birth-name.md
staged_draft: research/_staging/claims/chunk-b8f4f0490a36-p0001-01-001-child-birth-name.md
reviewer: postconv-proof-review-20260522222759757
review_date: 2026-05-22
claim_type: birth_name
subject: "Jose del Carmen Segundo Pulgar Arriagada"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Child Birth Name

## Blockers

- The current referenced converted Markdown and job page Markdown still conflict with this staged claim: they transcribe entry 172 as `José Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, not as the Pulgar/Arriagada entry.
- The exact referenced source image path `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` and the manifest page image path were not present in this checkout during this review, so I could not personally reread the handwriting from the image.
- A later QA/review update reports that the image was located and reread, and that entry 172 visibly gives the child name as `Jose del Carmen Segundo Pulgar Arriagada`. Treat that as supporting QA context, but do not treat the conflicting converted Markdown as clean literal support until conversion QA reconciles or regenerates it.
- Do not silently normalize the staged spelling to `José`; the supported staged form is `Jose del Carmen Segundo Pulgar Arriagada`.

## Scores

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.90 | A civil birth registration is a high-quality source for a recorded birth name. |
| conversion_confidence_score | 0.62 | The assigned chunk and QA reread support the name, but the current converted Markdown/page Markdown materially conflict and the image file is absent here. |
| evidence_quantity_score | 0.72 | One direct civil-registration entry, one assigned chunk transcription, source packet support, and an image-reread QA note support the narrow claim. |
| agreement_score | 0.58 | The staged draft, source packet, assigned chunk, and image-reread note agree; the referenced converted Markdown and job page Markdown disagree. |
| identity_confidence_score | 0.82 | The child name is distinctive and tied to entry 172/page 58 in the supporting packet and chunk, but derivative-text conflict leaves some identity-context risk. |
| claim_probability | 0.88 | The narrow birth-name claim is probably correct based on the assigned chunk plus image-reread QA note, but not fully cleared while the conversion conflict remains unresolved. |
| relevance_level | critical | The claim identifies the recorded child in the birth entry. |
| relevance_confidence | 0.95 | The evidence directly concerns the staged birth-name field. |
| canonical_readiness | hold_for_conversion_qa | Supported enough to preserve, but not cleanly promotion-ready from the current referenced conversion set. |

## Evidence Strengths

- The staged draft claims only the recorded birth name, and the assigned chunk gives direct literal support: `**Nombre.** Jose del Carmen Segundo Pulgar Arriagada`.
- The staged source packet repeats the same child-name reading for entry 172 on register page 58 and flags the converted-file conflict explicitly.
- The QA image-reread note for this same source SHA reports that the visible entry 172 child name is `Jose del Carmen Segundo Pulgar Arriagada`, resolving the earlier image-availability blocker for this narrow field as review context.
- No relationship jump is required for this claim. It asserts the recorded name of the child named in the entry, not a merged identity across records.

## Review Judgment

The staged birth-name claim is well supported by the assigned chunk and by the later image-reread QA note. The claim should remain literal and unaccented as staged: `Jose del Carmen Segundo Pulgar Arriagada`.

The main risk is not the name reading itself; it is source-control and conversion integrity. The active referenced converted Markdown and page Markdown still point to a different entry 172, and the source image was not available for direct visual verification in this checkout. Because of that mismatch, this review should not be used as a clean canonical-clearance signal until conversion QA reconciles the converted file or restores a directly verifiable source image in the expected path.

## Next Action

Hold for conversion QA. Reconcile or regenerate the referenced converted Markdown/page Markdown so entry 172 matches the image-reread Pulgar/Arriagada row, or restore the source/page image at the manifest path for direct verification. After that, rerun proof review for canonical readiness.
