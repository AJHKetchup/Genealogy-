---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260530065614506
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527025657315.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527025657315.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
reviewed_conversion_qa_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_image_status: "referenced_but_not_available_at_declared_path"
source_quality_score: 0.86
conversion_confidence_score: 0.38
evidence_quantity_score: 0.68
agreement_score: 0.44
identity_confidence_score: 0.70
claim_probability: 0.76
relevance_level: high
relevance_confidence: 0.93
canonical_readiness: hold_for_conversion_qa
canonical_readiness_score: 0.10
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Source-image availability blocker: the staged draft, source packet, QA note, chunk, converted file, and manifest all reference `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` or the equivalent accented path, but the source PNG was not present at that path during this review. The manifest also references `page-images/page-0001.png`, but no `page-images` directory was present under the conversion job. This review therefore cannot independently certify the handwriting from the image.
- Conversion-control blocker: the assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, while the current converted Markdown transcribes entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. These are mutually incompatible row identities.
- Father-field blocker: the chunk includes `Jose del Carmen Pulgar S.`, but the source packet and targeted QA note certify only `Jose del Carmen Pulgar`; the terminal mark or suffix is unresolved and should not be promoted.
- Identity-link blocker: this source set does not name Dario, Arturo, Smith, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`. Any bridge to those candidates would be a relationship jump unsupported by this row-level evidence.
- Canonical-readiness blocker: because the primary source image was unavailable to this reviewer and the derivative conversion products conflict materially, no fact, relationship, merge, or parent identity should be promoted from this staged draft to canonical files.

## Evidence Strengths

- The staged draft accurately preserves the material conflict between the chunk/source-packet/QA-note cluster and the converted Markdown. It does not flatten the issue into a name variant.
- The source packet and targeted QA note are internally consistent: both identify physical row `172` as a Pulgar/Arriagada birth registration, both bound the father reading to `Jose del Carmen Pulgar`, and both recommend holding promotion for conversion QA.
- The assigned chunk provides a coherent row transcription for entries 171-176 on pages 58-59, with entry `172` aligned to the Pulgar/Arriagada row. This gives derivative support for the staged draft's local row-control hypothesis.
- The converted Markdown is also internally coherent, but it conflicts with the chunk on every identity-bearing element for entry `172`: child name, parents, birth date/time, place/residence context, informant, and officer context. That supports the staged draft's conclusion that this is a severe conversion-control conflict.
- The staged draft properly separates the local row identity question from broader Pulgar-line identity bridges. Its low probabilities for Dario-related hypotheses are justified by the absence of direct names or relationship statements.

## Scoring

| Metric | Score / Value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register images are strong source material, but the image was not available for this proof review. |
| conversion_confidence_score | 0.38 | Low-mixed confidence because the chunk and QA packet agree with one another while the converted Markdown disagrees materially. |
| evidence_quantity_score | 0.68 | Adequate local evidence from staged draft, packet, QA note, chunk, converted file, and manifest; insufficient for independent image certification or broader identity bridges. |
| agreement_score | 0.44 | Agreement is strong inside the Pulgar/Arriagada derivative cluster but poor across all conversion outputs. |
| identity_confidence_score | 0.70 | Moderate confidence that the staged draft identifies a real row-control problem; low confidence for any identity beyond the local entry. |
| claim_probability | 0.76 | Probable that the staged draft's core claim is correct: entry `172` needs conversion-control review before use. |
| relevance_level | high | The conflict affects Pulgar/Arriagada evidence and has high risk for incorrect canonical attachment. |
| relevance_confidence | 0.93 | The relevance is clear from repeated Pulgar and Arriagada terms and explicit staging metadata. |
| canonical_readiness | hold_for_conversion_qa | Do not promote. Reconcile the missing image and conflicting conversion outputs first. |
| canonical_readiness_score | 0.10 | Very low readiness while image verification is unavailable and derivative files conflict. |

## Review Judgment

This staged draft is supportable as an identity-conflict analysis and should remain on `hold_for_conversion_qa`. The review accepts the draft's main risk assessment: the current conversion state cannot safely support canonical claims because two derivative readings assign entry `172` to different children and parents.

The review does not independently certify the Pulgar/Arriagada handwriting because the referenced source image and page image were unavailable in this workspace at review time. The source packet and QA note may reflect prior direct image review, but this proof review can only score that as staged QA evidence, not as a fresh visual confirmation.

No same-person merge, parent relationship bridge outside this row, Dario connection, or Juana-name normalization is ready. The only safe conclusion is that the staged conflict is real and conversion-control must resolve which row/image controls entry `172`.

## Next Action

Hold the staged draft for conversion QA. Conversion-control should restore or locate the source/page image, recheck physical row `172`, and then decide whether to supersede the current converted Markdown, revise the chunk, or preserve the conflict with an explicit source-image citation. After that, run a separate proof review for any proposed canonical child-parent claim or Pulgar-line identity bridge.
