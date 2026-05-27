---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260527145807947
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525205449265.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525205449265.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row Conflict

## Blockers First

1. The staged identity analysis correctly identifies a hard row-level conflict between the assigned converted Markdown and the assigned chunk/source packet. The converted Markdown records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the chunk/source packet records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
2. The visible page image supports the presence of a Pulgar/Arriagada entry at row 172 at a high level, but the father-field ending after `Pulgar` remains too uncertain for proof promotion without targeted conversion QA.
3. The claim set cannot be canonicalized because child identity, parents, birth date/time/place, informant, and relationship claims differ across derivative files.
4. No Dario-line identity or relationship claim is literally supported by this entry. Any Dario connection remains an anti-conflation context only.

## Evidence Strengths

- The source type is strong: a civil birth registration is direct evidence for a birth event and named parents when the row is correctly read.
- The assigned chunk, source packet, conflict draft, and visible image are broadly consistent that entry 172 is a Pulgar/Arriagada row.
- The identity analysis preserves uncertainty instead of forcing a merge, and it correctly treats the Dario names as non-evidence for this row.
- The staged recommendation to hold for conversion QA is supported by the derivative conflict and by the unresolved father-field reading.

## Scored Judgment

| Review dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration is a high-quality original-style source for birth and parent claims, assuming correct row transcription. |
| conversion_confidence_score | 0.42 | The chunk and image align at a high level, but the converted Markdown contradicts the chunk in every identity-bearing field. |
| evidence_quantity_score | 0.62 | One direct source image plus derivative chunk/source packet/conflict note; quantity is adequate for a narrow row review but not enough to resolve the conversion conflict alone. |
| agreement_score | 0.35 | Chunk/source packet/image agree broadly; converted Markdown disagrees completely for entry 172. |
| identity_confidence_score | 0.58 | Pulgar/Arriagada is more likely than Burgos/de la Cruz for the visible row, but exact identity claims remain below promotion confidence. |
| claim_probability | 0.58 | Probability that the Pulgar/Arriagada row is the controlling entry 172 reading, pending QA. Parent-child relationship probability should remain no higher than this. |
| relevance_level | high | If confirmed, the row names a Pulgar child and Arriagada mother in a birth register. |
| relevance_confidence | 0.86 | Family-name relevance is clear under the chunk/image reading, but relevance does not overcome the conversion conflict. |
| canonical_readiness | blocked | Do not promote birth, parent, relationship, identity merge, or Dario-bridge claims from this staged draft. |

## Literal Support Check

- Supported by chunk/source packet and visible image at row level: entry 172 is plausibly a Pulgar/Arriagada birth-registration row.
- Supported by converted Markdown only: entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- Not safely resolved: whether the father field should be read as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Not supported: any claim that this entry names Dario, proves a Dario-line relationship, or bridges any Dario candidate to this birth row.

## Next Action

Hold for targeted conversion QA. QA should compare the source image, assigned converted Markdown, assigned chunk, and source packet for `CHUNK-b8f4f0490a36-P0001-01`; certify the controlling entry-172 row; and explicitly record the father-field reading. After QA, rerun proof review before any canonical promotion.
