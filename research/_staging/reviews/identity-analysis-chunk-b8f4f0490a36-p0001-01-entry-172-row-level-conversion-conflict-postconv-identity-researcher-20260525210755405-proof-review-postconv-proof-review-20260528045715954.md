---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528045715954
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525210755405.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525210755405.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote child, parent, birth, identity, or relationship claims from this staged draft until targeted conversion QA reconciles the source image, converted Markdown, chunk, and source packet.
2. The assigned converted Markdown and assigned chunk materially disagree for entry 172. The converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the chunk reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
3. The visible source image supports the Pulgar/Arriagada row for entry 172, but this review does not correct the converted Markdown or certify the final conversion. The proper action remains conversion QA.
4. The father field in the Pulgar/Arriagada row remains uncertain at the suffix level. The visible and derivative evidence is consistent with `Jose del Carmen Pulgar...`, but the exact ending should be certified by QA as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
5. Entry 172 does not name Dario, Dario Arturo, Dario Jose, Darío, Smith, or any downstream Pulgar identity bridge. No merge or relationship claim to those identity clusters is supported by this source.

## Evidence Strengths

- The source type is a civil birth register, which is generally strong direct evidence for a birth event, parent names, registration date, and declarant when the row reading is stable.
- The assigned chunk gives a coherent row for page 58, entry 172: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source packet explicitly identifies the conversion conflict and says direct image inspection supports the Pulgar/Arriagada row rather than the Burgos/de la Cruz row.
- Independent visual review for this proof review also supports the Pulgar/Arriagada row in the source image at page 58, entry 172.
- The staged identity analysis correctly treats the disagreement as a row-level conversion or file-assignment conflict, not as a name variant or same-person identity conflict.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 3/10 overall until conversion QA; 7/10 for the narrow observation that the visible source image aligns with the Pulgar/Arriagada row |
| evidence_quantity_score | 5/10 |
| agreement_score | 4/10 overall because converted Markdown conflicts with chunk/source packet/image; 8/10 among chunk, source packet, and visible image for the Pulgar/Arriagada row |
| identity_confidence_score | 7/10 that the visible entry-172 row is a Pulgar/Arriagada child record; 2/10 for any Burgos/de la Cruz claim from this assigned source; 1/10 for any Dario-line identity bridge |
| claim_probability | 0.80 for the claim that source image page 58 entry 172 records a Pulgar/Arriagada child; 0.20 for the converted Markdown Burgos/de la Cruz reading as controlling this same entry; 0.05 or lower for any same-person/relationship bridge to Dario identities |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold. The source image, chunk, and source packet support the Pulgar/Arriagada interpretation for page 58, entry 172, while the assigned converted Markdown contains a different family for entry 172. That disagreement is substantial enough to block canonical promotion even though the visible source leans toward the Pulgar/Arriagada row.

The review should not be used to alter transcription text directly. It is appropriate to ask conversion QA to double-check the controlling row and father-field suffix. It is not appropriate to rewrite the converted Markdown or promote Pulgar/Arriagada claims from this proof-review task alone.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`. The QA note should state which row controls entry 172 and should explicitly certify the father field. After that, rerun proof review for any proposed child, birth, parent, or relationship claim. Keep Dario-line identity bridges and all same-person merges out of canonical space unless a separate source explicitly supports them.
