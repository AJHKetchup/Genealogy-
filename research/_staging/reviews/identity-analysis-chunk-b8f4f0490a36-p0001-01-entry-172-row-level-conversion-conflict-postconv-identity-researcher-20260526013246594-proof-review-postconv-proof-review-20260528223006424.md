---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528223006424
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013246594.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013246594.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical promotion remains blocked. The staged draft correctly identifies a row-level conflict: the assigned chunk/source packet and visible source image support entry 172 as a Pulgar/Arriagada birth, while the current converted Markdown records entry 172 as a Burgos/de la Cruz birth.
2. The current converted Markdown is not reliable for entry 172. It gives `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth 6 April 1888, and place `En esta`; those details do not match the visible entry 172 row in the cited source image.
3. No Dario-line identity or relationship claim is supported by this entry. The visible entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario, Arturo, Smith, Dario Jose, Dario J., or Dario Pulgar Arriagada.
4. Parent identity merges remain blocked. The source supports names in this entry, but it does not prove that the father `Jose del Carmen Pulgar S.` or mother `Juana Arriagada de Pulgar` is identical with any existing profile beyond this record without a separate identity proof.

## Evidence Strengths

- The source image visibly places entry `172` on page 58 and supports the Pulgar/Arriagada row transcribed in the assigned chunk.
- The assigned chunk and source packet agree that entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at Calle de Valdivia.
- The father field is visibly consistent with the chunk reading `Jose del Carmen Pulgar S.`; the trailing initial should still be treated carefully in any downstream literal transcription.
- The mother field is visibly consistent with `Juana Arriagada de Pulgar`.
- The informant field is visibly consistent with `Ernesto Herrera L.`, present at the birth, age twenty-six, employee, domiciled Calle de Valdivia.
- The staged identity analysis correctly treats the broader Dario and Pulgar-family comparisons as relevance leads only, not as promotable identity bridges.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 4/10 overall; 8/10 for the assigned chunk/source packet against the source image; 1/10 for the current converted Markdown entry-172 row |
| evidence_quantity_score | 4/10 |
| agreement_score | 7/10 among source image, assigned chunk, source packet, and staged conflict draft; 2/10 when the current converted Markdown is included |
| identity_confidence_score | 7/10 for the narrow entry-172 child identity as `Jose del Carmen Segundo Pulgar Arriagada`; 4/10 for parent-candidate identity beyond this record; 1/10 for any Dario-line same-person claim |
| claim_probability | 0.88 for the narrow claim that visible entry 172 is the Pulgar/Arriagada birth row; 0.08 for the Burgos/de la Cruz reading as applied to this cited image; 0.05 or lower for Dario-line attachment |
| relevance_level | high for Pulgar/Arriagada birth and parent-candidate review; low for Dario-line identity without a bridge |
| relevance_confidence | 0.90 for Pulgar/Arriagada relevance; 0.20 for Dario-line relevance |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a proof-review hold. The visible source image supports the Pulgar/Arriagada row described by the assigned chunk and source packet, and it undermines the current converted Markdown's Burgos/de la Cruz reading for this same entry number.

This review does not promote any claim. It only supports routing the item to targeted conversion QA and preserving the hard boundary between a visible-source correction question and canonical identity attachment.

## Next Action

Keep this item at `hold_for_conversion_qa`. The next action is targeted conversion QA on entry 172 using the source image, assigned chunk, source packet, and current converted Markdown to resolve the derivative conversion conflict. After that, rerun proof review before promoting child identity, birth facts, parent-child relationships, parent merges, or any Dario-line comparison.
