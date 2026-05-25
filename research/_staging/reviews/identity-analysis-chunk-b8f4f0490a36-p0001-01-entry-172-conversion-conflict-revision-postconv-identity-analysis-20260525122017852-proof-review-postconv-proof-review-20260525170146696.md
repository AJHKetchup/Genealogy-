---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260525170146696
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity/Conflict Analysis

## Blockers First

1. Revise before downstream use: the staged identity-analysis draft correctly identifies a material row-level conversion conflict, but it misstates the current converted-file details. The staged draft says the converted Markdown reads entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born 26 March 1888 at `En esta`; the reviewed converted file currently reads entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 20 February 1888 at `En Pellin`.
2. The source packet and conflict draft repeat the unsupported `Emilia de la Cruz` / 26 March / `En esta` description of the converted Markdown. The conflict itself is real, but that literal summary is not supported by the referenced converted file reviewed for this task.
3. Canonical readiness remains blocked by row-level conversion disagreement. The chunk and source image support a Pulgar/Arriagada row for entry 172, while the converted Markdown supports a different Gomez/de la Cruz de la Maza row for the same entry number.
4. The father field in the Pulgar/Arriagada row remains a transcription-risk field. The chunk reads `Jose del Carmen Pulgar S.`, but the visible ending after `Pulgar` should remain unresolved pending targeted conversion QA.
5. No Dario-line bridge is supported. Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, Dario Jose, Darío, a spouse, child, grandchild, occupation bridge, passenger context, or later-life identity.

## Evidence Strengths

- The staged draft's main caution is well supported: this is a row-level conversion or assignment conflict, not a spelling variant or same-person merge problem.
- The current chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The visible source image aligns materially with the chunk/source-packet Pulgar/Arriagada row for page 58, entry 172, including the child name, mother name, Calle de Valdivia context, and informant cluster.
- The converted file's competing entry-172 row is internally coherent but belongs to a different family cluster: `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, Pellin context.
- The staged draft appropriately rejects relationship jumps to Dario/Pulgar-Smith or other Dario/Pulgar-Arriagada identities.

## Scores

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration image is a strong source class, but this review depends on a disputed conversion chain and a difficult father-name ending. |
| conversion_confidence_score | 0.42 | Chunk/source image and converted Markdown disagree on child, parents, place, and date; the staged draft also misreports the converted-file details. |
| evidence_quantity_score | 0.52 | One direct source image plus derivative chunk/source-packet/converted layers; no independent corroborating record was reviewed or needed for this task. |
| agreement_score | 0.34 | Agreement is strong between chunk and source packet, but low across the full evidence stack because the converted file assigns entry 172 to a different family. |
| identity_confidence_score | 0.70 for the source-visible Pulgar/Arriagada row; 0.04 for any Dario-line attachment | Entry 172 likely concerns the Pulgar/Arriagada child in the visible page/chunk, but no Dario identity bridge is present. |
| claim_probability | 0.68 | Probable that the source-visible row is for `Jose del Carmen Segundo Pulgar Arriagada`, but not promotable until conversion QA resolves the assigned converted-file conflict. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child candidates; only negatively relevant to Dario-line anti-conflation. |
| relevance_confidence | 0.91 | The Pulgar and Arriagada names in the chunk/source image make relevance high if the row is certified. |
| canonical_readiness | hold_for_conversion_qa | Do not promote child identity, parent-child relationships, parent merges, or Dario comparisons from this draft. |

## Claim-Level Judgment

| Claim / hypothesis | Probability | Review judgment |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.68 | Hold pending targeted conversion QA; likely from visible source/chunk, but derivative conflict remains unresolved. |
| The converted Markdown conflicts with the chunk/source packet at row level. | 0.98 | Supported, with revision needed to state the converted row accurately as currently reviewed. |
| Father can be used canonically as `Jose del Carmen Pulgar S.`. | 0.55 | Hold; visible/source-packet support is plausible, but exact suffix/ending requires QA. |
| Mother candidate is `Juana Arriagada de Pulgar`. | 0.70 | Hold; supported by chunk/source image if the Pulgar/Arriagada row is certified. |
| Entry 172 supports a Dario/Pulgar-Smith or Dario/Pulgar-Arriagada bridge. | 0.04 | Not supported; keep as anti-conflation only. |

## Next Action

Revise the staged conflict summary or run targeted conversion QA so the converted-file side of the conflict is quoted accurately from the current file: `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born 20 February 1888 at `En Pellin`. Then rerun proof review after QA certifies whether the controlling entry-172 row is the Pulgar/Arriagada row or the Gomez/de la Cruz de la Maza row, and after the father-field ending after `Pulgar` is explicitly recorded.
