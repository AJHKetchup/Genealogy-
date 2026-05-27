---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527074547308
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
reviewed_staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_quality_score: 0.90
conversion_confidence_score: 0.52
evidence_quantity_score: 0.72
agreement_score: 0.58
identity_confidence_score: 0.88
claim_probability: 0.90
relevance_level: critical
relevance_confidence: 0.97
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict Identity Analysis

## Blockers

- Canonical readiness remains `hold_for_conversion_qa` because the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the chunk, source packet, targeted QA note, and direct image review support the physical row `172` as `Jose del Carmen Segundo Pulgar Arriagada`.
- The father field should not be promoted with the chunk's terminal `S.`. The visible source and targeted QA support `Jose del Carmen Pulgar`; the suffix or terminal mark remains unresolved.
- The staged identity analysis does not prove any Dario-line bridge. It should not be used to attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.
- The staged identity analysis does not prove same-person identity between the 1888 parents and other Jose/Juana parent candidates. `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` must remain unresolved candidate/variant contexts until separately reviewed.

## Scoring

- source_quality_score: 0.90
- conversion_confidence_score: 0.52
- evidence_quantity_score: 0.72
- agreement_score: 0.58
- identity_confidence_score: 0.88
- claim_probability: 0.90
- relevance_level: critical
- relevance_confidence: 0.97
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The cited source image is available and directly relevant: page 58, physical row `172` visibly aligns with the Pulgar/Arriagada entry.
- Direct visual review supports the core row-control claim: child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date/time `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, birth place `Calle de Valdivia`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The assigned chunk agrees with the Pulgar/Arriagada row for entry `172`, except for the unresolved terminal mark after the father's surname.
- The staged identity analysis handles the conflict conservatively: it separates image-reviewed row control from derivative conversion conflict, keeps Dario-line attachment blocked, and keeps parent-candidate identity bridges below promotion readiness.

## Review Judgment

The staged identity analysis is well supported as a conflict analysis and row-control judgment. The source image and assigned chunk make it highly probable that the physical entry `172` on this page is the Pulgar/Arriagada birth registration rather than the Burgos/de la Cruz entry currently present in the converted Markdown.

This review accepts the staged analysis as a reliable staged finding, but not as canonical-ready evidence. The disagreement between the converted Markdown and the source-image-reviewed row is material and tree-impacting. Canonical claims, relationships, parent-pair promotion, duplicate-person handling, and Dario-line attachment should remain held until conversion-control reconciles or supersedes the conflicting derivative conversion.

## Next Action

Send the converted Markdown and chunk set to conversion-control for reconciliation against the source image. After conversion-control resolves the derivative conflict, run a focused parent-identity proof review before merging or linking `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar` to any existing parent candidates.
