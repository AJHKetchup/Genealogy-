---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526140738334
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md
reviewed_staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
created: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

- Review task id: `proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md`
- Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045956374.md`
- Role: claim_reviewer
- Review status: hold
- canonical_readiness: hold_for_conversion_qa

## Blockers

- The same source hash, converted file, chunk id, and entry number carry incompatible derivative readings. The current converted Markdown reads entry `172` as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the current chunk and held source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- This is a row-level conversion conflict, not a name variant. It changes the child identity, sex label, birth date and time, birth place, father, mother, informant, and downstream relationship claims.
- The father-field reading in the Pulgar row remains uncertified. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as review alternatives until targeted conversion QA resolves the source reading.
- No Dario-line identity bridge is supported by the reviewed evidence. The reviewed artifacts do not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.
- No child identity, birth fact, parent-child relationship, person merge, parent normalization, or Dario-line comparison should be promoted while the derivative conversion conflict remains open.

## Scoring

- source_quality_score: 0.86
- conversion_confidence_score: 0.36
- evidence_quantity_score: 0.62
- agreement_score: 0.44
- identity_confidence_score: 0.66
- claim_probability: 0.84 for the staged claim that a material conversion conflict exists
- claim_probability: 0.58 for the Pulgar/Arriagada identity row as canonically usable before QA
- relevance_level: critical
- relevance_confidence: 0.93
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The staged identity-analysis draft accurately identifies the controlling problem: two incompatible readings are attached to entry `172` for the same source package and derivative file set.
- The held source packet explicitly marks conversion confidence as low and recommends `hold_for_conversion_qa`, which matches the observed conflict.
- The current chunk supports the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on `Ocho de Marzo de mil ochocientos ochenta i ocho`, and informant `Ernesto Herrera L.`
- Visual review of the cited page image supports the chunk/source-packet row at a broad level for entry `172`, including the Pulgar/Arriagada names and the Calle de Valdivia/Colipi context.
- The staged draft correctly avoids promotion and correctly treats existing wiki pages as context only, not independent proof for the contested row.

## Review Judgment

The staged identity-analysis draft is supported as a conflict analysis. Its central claim, that entry `172` is blocked by a material row-level conversion conflict, is well supported by direct comparison of the current converted Markdown, current chunk, held source packet, and page image.

The Pulgar/Arriagada row is plausible and visibly relevant, but not canonically ready because the assigned converted Markdown still preserves a contradictory Burgos/de la Cruz transcription for the same entry number. The evidence supports a hold, not promotion or merge activity.

## Next Action

Send this item to targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`. QA should reconcile the source image, current converted Markdown, current chunk, and held source packet; decide whether entry `172` is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row; and certify the father field before any renewed proof review or canonical promotion.
