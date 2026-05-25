---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525161006105
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Conversion Conflict Identity Analysis

## Blockers First

1. The staged draft correctly identifies a material row-level conflict between the referenced chunk/source packet and the referenced converted Markdown, so no canonical claim, relationship, merge, or Dario-line bridge is ready.
2. The staged draft's conflict wording needs revision because it says the converted Markdown assigns entry 172 to `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`. The current referenced converted file instead records entry 172 as `Jose Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`.
3. The source image and chunk support a Pulgar/Arriagada entry 172, but the exact father ending remains a conversion-QA item. The visible source is consistent with `Jose del Carmen Pulgar` plus a possible trailing mark or abbreviation; it should not be normalized beyond source-visible support.
4. The reviewed evidence does not name Dario, Arturo, Smith, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada. Any Dario-line bridge remains unsupported by this entry.
5. Derivative local context and prior staged reviews should not be treated as independent corroboration while the controlling conversion record is conflicted.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md`.
- Conflict draft referenced by the staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image visibly places entry 172 on page 58 and supports the child as `Jose del Carmen Segundo Pulgar Arriagada`, male, with birth date 8 March 1888, place Calle de Valdivia, father `Jose del Carmen Pulgar...`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The chunk and source packet are aligned with the visible source image for the Pulgar/Arriagada row.
- Civil birth registration is a strong source class for a child-parent event when the row assignment and literal transcription are stable.
- The staged draft is appropriately conservative about canonical readiness and Dario-line attachment.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil registration image is a strong original/near-original source class; image legibility is usable but handwriting leaves a narrow father-ending uncertainty. |
| conversion_confidence_score | 0.48 | The chunk/source packet match the image, but the referenced converted Markdown describes a different entry set. |
| evidence_quantity_score | 0.58 | There is one relevant source image plus derivative transcriptions; no independent corroborating source was reviewed or needed for this proof review. |
| agreement_score | 0.56 | Source image, chunk, and source packet agree on the Pulgar/Arriagada row; converted Markdown conflicts, and the staged draft misstates the current converted file's conflicting names. |
| identity_confidence_score | 0.78 for the Pulgar/Arriagada row; 0.04 for any Dario-line bridge | The row identity is visually supported, but Dario identity evidence is absent. |
| claim_probability | 0.82 that source entry 172 is the Pulgar/Arriagada birth row; 0.04 that it supports a Dario identity bridge | The image strongly favors Pulgar/Arriagada for entry 172, but derivative conversion conflict still blocks promotion. |
| relevance_level | high | The entry directly names Pulgar and Arriagada candidates. |
| relevance_confidence | 0.92 | Family relevance is clear if the Pulgar/Arriagada reading is the target research cluster. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until the converted-file conflict and father-ending uncertainty are resolved in conversion QA. |

## Claim Review

The staged draft's core recommendation to hold for conversion QA is supported. The visible source image and the chunk/source packet support the Pulgar/Arriagada entry rather than the currently referenced converted Markdown. However, the staged draft should be revised before downstream use because it inaccurately reports the converted Markdown's conflicting row as `Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz`; the current converted file says `Jose Miguel` / `Oswaldo Bunster` / `Amelia de la Maza`.

The father should remain unresolved as an exact literal form until conversion QA. The source image supports `Jose del Carmen Pulgar` with a possible suffix/mark, but this proof review should not force a normalized reading beyond what the source visibly supports.

## Next Action

Hold the staged identity analysis for targeted conversion QA. The QA note should reconcile the source image, chunk, source packet, and converted Markdown; correct the converted-row conflict summary; and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim, parent-child relationship, parent merge, or Dario-line comparison is promoted.
