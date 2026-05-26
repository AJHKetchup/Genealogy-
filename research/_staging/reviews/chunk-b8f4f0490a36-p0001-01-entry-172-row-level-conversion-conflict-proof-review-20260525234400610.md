---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525234400610
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-25
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. **Canonical converted-file conflict:** the assigned chunk/source packet and the page image support entry 172 as the Pulgar/Arriagada row, but the current converted Markdown for the same source path records a materially different Burgos/de la Cruz row. This blocks canonical promotion until conversion QA reconciles the converted file against the source image and chunk.
2. **Father-name precision blocker:** the visible record and chunk support a father named `Jose del Carmen Pulgar`, but the final suffix/mark after `Pulgar` is not proof-ready from this review alone. Keep the exact form open as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted QA certifies it.
3. **Relationship/identity jump blocker:** the staged draft correctly avoids merging the entry-172 father with other `Jose del Carmen Pulgar` candidates and avoids attaching this entry to any Dario identity. The entry does not name Dario.
4. **No source-transcription edit authorized:** this review may confirm that the row-control conflict is real and that the image favors the chunk reading, but it should not rewrite the converted Markdown or canonical wiki pages.

## Evidence Checked

- Staged identity analysis: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md`
- Conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Evidence Strengths

- The source image visibly places entry 172 on page 58 as a Pulgar/Arriagada birth registration, matching the assigned chunk and source packet rather than the current converted Markdown.
- The chunk/source packet evidence supports a civil birth-registration event for `Jose del Carmen Segundo Pulgar Arriagada`, with parents in the Pulgar/Arriagada family context and an informant separate from the father.
- The staged identity analysis handles the conflict conservatively: it keeps the Burgos/de la Cruz converted-file reading separate, treats row control as unresolved at the artifact level, and blocks Dario attachment.
- The source type is a contemporary civil birth register, so the underlying source quality is strong once the row and transcription are certified.

## Scores

- source_quality_score: 0.88
- conversion_confidence_score: 0.42
- evidence_quantity_score: 0.62
- agreement_score: 0.55
- identity_confidence_score: 0.66 for the entry-172 child as `Jose del Carmen Segundo Pulgar Arriagada`; 0.40 for the exact father suffix; 0.05 for any Dario identity attachment
- claim_probability: 0.76 that entry 172 is the Pulgar/Arriagada row shown in the chunk/source packet; 0.38 that the exact father form includes a literal `S.` suffix; 0.05 that this evidence directly supports any Dario merge
- relevance_level: high for Pulgar/Arriagada family reconstruction; low for direct Dario identity proof
- relevance_confidence: 0.86 for Pulgar/Arriagada relevance; 0.18 for Dario relevance
- canonical_readiness: hold_for_conversion_qa

## Claim Judgment

The staged draft is supported as a conflict analysis. It should remain staged and should not promote child identity, birth facts, parent-child relationships, parent identity merges, or any Dario-related bridge.

The strongest supported judgment is that the current converted Markdown is not controlling the same visible row as the assigned chunk/source packet. The Pulgar/Arriagada row is probable from the page image and chunk, but canonical readiness remains blocked because the repository's converted Markdown artifact still disagrees materially.

## Next Action

Run targeted conversion QA for this source image, assigned chunk, and converted Markdown. QA should certify row control for entry 172 and record the father field only to the visible extent. After that, rerun proof review before any canonical promotion or identity merge.
