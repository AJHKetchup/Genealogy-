---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260528171736093
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225231661.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225231661.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md
conflict_candidate: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This note reviews staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225231661.md`.

## Blockers First

- The staged draft is supported as an identity/conflict analysis, but it is not promotion-ready because the assigned chunk/source packet and assigned converted Markdown still disagree about the same entry number.
- The chunk and source packet read entry 172 as a Pulgar/Arriagada birth: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. on `Calle de Valdivia`.
- The converted Markdown reads entry 172 as a Burgos/de la Cruz birth: `José Miguel`, father/informant `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- These are incompatible child, parent, birth-date, birthplace, and informant claims. This is a row-control or conversion-control conflict, not a name variant or same-person problem.
- The father field in the Pulgar/Arriagada row remains a transcription-precision blocker. It should stay as `Jose del Carmen Pulgar S.` or be marked uncertain until targeted QA certifies the visible reading.
- No Dario, Arturo, Smith, medical-title, passenger, legal-notice, photograph, or lineage bridge appears in the reviewed entry. Any Dario-line attachment would be an unsupported relationship jump.

## Evidence Strengths

- The underlying source type is a civil birth register, which is high-quality primary evidence for a birth event, parent names, and informant details once row control is resolved.
- The source image, chunk, source packet, and conflict candidate support treating the Pulgar/Arriagada row as the relevant entry-172 candidate for this staged task.
- The staged identity analysis correctly keeps the item in `hold_for_conversion_qa` and does not promote a child identity, parent-child relationship, parent identity merge, or Dario-line bridge.
- The converted Markdown is useful negative evidence because it shows a materially different row/family assignment, making the conversion conflict explicit.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525225231661.md`
- Conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Assigned converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`
- Prior review context: `research/_staging/reviews/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-proof-review-20260525225023906.md`

## Scored Judgment

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth registration is strong primary evidence, but proof value is limited until the controlling row/conversion issue is certified. |
| conversion_confidence_score | 0.30 | The chunk/source packet and converted Markdown materially disagree on child, parents, date, place, and informant. |
| evidence_quantity_score | 0.64 | One source image plus several derivative/staged artifacts support the conflict assessment; they are not independent enough to resolve row control alone. |
| agreement_score | 0.42 | The source image, chunk, source packet, and conflict note align toward Pulgar/Arriagada; the converted Markdown directly contradicts them. |
| identity_confidence_score | 0.58 | The Pulgar/Arriagada row appears likely for the referenced image, but canonical person attachment remains blocked. |
| claim_probability | 0.68 | The narrow claim that this staged item is a row-level conversion conflict is well supported; the underlying Pulgar birth and relationships are not yet promotion-ready. |
| relevance_level | high | The conflict directly controls whether Pulgar/Arriagada birth and parent-child claims can be used. |
| relevance_confidence | 0.90 | Relevance to the Pulgar/Arriagada cluster is clear; relevance to Dario candidates is only anti-conflation context. |
| canonical_readiness | 0.10 | Hold for conversion QA. Not ready for canonical claims, relationships, people pages, family pages, or merges. |

## Review Decision

Hold for conversion QA. The staged identity analysis is acceptable as a conflict/anti-conflation note and its caution is supported. It should not be promoted or used as canonical evidence for a child identity, birth event, parent claim, parent-child relationship, duplicate merge, or Dario-line connection.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, source packet, and converted Markdown. The QA note should explicitly decide whether entry 172 controls as the Pulgar/Arriagada row or the Burgos/de la Cruz row, and it should certify the father field only to the visible source-supported extent.
