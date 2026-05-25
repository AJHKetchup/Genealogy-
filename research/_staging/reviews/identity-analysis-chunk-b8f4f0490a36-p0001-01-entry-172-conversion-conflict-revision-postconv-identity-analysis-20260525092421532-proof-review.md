---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525120411651
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525092421532.md"
reviewed_staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525092421532.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

- Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525092421532.md`
- Review task id: `proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525092421532.md`
- Role: `claim_reviewer`
- Review status: `hold`
- canonical_readiness: `hold_for_conversion_qa`

## Blockers

- The assigned converted Markdown and the current chunk still disagree at the row level for entry 172. The converted file reads entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`; the chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- Because the controlling derivative artifacts conflict, no dependent identity, parent-child relationship, same-person merge, or Dario-line bridge is canonical-ready.
- The visible source image supports the Pulgar/Arriagada row more strongly than the converted-file Gomez/de la Cruz reading, but this proof review should not rewrite the source transcription. Conversion QA must reconcile or supersede the inconsistent converted file/chunk state.
- The father-name ending after `Pulgar` remains a literal-reading uncertainty. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted QA certifies the visible reading.
- The staged draft correctly refuses any bridge to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`; no such same-person or relationship jump is supported by this entry.

## Scoring

| Score | Value | Reason |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration image is an original-style source and is available for direct visual review. |
| conversion_confidence_score | 0.42 | The current chunk matches the visible row better than the converted file, but the workspace has unreconciled derivative transcripts for the same entry. |
| evidence_quantity_score | 0.60 | One direct source image plus derivative chunk/source-packet support; no independent corroborating source was reviewed or needed for this conflict judgment. |
| agreement_score | 0.48 | Chunk, source packet, and image broadly agree on Pulgar/Arriagada, while the assigned converted file materially disagrees. |
| identity_confidence_score | 0.72 | The image and current chunk support a distinct `Jose del Carmen Segundo Pulgar Arriagada` entry, but identity use is held by conversion conflict. |
| claim_probability | 0.78 | The Pulgar/Arriagada reading is probable from visual review and the current chunk, but not final until conversion QA resolves the derivative conflict. |
| relevance_level | critical | If confirmed, entry 172 directly concerns Pulgar/Arriagada identity and parent candidates. |
| relevance_confidence | 0.94 | The visible row and chunk contain Pulgar and Arriagada names; relevance is high if the row assignment is certified. |
| canonical_readiness | hold_for_conversion_qa | Do not promote dependent claims, relationships, identity merges, or lineage bridges until QA resolves the transcript conflict. |

## Evidence Strengths

- The staged identity analysis accurately identifies the disagreement as a material row-level conversion or assignment conflict, not a spelling variation.
- The source packet and chunk preserve a coherent Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`, registration date 7 April 1888, birth date 8 March 1888, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- Visual review of page 58, entry 172 supports the Pulgar/Arriagada row and does not support the converted file's Gomez/de la Cruz family for that visible row.
- The staged analysis appropriately treats existing wiki pages and Dario-line candidates as cautionary context only, not independent proof or merge support.

## Review Judgment

The staged identity analysis is supported as a conflict analysis and should remain on hold. Its main conclusion, `hold_for_conversion_qa`, is the correct proof posture because the image and chunk make the Pulgar/Arriagada reading probable, while the assigned converted Markdown still records a different child and parents for the same entry number.

This review does not authorize canonical promotion. The evidence is strong enough to justify targeted conversion QA and later proof review, but not strong enough to use the entry for canonical person, parent-child, same-person, or Dario-line conclusions while the derivative transcript conflict remains unresolved.

## Next Action

Run targeted conversion QA against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, the assigned converted Markdown, and the current chunk. QA should decide whether entry 172 is the Pulgar/Arriagada row, correct or retire the conflicting Gomez/de la Cruz converted reading as appropriate, and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any claim or relationship for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar [S./?]`, `Juana Arriagada de Pulgar`, or any proposed Dario-line bridge.
