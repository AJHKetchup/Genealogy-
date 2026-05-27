---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527202810251
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md
reviewed: 2026-05-27
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Control Hold

## Blockers First

1. Canonical promotion remains blocked because the referenced converted Markdown and assigned chunk materially disagree on entry `172`.
2. The current converted Markdown records entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888; the assigned chunk and source packet record entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888.
3. The staged draft's statement that direct image review supports the Pulgar/Arriagada row cannot be independently re-certified in this pass because the referenced source image path is not present in `raw/sources`. A later conversion follow-up also reports the source image missing.
4. The father-field suffix after `Jose del Carmen Pulgar` remains unresolved. Do not certify `S.` or any other suffix until the physical image is restored and reviewed.
5. No Dario identity bridge is supported. The anti-conflation warning is appropriate and should remain in force.

## Scored Judgment

- `source_quality_score`: 0.86 for the civil birth register as a source type, but unavailable image access limits this review.
- `conversion_confidence_score`: 0.30 because the converted Markdown and chunk conflict at the row level.
- `evidence_quantity_score`: 0.58 based on one chunk, one converted Markdown file, one source packet, and conversion-review notes; no available source image for fresh certification.
- `agreement_score`: 0.36 because derivative artifacts disagree materially.
- `identity_confidence_score`: 0.62 for the limited conclusion that a Pulgar/Arriagada candidate row is documented in the assigned chunk/source packet; 0.02 for any Dario same-person bridge.
- `claim_probability`: 0.88 that a row-control/conversion conflict exists; 0.58 that the Pulgar/Arriagada row controls entry `172` pending restored image QA.
- `relevance_level`: high
- `relevance_confidence`: 0.92
- `canonical_readiness`: blocked

## Evidence Strengths

The staged draft accurately identifies the material conflict between the current converted Markdown and the assigned chunk. This is not a minor spelling discrepancy: the child name, birth date, birth time, birthplace, father, mother, and informant differ.

The assigned chunk and source packet consistently support the Pulgar/Arriagada candidate row for entry `172`, including child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, birth at Calle de Valdivia, and an unresolved father suffix after `Jose del Carmen Pulgar`.

The staged draft correctly recommends `hold_for_conversion_qa` and correctly avoids promoting a relationship jump or Dario-line merge.

## Next Action

Restore or locate the source image matching SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then run targeted conversion QA against the physical image, assigned chunk, source packet, and current converted Markdown. After row control and the father-field ending are certified, rerun proof review before any canonical claim, relationship, identity merge, or wiki update.
