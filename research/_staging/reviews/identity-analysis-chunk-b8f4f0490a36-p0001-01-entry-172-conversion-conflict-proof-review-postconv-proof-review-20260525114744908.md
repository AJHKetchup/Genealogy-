---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525114744908
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525091344655.md
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525091344655.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525081514407.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
review_decision: hold
canonical_readiness: blocked
---

# Proof Review: Entry 172 Identity Conflict

## Blockers

1. The assigned converted Markdown and the current chunk materially disagree for entry 172. The converted file reads `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`; the chunk reads `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
2. The source image visibly supports the Pulgar/Arriagada row for entry 172 more strongly than the converted Markdown, but this proof review should not rewrite the source transcription. A targeted conversion QA note is still required to supersede or reconcile the converted Markdown.
3. The father-name ending remains uncertain for canonical use. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as separate verification outcomes until QA certifies the visible reading.
4. No parent relationship, same-person merge, duplicate-person merge, Dario-line bridge, or canonical wiki promotion is ready from this draft.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth registration image is direct, contemporaneous evidence, but current use is constrained by derivative transcript disagreement. |
| conversion_confidence_score | 0.42 | The chunk and source packet agree, and the source image appears to support the chunk, but the assigned converted Markdown conflicts at row level. |
| evidence_quantity_score | 0.54 | Evidence consists of one source image plus conflicting derivative outputs; no independent corroborating source is reviewed here. |
| agreement_score | 0.48 | Chunk, source packet, and visible image trend together; converted Markdown is mutually inconsistent. |
| identity_confidence_score | 0.62 | Pulgar/Arriagada identity is plausible for the visible entry 172, but not stable enough for canonical identity action. |
| claim_probability | 0.64 | Probable that the source image entry 172 is the Pulgar/Arriagada registration, pending formal conversion QA. |
| relevance_level | high | If confirmed, this is direct evidence for the named child and parent candidates. |
| relevance_confidence | 0.92 | Pulgar and Arriagada names are visible/reported in the reviewed chunk and source packet, and the staged draft correctly limits Dario-line relevance. |
| canonical_readiness | blocked | Hold for conversion QA before any claim, relationship, merge, or wiki promotion. |

## Evidence Strengths

- The staged draft accurately identifies a row-level conflict rather than treating the Gomez/de la Cruz and Pulgar/Arriagada readings as name variants.
- The chunk and source packet consistently report entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, with mother `Juana Arriagada de Pulgar`, and the reviewed source image visibly aligns with that row structure.
- The staged draft properly separates literal evidence from interpretation and correctly warns against Dario-line conclusions from this entry alone.
- The recommendation to keep dependent identity and relationship work at `hold_for_conversion_qa` is supported.

## Review Judgment

Revise is not required for the staged identity analysis itself. Its conflict framing, uncertainty handling, and hold recommendation are supported by the reviewed files.

The claim set remains blocked for canonical use. The most likely supported direction is the Pulgar/Arriagada entry-172 reading, but the repository still contains an assigned converted Markdown file with a different entry-172 family. That conflict must be resolved by conversion QA before proof can be used for canonical person, parent, relationship, or Dario-line work.

## Next Action

Run targeted conversion QA against the source image, converted Markdown, chunk, and source packet. The QA note should explicitly decide whether the controlling entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row and should certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before promotion.
