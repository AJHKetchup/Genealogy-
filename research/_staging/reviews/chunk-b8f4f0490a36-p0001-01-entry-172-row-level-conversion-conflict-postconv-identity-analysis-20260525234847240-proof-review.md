---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525234847240.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525234847240.md
reviewer: postconv-proof-review-20260526002657809
review_date: 2026-05-26
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Hold for conversion QA: the staged identity analysis correctly identifies a material row-control conflict. The assigned chunk, source packet, and visible source image support entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown records entry 172 as a Burgos/de la Cruz birth row.
- Hold for targeted father-field QA: the source image supports the father field beginning `Jose del Carmen Pulgar`, but this review does not certify the trailing element. Keep the accepted wording open between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until a conversion-QA pass records the visible reading.
- Do not promote child identity, birth facts, parent-child relationships, parent merges, or any Pulgar-to-Dario identity comparison from this draft. The conflict changes the child name, both parents, birth date, birth place, and informant.
- The requested `$genealogy-proof-review` skill is not installed in this session, so this review follows the task contract directly and stays within the staged review output area.

## Scores

- source_quality_score: 0.88
- conversion_confidence_score: 0.30
- evidence_quantity_score: 0.70
- agreement_score: 0.52
- identity_confidence_score: 0.70
- claim_probability: 0.78
- relevance_level: high
- relevance_confidence: 0.95
- canonical_readiness: hold

## Evidence Strengths

- The reviewed source class is a civil birth register, which is strong primary evidence for the birth event and declared parent/compareciente details once the controlling transcription is settled.
- The assigned chunk and source packet agree that entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with mother `Juana Arriagada de Pulgar` and informant `Ernesto Herrera L.`.
- Direct image review supports the row-number/control point in the staged analysis: page 58 entry 172 is visibly the Pulgar/Arriagada row, not the `Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz` row found in the current converted Markdown.
- The staged analysis keeps interpretation separate from transcription and properly rejects a Dario/Pulgar identity merge from this source alone.

## Review Judgment

The staged identity analysis is supported as a hold finding. Its core conclusion is sound: this is a conversion-control problem rather than a normal identity-variant problem. The Pulgar/Arriagada reading is probable for the visible entry-172 row, but the canonical record cannot safely absorb any claim while the current converted Markdown still carries a contradictory entry-172 family.

The probability score reflects the direct image support for the Pulgar/Arriagada row and the agreement between the chunk and source packet. The low conversion confidence and moderate agreement score reflect the severe disagreement with the converted Markdown. Identity risk remains high because accepting the wrong derivative would attach an entirely different child and parent set to entry 172.

No support was found in this verification context for treating `Jose del Carmen Segundo Pulgar Arriagada` as Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Darío Pulgar Arriagada. Any such bridge would require separate reviewed evidence.

## Next Action

Keep the staged draft at `hold_for_conversion_qa`. A targeted conversion-QA worker should compare the source image against entry 172 on page 58, decide the controlling row transcription, and certify the father-field wording before any follow-on proof review or canonical promotion.
