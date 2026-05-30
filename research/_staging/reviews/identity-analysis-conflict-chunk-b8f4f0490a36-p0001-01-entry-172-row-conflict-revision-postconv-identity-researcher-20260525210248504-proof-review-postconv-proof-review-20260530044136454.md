---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530044136454
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_conflict_note: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_conversion_page_markdown: "raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-markdown/page-0001.md"
source_image_status: missing_from_recorded_paths
source_quality_score: 0.82
conversion_confidence_score: 0.25
evidence_quantity_score: 0.45
agreement_score: 0.18
identity_confidence_score: 0.40
claim_probability: 0.86
pulgar_row_claim_probability: 0.50
relevance_level: high
relevance_confidence: 0.80
canonical_readiness: hold_for_conversion_qa
created: 2026-05-30
---

# Proof Review: Entry 172 Row Conflict Identity Analysis

This review covers the exact staged draft `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md`.

## Blockers First

1. Canonical readiness remains `hold_for_conversion_qa`. The staged draft correctly identifies a row-level conflict between the assigned chunk/source packet and the current converted Markdown.
2. The source image cannot be visually checked from the recorded source path or the manifest page-image path. The missing image prevents handwriting-level certification of either row reading in this proof-review pass.
3. The assigned chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
4. The converted Markdown and conversion-job page Markdown identify entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
5. These are incompatible row identities. The conflict changes child, parents, birth date, time, place, residence/informant context, and family relevance.
6. No relationship claim involving Pulgar/Arriagada parents, no child identity claim, and no Dario-line bridge is promotion-ready from this staged draft.
7. The father-field form `Jose del Carmen Pulgar S.` remains uncertified at source-image precision. Do not normalize it to `Jose del Carmen Pulgar` unless a later visual QA note supports that reading.

## Evidence Strengths

- The staged draft accurately reports the conflict found in the reviewed source packet, assigned chunk, converted file, conversion-job page Markdown, and staged conflict note.
- The underlying source type is a civil birth register, which would normally be strong evidence for a birth identity and parent-child relationship if the row reading were visually certified.
- The source packet and chunk provide a coherent Pulgar/Arriagada row, and the converted Markdown provides a coherent Burgos/de la Cruz row; the problem is assignment/control, not a minor transcription variant.
- The staged draft appropriately treats Dario-line relevance as anti-conflation context only. The reviewed materials do not name Dario or provide a direct bridge to any Dario identity cluster.

## Scored Judgment

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth-register evidence is potentially strong, but the image was unavailable for this review. |
| conversion_confidence_score | 0.25 | The chunk/source packet and converted Markdown disagree at row level, and the image could not be rechecked. |
| evidence_quantity_score | 0.45 | Several local derivatives were reviewed, but they are not independent enough to overcome the row conflict. |
| agreement_score | 0.18 | Agreement is low because the derivative witnesses split into Pulgar/Arriagada versus Burgos/de la Cruz readings. |
| identity_confidence_score | 0.40 | Identity confidence for any person claim from entry 172 is low until row control is resolved. |
| claim_probability | 0.86 | The staged draft's core claim, that this is a blocking row-level conversion conflict, is well supported. |
| pulgar_row_claim_probability | 0.50 | The Pulgar/Arriagada row is plausible from the chunk/source packet but not visually certified here. |
| relevance_level | high | If the Pulgar row controls, it is highly relevant to Pulgar/Arriagada parent candidates; otherwise it is not family-relevant. |
| relevance_confidence | 0.80 | The relevance assessment is clear, but conditional on row-control QA. |
| canonical_readiness | hold_for_conversion_qa | No canonical promotion, merge, or relationship attachment should proceed. |

## Review Decision

The staged draft is supported as a conflict/hold analysis. It should not be revised into a promoted proof statement because the underlying entry-172 row is not controlled. The draft's caution against same-person treatment, parent attachment, and Dario-line linkage is appropriate.

## Next Action

Run targeted conversion QA against the actual page image, including the manifest SHA `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2` if available. The QA note must decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and must certify the father field only as far as visible: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical claim or relationship is promoted.
