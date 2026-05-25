---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525205452095
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525205500000.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525205500000.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525205500000.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion-Conflict Identity Analysis

## Blockers First

- Conversion blocker: the assigned chunk and source image support a Pulgar/Arriagada row at page 58, entry 172, while the current assigned converted Markdown records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- Row-control blocker: this is not a minor name or spelling variance. The child, parents, birth date, birth place, declarant, and surrounding page context materially differ between the converted Markdown and the reviewed chunk/source-image context.
- Father-field blocker: the chunk reads `Jose del Carmen Pulgar S.`, but proof review should not normalize the father beyond the visible and QA-certified reading. The staged draft correctly holds this for targeted conversion QA.
- Identity-risk blocker: the reviewed entry does not name Dario. No merge, bridge, or relationship jump to any Dario/Dario Jose/Dario Arturo Pulgar identity is supported by this source alone.
- Canonical-readiness blocker: no child identity, birth fact, parent-child relationship, parent identity normalization, or Dario-line comparison from this staged draft is ready for canonical promotion.

## Evidence Strengths

- The staged draft accurately describes the current converted-file conflict: the converted file has the Jose Miguel / Oswaldo Burgos / Concepcion de la Cruz row for entry 172, not the Pulgar/Arriagada row.
- The assigned chunk gives a complete Pulgar/Arriagada row for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, male; birth 8 March 1888 at 3 p.m.; place Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; compareciente `Ernesto Herrera L.`
- Direct source-image review supports the broad Pulgar/Arriagada row on page 58, entry 172, including the child name, parents, and Calle de Valdivia / Calle de Colipi locality context.
- The staged draft correctly recommends `hold_for_conversion_qa` and preserves anti-conflation boundaries.

## Scored Judgment

| Dimension | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth-register image is a strong source type; the image is usable but not ideal for resolving every handwritten mark or suffix. |
| conversion_confidence_score | 0.40 | The reviewed chunk and image agree broadly, but the assigned converted Markdown conflicts at the row level. |
| evidence_quantity_score | 0.62 | One direct register row plus derivative chunk/source-packet evidence; no independent corroborating record was reviewed for this task. |
| agreement_score | 0.50 | Staged draft, source packet, chunk, and image align on the conflict; converted Markdown remains materially discordant. |
| identity_confidence_score | 0.67 | Pulgar/Arriagada identity is plausible from image/chunk, but row control and father suffix require QA. |
| claim_probability | 0.65 | More likely than not that the intended visible entry is the Pulgar/Arriagada row, but not proof-ready until conversion QA reconciles the file conflict. |
| relevance_level | high | The row is directly relevant to the proposed child identity and parent facts. |
| relevance_confidence | 0.94 | All reviewed materials point to the same source image and page 58, entry 172, despite the conversion conflict. |
| canonical_readiness | 0.10 | Hold. Requires targeted conversion QA before any canonical promotion. |

## Claim-Level Assessment

| Claim Or Hypothesis | Probability | Readiness | Notes |
| --- | ---: | --- | --- |
| Entry 172 is the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.65 | Hold | Supported by chunk and visible image; blocked by assigned converted-file disagreement. |
| Father is `Jose del Carmen Pulgar S.`. | 0.53 | Hold | Chunk supports the suffix reading, but final suffix/mark should be certified by conversion QA. |
| Father can be normalized as `Jose del Carmen Pulgar`. | 0.45 | Hold | Base-name reading is plausible, but normalization would exceed this proof-review scope. |
| Mother is `Juana Arriagada de Pulgar`. | 0.66 | Hold | Supported by chunk and visible row; still dependent on row-control QA. |
| The converted Markdown's Jose Miguel / Oswaldo Burgos row controls this source page entry 172. | 0.25 | Hold | Converted file is coherent internally but conflicts with the visible image context reviewed here. |
| Any Dario identity is directly supported by this entry. | 0.01 | Not ready | No Dario individual appears in the reviewed entry. |

## Relationship And Conflict Review

- Parent-child relationships from the Pulgar/Arriagada row are relevant but must remain staged-only until conversion QA resolves the controlling row.
- The staged draft makes no unsupported promotion claim and correctly treats the conflict as a conversion/file-assignment problem.
- The anti-conflation instruction is necessary: shared Pulgar/Arriagada context does not prove identity with later Dario-line candidates.

## Next Action

Keep this staged identity-analysis draft at `hold_for_conversion_qa`. Run targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and source packet to certify the controlling entry-172 row and the father field reading. After that QA note exists, rerun proof review for the child identity, birth facts, and parent-child relationships before any canonical promotion.
