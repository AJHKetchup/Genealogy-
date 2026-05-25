---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525215630512
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-analysis-20260525211749345.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-analysis-20260525211749345.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict Identity Analysis

## Blockers First

- The staged identity analysis is correctly held because the assigned converted Markdown and assigned chunk do not describe the same entry 172 row. The chunk/source-packet/conflict side identifies `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the converted Markdown identifies `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This is not a name-variant problem. The child, parents, birth date, birth place, declarant, surrounding entries, and official/signature context differ between derivative transcriptions.
- The reviewed source image visually supports the Pulgar/Arriagada row for page 58, entry 172 at a high level, but this proof review should not silently overwrite the converted Markdown. The controlling transcription and the father-field reading still require targeted conversion QA.
- No Dario-line same-person claim, relationship bridge, parent merge, or canonical attachment is supported by this source review. Entry 172 does not visibly or derivatively name Dario, Arturo, Smith, Pulgar-Smith, or Darío Pulgar Arriagada.
- The father field must remain unresolved as recorded in the derivative set, with QA needed before choosing among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Evidence Strengths

- The staged identity analysis accurately reports the core mismatch among the source packet, conflict draft, chunk, and converted Markdown.
- The source packet and conflict draft both state the promotion recommendation as hold for conversion QA, matching the severity of the row-level conflict.
- The assigned chunk gives a detailed full-row transcription for page 58, entry 172 with Pulgar/Arriagada names, dates, residences, and declarant.
- The source image is a civil birth register page, a high-quality source type for birth identity and parent-child relationship claims once transcription is settled.
- The identity analysis properly treats Dario comparisons as anti-conflation context rather than direct evidence.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a strong source type for the narrow birth row, but the current task is evaluating conflicted derivatives rather than certifying a fresh transcription. |
| conversion_confidence_score | 0.42 | The image and chunk favor a Pulgar/Arriagada row, yet the assigned converted Markdown contains a mutually incompatible Burgos/de la Cruz row. |
| evidence_quantity_score | 0.68 | Multiple local artifacts were reviewed, but they are not independent sources and mostly document the same conversion conflict. |
| agreement_score | 0.46 | Chunk, source packet, conflict draft, and image-level inspection agree broadly on Pulgar/Arriagada; assigned converted Markdown sharply disagrees. |
| identity_confidence_score | 0.64 | Pulgar/Arriagada is the leading row hypothesis, but identity confidence is capped by the unresolved derivative conflict and father-field uncertainty. |
| claim_probability | 0.66 | The identity analysis's hold conclusion is well supported; promotion-ready Pulgar/Arriagada claims remain only probable pending QA. |
| relevance_level | high | If confirmed, entry 172 directly concerns a Pulgar child and Arriagada mother in the relevant family cluster. |
| relevance_confidence | 0.88 | Family relevance is strong for the Pulgar/Arriagada reading and low for the Burgos/de la Cruz reading; resolving assignment is therefore essential. |
| canonical_readiness | 0.12 | Hold. Do not promote claims, relationships, merges, or canonical page edits until conversion QA resolves row identity and father wording. |

## Review Decision

Hold the staged identity analysis for targeted conversion QA. The draft's blocker-first conclusion is supported: the evidence is sufficient to justify a high-priority row-conflict hold, but not sufficient to promote child identity, birth facts, father relationship, mother relationship, or any Dario-line comparison.

## Next Action

Perform targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and source packet. The QA note should explicitly state whether entry 172 controls as the Pulgar/Arriagada row or the Burgos/de la Cruz row, and if Pulgar/Arriagada controls, should certify the father field without normalizing away uncertainty.

After QA, rerun proof review before any canonical promotion.
