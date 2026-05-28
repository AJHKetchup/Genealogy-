---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260528130809162
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
recommendation: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Derivative-control blocker: the current converted Markdown and the current chunk carry the same source/conversion identifiers but describe different entry-172 rows. The converted Markdown reads a Burgos/de la Cruz child, while the chunk and source packet read a Pulgar/Arriagada child.
2. Canonical-readiness blocker: no child identity, birth fact, parent name, parent-child relationship, or Pulgar/Arriagada-to-Dario comparison should be promoted until a targeted conversion QA note resolves which derivative controls entry 172.
3. Literal-transcription blocker: the father field in the Pulgar/Arriagada row remains a visible-reading issue. This review must not normalize `Jose del Carmen Pulgar S.` to a fuller identity or silently drop the suffix.
4. Identity-risk blocker: the staged identity analysis properly treats the Burgos/de la Cruz and Pulgar/Arriagada readings as different row candidates, not as variants of one person or family. Any merge or relationship bridge would be unsupported.
5. Relevance-boundary blocker: this row does not name Dario, Arturo, Smith, or a later Pulgar-Arriagada public-role identity. It can only be relevant background after row control is certified.

## Evidence Checked

- Staged draft under review: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md`.
- Referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Review Judgment

The staged identity analysis is supported as a cautious hold note. The converted Markdown gives entry 172 as `Jose Miguel`, father/informant `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. The chunk and source packet give entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888.

The source image, checked only for verification, visibly aligns with the chunk/source-packet Pulgar/Arriagada row for entry 172. However, the converted Markdown conflict is still present in the controlled derivative set, so the correct proof action remains hold for conversion QA rather than canonical promotion from this review.

The staged analysis does not overclaim a Dario bridge and correctly separates verification context from source transcription. Its strongest point is the clear identification of a row-control problem; its main limitation is that formal conversion QA has not yet reconciled the derivative files.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a direct original-record source for the row, and the visible entry is usable though small/handwritten. |
| conversion_confidence_score | 0.40 | The chunk and image support one reading, but the converted Markdown contradicts the same entry number and blocks derivative confidence. |
| evidence_quantity_score | 0.55 | One direct source image plus two derivative transcriptions were checked; no independent corroborating record was reviewed or needed for this task. |
| agreement_score | 0.45 | Source packet, chunk, and image agree broadly, but the converted Markdown is in direct row-level disagreement. |
| identity_confidence_score | 0.52 | Good confidence that the competing row candidates are distinct; insufficient confidence for canonical identity attachment until QA resolves control. |
| claim_probability | 0.58 | The Pulgar/Arriagada row is probable from the image/chunk, but the claim remains below promotion threshold because controlled derivatives conflict. |
| relevance_level | high | If certified, the row directly concerns the Pulgar/Arriagada family line. |
| relevance_confidence | 0.86 | The surnames and parent/child structure are directly relevant, while broader Dario linkage is not supported by this row alone. |
| canonical_readiness | not_ready | Hold for targeted conversion QA; do not promote claims, relationships, or merges. |

## Evidence Strengths

- The staged draft accurately identifies the central conflict as row control/conversion control, not a same-person or name-variant problem.
- The chunk and source packet provide detailed, internally consistent Pulgar/Arriagada facts for entry 172.
- The page image visibly supports the chunk/source-packet row placement for entry 172, increasing the likelihood that the converted Markdown is the outlier derivative.
- The staged draft appropriately refuses Dario/Arturo/Smith and later Pulgar-Arriagada bridges from this source alone.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, converted Markdown, current chunk, and source packet. The QA note should record the controlling entry-172 row and, if the Pulgar/Arriagada row controls, certify the father field only to the visible level (`Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`). After that, review only the certified row's narrow child, birth, parent, informant, and parent-child claims.
