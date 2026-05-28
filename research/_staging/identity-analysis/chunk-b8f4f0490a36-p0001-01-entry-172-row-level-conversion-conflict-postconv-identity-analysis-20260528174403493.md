---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528165422297.md"
worker: "postconv-identity-analysis-20260528174403493"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528165422297.md"
subject: "Los Angeles birth register entry 172"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
promotion_recommendation: "hold_for_proof_review"
tags: [identity-analysis, conflict-review, row-control, pulgar]
---

# Identity And Conflict Analysis: Entry 172 Row-Control Conflict

## Blockers First

- The exact staged conflict draft analyzed here is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260528165422297.md`.
- The current converted Markdown for the same source file records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. The assigned chunk, source packet, and targeted row-control review instead identify physical entry `172` on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- This is a material derivative-conversion conflict, not a spelling or name-variant issue. The Burgos/de la Cruz text must be preserved as a conversion conflict and must not be merged into the Pulgar/Arriagada evidence.
- The father field is bounded to `Jose del Carmen Pulgar`; the trailing `S.` in the assigned chunk is not certified by the row-control review and should not be promoted from this task.
- The entry does not name `Dario`, `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar A.`, or `Dario/Dario Pulgar Arriagada`. Any Dario-line attachment requires a separate identity bridge.
- Existing canonical context contains Pulgar-line stubs and held identity clusters. Those are relevant anti-conflation checks, not proof that this 1888 birth entry belongs to a Dario-line person.
- No raw source, converted Markdown, chunk Markdown, source packet, reviewed note, or canonical wiki page was edited.

## Literal Source Reading

The assigned chunk records entry `172` on page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered on `Siete de Abril de mil ochocientos ochenta i ocho`, born on `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, at `Calle de Valdivia`.

The assigned chunk gives father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`. The targeted row-control QA narrows the image-controlled father reading to `Jose del Carmen Pulgar` and explicitly leaves the trailing suffix or mark uncertified.

Interpretation kept separate: the Pulgar/Arriagada row supports a birth-registration evidence cluster for the named child and stated parents after proof review. It does not itself prove a same-person, ancestor, descendant, or name-variant bridge to any Dario identity.

## Hypothesis 1: Physical Entry 172 Is The Pulgar/Arriagada Birth Row

Hypothesis: The source-controlled row for entry `172` is `Jose del Carmen Segundo Pulgar Arriagada`, male child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

Supporting evidence:

- The source packet identifies the image-controlled physical row as `Jose del Carmen Segundo Pulgar Arriagada birth registration`.
- The conversion review states that direct review of the original page image supports the middle row on register page 58 as physical entry `172`, the Pulgar/Arriagada birth registration.
- The assigned chunk gives the same row content for entry `172`, including registration date, birth date/time, birthplace, parents, residence, and informant.
- Existing canonical stubs for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` preserve this cluster cautiously, with evidence snapshot labels remaining probable, draft, or unknown where appropriate.

Conflicts and limits:

- The current converted Markdown is contradictory and names an unrelated Burgos/de la Cruz family for entry `172`.
- The father's trailing suffix or mark after `Pulgar` is not certified.
- Parent-child promotion should wait for proof review acceptance of the row-control QA and bounded father-field reading.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.91 | Strong agreement between row-control QA, source packet, and assigned chunk for the Pulgar/Arriagada physical row. |
| conflict_severity | 0.86 | The competing converted entry names a different child and different parents. |
| evidence_quality | 0.84 | Civil birth register row plus targeted image review; one derivative transcript conflict remains. |
| conversion_confidence | 0.82 | Row-control review is high; original converted Markdown is unreliable for this row. |
| claim_probability | 0.90 | Very probable that physical row 172 records the Pulgar/Arriagada birth. |
| relevance | 1.00 | Directly addresses the staged draft. |
| canonical_readiness | 0.58 | Ready for proof review, not direct promotion or merge. |

## Hypothesis 2: The Burgos/de la Cruz Text Is The Same Person Or A Variant

Hypothesis: `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, is a name variant or alternate reading of the Pulgar/Arriagada entry.

Supporting evidence:

- Both readings are assigned to entry number `172` in different derivative artifacts.

Conflicts and limits:

- The names, parents, birth dates, and family context differ materially.
- The row-control QA explicitly states that the Burgos/de la Cruz text is not the physical row 172 controlled for this task.
- No reviewed evidence supports treating `Jose Miguel` as `Jose del Carmen Segundo Pulgar Arriagada` or treating Burgos/de la Cruz parents as variants of Pulgar/Arriagada parents.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.02 | Only the entry-number collision connects them; all identity fields conflict. |
| conflict_severity | 0.94 | Merging would replace the child and both parents with unrelated people. |
| evidence_quality | 0.24 | Burgos/de la Cruz support is derivative and contradicted by row-control QA. |
| conversion_confidence | 0.12 | The current converted Markdown is unreliable for this row. |
| claim_probability | 0.02 | Same-person or variant reading is effectively unsupported. |
| relevance | 0.96 | Central derivative conflict. |
| canonical_readiness | 0.00 | Do not promote or merge. |

## Hypothesis 3: Same Person As Dario Arturo Pulgar-Smith

Hypothesis: The child or parent cluster in entry `172` is the same person as canonical `Dario Arturo Pulgar-Smith`.

Supporting evidence:

- The canonical page for `Dario Arturo Pulgar-Smith` is Pulgar-line context and explicitly warns that Pulgar-name records need identity review before attachment.
- The surname `Pulgar` appears in both clusters.

Conflicts and limits:

- Entry `172` does not name `Dario`, `Arturo`, `Smith`, a grandchild, spouse, child, or any relationship to Alexander John Heinz.
- The child in entry `172` was born in 1888. Canonical `Dario Arturo Pulgar-Smith` is represented only from family-supplied knowledge as Alexander John Heinz's maternal grandfather, with no bridge to this 1888 birth row in the reviewed materials.
- Name overlap alone is explicitly insufficient under the canonical identity notes.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | Shared `Pulgar` surname only. |
| conflict_severity | 0.72 | Premature attachment would create a serious duplicate-person and lineage conflict. |
| evidence_quality | 0.34 | The birth row is good for its own cluster, but gives no Dario-Smith bridge. |
| conversion_confidence | 0.70 | Pulgar row is usable after proof review; same-person attachment is unsupported. |
| claim_probability | 0.02 | No direct identity evidence. |
| relevance | 0.80 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not attach to Pulgar-Smith. |

## Hypothesis 4: Same Person As Dario Arturo Pulgar

Hypothesis: The entry `172` Pulgar/Arriagada cluster is the same person as the staged CV subject `Dario Arturo Pulgar`.

Supporting evidence:

- Existing staged CV materials preserve a document-level subject named `Dario Arturo Pulgar`.
- The birth row and CV subject share the surname `Pulgar`.

Conflicts and limits:

- Entry `172` does not name `Dario Arturo Pulgar`.
- Existing CV identity analyses keep the bridge from `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith` on hold; this birth row adds no bridge to that CV cluster.
- The birth row's named child is `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Arturo Pulgar`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.04 | Surname overlap without given-name, chronology, occupation, or family bridge. |
| conflict_severity | 0.66 | Risk of conflating separate Pulgar clusters. |
| evidence_quality | 0.38 | Both clusters may be useful locally, but not linked by this source. |
| conversion_confidence | 0.68 | Entry row-control is strong; CV linkage is outside this source. |
| claim_probability | 0.03 | Unsupported by the entry. |
| relevance | 0.78 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | No attachment supported. |

## Hypothesis 5: Same Person As Dario Jose Pulgar-Arriagada Or Dario/Dario Pulgar Arriagada

Hypothesis: The entry `172` child or parent cluster is the same person as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar A.`, or canonical/staged `Dario/Dario Pulgar Arriagada`.

Supporting evidence:

- `Jose del Carmen Segundo Pulgar Arriagada` and `Dario/Dario Pulgar Arriagada` share the `Pulgar Arriagada` surname combination.
- Existing local context includes separate Pulgar-Arriagada clusters: staged ICRC/Geneva materials for `Dario Jose Pulgar-Arriagada`, medical/passenger/property clusters for `Dario Pulgar A.` or `Dario J. Pulgar Arriagada`, and a canonical `Darío Pulgar Arriagada` stub tied to a 2000 Chiguayante expropriation notice.

Conflicts and limits:

- Entry `172` names `Jose del Carmen Segundo`, not `Dario`, `Dario Jose`, `Dario J.`, or `Darío`.
- The entry gives no medical title, 1928/1953 passenger details, Geneva context, property notice, or 2000 Chiguayante connection.
- Existing Pulgar-Arriagada clusters have their own QA and chronology holds; none supplies a direct bridge to this 1888 child in the reviewed materials.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Surname combination is relevant but given-name mismatch is substantial. |
| conflict_severity | 0.74 | High risk of collapsing separate Pulgar-Arriagada people by surname alone. |
| evidence_quality | 0.42 | Compared clusters are mixed and often held for proof review. |
| conversion_confidence | 0.58 | Entry row-control is stronger than the broader identity bridge evidence. |
| claim_probability | 0.06 | Possible family-line lead only; no same-person proof. |
| relevance | 0.86 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Preserve separately; do not merge. |

## Hypothesis 6: Jose/Juana Parent Candidates Are The Stated Parents In This Row

Hypothesis: Entry `172` supports the local parent candidates `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` as stated parents of `Jose del Carmen Segundo Pulgar Arriagada`.

Supporting evidence:

- The row-control QA records father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- The assigned chunk records the same parents, with a non-certified trailing `S.` after the father's surname.
- Existing canonical `Juana Arriagada de Pulgar` has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- Existing canonical `Jose del Carmen Pulgar` separately has a draft child link to `Tulio Cesar Luis Jose`; existing `Juana de Dios Amagada de Pulgar` also has a draft link to that Tulio cluster. These show that same-name Jose and Juana parent candidates require careful review rather than automatic merging.

Conflicts and limits:

- The father suffix is not certified.
- This row does not prove that the `Jose del Carmen Pulgar` here is the same person as any other Jose del Carmen Pulgar candidate in other register entries.
- This row does not prove that `Juana Arriagada de Pulgar` is the same as any other Juana/Amagada/Arriagada candidate outside this source cluster.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.76 | Strong for source-stated parent roles within the row; lower for cross-record parent identity. |
| conflict_severity | 0.48 | Main risk is over-merging same-name parents across entries. |
| evidence_quality | 0.78 | Civil register row with row-control review. |
| conversion_confidence | 0.80 | Parent names controlled except father's trailing suffix. |
| claim_probability | 0.82 | Probable stated-parent evidence after proof review. |
| relevance | 0.94 | Directly relevant to the staged row. |
| canonical_readiness | 0.46 | Promote only after proof review; no cross-record parent merge from this task. |

## Conflict Summary

- Same-person conflict: the Pulgar/Arriagada child is not supported as the same person as the derivative `Jose Miguel` Burgos/de la Cruz entry.
- Duplicate-person risk: high if `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or `Jose del Carmen Segundo Pulgar Arriagada` are merged with same-name or surname-similar candidates outside this row without identity-bridge evidence.
- Name-variant conflict: this row supports `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`. It does not support variants `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar A.`, or `Dario/Darío Pulgar Arriagada`.
- Relationship-conflict evidence: the row supports a stated parent-child relationship inside the birth entry after proof review, but not a relationship to any Dario cluster.
- Chronology-conflict evidence: no direct chronology contradiction inside the Pulgar/Arriagada row. Chronology becomes risky only if the 1888 child is merged into later Dario clusters without a vital-date and identity bridge.
- Conversion-confidence conflict: the row-control QA and chunk are stronger than the current converted Markdown for this row. Treat the converted Burgos/de la Cruz text as a derivative conflict.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Physical entry `172` is the Pulgar/Arriagada birth row | 0.90 | Send to proof review using the row-control QA; promote only bounded row claims if accepted. |
| 2 | `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are source-stated parents in this row | 0.82 | Hold for proof review; do not cross-merge parent candidates. |
| 3 | Same as `Dario Jose Pulgar-Arriagada` / `Dario/Darío Pulgar Arriagada` / `Dario Pulgar A.` | 0.06 | Preserve as anti-conflation context only. |
| 4 | Same as `Dario Arturo Pulgar` | 0.03 | No attachment; requires independent identity-bearing bridge. |
| 5 | Same as canonical `Dario Arturo Pulgar-Smith` | 0.02 | No attachment; requires independent identity-bearing bridge and promotion review. |
| 6 | Burgos/de la Cruz text is the same person/family as Pulgar/Arriagada | 0.02 | Reject as derivative conversion conflict; do not merge. |

## Recommended Next Action

Run proof review on the staged conflict draft and row-control QA for entry `172`. The exact review should accept or reject the image-controlled reading that physical row `172` is `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, while keeping the father field bounded to `Jose del Carmen Pulgar` unless the trailing mark after `Pulgar` is independently certified.

If proof review accepts the row-control evidence, promote only narrow birth-registration and stated-parent claims for the Pulgar/Arriagada row. Preserve the Burgos/de la Cruz material as a derivative conversion conflict. Do not merge people, rename canonical pages, attach the entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or any Jose/Juana parent candidate outside this row until a separate identity-bridge proof review supplies direct evidence.
