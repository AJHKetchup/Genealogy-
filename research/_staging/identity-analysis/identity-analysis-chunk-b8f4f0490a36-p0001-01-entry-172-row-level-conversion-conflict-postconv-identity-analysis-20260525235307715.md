---
type: identity_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525235307715
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525231501805.md"
subject: "Entry 172 birth-registration row"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525231501805.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
conflict_type: row_level_conversion_conflict
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers

- The controlling converted Markdown and the assigned chunk/source-packet reading do not identify the same entry-172 family. This is a row-level conversion-control conflict, not a spelling variant.
- No child identity, birth fact, parent name, parent-child relationship, parent-candidate merge, or Dario/Pulgar-line bridge should be promoted from this draft until targeted conversion QA reconciles or supersedes the converted Markdown for page 58, entry 172.
- The father field is not certification-ready. The chunk reads `Jose del Carmen Pulgar S.`, while the source-packet review says targeted QA must decide whether the visible reading is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- The entry does not name Dario. Surname overlap and possible Pulgar/Arriagada family context are only double-check prompts, not evidence for merging this entry with any Dario candidate.

## Literal Source Readings Kept Separate

Assigned chunk/source-packet reading for page 58, entry 172:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: 8 March 1888 at 3 p.m., `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk; suffix unresolved by the source-packet reviewer.
- Mother: `Juana Arriagada de Pulgar`.
- Informant/compareciente: `Ernesto Herrera L.`, present at the birth, age 26, employee, resident at `Calle de Valdivia`.

Current converted Markdown reading for entry 172:

- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: 6 April 1888 at 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant/compareciente: `Oswaldo Burgos`.

The staged conflict draft correctly treats these as incompatible row readings.

## Hypotheses And Evidence

| Rank | Hypothesis | Supporting evidence | Conflicts / limits | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | Entry 172 is the Pulgar/Arriagada birth-registration row for `Jose del Carmen Segundo Pulgar Arriagada`. | The assigned chunk and source packet both identify page 58, entry 172 as the Pulgar/Arriagada row; the source-packet review reports visual support for row `172` as the Pulgar/Arriagada row. | The current converted Markdown for the same converted file gives a different family, date, and place; father suffix remains unresolved. | 0.78 |
| 2 | Entry 172 is the Burgos/de la Cruz registration for `Jose Miguel`. | The current converted Markdown says entry 172 has child `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`. | This conflicts with the assigned chunk and image-reviewed source packet; no Pulgar/Arriagada family relevance follows from this reading. | 0.18 |
| 3 | The repository has an assignment/page-control error where the converted file text and assigned chunk/source image are not aligned to the same register row or source image. | The two readings differ across child, parents, date, place, and informant, which is characteristic of row/file assignment failure rather than a normal transcription disagreement. | Identity analysis cannot repair conversion outputs; requires targeted conversion QA. | 0.82 |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to merge records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith without identity review. Entry 172 does not name Dario, Arturo, Smith, a spouse, child, grandchild, or any direct bridge to this canonical person. Probability same person or direct relationship proved here: 0.01.
- `Dario Arturo Pulgar`: staged CV packets identify a document-level subject by source title and work-history context, but those records concern a 20th-century CV subject and do not supply a parent-child bridge to the 1888 entry. Probability of attachment from this entry alone: 0.02.
- `Dario Jose Pulgar-Arriagada`: the portrait packet gives this name only from source title/path context and has low identity extraction confidence. Entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. Probability of same person from this entry alone: 0.03.
- `Dario J. Pulgar Arriagada` / `Dario Pulgar Arriagada`: the 1918 medical-title packet names `Darío J. Pulgar Arriagada` under `Medicos-Cirujanos`; the later canonical stub for `Dario Pulgar Arriagada` has a 2000 expropriation notice. Entry 172 does not contain `Dario` or a medical/legal-office bridge. Probability of same person from this entry alone: 0.03.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are plausible parent candidates under the Pulgar/Arriagada reading, but the father suffix is unresolved and existing wiki context also has separate `Jose del Carmen Pulgar` / `Juana de Dios Amagada de Pulgar` parents for `Tulio Cesar Luis Jose`. Do not merge the Jose or Juana candidates by name similarity. Probability that entry 172 supports a mother candidate named `Juana Arriagada de Pulgar`: 0.72. Probability that entry 172 supports a father candidate named `Jose del Carmen Pulgar` with unresolved suffix: 0.68.

## Conflicts

- Child identity conflict: `Jose del Carmen Segundo Pulgar Arriagada` versus `Jose Miguel`.
- Parent conflict: `Jose del Carmen Pulgar S.` / `Juana Arriagada de Pulgar` versus `Oswaldo Burgos` / `Concepcion de la Cruz`.
- Chronology conflict: birth on 8 March 1888 at 3 p.m. versus 6 April 1888 at 10 p.m.
- Place conflict: `Calle de Valdivia` versus `En esta`.
- Informant conflict: `Ernesto Herrera L.` versus `Oswaldo Burgos`.
- Relationship conflict: the Pulgar/Arriagada reading creates a possible child-parent cluster; the converted Markdown creates an unrelated Burgos/de la Cruz cluster.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Moderate-high for a Pulgar/Arriagada entry-172 cluster, held down by the controlling converted-file conflict. |
| conflict_severity | 0.95 | Whole-row identity, parents, date, place, and informant disagree. |
| evidence_quality | 0.82 | Civil birth register image/chunk/source packet are strong, but the repository artifacts disagree. |
| conversion_confidence | 0.35 | The current converted Markdown is unreliable for this row until QA resolves the mismatch. |
| claim_probability | 0.78 | The Pulgar/Arriagada reading is more likely than the Burgos reading for the assigned image/chunk, but not promotion-ready. |
| relevance | 0.88 | High Pulgar/Arriagada relevance if the row is confirmed; low direct Dario relevance. |
| canonical_readiness | 0.00 | Hold. No promotion or merge should occur before conversion QA and proof review. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`, page 58, entry 172. The QA step must reconcile or supersede the converted Markdown, preserve the literal row reading, and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, run proof review on the child identity, birth facts, and Jose/Juana parent-child relationship candidates. Only after a separate identity-bridge review should any evidence be compared for attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.
