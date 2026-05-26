---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526140528374
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-evidence-extraction-20260526095657171.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-evidence-extraction-20260526095657171.md
subject: "register page 58, entry 172"
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Entry 172 Current Conversion Conflict

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-evidence-extraction-20260526095657171.md`.
- Material row-level conflict: the staged source packet and current chunk support a Pulgar/Arriagada entry 172, while the current converted Markdown describes a Burgos/de la Cruz entry 172.
- The source packet reports image review supporting the Pulgar/Arriagada row, but the assigned converted Markdown still contains the incompatible Burgos/de la Cruz row.
- The father field is not fully certified. Safe staged reading is `Jose del Carmen Pulgar`; the chunk reads `Jose del Carmen Pulgar S.`, but the final `S.` or other trailing mark requires targeted conversion QA.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` contain low-, draft-, probable-, or held-context evidence and must not be used as independent proof that this conversion conflict is resolved.
- No same-person merge, duplicate-person merge, name-variant certification, relationship promotion, or Dario-line bridge is ready.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, or canonical wiki pages were edited.

## Literal Source Readings

Current chunk and staged source-packet-supported reading:

```text
Entry 172 records Jose del Carmen Segundo Pulgar Arriagada, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at Calle de Valdivia; father read safely in the staged packet as Jose del Carmen Pulgar, with the chunk reading Jose del Carmen Pulgar S.; mother Juana Arriagada de Pulgar; informant Ernesto Herrera L.
```

Current converted Markdown reading:

```text
Entry 172 records Jose Miguel, male, registered 7 April 1888, born 6 April 1888 at 10 p.m. in En esta; father Oswaldo Burgos; mother Concepcion de la Cruz; informant Oswaldo Burgos.
```

Interpretation: local staged evidence favors the Pulgar/Arriagada row as the intended entry 172, but the identity and relationship claims remain blocked because the derivative files disagree materially.

## Hypothesis 1: Entry 172 Is Jose del Carmen Segundo Pulgar Arriagada

Evidence supporting:

- The staged conflict draft states that the image/current-chunk-supported reading records `Jose del Carmen Segundo Pulgar Arriagada`.
- The source packet says image review supports the Pulgar/Arriagada row as register entry 172.
- The current chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`.
- Canonical `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` reflects the same child-name cluster and 1888-03-08 15:00 birth event, but its evidence snapshot depends on this entry-172 source cluster and does not resolve the conversion conflict independently.

Conflicts and limits:

- The assigned converted Markdown records a different child, parents, birth date, place wording, and informant.
- The father-field ending remains unresolved and cannot be silently normalized.
- Canonical promotion is blocked until conversion QA reconciles image, chunk, converted Markdown, and source packet.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Image-reviewed packet and chunk align, but converted Markdown conflicts. |
| conflict_severity | 0.90 | Competing reading changes child, parents, date, place, and informant. |
| evidence_quality | 0.66 | Useful local staged evidence, still derivative-conflicted. |
| conversion_confidence | 0.35 | Low until row mismatch is reconciled. |
| claim_probability | 0.78 | Probable controlling row, not promotable. |
| relevance | 1.00 | Direct staged subject. |
| canonical_readiness | 0.10 | Hold for conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is Jose Miguel, Child Of Oswaldo Burgos And Concepcion de la Cruz

Evidence supporting:

- The current converted Markdown explicitly labels a Burgos/de la Cruz row as entry 172.
- The converted reading gives an internally coherent birth-registration set for `Jose Miguel`.

Conflicts and limits:

- The staged draft, source packet, and chunk all identify the Pulgar/Arriagada row as the image/current-chunk-supported entry 172.
- The converted file appears to diverge beyond a spelling variation; it is a different row/person family group.
- No canonical Burgos/de la Cruz attachment is supported by this task.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Supported only by the disputed converted Markdown. |
| conflict_severity | 0.90 | Acceptance would replace the whole Pulgar/Arriagada identity set. |
| evidence_quality | 0.24 | Single derivative layer conflicts with staged image review and chunk. |
| conversion_confidence | 0.20 | Converted file is the artifact under dispute. |
| claim_probability | 0.16 | Possible only if QA overturns the chunk/source-packet reading. |
| relevance | 0.92 | Direct competing row. |
| canonical_readiness | 0.00 | No promotion supported. |

## Hypothesis 3: Jose del Carmen Pulgar Is The Father Candidate

Evidence supporting:

- The staged draft and source packet preserve `Jose del Carmen Pulgar` as the safe father reading.
- The chunk reads `Jose del Carmen Pulgar S.` with attributes Chilean, employed, resident at Calle de Colipi.
- Canonical `wiki/people/jose-del-carmen-pulgar.md` exists, but its visible evidence snapshot currently links to a separate Tulio Cesar Luis Jose draft relationship and does not prove the entry-172 father identity.

Conflicts and limits:

- The current converted Markdown names `Oswaldo Burgos` as father.
- The final `S.` or trailing mark is uncertified.
- Existing Jose del Carmen Pulgar mentions may represent one person or multiple same-name candidates; no merge is justified by this staged draft.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.56 | Name is locally supported in the Pulgar row; exact identity and suffix are held. |
| conflict_severity | 0.76 | Wrong father attachment would create a false parent-child link. |
| evidence_quality | 0.54 | Supported by chunk/source packet, limited by conversion conflict. |
| conversion_confidence | 0.34 | Blocked by row conflict and suffix uncertainty. |
| claim_probability | 0.60 | Probable if Pulgar row controls. |
| relevance | 0.96 | Direct parent candidate. |
| canonical_readiness | 0.08 | Hold pending QA and relationship proof review. |

## Hypothesis 4: Juana Arriagada de Pulgar Is The Mother Candidate

Evidence supporting:

- The staged draft, source packet, and chunk agree on mother `Juana Arriagada de Pulgar`.
- Canonical `wiki/people/juana-arriagada-de-pulgar.md` has a probable child link and mother attributes from the entry-172 cluster.

Conflicts and limits:

- The converted Markdown names `Concepcion de la Cruz` as mother.
- The canonical Juana page depends on this same conflicted source cluster and cannot resolve it.
- Do not merge or conflate this Juana candidate with any other Jose/Juana parent candidates without a separate reviewed bridge.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Mother name is consistent across the staged Pulgar row evidence. |
| conflict_severity | 0.78 | Wrong mother attachment would misstate parentage. |
| evidence_quality | 0.58 | Multiple local layers agree, but all remain held. |
| conversion_confidence | 0.35 | Row conflict blocks promotion. |
| claim_probability | 0.66 | Probable if Pulgar row controls. |
| relevance | 0.96 | Direct parent candidate. |
| canonical_readiness | 0.08 | Hold pending QA and relationship proof review. |

## Hypothesis 5: Entry 172 Bridges To Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Evidence supporting:

- The Pulgar and Arriagada surnames are relevant to Pulgar-line review.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` represents Dario Arturo Pulgar-Smith from family-supplied knowledge as Alexander John Heinz's maternal grandfather and warns against automatic merges with similar Pulgar clusters.
- Local staged CV analyses preserve `Dario Arturo Pulgar` as a document-level CV subject with an unresolved possible bridge to canonical `Dario Arturo Pulgar-Smith`.

Conflicts and limits:

- This staged birth-row conflict does not name Dario, Arturo, Smith, Alexander John Heinz, or any relationship tying entry 172 to Dario Arturo Pulgar-Smith.
- A Pulgar surname match is only a family-context hint for later review.
- The named child is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | No direct Dario/Arturo/Smith bridge. |
| conflict_severity | 0.72 | Unsupported lineage attachment could collapse separate Pulgar-line identities. |
| evidence_quality | 0.30 | Surname/context overlap only. |
| conversion_confidence | 0.32 | Entry itself is held. |
| claim_probability | 0.06 | Possible broader family context only. |
| relevance | 0.74 | Required anti-conflation comparison. |
| canonical_readiness | 0.00 | No attachment or merge supported. |

## Hypothesis 6: Entry 172 Bridges To Dario Jose Pulgar-Arriagada Or Dario/Dario Pulgar Arriagada

Evidence supporting:

- The Pulgar/Arriagada surname combination appears in the entry-172 child name.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` records `Darío Pulgar Arriagada` in a 2000-12-05 Chiguayante expropriation event.
- Other local identity notes preserve Dario Jose, Dario J., Dario/Darío Pulgar Arriagada, and Dario Pulgar A. clusters as unresolved or separate candidates.

Conflicts and limits:

- This staged draft names no Dario and gives no Dario-specific age, date, occupation, spouse, child, property, medical, passenger, Geneva, CV, or relationship context.
- `Jose del Carmen Segundo Pulgar Arriagada` must not be treated as a Dario candidate by surname alone.
- The 1888 child row and 2000 Darío Pulgar Arriagada expropriation evidence may be different generations or same-surname relatives; no bridge is present here.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | Shared surname elements only. |
| conflict_severity | 0.80 | Name-only merge could collapse distinct people/events/generations. |
| evidence_quality | 0.28 | Dario evidence comes from separate clusters, not this row. |
| conversion_confidence | 0.32 | Entry-172 conflict blocks bridge use. |
| claim_probability | 0.04 | No direct Dario bridge. |
| relevance | 0.82 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | No merge, rename, or relationship promotion supported. |

## Conflict Summary

- Same-person conflict: unresolved row subject. Pulgar/Arriagada is favored locally, but the converted Markdown asserts a different Burgos/de la Cruz row.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` is treated as `Jose Miguel`, a Dario Pulgar candidate, or a broader Pulgar-line canonical person by name proximity.
- Name-variant conflict: `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` are not name variants. `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is an unresolved father-field reading, not a certified variant.
- Relationship conflict: high. Father and mother candidates differ completely between the chunk/source-packet row and the converted Markdown row.
- Chronology conflict: material. Pulgar row birth is 1888-03-08 at 3 p.m.; converted Burgos row birth is 1888-04-06 at 10 p.m.
- Conversion conflict: severe row-level disagreement requiring targeted QA before proof-review promotion.

## Ranked Hypotheses

| rank | hypothesis | probability | next action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada` | 0.78 | Hold for targeted conversion QA, then rerun proof review. |
| 2 | `Juana Arriagada de Pulgar` is the mother if the Pulgar row controls | 0.66 | Certify row first, then proof-review the mother-child relationship. |
| 3 | `Jose del Carmen Pulgar` is the father if the Pulgar row controls | 0.60 | Certify row and father-field ending. |
| 4 | Entry 172 is the Burgos/de la Cruz row for `Jose Miguel` | 0.16 | Retain only as competing converted-file reading until QA. |
| 5 | Entry 172 bridges to Dario Arturo Pulgar-Smith / Dario Arturo Pulgar | 0.06 | No bridge; revisit only after conversion QA and separate Dario identity proof review. |
| 6 | Entry 172 bridges to Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada | 0.04 | No bridge; preserve separate hypotheses and anti-conflation watch. |

## Recommended Next Action

Keep the staged conflict draft and all dependent identity/relationship claims at `hold_for_conversion_qa`. Do not merge people, rename canonical pages, promote facts, or attach entry-172 evidence to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío Pulgar Arriagada, Jose del Carmen Pulgar, Juana Arriagada de Pulgar, or any Jose/Juana parent candidate.

Exact next proof-review step: targeted conversion QA must compare the original image, current converted Markdown, current chunk, and source packet for register page 58, entry 172; decide whether the Pulgar/Arriagada row or the Burgos/de la Cruz row is controlling; explain why the derivative files disagree; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review on the child identity, birth facts, father claim, mother claim, parent-child relationships, and any Pulgar-line Dario bridge question.
