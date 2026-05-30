---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530065351963
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210707727.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Assignment Conflict

## Blockers

- The source image could not be opened at the referenced raw path `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`; the expected job page image `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` is also absent. This prevents visual certification of either row reading in this proof-review pass.
- The reviewed converted Markdown and page Markdown read entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The reviewed chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- This is a controlling-row/conversion conflict, not a minor transcription uncertainty. No child identity, parent-child relationship, birth event, residence, informant, parent merge, or Dario-line connection should be promoted from this staged draft.
- The father field for the Pulgar reading remains uncertified. This review cannot choose between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` without the visible source.

## Evidence Strengths

- The staged identity-analysis draft accurately reports the derivative-file disagreement and keeps the item on hold.
- The conflict is internally well documented across the source packet and conflict draft, including the exact rows and names that disagree.
- The underlying source type, if visually verified, would be strong: an 1888 civil birth registration page for Los Ángeles, Chile.
- The derivative evidence is relevant to Pulgar/Arriagada research only if the chunk row is the controlling row; it is not relevant to Dario identity attachment as currently supported.

## Scores

| category | score | review judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registers are high-quality direct sources for birth and parent declarations, but the source image is unavailable in this review pass. |
| conversion_confidence_score | 0.20 | Two derivative conversions disagree across multiple entries and names; visual certification is missing. |
| evidence_quantity_score | 0.35 | There are multiple local derivative files, but they are not independent evidence and directly conflict. |
| agreement_score | 0.10 | Agreement is low because the converted Markdown/page Markdown and chunk/source packet assert incompatible entry-172 readings. |
| identity_confidence_score | 0.18 | Identity confidence for any named child or parent relationship is low until row control is resolved. |
| claim_probability | 0.95 | High probability that the correct current claim is procedural: this staged draft must remain held for conversion QA. |
| relevance_level | medium | Relevant to Pulgar/Arriagada research only after row QA; low relevance to any Dario cluster from this evidence alone. |
| relevance_confidence | 0.78 | The conflict and surname-match relevance are clear, but substantive family relevance depends on the unresolved row. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical claims, relationships, person pages, family pages, or merge decisions. |

## Claim Probability Detail

| claim reviewed | probability | disposition |
| --- | ---: | --- |
| A row-control conflict exists between the assigned chunk/source packet and converted Markdown for entry 172. | 0.97 | Supported by local derivative files. |
| Entry 172 can currently support `Jose del Carmen Segundo Pulgar Arriagada` as a canonical child identity. | 0.25 | Hold; derivative support exists but conflicts with the converted Markdown and lacks visual certification. |
| Entry 172 can currently support `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, as canonical. | 0.25 | Hold; converted Markdown support exists but conflicts with the assigned chunk/source packet and lacks visual certification. |
| Entry 172 supports a Dario/Darío Pulgar identity bridge. | 0.02 | Not supported; no reviewed derivative reading names Dario, Arturo, Smith, or a connecting relationship. |

## Next Action

Keep `canonical_readiness: hold_for_conversion_qa`. The next action is targeted conversion QA with the actual page image available: reconcile the source image, page Markdown, converted Markdown, assigned chunk, and source packet; identify the controlling entry-172 row; and certify the father field only to the visible-source level of certainty. After that, rerun proof review before promotion or any canonical wiki update.
