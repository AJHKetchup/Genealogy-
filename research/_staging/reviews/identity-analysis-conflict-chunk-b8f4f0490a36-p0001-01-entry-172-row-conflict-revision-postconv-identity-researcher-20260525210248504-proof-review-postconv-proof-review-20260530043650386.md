---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530043650386
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.82
conversion_confidence_score: 0.30
evidence_quantity_score: 0.42
agreement_score: 0.18
identity_confidence_score: 0.50
claim_probability: 0.56
relevance_level: high_for_pulgar_arriagada_row_conflict
relevance_confidence: 0.86
canonical_readiness: hold_for_conversion_qa
created: 2026-05-30
---

# Proof Review: Entry 172 Row Conflict Revision

This review covers the exact staged draft `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md`.

## Blockers First

1. Canonical readiness remains `hold_for_conversion_qa`. The reviewed derivatives disagree at the row level for register page 58, entry 172.
2. The assigned chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
3. The current converted file reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
4. The referenced source image path from the source packet did not resolve locally during this review: `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` with accents in the packet path. No visual handwriting certification was possible in this pass.
5. The draft's Pulgar/Arriagada identity probability is therefore a derivative-context judgment, not a source-image-certified proof conclusion.
6. No Dario identity bridge is supported by the reviewed materials. The Dario-line discussion is relevant only as anti-conflation context.

## Evidence Strengths

- The staged draft accurately reports the central conflict between the assigned chunk/source packet and the converted file.
- The assigned chunk is internally coherent as a civil birth-register transcription for entries 171-176 and gives a full row for entry 172 with child, parents, birth date/time/place, informant, residence, and official signature fields.
- The source packet preserves uncertainty and explicitly blocks promotion pending targeted conversion QA.
- The conflict draft correctly treats this as a conversion row-assignment conflict rather than a name variant, same-person merge, or relationship proof.
- The civil birth-register source type would normally be strong evidence for birth and parentage if the source image and controlling row were certified.

## Scored Judgment

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registration is a high-quality source type for birth and parent names, but the image was unavailable for direct verification in this review. |
| conversion_confidence_score | 0.30 | The assigned chunk and current converted file give incompatible entry-172 rows. |
| evidence_quantity_score | 0.42 | There are several derivative artifacts, but only one conflicted source event and no independent corroborating record in scope. |
| agreement_score | 0.18 | Agreement is low because the chunk/source packet and converted file disagree on child, parents, birth date, birth time, place, residence, and informant. |
| identity_confidence_score | 0.50 | The Pulgar/Arriagada row is plausible from the assigned chunk but not source-image-certified and not promotion-ready. |
| claim_probability | 0.56 | The staged draft's hold conclusion is more probable than either row-specific promotion; probability for the Pulgar/Arriagada row remains limited by the unresolved conversion conflict. |
| relevance_level | high_for_pulgar_arriagada_row_conflict | Directly relevant to Pulgar/Arriagada parent candidates if the row is certified; not direct evidence for any Dario identity. |
| relevance_confidence | 0.86 | The relevance of the conflict itself is clear from all reviewed derivatives. |
| canonical_readiness | hold_for_conversion_qa | Do not promote child identity, birth facts, parent claims, relationships, merge decisions, or Dario-line attachments. |

## Claim And Identity Risk

- Literal support for the existence of a Pulgar/Arriagada row is present in the assigned chunk and source packet, but the current converted file contradicts it.
- Relationship jumps are high risk: accepting the Pulgar row would create child-parent relationships to `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; accepting the converted row would instead support Burgos/de la Cruz parents.
- Name-variant handling should preserve the literal father field as `Jose del Carmen Pulgar S.` until QA certifies whether the final mark is a suffix, abbreviation, uncertain letter, or not present.
- Duplicate-person and family-attachment risk is high if `Jose del Carmen Pulgar S.` is merged with an existing `Jose del Carmen Pulgar` only by base-name similarity.
- The Dario candidates named in the staged draft remain unsupported by this entry. No reviewed material names Dario or supplies a direct bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the actual source image and the two conflicting derivative readings. The QA note should decide which row controls entry 172 and certify the father field only to the extent visible: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before any canonical claim, relationship, identity merge, parent-pair conclusion, or Dario-line comparison is promoted.
