---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528133323762
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
output_area: "research/_staging/reviews/"
canonical_readiness: not_ready
recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md`.

## Blockers First

1. Conversion-control blocker: the referenced converted Markdown and referenced chunk give incompatible entry-172 families. The converted Markdown reads `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the chunk reads `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
2. Canonical-readiness blocker: no child identity, birth fact, parent-child relationship, parent identity merge, or Pulgar/Arriagada bridge should be promoted from this staged draft until targeted conversion QA resolves row control.
3. Father-literal blocker: the Pulgar/Arriagada reading should preserve the father field at the certified visible level only. The draft's caution between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` is warranted.
4. Relationship-jump blocker: the source does not name Dario, Arturo, Smith, or any later Pulgar-Arriagada candidate. A Dario-family bridge cannot be inferred from surname pattern or later local context.

## Verification Context

- Staged identity-analysis draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md`.
- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md`.
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

The source image was checked only as verification context. It visibly supports the chunk/source-packet side of the conflict: page 58 entry 172 appears to be the Pulgar/Arriagada registration, not the Burgos/de la Cruz registration in the converted Markdown.

The chunk and source packet agree on the core Pulgar/Arriagada fields: registration date 7 April 1888, child `Jose del Carmen Segundo Pulgar Arriagada`, male sex, birth on 8 March 1888 at 3 p.m., birthplace `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`. A civil birth register is a strong source type for these narrow claims once the row-control problem is formally certified.

The staged draft correctly treats the issue as row-level conversion conflict, not a same-person conflict, duplicate-person finding, or normalized name variant. It also correctly blocks any Dario/Arturo/Smith attachment.

## Scored Judgment

| Dimension | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is direct, contemporaneous evidence for birth and parent claims; image is usable but handwritten. |
| conversion_confidence_score | 0.40 | Image, chunk, and source packet favor Pulgar/Arriagada, but the official converted Markdown attached to the source gives a contradictory row. |
| evidence_quantity_score | 0.55 | One source image plus agreeing chunk/source packet; no independent corroborating source was reviewed for this task. |
| agreement_score | 0.45 | Agreement is good among image/chunk/source packet, but the converted Markdown sharply disagrees. |
| identity_confidence_score | 0.62 | Moderate confidence for the Pulgar/Arriagada row as visible entry 172; low confidence for canonical attachment until QA resolves derivative control. |
| claim_probability | 0.68 | Pulgar/Arriagada row claims are probable from the visible source and chunk, but not promotable while derivative conflict persists. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada family-line review if certified. |
| relevance_confidence | 0.90 | The row explicitly names Pulgar and Arriagada; relevance does not depend on a Dario bridge. |
| canonical_readiness | not_ready | Hold for targeted conversion QA, then review only the certified row claims. |

## Claim Probability Notes

- Pulgar/Arriagada as controlling entry-172 row for the referenced image: 0.68. The visual check, chunk, and source packet align, but the converted Markdown conflict blocks promotion.
- Burgos/de la Cruz as controlling entry-172 row for the referenced image: 0.18. It is internally coherent in the converted Markdown, but not supported by the visual check of the referenced page image.
- Father literal `Jose del Carmen Pulgar S.`: 0.55. The chunk/source packet read this way and the image is broadly consistent, but the suffix is a small handwriting detail requiring QA certification.
- Mother literal `Juana Arriagada de Pulgar`: 0.72. Supported by the chunk/source packet and visible row context, still dependent on row-control QA.
- Any same-person or family bridge claim to Dario/Arturo/Smith candidates: 0.03. The row provides no direct bridge.

## Next Action

Hold for targeted conversion QA. The QA note should compare the source image, converted Markdown, chunk, and source packet for page 58 entry 172; identify the controlling row; and certify the father field only to the visible extent. After that, run narrow proof review only for the certified child identity, registration date, birth date/time, birthplace, father claim, mother claim, informant claim, and parent-child relationships.
