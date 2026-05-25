---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525175029140
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Conversion Conflict

This note analyzes the exact staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md`.

## Blockers First

1. The same assigned entry slot has two materially different readings. The staged conflict draft and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of a Pulgar father and Arriagada mother. The referenced converted Markdown identifies entry 172 as `José Francisco`, child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`, born at `En Pellin`.
2. This is not a spelling variant. It is a row-level, image-assignment, or converted-file assignment conflict.
3. The father field in the Pulgar/Arriagada reading is unresolved. The proof-review/control outcome must preserve all three possibilities: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` are not independent corroboration for this entry because their evidence snapshots include staged or draft b8f4f0490a36-derived material.
5. Entry 172 does not name Dario. It cannot bridge this record to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, or passenger/property/medical Dario clusters by surname pattern alone.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md`.
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md`.
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical wiki context for `Dario Arturo Pulgar-Smith`, `Darío Pulgar Arriagada`, `Dario Pulgar` passenger candidates, `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Existing local staged context located by repository search for `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario Pulgar-Arriagada`, `Dario Pulgar A.`, and Jose/Juana Pulgar-line candidates.

## Literal Source Readings Kept Separate

### Pulgar/Arriagada Reading

The current chunk and source packet support the following row-level reading for page 58, entry 172:

- Registration number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: broad reading `Jose del Carmen Pulgar`; chunk reads `Jose del Carmen Pulgar S.`; final suffix/mark unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age `Veintiseis años`, profession `Empleado`, residence `Calle de Valdivia`.

### Converted Markdown Reading

The referenced converted Markdown for the same assigned file and entry number gives a different row:

- Entry number: `172`.
- Child: `José Francisco`.
- Sex: `Hombre`.
- Birth: `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birth place: `En Pellin`.
- Father: `Oswaldo Gomez`.
- Mother: `Rosario de la Cruz de la Maza`.
- Informant: `Oswaldo Gomez`.

## Hypotheses And Evidence

| Rank | Hypothesis | Supporting evidence | Conflicts / limits | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | The controlling entry 172 is the Pulgar/Arriagada birth row, and the converted Markdown row is misassigned or stale. | The staged conflict draft and source packet say the assigned chunk and source-image review support `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`/`Pulgar S.`, mother `Juana Arriagada de Pulgar`. The current chunk also contains this Pulgar/Arriagada row. | The referenced converted Markdown still gives the unrelated Gomez/de la Cruz de la Maza row. Conversion QA has not certified which row controls. | 0.68 held |
| 2 | The controlling entry 172 is the Gomez/de la Cruz de la Maza row, and the Pulgar/Arriagada staged packet/chunk is misassigned. | The referenced converted Markdown explicitly gives `José Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza` for entry 172. | This conflicts with the staged image-reviewed source packet and current chunk. No Pulgar/Juana/Dario identity claim can proceed under this hypothesis. | 0.24 held |
| 3 | If hypothesis 1 is certified, the child candidate is `Jose del Carmen Segundo Pulgar Arriagada`. | The Pulgar/Arriagada row gives the full child name, male sex, birth date/time, and birth place. Existing canonical stub has b8f4f0490a36-derived evidence. | The canonical page is not independent proof; identity remains blocked by row conflict. | 0.66 conditional |
| 4 | If hypothesis 1 is certified, the father candidate is `Jose del Carmen Pulgar`, possibly with suffix/initial `S.`. | The Pulgar/Arriagada reading names a father as `Jose del Carmen Pulgar`; the current chunk has `Jose del Carmen Pulgar S.`. A canonical `Jose del Carmen Pulgar` stub exists. | The suffix/mark is unresolved; other local Jose Pulgar evidence exists but should not be merged by name alone. | 0.57 conditional |
| 5 | If hypothesis 1 is certified, the mother candidate is `Juana Arriagada de Pulgar`. | The Pulgar/Arriagada reading names mother `Juana Arriagada de Pulgar`; a canonical stub exists with b8f4f0490a36-derived material. | The canonical page is not independent proof. Do not merge with `Juana de Dios Amagada de Pulgar` or other Juana candidates from this entry alone. | 0.60 conditional |
| 6 | `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person. | Both are local Pulgar-line Juana candidates with married-name style `de Pulgar`, making this a future comparison target. | Entry 172 does not state `de Dios` or `Amagada`; separate entry-513 notes describe unresolved maternal surname issues. | 0.25 |
| 7 | Entry 172 directly supports `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Dario/Darío Pulgar Arriagada`. | Only the broader Pulgar/Arriagada surname pattern overlaps with staged Dario Pulgar-Arriagada medical/diplomatic/property clusters. | Entry 172 names `Jose del Carmen Segundo`, not Dario; no middle-name, age, occupation, parent-child, spouse, residence, medical, Geneva, passenger, or property bridge is present. | 0.04 |
| 8 | Entry 172 directly supports `Dario Arturo Pulgar` or canonical `Dario Arturo Pulgar-Smith`. | Only broad Pulgar surname context overlaps with the family-supplied canonical Dario page and staged CV/Habitat Dario clusters. | No `Dario`, `Arturo`, `Smith`, `Pulgar-Smith`, relationship to Alexander John Heinz, CV, Habitat, passenger, or chronology bridge appears in entry 172. | 0.02 |

## Conflict Types

- Same-person conflict: unresolved for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar [?]`.
- Duplicate-person risk: high if the father or mother candidates are merged into existing canonical pages before row QA and proof review.
- Name-variant conflict: high for the father suffix/mark; medium for Juana Arriagada versus other Juana Pulgar-line candidates; not supported for Dario variants from this entry.
- Relationship conflict: high for any parent-child relationship if derived from the disputed row before conversion QA; unsupported for any Dario relationship.
- Chronology conflict: not directly present inside the Pulgar/Arriagada row, but chronology cannot be used for Dario-line bridging because the entry supplies no Dario identity anchor.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | The Pulgar/Arriagada identity cluster is internally coherent in the source packet and current chunk, but the assigned converted Markdown conflicts at row level. |
| conflict_severity | 0.94 | The conflict changes the child, parents, birth date/time, place, and informant. |
| evidence_quality | 0.58 | Local staged image-review and chunk support are useful, but conversion disagreement blocks proof-level use. |
| conversion_confidence | 0.32 | The current converted Markdown and current chunk/source packet materially disagree. |
| claim_probability | 0.64 | Pulgar/Arriagada claims are plausible as held staged claims only; probability drops sharply for canonical promotion before QA. |
| relevance | 0.95 | The conflict is directly relevant to Pulgar/Arriagada identity, parent candidates, and anti-conflation with Dario clusters. |
| canonical_readiness | 0.08 | Not ready for canonical promotion, merge, or relationship attachment until conversion QA and renewed proof review. |

## Ranked Identity Handling

| Rank | Candidate / cluster | Handling |
| ---: | --- | --- |
| 1 | Entry 172 Pulgar/Arriagada child cluster: `Jose del Carmen Segundo Pulgar Arriagada` | Hold as a staged candidate only. Require row-level conversion QA first. |
| 2 | Father candidate: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` | Preserve all readings. Require targeted father-field certification before any canonical merge. |
| 3 | Mother candidate: `Juana Arriagada de Pulgar` | Hold as conditional on the Pulgar/Arriagada row. Compare separately with other Juana candidates only after row certification. |
| 4 | Converted-row cluster: `José Francisco`, `Oswaldo Gomez`, `Rosario de la Cruz de la Maza` | Preserve as the alternate controlling-row hypothesis until conversion QA resolves the assignment. |
| 5 | `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar-Arriagada`, `Dario Pulgar A.` | No attachment from this entry. Require direct identity-bearing local evidence tying a Dario identity to this Jose/Juana family cluster. |
| 6 | `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | No attachment from this entry. Require a separate reviewed bridge that explicitly connects the CV/family-supplied Dario identity to this Pulgar/Arriagada lineage. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current chunk, source packet, and referenced converted Markdown. The QA result must decide whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz de la Maza row and must certify the father field exactly as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review on only the certified row-level claims: child identity, registration date, birth date/time, birth place, father candidate, mother candidate, informant, parent-child relationships, and parent attributes. A separate identity-bridge review is required before any promotion or merge involving `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, or Jose/Juana parent-candidate consolidation.
