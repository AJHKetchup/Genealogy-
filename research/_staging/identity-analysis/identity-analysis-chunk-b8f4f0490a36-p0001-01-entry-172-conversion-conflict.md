---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-20260522150707183.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-20260522150707183.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-jose-del-carmen-segundo-pulgar-arriagada.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
worker: postconv-evidence-extraction-20260523181508215
---

# Identity Analysis: Entry 172 Conversion Conflict

## Blockers

- The exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-20260522150707183.md` reports a material derivative conflict for entry 172. The source image and assigned chunk/source packet support the child as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`; the converted Markdown reads `Jose Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`.
- The source image is now available and was directly reread for this revision. It supports the Pulgar/Arriagada row, so the remaining blocker is not image absence but a conflicting assigned converted Markdown transcript plus an unresolved father-name suffix.
- The father's final abbreviated element is unresolved: the assigned chunk has `Jose del Carmen Pulgar S.`, while the direct image reread supports `Jose del Carmen Pulgar` without a clearly visible suffix.
- Existing canonical pages already contain auto-generated evidence from this b8f4 staging for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and an entry-registration stub. Because the controlling conversion is conflicted, no additional promotion, merge, or canonical normalization should occur from this draft.
- The entry does not name Dario. Existing Dario-line context is relevant only as a guardrail against name-based merging.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Literal evidence:

- The source image and assigned chunk transcribe entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source packet now records a direct 2026-05-23 image reread supporting the child, mother, and father as `Jose del Carmen Pulgar` without a clearly visible suffix.
- Existing wiki pages for `jose-del-carmen-segundo-pulgar-arriagada` and `juana-arriagada-de-pulgar` contain auto-generated evidence from this staged source packet, but those pages label the key relationship as probable/low confidence rather than fully accepted.

Interpretation:

- This is the leading hypothesis for the intended Pulgar-line evidence because two local staged artifacts for this task point to the same Pulgar/Arriagada row and a separate earlier reread note supports the same child and mother.
- It remains blocked for canonical readiness in this b8f4 pass because the converted Markdown names an unrelated Bunster/de la Maza family and the father suffix requires explicit conversion QA.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.86 | Strong visible source-image, chunk, and source-packet support for the Pulgar/Arriagada identity cluster, reduced by conflicting converted Markdown and father-suffix uncertainty. |
| conflict_severity | 0.94 | The competing readings change the child, both parents, birth details, informant, and official context. |
| evidence_quality | 0.84 | Civil-registration image is available and supports the row, but derivative transcript conflict remains. |
| conversion_confidence | 0.50 | The image and chunk support this reading, but the assigned converted file does not. |
| claim_probability | 0.86 | More probable than the Bunster/de la Maza reading on current source-image evidence, but not promotion-ready. |
| relevance | 0.96 | Directly relevant to Pulgar-line parent-child evidence. |
| canonical_readiness | 0.15 | Hold for conversion QA and image/page reconciliation. |

## Hypothesis 2: Entry 172 Is The Bunster/de la Maza Birth Registration

Literal evidence:

- The converted Markdown reads entry 172 as `Jose Miguel`, male, born 26 March 1888 at 10 p.m., father `Oswaldo Bunster`, mother `Amelia de la Maza`, and informant `Oswaldo Bunster`.
- The staged conflict draft preserves this converted text as a literal derivative reading.

Interpretation:

- This is a necessary competing hypothesis because it is the assigned converted file, but it is weaker than Hypothesis 1 because the source image, assigned chunk, and source packet all support the Pulgar/Arriagada row.
- Do not create or promote Bunster/de la Maza people from this entry unless conversion QA proves the Pulgar/Arriagada chunk/source-packet assignment is wrong.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Supported by one conflicted derivative transcript and contradicted by the visible source image. |
| conflict_severity | 0.94 | Accepting it would displace all Pulgar/Arriagada identity and relationship claims from this entry. |
| evidence_quality | 0.28 | Derivative-only support in direct conflict with the assigned chunk and source packet. |
| conversion_confidence | 0.12 | Low because the visible source image and staging identify the conversion as mismatched. |
| claim_probability | 0.14 | Plausible only if the chunk/source packet is attached to the wrong converted source. |
| relevance | 0.70 | Relevant chiefly as a false-positive guardrail. |
| canonical_readiness | 0.01 | Do not promote. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Pulgar-Line Jose/Juana Candidates

Literal evidence:

- The entry-172 Pulgar reading names father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` has a drafted child link to `Tulio Cesar Luis Jose` from a different staged relationship, not from this entry.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` has a drafted child link to `Tulio Cesar Luis Jose`; this name is not the same literal reading as `Juana Arriagada de Pulgar`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` carries this b8f4 entry-172 mother evidence as probable with very low confidence.

Interpretation:

- The father-name overlap justifies a targeted parent-candidate review, but the unresolved suffix and different child evidence prevent a merge by name alone.
- `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` must remain separate hypotheses unless a proof review establishes that the apparent surname/name differences are variant readings of the same person.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Plausible same-family cluster, not proven across entries. |
| conflict_severity | 0.58 | Premature merging could combine separate couples or misread mother-name variants. |
| evidence_quality | 0.52 | Local wiki/staged evidence exists, but not enough for cross-entry identity proof. |
| conversion_confidence | 0.35 | The b8f4 entry is conversion-blocked; related entries have their own review status. |
| claim_probability | 0.42 | Possible, but unresolved. |
| relevance | 0.86 | Important to Pulgar-line structure and downstream Dario-line hypotheses. |
| canonical_readiness | 0.08 | Hold pending targeted Jose/Juana parent-candidate proof review. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical context identifies him from family-supplied knowledge as Alexander John Heinz's maternal grandfather and explicitly warns not to merge similarly named Pulgar records without identity review. Entry 172 does not name him.
- `Dario Arturo Pulgar`: Staged CV packets use `Dario Arturo Pulgar` as document-level identity context. Entry 172 does not name Dario Arturo and gives no CV-era bridge.
- `Dario Jose Pulgar-Arriagada`: Staged ICRC/Geneva photograph packets name Dario Jose Pulgar-Arriagada from source titles or metadata. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose Pulgar-Arriagada.
- `Dario Pulgar Arriagada`: Existing canonical `dar-o-pulgar-arriagada.md` contains a 2000 expropriation event for `Dario Pulgar Arriagada`. Entry 172 is an 1888 birth-registration conflict for a different given-name cluster.
- Ranked impact: (1) direct impact on `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; (2) indirect need to keep Jose/Juana parent candidates unmerged; (3) no present evidence to attach this entry to any Dario identity.

## Conflicts

- Same-entry conflict: Pulgar/Arriagada source image, assigned chunk, and source packet versus Bunster/de la Maza converted Markdown. Severity: critical.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar`. Severity: moderate because it affects father identity matching.
- Relationship conflict: Parent-child links from this entry are not canonical-ready until conversion QA confirms which row controls. Severity: high.
- Duplicate-person risk: High if Bunster/de la Maza people are promoted from this mismatched conversion; moderate if Jose/Juana parent candidates are merged across Pulgar records without proof review.
- Chronology conflict: The two competing readings give different birth dates and places. Severity: high for this entry, low for Dario-line chronology because no Dario is named.

## Recommended Next Action

Keep the staged conflict and all affected claims/relationships at `hold_for_conversion_qa`.

Exact next proof-review step: perform targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the restored source image or authoritative page image, then revise or retire the converted Markdown/chunk assignment so entry 172 has one controlling transcript. That QA must explicitly decide whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form.

After conversion QA, run proof review on the child birth-name, birth-event, father, mother, and child-parent relationship claims. Separately run a Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar` across entries. Do not attach this entry to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada without a later identity-bridging source.
