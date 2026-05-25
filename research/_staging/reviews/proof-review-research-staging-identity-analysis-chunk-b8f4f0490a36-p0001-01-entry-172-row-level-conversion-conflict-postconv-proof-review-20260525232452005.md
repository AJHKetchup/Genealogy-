---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260525232452005"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230105907.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230105907.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_page: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. Do not promote child identity, birth facts, parent names, parent-child relationships, parent merges, or Dario-line comparisons from this staged draft until conversion-control QA resolves why the converted Markdown and chunk disagree.
- The referenced converted file gives entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The referenced chunk, source packet, conflict draft, and visible source page give entry 172 on page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- These are not name variants or duplicate-person evidence. The conflict changes the child, parents, birth date, birth place, and informant.
- The father-name suffix remains a transcription-risk point. I can see support for `Jose del Carmen Pulgar` and an apparent trailing initial/suffix, but this proof review should not certify beyond the staged wording without targeted conversion QA.

## Evidence Strengths

- The source type is a civil birth register, which is a strong original-record class for birth identity and parent-name claims.
- The page image visibly supports the chunk/source-packet row order: page 58 includes entries 171, 172, and 173; entry 172 is the middle row and reads as a Pulgar/Arriagada registration rather than the Burgos/de la Cruz text in the converted file.
- The staged identity-analysis draft accurately characterizes the problem as a row-level conversion conflict and correctly recommends holding promotion.
- The draft correctly treats Dario/Pulgar comparisons as anti-conflation checks only. Entry 172 does not visibly name Dario, Arturo, Smith, Pulgar-Smith, or a later Dario identity bridge.

## Scorecard

| Metric | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth-registration page is a strong source type; image quality is usable but handwriting and suffix details require care. |
| conversion_confidence_score | 0.34 | The converted Markdown conflicts materially with the chunk, source packet, conflict draft, and visible page image. |
| evidence_quantity_score | 0.62 | There is one direct source page plus derivative chunk/source-packet readings; quantity is modest but directly relevant. |
| agreement_score | 0.46 | Chunk, source packet, conflict draft, and image agree on Pulgar/Arriagada, but the referenced converted file disagrees completely. |
| identity_confidence_score | 0.58 | The visible entry-172 identity is probably Pulgar/Arriagada, but conversion-control conflict blocks certification. |
| claim_probability | 0.91 | The staged draft's main claim, that this is a serious row-level conversion conflict requiring hold/QA, is strongly supported. |
| relevance_level | direct | The reviewed evidence is exactly the assigned entry-172 row and its conversion conflict. |
| relevance_confidence | 0.99 | All reviewed materials reference the same staged draft, source packet, chunk id, and source page. |
| canonical_readiness | 0.05 | Hold. The evidence is useful for QA direction, not ready for canonical identity or relationship promotion. |

## Claim Review

- Supported: The draft's blocker that the converted Markdown and chunk/source-packet readings identify different entry-172 families is supported.
- Supported: The draft's warning against merging `Jose del Carmen Segundo Pulgar Arriagada` with `José Miguel` is supported.
- Supported: The draft's warning against Dario-line promotion or same-person inference is supported; the source page supplies no Dario bridge.
- Revise before promotion: The Pulgar/Arriagada row can be treated as source-image-supported for QA triage, but not as a canonical identity claim until the converted file is corrected or superseded by a targeted QA note.
- Revise before promotion: Father field should remain bounded as `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` until QA certifies the suffix.

## Next Action

Run targeted conversion QA on the source image, converted Markdown, chunk, and source packet. The QA note should decide the controlling entry-172 row, explain whether the converted Markdown belongs to a different page/register image or is a row-control error, and certify the father-name field only to the visible extent. After that, rerun proof review for any atomic child, birth, parent-name, and parent-child claims.
