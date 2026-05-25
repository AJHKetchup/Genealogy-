---
type: identity_conflict_analysis
status: hold
role: identity_researcher
worker: postconv-identity-analysis-20260525123339261
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
conflict_type: row_level_conversion_conflict
canonical_readiness: hold_for_conversion_qa
---

# Identity Conflict Analysis: Entry 172 Conversion Conflict

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The assigned converted Markdown and the current chunk identify different row-level people for entry 172.
- The converted Markdown reads entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born `El veinte i seis de Marzo de mil ochocientos ochenta i ocho` at `En esta`.
- The current chunk and this task's source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde` at `Calle de Valdivia`.
- This is not a spelling variant, duplicate-person issue, or minor transcription disagreement. It is a material row-level conversion/file-assignment conflict.
- The father field remains unresolved at the suffix level: preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as possible QA outcomes until targeted conversion QA certifies the reading.
- The assigned entry does not name Dario. Do not attach this record to `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, or any Dario passenger candidate by surname or family context alone.
- Existing canonical wiki pages already contain some Entry 172-derived evidence for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`; this analysis does not edit or promote those pages. Their dependency on the conflicted b8f4f0490a36 evidence should be rechecked after conversion QA.

## Literal Evidence Reviewed

### Current chunk/source-packet reading

- Entry: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk and source packet, with the suffix explicitly flagged for QA.
- Mother: `Juana Arriagada de Pulgar`.
- Parent residence: `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at the birth.

### Assigned converted Markdown reading

- Entry: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `José Francisco`.
- Sex: `Varon`.
- Birth: `El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birth place: `En esta`.
- Father: `Oswaldo Gomez`.
- Mother: `Emilia de la Cruz`.
- Informant: `Oswaldo Gomez`.

### Reviewed notes and wiki context

- The 2026-05-25 conversion QA follow-up task for this same worker batch requires targeted QA against the source image, converted Markdown, current chunk, and source packet before dependent claims or relationships move forward.
- Earlier reviewed proof notes for the Entry 172 identity analysis also kept canonical readiness at `hold_for_conversion_qa`, while treating negative Dario attachment as a supported guardrail.
- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` currently carries Entry 172-derived birth facts and a probable parent link to `Juana Arriagada de Pulgar`.
- `wiki/people/juana-arriagada-de-pulgar.md` currently carries Entry 172-derived mother attributes and a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- `wiki/people/jose-del-carmen-pulgar.md` is a separate Jose candidate tied canonically to draft child `Tulio Cesar Luis Jose`, not to this Entry 172 child in the page snapshot reviewed here.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate Juana candidate tied canonically to draft child `Tulio Cesar Luis Jose`; similarity to `Juana Arriagada de Pulgar` is only a review lead.

## Hypotheses And Evidence

### Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Interpretation: The controlling row for register page 58, entry 172 is the Pulgar/Arriagada row, and the converted Markdown is misassigned or stale.

Evidence supporting:

- The current chunk and this task's source packet agree on the Pulgar/Arriagada row.
- Multiple local conversion/proof-review notes preserve the same row-level conflict and require QA rather than rejecting the Pulgar/Arriagada reading.
- Existing wiki pages have already been generated from the Pulgar/Arriagada interpretation, showing local relevance and prior extraction continuity.

Evidence limiting:

- The assigned converted Markdown for the same source path and converted SHA records a different entry 172 row.
- The father's suffix after `Pulgar` is unresolved.
- Existing wiki promotion cannot substitute for source-row QA because the conflict is in the derivative evidence chain itself.

Score: claim probability 0.78; identity confidence 0.74; evidence quality 0.72; conversion confidence 0.45; canonical readiness `hold_for_conversion_qa`.

### Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Interpretation: The controlling row for the assigned converted Markdown is correct, and the current chunk/source packet carry a row assignment error.

Evidence supporting:

- The assigned converted Markdown literally records entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`.

Evidence limiting:

- The staged conflict draft, current chunk, source packet, conversion QA task, and earlier proof reviews all identify this as a conflict requiring source-image reconciliation.
- The Gomez/de la Cruz row has no Pulgar/Arriagada names and provides no family relevance to the Pulgar line if it is the controlling row.

Score: claim probability 0.22; identity confidence 0.30; evidence quality 0.46; conversion confidence 0.45; canonical readiness `hold_for_conversion_qa`.

### Hypothesis 3: Jose del Carmen Pulgar In This Entry Is Same As Canonical `Jose del Carmen Pulgar`

Interpretation: The Entry 172 father, if the Pulgar row is confirmed, may be the same person as the canonical `Jose del Carmen Pulgar` page.

Evidence supporting:

- The broad name `Jose del Carmen Pulgar` matches the father name in the Pulgar-row reading.
- Both appear in local Pulgar-line context.

Evidence limiting:

- The reviewed canonical page currently links `Jose del Carmen Pulgar` to draft child `Tulio Cesar Luis Jose`, not to the Entry 172 child in its evidence snapshot.
- The Entry 172 father suffix/mark after `Pulgar` is unresolved.
- No birth date, spouse proof, residence bridge, or explicit same-person evidence has been reviewed here.

Score: same-person probability 0.34; identity confidence 0.38; conflict severity moderate; canonical readiness `hold_for_conversion_qa`.

### Hypothesis 4: `Juana Arriagada de Pulgar` Is Same As `Juana de Dios Amagada de Pulgar`

Interpretation: The Entry 172 mother candidate could be related to or conflated with the separate Juana candidate from other Pulgar-line staging.

Evidence supporting:

- Both are Juana + Pulgar-associated female parent candidates in local wiki context.
- Both appear in Jose/Juana parent-candidate comparison context.

Evidence limiting:

- The literal names differ: `Arriagada` versus `de Dios Amagada`.
- The reviewed canonical pages tie them to different child clusters.
- Similarity is a double-check lead, not evidence for a merge or name correction.

Score: same-person probability 0.18; identity confidence 0.24; duplicate-person risk high if merged by name/context alone; canonical readiness `do_not_merge`.

### Hypothesis 5: Entry 172 Child Or Parents Bridge To Dario-Line Candidates

Interpretation: The Entry 172 Pulgar/Arriagada child-parent cluster might connect later to a Dario identity, but this record itself does not prove that bridge.

Evidence supporting:

- The staged task requires Pulgar-line comparison because existing local context includes Dario candidates and Jose/Juana parent candidates.
- The surnames `Pulgar` and `Arriagada` overlap with some Dario-line candidate names.

Evidence limiting:

- Entry 172 names no Dario.
- The child name is `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Darío Pulgar Arriagada`.
- No reviewed source here states a child, spouse, parent, or identity bridge connecting Entry 172 to any Dario candidate.

Score: identity-bridge probability 0.06; identity confidence 0.12; relationship relevance as a future lead 0.42; canonical readiness `no_dario_attachment`.

## Required Pulgar-Line Comparison

| Candidate | Evidence in reviewed local context | Rank for this Entry 172 task | Judgment |
| --- | --- | ---: | --- |
| `Jose del Carmen Segundo Pulgar Arriagada` | Directly named by current chunk/source packet as Entry 172 child; contradicted by assigned converted Markdown. | 1 | Strong staged candidate if Pulgar row is confirmed; hold for conversion QA. |
| `Juana Arriagada de Pulgar` | Directly named by current chunk/source packet as Entry 172 mother; existing canonical page carries Entry 172-derived child link. | 2 | Strong staged mother candidate if Pulgar row is confirmed; hold for conversion QA. |
| `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` / `Jose del Carmen Pulgar [?]` | Father named in current chunk/source packet; exact suffix unresolved. | 3 | Broad father identity likely under Pulgar-row hypothesis; exact identity/page attachment requires father-field QA and parent proof review. |
| `Jose del Carmen Pulgar` canonical page | Existing page is tied to a different draft child cluster in reviewed snapshot. | 4 | Possible same-name candidate only; do not merge with Entry 172 father without identity bridge. |
| `Juana de Dios Amagada de Pulgar` | Existing page is tied to a different draft child cluster. | 5 | Anti-conflation candidate; do not normalize to `Juana Arriagada de Pulgar`. |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal grandfather identity; page warns not to merge similar source clusters automatically. | 6 | No attachment from this record; require explicit identity bridge before any comparison beyond guardrail. |
| `Dario Arturo Pulgar` | Staged CV document-subject candidate from `CV of Dario Arturo Pulgar.pdf`; separate page-image/proof-review holds. | 7 | No attachment from this record; no name, date, or relationship bridge. |
| `Dario Jose Pulgar-Arriagada` | Staged portrait/source-context candidate; low confidence and held for QA. | 8 | No attachment from this record; surname overlap only. |
| `Dario/Dario Pulgar Arriagada` / canonical `Darío Pulgar Arriagada` | Canonical page carries a 2000 Chiguayante expropriation event; separate Arriagada/Dario cluster. | 9 | No attachment from this record; surname overlap only and chronology bridge absent. |

## Conflict Summary

- Same-person conflict: unresolved for Entry 172 father versus canonical `Jose del Carmen Pulgar`; evidence is name-compatible but not identity-proof.
- Duplicate-person conflict: high risk for `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar` if normalized by eye; keep separate.
- Name-variant conflict: `Jose del Carmen Pulgar S.` may be a suffix/abbreviation/mark or uncertainty; do not encode as a stable variant until QA.
- Relationship conflict: current wiki has an Entry 172-derived mother-child link, but this task's evidence chain says dependent relationships must be held pending conversion QA.
- Chronology conflict: none within the Pulgar-row reading itself; no Dario chronology should be introduced from this record.
- Row-level conversion conflict: severe; converted Markdown and chunk cannot both be the same literal entry 172.

## Scores

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Pulgar-row child/mother identity is coherent in chunk/source packet, reduced by derivative row conflict. |
| conflict_severity | 0.92 | Different child, parents, dates, place, informant, and official signature context between converted Markdown and chunk. |
| evidence_quality | 0.72 | Civil registration source is strong, but this analysis relies on conflicting derivative readings and reviewed notes rather than performing new conversion. |
| conversion_confidence | 0.45 | Current chunk and converted Markdown disagree materially. |
| claim_probability | 0.78 | Best staged judgment: Pulgar-row hypothesis is likely enough for follow-up, not promotion. |
| relevance | 0.94 | Directly relevant to Pulgar/Arriagada child-parent evidence and anti-conflation controls. |
| canonical_readiness | hold_for_conversion_qa | Requires targeted conversion QA and rerun proof review before promotion. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned converted Markdown, current chunk, and this task's source packet. The QA result must decide whether the controlling entry 172 row is Pulgar/Arriagada or Gomez/de la Cruz, or whether one derivative file assignment must be superseded.

After QA, rerun proof review for:

- child identity and birth facts for `Jose del Carmen Segundo Pulgar Arriagada`;
- mother relationship and attributes for `Juana Arriagada de Pulgar`;
- father field representation as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`;
- any proposed same-person action involving canonical `Jose del Carmen Pulgar`;
- explicit anti-conflation checks against `Juana de Dios Amagada de Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Dario/Dario Pulgar Arriagada`.

No merge, rename, promotion, or Dario-line attachment is supported by this staged conflict note alone.
