---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525093246706
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Conversion Conflict

## Blockers First

- The exact staged conflict draft reviewed is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md`.
- The assigned converted Markdown and the assigned chunk disagree on the controlling entry 172 row. The chunk/source-packet layer records a Pulgar/Arriagada birth registration; the converted-file layer records a different child and different parents.
- This is a row-level conversion or file-assignment conflict, not a name variant, duplicate-person issue, or minor spelling problem.
- No canonical person merge, relationship promotion, name normalization, or Dario-line linkage should be made from this evidence until targeted conversion QA reconciles the source image, converted Markdown, and chunk.
- The father-name ending remains unresolved. Preserve the alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until a source-image QA note certifies the literal reading.

## Literal Evidence Layer

The current chunk and staged source packet support this entry-172 reading:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk, with the final element held as unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth.

The assigned converted Markdown instead records entry 172 as:

- Child: `Jose Francisco`.
- Birth date/time: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birth place: `En esta`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.
- Informant: `Oswaldo Gomez`.

## Hypotheses Ranked

| Rank | Hypothesis | Current judgment | Probability | Identity confidence | Evidence basis |
| ---: | --- | --- | ---: | ---: | --- |
| 1 | The assigned chunk/source-packet row is the family-relevant entry 172 for `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`. | Plausible but blocked. | 0.72 | 0.68 | Chunk and staged packet agree, but converted-file disagreement blocks promotion. |
| 2 | The assigned converted Markdown row is the controlling entry 172 for `Jose Francisco`, child of `Oswaldo Gomez` and `Emilia de la Cruz`. | Plausible as derivative text, but conflicts with the chunk/source-packet row. | 0.35 | 0.30 | Converted file says this, but the staged conflict and chunk identify it as a material mismatch. |
| 3 | The Pulgar/Arriagada row and the Gomez/de la Cruz row are duplicate or same-person references. | Not supported. | 0.03 | 0.02 | Names, parents, date/place details, and informant differ materially. |
| 4 | `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` are variants of the same father reading in this row. | Hold as literal-reading alternatives, not separate persons yet. | 0.55 | 0.45 | The base name is consistent in the chunk; the suffix/final mark needs QA. |
| 5 | `Juana Arriagada de Pulgar` is the mother in the Pulgar/Arriagada row. | Plausible but blocked with the row. | 0.70 | 0.66 | Chunk and source packet agree; converted-file conflict prevents readiness. |
| 6 | `Juana Arriagada de Pulgar` is the same person as `Juana de Dios Amagada de Pulgar` or another Juana parent candidate. | Not supported from this draft. | 0.18 | 0.15 | Existing wiki context has separate Juana candidates; this entry does not prove a merge. |
| 7 | Entry 172 supplies an identity bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. | Not supported. | 0.05 | 0.05 | This entry does not name Dario, Arturo, Smith, Dario Jose, or any later professional/property/passenger context. |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merges with similarly named Pulgar records. Entry 172 does not name him or bridge to him.
- `Dario Arturo Pulgar`: existing staged CV work treats this as a document-level subject requiring a separate identity bridge to `Dario Arturo Pulgar-Smith`. Entry 172 has no `Dario` or `Arturo` evidence.
- `Dario Jose Pulgar-Arriagada`: staged photograph/ICRC contexts use this name, but this entry does not name Dario Jose or provide age, occupation, residence, event context, or family bridge.
- `Dario/Dario Pulgar Arriagada`: existing canonical `Darío Pulgar Arriagada` has a narrow 2000 legal-notice/expropriation evidence snapshot. Entry 172 is an 1888 birth registration for a different named child if the chunk is confirmed, and it cannot connect the 2000 notice subject to this family by surname alone.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar` remain possible parents only within the unresolved Pulgar/Arriagada row. Do not merge them with `Jose del Carmen Pulgar` or `Juana de Dios Amagada de Pulgar` canonical/staged candidates until the row and literal names are proof-reviewed.

## Conflicts

- Conversion conflict severity: critical. The child, father, mother, birth date/place, and informant differ between converted Markdown and chunk/source packet.
- Relationship conflict severity: high if promoted prematurely. The Pulgar child-parent relationship and the Gomez/de la Cruz child-parent relationship cannot both describe the same row as currently staged.
- Chronology conflict severity: medium. The conflicting rows have different March 1888 birth dates, but the bigger issue is row identity rather than life chronology.
- Name-variant conflict severity: medium for the father suffix only; critical for treating the two entry-172 rows as variants.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Moderately strong for the Pulgar/Arriagada cluster within the chunk, but not reliable enough for canonical use while the converted file disagrees. |
| conflict_severity | 0.95 | Material row-level disagreement across multiple identity and relationship fields. |
| evidence_quality | 0.62 | Civil birth registration is strong in principle; the local evidence chain is impaired by derivative transcript disagreement. |
| conversion_confidence | 0.34 | Chunk and converted file are inconsistent for the same assigned entry. |
| claim_probability | 0.72 | The Pulgar/Arriagada row is plausible from the chunk/source packet but remains unpromoted. |
| relevance | 0.90 | Directly relevant to Pulgar/Arriagada parent-candidate work if QA confirms the row. |
| canonical_readiness | 0.10 | Hold for conversion QA and later proof review. |

## Recommended Next Action

Run targeted conversion QA on the source image, assigned converted Markdown, current chunk, and staged source packet. The QA note must decide which row is controlling for entry 172 and must record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth claim, parent-child relationship, parental-pair clue, Jose/Juana merge, or Dario-line comparison. Until then, keep all dependent staged claims and relationships at `hold_for_conversion_qa`.
