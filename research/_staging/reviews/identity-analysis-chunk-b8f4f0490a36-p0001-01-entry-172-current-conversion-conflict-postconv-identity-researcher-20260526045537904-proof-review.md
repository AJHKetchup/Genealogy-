# Proof Review: identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict

- Review task id: `proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045537904.md`
- Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045537904.md`
- Role: claim_reviewer
- Worker: `postconv-proof-review-20260526085239882`
- Review status: hold
- canonical_readiness: blocked_pending_conversion_qa

## Blockers

- The staged draft is correct that entry `172` has a material row-level conflict: the current chunk and source packet give a Pulgar/Arriagada row, while the current converted Markdown gives a Burgos/de la Cruz row for the same entry number.
- This conflict affects every identity-bearing field: child name, sex wording, birth date and time, birth place, father, mother, informant, and all downstream parent-child or identity-link claims.
- Visual review of the cited source image broadly supports the Pulgar/Arriagada row at page 58, entry 172, but this proof review is not a full conversion-QA certification of every word or the father's final field form.
- The father field must remain unresolved as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted QA certifies what the visible source supports.
- Existing canonical wiki pages cannot be used as independent corroboration here because the staged draft notes that some relevant evidence may be Entry 172-derived.
- No Dario-line bridge is supported by this staged draft or the reviewed source artifacts. Do not attach this record to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

## Scoring

- source_quality_score: 0.86
- conversion_confidence_score: 0.34
- evidence_quantity_score: 0.62
- agreement_score: 0.48
- identity_confidence_score: 0.70 for the Pulgar/Arriagada row as the likely image row; 0.18 for the Burgos/de la Cruz converted-file row as controlling this image
- claim_probability: 0.78 that page 58 entry 172 is the Pulgar/Arriagada row; 0.16 that the Burgos/de la Cruz row in the converted Markdown controls this source image
- relevance_level: critical for Pulgar/Arriagada identity and parent-child claims; low for any Dario-line bridge
- relevance_confidence: 0.94 for the row-conflict issue; 0.18 for Dario-line identity linkage
- canonical_readiness: blocked_pending_conversion_qa

## Evidence Strengths

- The staged identity analysis accurately treats the two readings as a row-control conflict, not a name variant.
- The source packet explicitly records low conversion confidence and recommends `hold_for_conversion_qa`.
- The current chunk and source packet agree on the Pulgar/Arriagada row for entry `172`: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The cited source image is available and broadly aligns with the Pulgar/Arriagada row at page 58, entry `172`.
- The current converted Markdown gives a clearly different Burgos/de la Cruz row, which supports the staged draft's central conflict finding and the hold recommendation.
- The staged draft appropriately avoids promoting a parent merge, Dario comparison, or same-person conclusion from surname overlap.

## Review Judgment

The staged draft is supported as an identity-conflict analysis. Its main proof point is that the workspace contains incompatible derivative readings for the same entry number and that canonical promotion should remain blocked until conversion QA resolves the controlling row.

The best current probability favors the Pulgar/Arriagada row because the current chunk, source packet, and visible image align at the row level. However, the current converted Markdown remains a direct contradictory derivative transcript, and this review does not certify the father's final name field. Canonical readiness therefore remains `blocked_pending_conversion_qa`.

## Next Action

Send `CHUNK-b8f4f0490a36-P0001-01` to targeted conversion QA. QA should compare the source image, current converted Markdown, current chunk, and source packet for page 58, entry `172`; decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz; and certify the father field only to the visible extent.

After QA, rerun proof review before promoting any child identity, birth fact, parent claim, parent-child relationship, parent merge, or Dario-line bridge from this record.
