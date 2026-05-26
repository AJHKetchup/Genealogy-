---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260526231701601"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-held-postconv-evidence-extraction-20260526002943637.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-held-postconv-evidence-extraction-20260526002943637.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
reviewed_conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-26
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers

- Canonical promotion is blocked by a row-level conversion conflict. The converted Markdown assigns entry 172 to a Burgos/de la Cruz birth row, while the assigned chunk and source packet assign entry 172 to a Pulgar/Arriagada birth row.
- The source image visually supports the general Pulgar/Arriagada row for entry 172 more than the Burgos/de la Cruz converted text, but targeted conversion QA is still required because the controlling derivative file is contradictory and the father-field ending is not independently certified.
- The father field should not be normalized beyond visible support. The chunk reads `Jose del Carmen Pulgar S.`, but the review should hold until QA certifies whether the visible source supports `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No Dario, Arturo, Smith, Dario Jose, or later Dario Pulgar-Arriagada identity is directly named in this entry. Any Dario-line comparison or merge would be an unsupported relationship jump at this stage.

## Evidence Strengths

- The source is a civil birth register image, which is generally a strong source type for a birth registration, child name, parents, residence, informant, and registration date when the row is correctly controlled.
- The assigned chunk gives coherent row data for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on 8 March 1888 at about 3 p.m., Calle de Valdivia, and informant `Ernesto Herrera L.` present at the birth.
- Visual inspection of the referenced source image is consistent with the chunk's Pulgar/Arriagada reading at the row level and inconsistent with the current converted Markdown's Burgos/de la Cruz row for entry 172.
- The staged draft correctly treats the problem as a conversion row-control issue before treating it as an identity-linking issue.

## Scores

- source_quality_score: 0.86
- conversion_confidence_score: 0.35
- evidence_quantity_score: 0.45
- agreement_score: 0.30
- identity_confidence_score: 0.48
- claim_probability: 0.72 that the staged draft's hold-for-QA recommendation is correct; 0.58 that the Pulgar/Arriagada row is the correct entry 172 reading pending formal QA
- relevance_level: high
- relevance_confidence: 0.82
- canonical_readiness: hold_for_conversion_qa

## Review Judgment

The staged draft is supported as a conservative conflict analysis and should remain on hold. The source image and assigned chunk provide meaningful support for a Pulgar/Arriagada entry 172, but the current converted Markdown directly contradicts that reading. Because the conflict affects the child identity, parent identities, birth date, birthplace, residence, and informant, the evidence is not ready for canonical claims, relationships, identity merges, or Dario-line comparisons.

## Next Action

Route the source image, converted Markdown, assigned chunk, source packet, and conflict candidate to targeted conversion QA. QA should first certify the controlling row for entry 172 and then certify the father-field reading only to the visible extent. After QA updates or validates the derivative transcription, rerun proof review before any canonical promotion.
