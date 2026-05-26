---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526062744146
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044737235.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044737235.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
review_result: hold
canonical_readiness: blocked
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

1. The reviewed staged draft is supported in its central blocker: the assigned chunk/source packet and current converted Markdown give mutually exclusive readings for entry 172.
2. The conflict is material, not a name spelling issue. It changes the child, parents, birth date/time, birth place, informant, and all downstream parent-child relationship candidates.
3. The page image is broadly consistent with the assigned chunk's Pulgar/Arriagada row, but this proof review is not a targeted conversion-QA certification. Row control and the exact father-field reading must still be resolved by conversion QA.
4. No canonical claim, relationship, merge, same-person conclusion, duplicate-person conclusion, or Dario-line bridge should be promoted from this staged draft.
5. Same-cluster wiki pages and prior derivative notes cannot independently corroborate the entry-172 identity because they depend on the disputed source cluster.

## Evidence Checked

- Staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044737235.md`
- Prior conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Review Judgment

The staged identity analysis accurately identifies a row-level conversion conflict and correctly recommends `hold_for_conversion_qa`. The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. The current converted Markdown transcribes entry 172 as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.

A direct visual check of the page image supports the concern that the converted Markdown is not aligned with the visible entry 172 row. However, because the task is proof review rather than conversion correction, I do not change the transcription or certify the exact father suffix. The correct proof result is hold/blocked pending targeted conversion QA.

## Scores

| Field | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registration is a strong primary source type for birth and parent declarations, but the present review depends on resolving which transcription controls. |
| conversion_confidence_score | 0.35 | The assigned chunk and source packet conflict with the current converted Markdown for the same entry number. |
| evidence_quantity_score | 0.45 | There is one source image plus derivative layers; no independent corroborating source was reviewed or needed for this task. |
| agreement_score | 0.40 | The assigned chunk, source packet, and broad visual page check align with Pulgar/Arriagada, while the current converted Markdown directly contradicts them. |
| identity_confidence_score | 0.60 | Pulgar/Arriagada is the stronger local reading, but not proof-ready until row-control QA certifies the transcription. |
| claim_probability | 0.64 | Probability that the controlling row is the Pulgar/Arriagada entry is above even odds after visual review, but still held because the official converted Markdown conflicts. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child claims; only anti-conflation context for Dario-line candidates. |
| relevance_confidence | 0.88 | The staged draft and source packet explicitly match Pulgar and Arriagada family terms. |
| canonical_readiness | blocked | Do not promote until conversion QA resolves row control and proof review is rerun. |

## Evidence Strengths

- The staged draft preserves uncertainty and does not overstate the Pulgar/Arriagada reading as canonical proof.
- It correctly separates the assigned chunk reading from the current converted Markdown reading.
- It flags high identity and relationship risk from mutually exclusive parent-child claims.
- It avoids treating same-cluster wiki pages as independent support.
- The recommended father-field caution is appropriate because the suffix or terminal mark after `Jose del Carmen Pulgar` is a transcription-sensitive detail.

## Identity And Relationship Risk

- Child identity risk: high.
- Parent-child relationship risk: high.
- Same-person merge risk: high for `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` if merged by name only.
- Juana-name conflation risk: moderate-high for `Juana Arriagada de Pulgar` versus similarly named Juana candidates in other staged contexts.
- Dario-line bridge risk: low as direct evidence, but high enough as a conflation hazard to require a separate later review if this row becomes canonical.

## Next Action

Hold for targeted conversion QA. QA should compare the page image, assigned chunk, source packet, and current converted Markdown for `CHUNK-b8f4f0490a36-P0001-01`, decide which entry-172 row controls, and certify only the visible father-field reading. After QA, rerun proof review before any canonical claim, parent-child relationship, same-person conclusion, or Dario-line comparison is promoted.
