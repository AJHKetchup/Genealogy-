---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525211334388
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
conflict_type: row_level_conversion_conflict
canonical_readiness: not_ready
---

# Identity Analysis: Entry 172 Row Conflict Hold

## Blockers First

- The exact staged draft under review is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md`.
- The assigned chunk and staged source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the assigned converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This is an incompatible row-level conflict, not a spelling or name-variant conflict. Identity analysis cannot choose a canonical person or relationship until targeted conversion QA certifies the controlling row.
- The father field in the Pulgar/Arriagada reading remains specifically unresolved: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical wiki pages contain generated evidence for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` from this chunk family. Those pages should not be treated as resolving the current conversion conflict.
- Entry 172 does not literally name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario Pulgar Arriagada`. Any Dario-line use is an anti-conflation check only.

## Literal Evidence

The staged source packet repeats the assigned chunk's Pulgar/Arriagada row for page 58, entry 172: registration on 7 April 1888, child `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar S.`, Chilean, employee, resident Calle de Colipi; mother `Juana Arriagada de Pulgar`, Chilean, resident Calle de Colipi.

The assigned chunk contains the same Pulgar/Arriagada row and presents entries 171-176 on a two-page spread. Its page 58 entry 172 conflicts with the assigned converted Markdown.

The assigned converted Markdown gives a different page 58 entry 172: child `Jose Miguel`, male, born 6 April 1888 at 10 p.m.; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; declarant `Oswaldo Burgos`.

Existing canonical wiki context includes a stub for `Jose del Carmen Segundo Pulgar Arriagada` with generated birth facts from the older entry-172 source packet; a stub for `Juana Arriagada de Pulgar` with a probable child link to that child; a stub for `Jose del Carmen Pulgar` with a separate draft child link to `Tulio Cesar Luis Jose`; and a separate stub for `Juana de Dios Amagada de Pulgar` linked to `Tulio Cesar Luis Jose`.

## Hypotheses

| Rank | Hypothesis | Supporting evidence | Conflicts and limits | Claim probability |
| ---: | --- | --- | --- | ---: |
| 1 | The controlling source row for entry 172 is the Pulgar/Arriagada birth of `Jose del Carmen Segundo Pulgar Arriagada`. | The staged source packet and assigned chunk agree on the Pulgar/Arriagada row; the source packet states family relevance and holds only for conversion QA. Existing canonical generated evidence also reflects this row family. | The assigned converted Markdown gives a complete Burgos/de la Cruz row for the same entry number. Father suffix remains unresolved. | 0.70 |
| 2 | The controlling source row for entry 172 is the Burgos/de la Cruz birth of `Jose Miguel`. | The assigned converted Markdown gives a coherent entry 172 for `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`. | The staged source packet and assigned chunk directly contradict it; no Pulgar/Arriagada evidence would survive if this row controls. | 0.22 |
| 3 | Both rows are real register rows, but one derivative artifact is assigned to the wrong page, row, or image boundary. | The two readings are internally coherent but mutually incompatible under the same entry number, which is consistent with source-to-conversion assignment drift. | Requires targeted image and artifact QA; cannot be settled from identity context alone. | 0.62 |
| 4 | `Jose del Carmen Pulgar S.` in the Pulgar/Arriagada row is the same person as canonical `Jose del Carmen Pulgar`. | The name core matches; the existing `Jose del Carmen Pulgar` page already has a Pulgar-line parent context from a separate child relationship. | The `S.` suffix is unresolved, and the other canonical link involves `Tulio Cesar Luis Jose`, not this entry-172 child. Same-person evidence is insufficient. | 0.46 |
| 5 | `Juana Arriagada de Pulgar` in this row is the same person as canonical `Juana Arriagada de Pulgar`. | Exact name match and existing generated evidence connect her as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`. | The underlying row conflict blocks readiness. This does not prove same-person identity with `Juana de Dios Amagada de Pulgar` or any other Juana candidate. | 0.61 |
| 6 | `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person under variant readings. | Both are Juana-with-Pulgar parent candidates in existing wiki context. | Literal surnames differ (`Arriagada` versus `Amagada`), children differ, and this staged draft supplies no direct identity bridge. Family-context overlap supports only a double-check. | 0.28 |
| 7 | Entry 172 provides a lineage bridge to a Dario candidate. | The Pulgar surname and an Arriagada mother appear if the Pulgar/Arriagada row controls. | No Dario, Arturo, Smith, Dario Jose, medical-title, CV, expropriation, spouse, child, or grandchild evidence appears in entry 172. Name overlap is not enough. | 0.05 |

## Conflict Assessment

- Same-person conflict: moderate for `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar`; moderate for `Juana Arriagada de Pulgar` versus other Juana parent candidates; low-to-moderate for Dario candidates because entry 172 does not name them.
- Duplicate-person conflict: possible for `Juana Arriagada de Pulgar` if generated canonical evidence is assumed to settle this row before QA; possible for Jose parent candidates only after father-field review.
- Name-variant conflict: the father suffix `S.` is an unresolved reading; `Jose Miguel` and `Jose del Carmen Segundo Pulgar Arriagada` are separate identity readings, not variants.
- Relationship conflict: high. The two derivative readings assign different children to different parents under the same entry number.
- Chronology conflict: high. The Pulgar/Arriagada reading gives birth on 8 March 1888; the Burgos/de la Cruz reading gives birth on 6 April 1888.

## Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.56 | The Pulgar/Arriagada row has stronger staged support, but the assigned converted Markdown is directly incompatible. |
| conflict_severity | 0.93 | Child identity, parent identities, birth date, and parent-child relationships all change depending on the controlling row. |
| evidence_quality | 0.72 | Civil birth registration evidence would be strong, but the current usable evidence is derivative and pending targeted QA. |
| conversion_confidence | 0.28 | Assigned chunk and assigned converted Markdown disagree at row level. |
| claim_probability | 0.70 | Best current narrow probability favors the Pulgar/Arriagada row, but not to promotion standard. |
| relevance | 0.89 | Highly relevant to Pulgar/Arriagada parent-child identity sorting and to preventing Dario-line overreach. |
| canonical_readiness | 0.10 | Not ready for promotion, merge, relationship creation, or Dario-line attachment. |

## Dario-Line Anti-Conflation Ranking

| Candidate | Rank for use from this entry | Evidence comparison |
| --- | ---: | --- |
| Jose/Juana parent candidates | 1 | The only directly relevant identities are the recorded parents if the Pulgar/Arriagada row controls. Next step: conversion QA must certify the row and father field before proof review evaluates parent identity and any Jose/Juana same-person question. |
| Dario Arturo Pulgar-Smith | 5 | Canonical page is family-supplied as Alexander John Heinz's maternal grandfather. Entry 172 gives no Dario, Arturo, Smith, grandchild, or family bridge. |
| Dario Arturo Pulgar | 5 | CV-related staged context elsewhere uses this document-level name, but entry 172 does not name or bridge to it. |
| Dario Jose Pulgar-Arriagada / Dario J. Pulgar Arriagada | 4 | Arriagada and Pulgar appear only in the disputed Pulgar/Arriagada row. The child here is `Jose del Carmen Segundo`, not `Dario Jose` or `Dario J.` |
| Dario Pulgar Arriagada / Darío Pulgar Arriagada | 4 | Existing canonical context has a 2000 expropriation event for `Darío Pulgar Arriagada`; entry 172 is an 1888 birth row with no same-person bridge. |

## Recommended Next Action

Keep this staged draft on `hold_for_conversion_qa`. The exact next proof-review or promotion step is targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and this staged source packet to certify the controlling row for entry 172 and the father-name field. After that, rerun proof review before any child identity, parent relationship, Jose/Juana same-person conclusion, or Dario-line bridge is promoted. Do not merge `Jose del Carmen Pulgar S.` with `Jose del Carmen Pulgar`, do not merge Juana variants, and do not attach this entry to any Dario candidate by name overlap alone.
