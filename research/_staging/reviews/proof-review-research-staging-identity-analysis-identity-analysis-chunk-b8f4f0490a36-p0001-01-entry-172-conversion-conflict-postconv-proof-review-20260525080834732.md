---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260525080834732
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md
reviewed_at: 2026-05-25T08:08:34Z
decision: hold
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.90
conversion_confidence_score: 0.35
evidence_quantity_score: 0.68
agreement_score: 0.50
identity_confidence_score: 0.72
claim_probability: 0.74
relevance_level: direct
relevance_confidence: 0.95
next_action: targeted_conversion_qa_then_revise_identity_analysis_before_canonical_use
---

# Proof Review: Entry 172 Conversion-Conflict Identity Analysis

## Blockers

- Canonical promotion is blocked. The staged draft correctly identifies a material row-level conversion conflict, and no claim, relationship, identity merge, or Dario-line attachment should move to canonical space from this draft.
- The staged draft's description of the assigned converted Markdown is partly unsupported by the actual converted file reviewed. The draft says the converted Markdown gives entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born in `Pellin` on `20 February 1888`; the referenced converted file actually gives `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, place `En esta`, and birth date `26 March 1888`. This does not remove the row-level conflict, but the draft should be revised before reuse.
- The father-name ending remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, and the visible source image appears broadly consistent with a final mark or suffix after `Pulgar`, but proof review should not force a normalized reading without targeted conversion QA.
- Identity and relationship jumps remain blocked. This entry does not visibly name Dario, Arturo, Smith, Dario Jose, Geneva/ICRC context, expropriation context, Alexander John Heinz, or any bridge to the canonical Dario pages.
- The entry-172 mother `Juana Arriagada de Pulgar` must not be merged with separate entry-513 `Juana de Dios Amagada/Amador de Pulgar` candidates from similarity alone.

## Evidence Strengths

- The raw source image is available and is a civil birth register, a strong primary source class for birth facts and declared parent information.
- The visible source image and the current chunk support the broad Pulgar/Arriagada row for page 58, entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` with an unresolved final element, mother `Juana Arriagada de Pulgar`, and informant/compareciente `Ernesto Herrera L.`
- The source packet and conflict candidate appropriately label the issue as a row-level conversion or file-assignment conflict, not a spelling variant.
- The staged identity analysis is appropriately conservative in its main recommendation: hold for conversion QA and avoid canonical identity, claim, relationship, and parent-candidate promotion.

## Scored Judgment

| Factor | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth registration image is a strong direct source for the entry, though the father suffix still needs targeted visual QA. |
| conversion_confidence_score | 0.35 | The chunk and visible image support the Pulgar/Arriagada row, while the assigned converted Markdown records a materially different row. |
| evidence_quantity_score | 0.68 | One source image plus derivative chunk/source-packet evidence support the Pulgar/Arriagada row; no independent corroborating record was reviewed. |
| agreement_score | 0.50 | Image and chunk agree in broad substance, but converted Markdown conflicts and the staged draft misstates some converted-file details. |
| identity_confidence_score | 0.72 | The Pulgar/Arriagada identity cluster is probable for the visible entry 172 row, with moderate caution due to conversion conflict and father suffix. |
| claim_probability | 0.74 | The staged draft's central hold judgment is well supported; its exact converted-file summary needs revision. |
| relevance_level | direct | The reviewed materials directly concern the assigned entry 172 identity conflict. |
| relevance_confidence | 0.95 | File paths, chunk id, page reference, and visible page all point to the assigned review target. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical use until the conversion/chunk assignment is reconciled and the father field is explicitly reread. |

## Reviewed Evidence

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525070445041.md`
- Conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md`
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Next Action

Run targeted conversion QA against the source image, assigned converted Markdown, and current chunk for page 58, entry 172. The QA note should decide whether the controlling row is the visible Pulgar/Arriagada entry or whether the converted file is misassigned, and it should record the father field as exactly source-supported: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, revise this identity analysis to correct the converted-file summary before any proof review for promotion.
