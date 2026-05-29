---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528234722087
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Row-control remains blocked. The staged identity analysis, conflict draft, source packet, chunk, and source image support an entry 172 Pulgar/Arriagada row, while the referenced converted Markdown gives an incompatible Burgos/de la Cruz row for the same entry number.
2. Do not promote child identity, birth facts, parent-child relationships, parent merges, name variants, or Dario-line comparisons from this item until targeted conversion QA resolves the controlling row in the converted Markdown workflow.
3. The father field is not ready for canonical use beyond a QA prompt. The chunk/source packet read `Jose del Carmen Pulgar S.`, but the review task correctly frames the visible extent as needing certification.
4. The source does not name Dario, Arturo, Smith, Pulgar-Smith, a spouse, a child of a Dario candidate, or a travel/professional identifier. Any Dario identity bridge or relationship conclusion remains unsupported by this entry.

## Evidence Strengths

- The conflict draft and source packet accurately describe the core conflict: assigned chunk/source packet versus current converted Markdown.
- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 about 3 p.m. at Calle de Valdivia, with parents read as `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- Visual review of the referenced source image favors the Pulgar/Arriagada row for entry 172 and does not favor the Burgos/de la Cruz row currently present in the converted Markdown.
- The staged identity analysis is appropriately conservative: it keeps interpretation separate from transcription and recommends hold rather than canonical promotion.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 4/10 overall because the authoritative converted Markdown conflicts with the chunk; 8/10 for the narrow chunk/source-image support of a Pulgar/Arriagada entry 172 row |
| evidence_quantity_score | 5/10 |
| agreement_score | 6/10 overall; high agreement among staged draft, conflict draft, source packet, chunk, and image, but direct disagreement with the referenced converted Markdown |
| identity_confidence_score | 6/10 for a distinct child entry `Jose del Carmen Segundo Pulgar Arriagada` if the Pulgar row controls; 2/10 for any parent merge; 0.5/10 for any Dario identity bridge |
| claim_probability | 0.85 that the source image/chunk support a Pulgar/Arriagada entry 172 row; 0.20 that the converted Markdown's Burgos/de la Cruz row is the correct controlling row for this source image; 0.05 or lower for any Dario-line identity or relationship claim from this entry |
| relevance_level | high for Pulgar/Arriagada source cleanup; low for Dario-line identity proof |
| relevance_confidence | 0.90 for Pulgar/Arriagada cleanup relevance; 0.25 for Dario-line relevance |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a hold. It should not be revised into a promoted claim because the converted Markdown still contains a material row-level conflict, even though the source image and chunk favor the Pulgar/Arriagada reading for entry 172.

The only presently defensible proof judgment is that targeted conversion QA is required. After QA, the narrow reviewed claims should be child name, sex, registration date, birth date/time/place, father field, mother field, informant, and any parent residences visible in the certified row. No same-person merge or Dario-line relationship should be inferred from this source.

## Next Action

Run targeted conversion QA against the referenced source image, chunk, and converted Markdown to decide the controlling entry 172 row and certify the father-field extent. Then rerun proof review on the certified row-level claims before any canonical claim, relationship, or identity-bridge action.
