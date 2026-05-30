---
type: proof_review
status: hold
role: claim_reviewer
worker: "postconv-proof-review-20260530102037149"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md"
reviewed_source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530072501797.md"
reviewed_conversion_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530072501797.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530072501797.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: hold
source_quality_score: 0.86
conversion_confidence_score: 0.42
evidence_quantity_score: 0.54
agreement_score: 0.36
identity_confidence_score: 0.58
claim_probability: 0.70
relevance_level: direct
relevance_confidence: 0.96
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers only the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530092229282.md` and its referenced verification context.

## Blockers First

- Canonical readiness is `hold`. The original full-page PNG referenced as `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` is not present in this checkout, so this proof review cannot certify full-page row control.
- The referenced chunk and the current converted Markdown materially disagree for entry `172`. The chunk records `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`; the converted Markdown records `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- Existing staged crop assets visibly support a Pulgar/Arriagada parent and informant field, but the crops do not by themselves prove the entry number, full-row alignment, or the complete birth row.
- The father suffix after `Jose del Carmen Pulgar` remains uncertified. Preserve the staged caution and do not promote `Jose del Carmen Pulgar S.` as a normalized identity.
- No Dario/Dario Arturo/Dario Jose identity bridge is supported by this staged draft. Surname overlap is not enough for a same-person or family-link promotion.
- Relationship promotion remains blocked because the competing derivative readings assign different children, parents, dates, and places to entry `172`.

## Evidence Strengths

- The staged identity-analysis note accurately identifies the issue as a row-control conflict rather than a name variant or merge candidate.
- The reviewed chunk directly supports the Pulgar/Arriagada reading for entry `172`, including child name, sex, registration date, birth date/time/place, parent fields, and informant.
- The reviewed conversion QA note correctly preserves the missing-original-image limitation and recommends `hold_for_conversion_qa`.
- The current converted Markdown confirms the conflict by giving a different entry-172 family group, making the staged draft highly relevant to conversion QA.
- The civil birth register is a strong source type for the narrow facts recorded in the row once row control is certified.

## Scores

| Dimension | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth registration is high-quality for birth and parent fields, but review is derivative-only because the original full-page image is missing. |
| conversion_confidence_score | 0.42 | Chunk and crop evidence favor Pulgar/Arriagada locally, while the converted Markdown conflicts materially and row control is not independently certified here. |
| evidence_quantity_score | 0.54 | There is one chunk, one converted file, one source packet, one QA note, one conflict note, and two local crops; quantity is adequate for a hold judgment but insufficient for promotion. |
| agreement_score | 0.36 | Agreement is strong among the staged packet, QA note, conflict note, and chunk, but poor against the current converted Markdown. |
| identity_confidence_score | 0.58 | Moderate confidence for a local Pulgar/Arriagada row hypothesis; low confidence for any broader identity attachment. |
| claim_probability | 0.70 | The Pulgar/Arriagada interpretation is the leading hypothesis, but unresolved conversion conflict prevents a higher proof score. |
| relevance_level | direct | The staged draft directly concerns the assigned entry-172 conversion conflict. |
| relevance_confidence | 0.96 | All reviewed materials point to the same row-control problem. |
| canonical_readiness | hold | Do not promote or merge until full-page source-image row control is resolved. |

## Judgment

The staged identity-analysis draft is supported as a cautious conflict analysis and should remain held. Its core conclusion is proof-review appropriate: this is a conversion row-control conflict, not an identity merge, not a spelling variant, and not a basis for attaching the Pulgar/Arriagada row to any Dario-line candidate.

The score applies to the conflict-analysis judgment, not to promotion of the underlying birth or parent-child facts. The underlying Pulgar/Arriagada row facts may be probable, but they are not canonical-ready from the available verification context.

## Next Action

Keep this staged draft at `hold_for_conversion_qa`. The next worker should perform original full-page image review for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then decide which physical row controls entry `172` and whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an explicitly uncertain form.
