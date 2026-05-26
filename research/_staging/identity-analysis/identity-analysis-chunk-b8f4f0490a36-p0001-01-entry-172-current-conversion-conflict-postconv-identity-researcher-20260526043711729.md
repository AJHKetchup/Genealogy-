---
type: identity_conflict_analysis
role: identity_researcher
status: hold
worker: postconv-identity-analysis-20260526043711729
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
referenced_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: hold_for_conversion_qa
created_at: 2026-05-26T04:37:11Z
---

# Identity Analysis: Entry 172 Current Conversion Conflict

## Blockers

- Material row-level blocker: the staged conflict draft reports two incompatible entry `172` readings for the same source path and chunk id. The assigned chunk/source packet reads a Pulgar/Arriagada row; the current converted Markdown reads a Burgos/de la Cruz row. This is not a spelling variant.
- Father-field blocker: under the Pulgar/Arriagada reading, the father may be `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Do not normalize or merge the father candidate until targeted conversion QA certifies the field.
- Canonical-readiness blocker: existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` contain provisional/generated context, but those pages do not resolve this current row conflict.
- Dario-line blocker: this staged draft does not name `Dario`, `Arturo`, `Smith`, `Dario Jose`, or a descendant/lineage bridge. It cannot support same-person attachment to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Darío Pulgar Arriagada, or other Dario candidates.

## Literal Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md`.
- Source packet: records entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- Referenced chunk: agrees with the Pulgar/Arriagada row and gives the same child, birth timing, place, parents, and informant cluster.
- Current converted Markdown: records entry `172` as `José Miguel`, male, born 6 April 1888 at 10 p.m. at `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.
- Existing canonical context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` carries provisional birth/child evidence tied to entry `172`; `wiki/people/juana-arriagada-de-pulgar.md` carries a probable child link to Jose del Carmen Segundo; `wiki/people/jose-del-carmen-pulgar.md` has a separate draft child context for Tulio Cesar Luis Jose, not a settled entry-172 parent link.
- Existing Dario context: `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather; `wiki/people/dar-o-pulgar-arriagada.md` is a separate stub with a 2000 expropriation mention. Staged Dario notes elsewhere keep `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, and `Dario/Darío Pulgar Arriagada` unresolved unless a separate identity bridge is proof-reviewed.

## Interpretation

The strongest narrow interpretation is that this staged task identifies a conversion-row conflict affecting entry `172`. If the chunk/source-packet row is controlling, the record concerns a non-Dario birth-registration cluster for `Jose del Carmen Segundo Pulgar Arriagada`, with parent candidates `Jose del Carmen Pulgar [suffix unresolved]` and `Juana Arriagada de Pulgar`. If the current converted Markdown is controlling, entry `172` instead concerns `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. These cannot both describe the same row.

Family context may justify a targeted double-check of the Pulgar/Arriagada row, but it does not justify correcting the converted Markdown silently or attaching the entry to any Dario-line person.

## Hypotheses

| rank | hypothesis | supporting evidence | conflicts / limits | claim probability |
| ---: | --- | --- | --- | ---: |
| 1 | Entry `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | Source packet and referenced chunk agree on child, parents, date, place, and informant; prior reviewed notes in staging repeatedly call for conversion QA rather than rejection of the Pulgar row. | Current converted Markdown gives an unrelated Burgos/de la Cruz row; father suffix remains unresolved. | 0.70 |
| 2 | Entry `172` is the Burgos/de la Cruz row for `Jose Miguel`. | Current converted Markdown explicitly transcribes entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`. | Conflicts with the assigned chunk/source packet and Pulgar-family staging; no Pulgar/Arriagada relevance if this controls. | 0.30 |
| 3 | `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` in this row is the same person as canonical `wiki/people/jose-del-carmen-pulgar.md`. | Shared name core and existing Pulgar-line context. | Exact father suffix is unresolved; existing canonical page has a separate draft child context and no settled entry-172 parent link. | 0.46 |
| 4 | `Juana Arriagada de Pulgar` in this row is the same person as canonical `wiki/people/juana-arriagada-de-pulgar.md`. | Same name form; canonical page already has provisional/generated entry-172 child context. | Depends on row QA; no independent identity details beyond the mother name and attributes in this task. | 0.64 |
| 5 | This entry provides a bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Darío Pulgar Arriagada. | Only broad surname/family-line interest. | The entry does not name Dario or supply a lineage chain. Existing Dario candidates remain separate/unresolved. | 0.03 |

## Conflict Assessment

- Same-person conflict: unresolved for father `Jose del Carmen Pulgar` versus existing canonical Jose page; unresolved for mother `Juana Arriagada de Pulgar` only because the controlling row is held.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is merged into `Jose del Carmen Pulgar` before suffix QA and parent-candidate proof review.
- Name-variant risk: moderate for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`; low-to-moderate for Juana candidates unless separate Juana context is introduced; minimal for Dario within this draft because no Dario appears.
- Relationship conflict: the Pulgar/Arriagada row would support child-parent relationships for `Jose del Carmen Segundo Pulgar Arriagada`; the converted Markdown supports unrelated Burgos/de la Cruz parents for entry `172`.
- Chronology conflict: Pulgar/Arriagada birth date is 8 March 1888; Burgos/de la Cruz birth date is 6 April 1888. The dates belong to competing row readings, not to a single person.

## Scores

| factor | score / value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | The Pulgar/Arriagada cluster is stronger than the converted-text alternative in staged context, but the row conflict blocks a settled identity conclusion. |
| conflict_severity | high | Child, parents, birth date, birth place, informant, and relationship candidates all change. |
| evidence_quality | 0.78 | Civil birth-register evidence is high value, and the chunk/source packet are detailed; derivative disagreement lowers usable quality until QA. |
| conversion_confidence | 0.38 | The current converted Markdown and assigned chunk materially disagree for the same entry number. |
| claim_probability | 0.70 | Probability that the staged Pulgar/Arriagada row is the relevant family candidate, not probability of canonical readiness. |
| relevance | high | Directly concerns the assigned staged conflict draft and referenced entry `172`. |
| canonical_readiness | 0.10 | Hold for conversion QA; no promotion, merge, or relationship update should proceed from this note. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, referenced chunk, and source packet. QA must decide the controlling entry `172` row and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review for child identity, birth facts, parent claims, child-parent relationships, and parent-candidate comparisons against existing Jose/Juana pages. A separate proof-reviewed lineage bridge is required before any Dario-line use.
