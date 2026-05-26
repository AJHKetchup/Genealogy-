---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526135632244
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
- This is a row-level derivative conflict. The source packet and current chunk support a Pulgar/Arriagada entry 172, while the current converted Markdown describes a Burgos/de la Cruz entry 172.
- The staged source packet reports image review supporting the Pulgar/Arriagada row, but the assigned converted Markdown still contains the incompatible Burgos/de la Cruz row.
- The father field is not fully certified. The safe reading in the staged draft is `Jose del Carmen Pulgar`, with the final `S.` or other trailing mark unresolved until targeted conversion QA.
- No identity, parent-child relationship, duplicate-person merge, name variant, or Dario-line bridge should be promoted until the original image, current converted Markdown, current chunk, and source packet are reconciled.
- Existing canonical pages already contain low- or held-confidence Pulgar/Juana/Jose evidence generated from earlier entry-172 staging; those pages must not be treated as independent proof that the current conflicted conversion is resolved.
- No external research was performed. No raw sources, converted Markdown, chunks, reviewed notes, source packets, or canonical wiki pages were edited.

## Literal Source Readings

Current chunk and source-packet-supported reading:

```text
Entry 172 records Jose del Carmen Segundo Pulgar Arriagada, male, born 8 March 1888 at 3 p.m. at Calle de Valdivia; father Jose del Carmen Pulgar S. in the chunk but only Jose del Carmen Pulgar safely certified by the staged source packet; mother Juana Arriagada de Pulgar; informant Ernesto Herrera L.
```

Current converted Markdown reading:

```text
Entry 172 records Jose Miguel, male, born 6 April 1888 at 10 p.m. in En esta; father Oswaldo Burgos; mother Concepcion de la Cruz; informant Oswaldo Burgos.
```

Interpretation kept separate: the stronger local evidence for this staged packet favors the Pulgar/Arriagada row as the intended entry 172, but identity conclusions remain blocked because the converted file and chunk disagree at the row level.

## Hypothesis 1: Entry 172 Is Jose del Carmen Segundo Pulgar Arriagada

Hypothesis: the controlling row for register page 58, entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`.

Evidence supporting:

- The staged conflict draft states that the image/current-chunk-supported reading records `Jose del Carmen Segundo Pulgar Arriagada`.
- The source packet says image review supports the Pulgar/Arriagada row as register entry 172.
- The current chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`.
- Existing canonical `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` reflects this same child-name cluster and a birth date of 1888-03-08 15:00, but its evidence snapshot depends on this entry-172 source cluster and does not resolve the current conversion conflict by itself.

Conflicts and limits:

- The assigned converted Markdown currently records a different child, parents, birth date, place wording, and informant.
- The father field ending is unresolved in the staged draft. Do not silently normalize `Jose del Carmen Pulgar S.` to a specific full name or surname variant.
- Canonical evidence should remain held because the conversion artifact conflict is material.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Image-reviewed staged packet and chunk align on the Pulgar/Arriagada child, but the converted file conflicts. |
| conflict_severity | 0.90 | The competing reading changes the child, parents, birth details, and informant. |
| evidence_quality | 0.66 | Chunk plus image-reviewed source packet are strong local evidence, but derivative disagreement remains unresolved. |
| conversion_confidence | 0.35 | Low until targeted conversion QA reconciles the row-level mismatch. |
| claim_probability | 0.78 | Probable controlling row, not promotable yet. |
| relevance | 1.00 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.10 | Hold for conversion QA and proof review before promotion. |

## Hypothesis 2: Entry 172 Is Jose Miguel, Child Of Oswaldo Burgos And Concepcion de la Cruz

Hypothesis: the current converted Markdown's Burgos/de la Cruz transcription is the controlling entry 172.

Evidence supporting:

- The current converted Markdown explicitly labels its Burgos/de la Cruz row as entry 172.
- That derivative reading gives a coherent birth-registration set: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, informant `Oswaldo Burgos`.

Conflicts and limits:

- The staged conflict draft and source packet state that the image/current chunk support the Pulgar/Arriagada row instead.
- The surrounding entries in the converted Markdown also diverge from the chunk's page-58 and page-59 entries, suggesting a broader row/page-source mismatch rather than a simple spelling error.
- No canonical Burgos/de la Cruz person page was identified in the targeted local wiki search for this task.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Supported only by the conflicted converted Markdown for this assignment. |
| conflict_severity | 0.90 | If accepted, it would replace the entire Pulgar/Arriagada identity and relationship set. |
| evidence_quality | 0.24 | Single derivative transcript conflicts with image-reviewed staging and chunk. |
| conversion_confidence | 0.20 | Converted file is the artifact under dispute. |
| claim_probability | 0.16 | Possible only if QA determines the chunk/source-packet alignment is wrong. |
| relevance | 0.92 | This is the direct competing row. |
| canonical_readiness | 0.00 | No promotion supported. |

## Hypothesis 3: Jose del Carmen Pulgar Is The Father Candidate For Entry 172

Hypothesis: if the Pulgar/Arriagada row controls, the father is `Jose del Carmen Pulgar`, possibly with a trailing `S.` or unresolved mark.

Evidence supporting:

- The staged conflict draft and source packet both preserve a safe father reading of `Jose del Carmen Pulgar`.
- The current chunk reads `Jose del Carmen Pulgar S.` and adds father attributes: Chilean, employed, resident at Calle de Colipi.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` represents a Jose del Carmen Pulgar stub, but its visible evidence snapshot currently links him to a separate Tulio Cesar Luis Jose draft relationship, not a promoted entry-172 father link.

Conflicts and limits:

- The staged source packet explicitly declines to certify the final `S.` or trailing mark.
- The current converted Markdown's competing row names `Oswaldo Burgos` as father, not Jose del Carmen Pulgar.
- Existing wiki context for Jose del Carmen Pulgar is not enough to infer this is the same Jose across all Pulgar-line records.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.56 | Good evidence for the name in the Pulgar row, weaker evidence for exact identity or suffix. |
| conflict_severity | 0.76 | Wrong father attachment would create an incorrect parent-child relationship. |
| evidence_quality | 0.54 | Name is locally supported, but exact father-field reading and identity bridge are held. |
| conversion_confidence | 0.34 | Blocked by row-level conflict and unresolved suffix. |
| claim_probability | 0.60 | Probable father candidate if Pulgar row controls. |
| relevance | 0.96 | Direct parent candidate in the staged draft. |
| canonical_readiness | 0.08 | Hold pending conversion QA and relationship proof review. |

## Hypothesis 4: Juana Arriagada de Pulgar Is The Mother Candidate For Entry 172

Hypothesis: if the Pulgar/Arriagada row controls, the mother is `Juana Arriagada de Pulgar`.

Evidence supporting:

- The staged draft, source packet, and current chunk agree on mother `Juana Arriagada de Pulgar`.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` includes a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` and mother attributes from the entry-172 source cluster.

Conflicts and limits:

- The current converted Markdown's competing row names `Concepcion de la Cruz` as mother.
- The canonical Juana page's evidence snapshot depends on the same conflicted entry-172 source cluster and should not be used to bypass QA.
- Separate canonical `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a different Juana-name candidate tied to Tulio Cesar Luis Jose draft evidence; this staged draft does not bridge her to `Juana Arriagada de Pulgar`.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Mother name is consistent across source packet and chunk, but conversion conflict remains. |
| conflict_severity | 0.78 | Wrong mother attachment would misstate a parent-child relationship and possibly merge Juana candidates. |
| evidence_quality | 0.58 | Multiple local layers agree, but canonical evidence is derivative of the same held source. |
| conversion_confidence | 0.35 | Hold until row conflict is resolved. |
| claim_probability | 0.66 | Probable mother candidate if Pulgar row controls. |
| relevance | 0.96 | Direct parent candidate in the staged draft. |
| canonical_readiness | 0.08 | Hold pending conversion QA and relationship proof review. |

## Hypothesis 5: Entry 172 Connects To Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Hypothesis: the Pulgar/Arriagada entry-172 cluster is genealogically connected to canonical `Dario Arturo Pulgar-Smith` or staged/CV `Dario Arturo Pulgar`.

Evidence supporting:

- The entry-172 Pulgar row uses the Pulgar and Arriagada surname context relevant to broader Pulgar-line work.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` represents Dario Arturo Pulgar-Smith from family-supplied knowledge as Alexander John Heinz's maternal grandfather and warns against automatic merges with similarly named Pulgar clusters.
- Existing staged CV analyses treat `Dario Arturo Pulgar` as a held document-level CV subject and preserve an unresolved possible bridge to canonical `Dario Arturo Pulgar-Smith`.

Conflicts and limits:

- This staged draft does not name Dario, Arturo, Smith, a spouse, child, grandchild, or any relationship connecting entry 172 to Dario Arturo Pulgar-Smith.
- A Pulgar surname match and family-context relevance justify later checking, not a lineage attachment.
- The child in this row is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | No direct Dario/Arturo/Smith bridge in this staged draft. |
| conflict_severity | 0.72 | Unsupported lineage attachment could collapse separate Pulgar-line generations. |
| evidence_quality | 0.30 | Only surname/family-context overlap. |
| conversion_confidence | 0.32 | Entry itself is held for conversion QA. |
| claim_probability | 0.06 | Possible broader family context only. |
| relevance | 0.74 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | No attachment or merge supported. |

## Hypothesis 6: Entry 172 Connects To Dario Jose Pulgar-Arriagada Or Dario/Dario Pulgar Arriagada

Hypothesis: `Jose del Carmen Segundo Pulgar Arriagada` or the Jose/Juana parent candidates in entry 172 identify, explain, or bridge `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, or canonical `Darío Pulgar Arriagada`.

Evidence supporting:

- The entry-172 child and mother use the Pulgar/Arriagada surname combination.
- Existing local identity analysis for `Dario Jose Pulgar-Arriagada` preserves a separate 1929 Geneva/photo-title cluster and explicitly compares it to Dario Arturo/Pulgar-Smith and Jose/Juana candidates.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` records `Darío Pulgar Arriagada` in a 2000 Chiguayante expropriation event.

Conflicts and limits:

- This staged draft names no Dario and gives no age, birth date, spouse, child, residence, property, Geneva, ICRC, medical, or CV context for any Dario candidate.
- `Jose del Carmen Segundo Pulgar Arriagada` cannot be treated as a Dario candidate by surname alone.
- A 1888 birth row, 1929 Dario Jose photo-title cluster, and 2000 Darío Pulgar Arriagada expropriation stub may involve different generations or same-surname relatives; no bridge is present here.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | Shared Pulgar/Arriagada surname elements only. |
| conflict_severity | 0.80 | Name-only merge could collapse distinct people, events, and generations. |
| evidence_quality | 0.28 | Compared Dario evidence is from separate clusters and not in this birth row. |
| conversion_confidence | 0.32 | Entry-172 conversion conflict blocks use as bridge evidence. |
| claim_probability | 0.04 | No direct Dario bridge. |
| relevance | 0.82 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | No merge, rename, or relationship promotion supported. |

## Conflict Summary

- Same-person conflict: unresolved only at the level of the row subject. The evidence favors Pulgar/Arriagada as the intended row, but the current converted Markdown asserts a different Burgos/de la Cruz row.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` is treated as the same person as `Jose Miguel`, any Dario Pulgar candidate, or any canonical Pulgar-line person by name proximity.
- Name-variant conflict: `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` are not spelling variants. `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is an unresolved father-field reading, not a certified name variant.
- Relationship conflict: high. Father and mother candidates differ completely between the chunk/source-packet row and the converted Markdown row.
- Chronology conflict: material. Pulgar row birth is 1888-03-08 at 3 p.m.; converted Burgos row birth is 1888-04-06 at 10 p.m.
- Conversion conflict: severe. The derivative artifacts disagree at the row level and must be reconciled before canonical use.

## Ranked Hypotheses

| rank | hypothesis | probability | next action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada` | 0.78 | Hold for targeted conversion QA; then rerun proof review. |
| 2 | `Juana Arriagada de Pulgar` is the mother if the Pulgar row controls | 0.66 | Certify row first; then proof-review the mother-child relationship. |
| 3 | `Jose del Carmen Pulgar` is the father if the Pulgar row controls | 0.60 | Certify row and father-field ending as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. |
| 4 | Entry 172 is the Burgos/de la Cruz row for `Jose Miguel` | 0.16 | Retain only as competing converted-file reading until QA. |
| 5 | Entry 172 bridges to Dario Arturo Pulgar-Smith / Dario Arturo Pulgar | 0.06 | No bridge; revisit only after conversion QA and separate Dario identity proof review. |
| 6 | Entry 172 bridges to Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada | 0.04 | No bridge; preserve separate hypotheses and anti-conflation watch. |

## Recommended Next Action

Keep the staged conflict draft and all dependent identity/relationship claims at `hold_for_conversion_qa`. Do not merge people, rename canonical pages, promote facts, or attach entry-172 evidence to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío Pulgar Arriagada, Jose del Carmen Pulgar, or either Juana candidate.

Exact next proof-review step: targeted conversion QA must compare the original image, current converted Markdown, current chunk, and source packet for register page 58, entry 172; decide whether the Pulgar/Arriagada row or the Burgos/de la Cruz row is controlling; explain why the derivative files disagree; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review on the child identity, birth facts, father claim, mother claim, parent-child relationships, and any Pulgar-line Dario bridge question.
