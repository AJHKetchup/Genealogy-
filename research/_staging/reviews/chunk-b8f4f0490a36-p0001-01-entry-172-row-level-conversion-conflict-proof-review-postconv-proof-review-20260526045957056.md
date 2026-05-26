# Proof Review: Entry 172 Row-Level Conversion Conflict

- Review task id: `proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015729976.md`
- Reviewed staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015729976.md`
- Role: claim_reviewer
- Review status: hold
- canonical_readiness: hold_for_conversion_qa

## Blockers

- The staged draft correctly identifies an unresolved row-control conflict: the assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown reads entry 172 as a Burgos/de la Cruz birth row.
- The visible source image supports the Pulgar/Arriagada row for page 58, entry 172, but the derivative converted file remains unreconciled. Canonical promotion should wait for conversion QA to correct or retire the conflicting converted text.
- The father field is mostly legible as `Jose del Carmen Pulgar`, but the terminal mark or suffix after `Pulgar` remains uncertain enough that it should be certified by targeted conversion QA before parent-child relationship promotion.
- No Dario/Dario-line identity bridge is supported by this entry. The source names a Pulgar/Arriagada child and parents, not Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Darío Pulgar Arriagada.

## Scoring

- source_quality_score: 0.88
- conversion_confidence_score: 0.42
- evidence_quantity_score: 0.66
- agreement_score: 0.48
- identity_confidence_score: 0.74
- claim_probability: 0.94
- relevance_level: critical
- relevance_confidence: 0.96
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The staged draft references the exact converted file, chunk, source packet, and source image needed to evaluate the conflict.
- The source packet and assigned chunk agree that entry 172 is for `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar`/possible `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- Visual review of the cited source image supports the Pulgar/Arriagada row for entry 172, including the child name, male sex, 7 April 1888 registration date, 8 March 1888 birth date, Calle de Valdivia birthplace, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The staged identity analysis keeps literal readings separate, avoids merging Pulgar/Arriagada with Burgos/de la Cruz, and appropriately recommends holding all canonical claims until conversion QA resolves the derivative conflict.

## Review Judgment

The reviewed draft is well supported as an identity-conflict analysis. Its main claim is not that the Pulgar/Arriagada facts are ready for canonical use, but that the row-control conflict blocks promotion. That blocker is strongly supported by the contradiction between the assigned chunk/source packet, the visible image, and the current converted Markdown.

The probability that the draft's hold recommendation is correct is high. The probability that entry 172 is the Pulgar/Arriagada row is also high on visible-image review, but canonical readiness remains a hold because the workspace's derivative conversion layer is inconsistent and the father-field suffix has not been QA-certified.

## Next Action

Send to targeted conversion QA for page 58, entry 172. QA should reconcile `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md` against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, then certify the father field exactly to the visible extent. Do not promote entry-172 identity, birth facts, parent-child relationships, or Dario-line comparisons before that QA note exists.
