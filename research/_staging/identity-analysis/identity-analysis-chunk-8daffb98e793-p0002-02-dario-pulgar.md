---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/identity/chunk-8daffb98e793-p0002-02-dario-pulgar-identity-candidate.md"
worker: postconv-identity-analysis-20260523054640100
staged_identity_draft: "research/_staging/identity/chunk-8daffb98e793-p0002-02-dario-pulgar-identity-candidate.md"
subject: "Dario Pulgar"
source_packet: "research/_staging/source-packets/chunk-8daffb98e793-p0002-02-osorio-anatomy-concepcion-pulgar.md"
source_path: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0002-chunk-02.md"
chunk_id: "CHUNK-8daffb98e793-P0002-02"
page_reference: "assigned source page range 2-2; chunk body reportedly includes Page Metadata: Page 4 and printed page 652"
analysis_status: hold_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
tags: [identity-analysis, conflict-review, pulgar]
---

# Identity And Conflict Analysis: Dario Pulgar

## Blockers First

- The exact staged draft analyzed here is `research/_staging/identity/chunk-8daffb98e793-p0002-02-dario-pulgar-identity-candidate.md`.
- The assigned draft and source packet identify a page-boundary conflict: the assignment says source page range 2-2, while the staged evidence says the chunk body contains Page Metadata for page 4 / printed page 652.
- The staged chunk path `raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0002-chunk-02.md` is not present in this checkout. The available sibling page-2 chunk is `page-0002-chunk-01.md`, and a separate page-4 staging for the same Osorio passage exists as `CHUNK-bdfcf4d3256f-P0004-01`.
- The controller requested page reread/conversion QA. Do not promote this draft or attach it to a canonical person until the correct rendered page and literal wording are confirmed.
- The literal evidence gives only `Darío Pulgar` in a list of surgeons. It gives no maternal surname, middle name, age, residence, birth, death, spouse, parent, child, signature, or direct family relationship.
- `San Juan de Dios Hospital` contains `Juan` and `Dios` as an institutional name only. It is not Jose/Juana parent evidence.
- No external research was performed. No raw sources, converted Markdown, chunks, staged source packets, claims, relationships, or canonical wiki pages were edited.

## Literal Source Reading

The staged draft quotes:

```text
accompanied by the surgeons Nicanor Durán, Darío Pulgar,
Enrique González Pastor and the dentist Víctor Villalobos
```

The staged source packet gives the fuller passage:

```text
These activities were carried out in a small room at the San Juan
de Dios Hospital, under the supervision of Dr. Gómez and
accompanied by the surgeons Nicanor Durán, Darío Pulgar,
Enrique González Pastor and the dentist Víctor Villalobos
(Solervicens, 1964).
```

Literal reading: a person named `Darío Pulgar` is described in a secondary journal article as one of several surgeons associated with practical anatomy activities at San Juan de Dios Hospital in Concepción.

Interpretation kept separate: this supports a narrow surgeon/activity identity candidate only. It does not identify him as `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or any Jose/Juana-linked family member.

## Hypothesis 1: Held Surgeon-List Identity Candidate

Hypothesis: the assigned draft should remain a held identity candidate for a source-mentioned surgeon named `Darío Pulgar`, with no canonical merge yet.

Supporting evidence:

- The staged identity draft, staged source packet, and staged claims for `CHUNK-8daffb98e793-P0002-02` consistently preserve the literal name `Darío Pulgar` and occupation/context `surgeon`.
- A separate local source packet for `CHUNK-bdfcf4d3256f-P0004-01` preserves the same Osorio passage with page 4 / printed page 652 metadata and the same literal support.
- The claim scope is narrow: named person plus surgeon/activity context.

Conflicts and limits:

- The assigned chunk/page metadata is not stable enough for promotion.
- The source is a secondary journal article citing Solervicens, not a vital or identity-bearing family source.
- No independent identity markers are present.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | The local staged derivatives agree on the name, but the chunk/page mismatch prevents stronger confidence. |
| conflict_severity | 0.28 | Low if held as a separate candidate; risk rises if merged by name alone. |
| evidence_quality | 0.52 | Direct name in article text, but secondary and non-genealogical. |
| conversion_confidence | 0.42 | Medium converted text but unresolved page-boundary/chunk-path problem. |
| claim_probability | 0.62 | Probable that the article names a surgeon `Darío Pulgar`, pending page reread. |
| relevance | 1.00 | Directly answers the assigned staged draft. |
| canonical_readiness | 0.08 | Not ready until conversion QA and identity review are complete. |

## Hypothesis 2: Same As The Earlier Page-4 Osorio Staging

Hypothesis: `CHUNK-8daffb98e793-P0002-02` and `CHUNK-bdfcf4d3256f-P0004-01` are duplicate/overlapping staging of the same Osorio article passage.

Supporting evidence:

- Both source packets cite the same source PDF, same converted file family, same article, and same literal passage naming `Darío Pulgar`.
- The `bdfcf4d3256f` packet has the cleaner page reference: source page 4, printed page 652.
- The assigned `8daffb98e793` packet itself says its body includes Page Metadata for page 4 / printed page 652 despite assignment page range 2-2.

Conflicts and limits:

- This is a staging/page-boundary issue, not proof of a person merge.
- The missing assigned chunk file prevents direct comparison of the exact `page-0002-chunk-02.md` body in this checkout.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | The same literal passage and source context strongly suggest duplicate staging of one mention. |
| conflict_severity | 0.44 | Moderate metadata conflict; person-level conflict remains low if not promoted. |
| evidence_quality | 0.58 | Useful local cross-check, but not independent evidence. |
| conversion_confidence | 0.46 | Page-4 staging is cleaner, but controller reread still applies. |
| claim_probability | 0.70 | Likely duplicate/overlap of the same article mention. |
| relevance | 0.92 | Important for avoiding duplicate claims. |
| canonical_readiness | 0.10 | Needs conversion/page QA before any deduplication or promotion. |

## Hypothesis 3: Same Person As Dario Arturo Pulgar-Smith / Dario Arturo Pulgar

Hypothesis: the Osorio `Darío Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith` or staged CV subject `Dario Arturo Pulgar`.

Supporting evidence:

- All forms share `Dario/Darío Pulgar`.
- The canonical page `wiki/people/dario-arturo-pulgar-smith.md` is the family-supplied home for Alexander John Heinz's maternal grandfather and explicitly warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records need identity review before attachment.
- Existing CV analyses preserve a `Dario Arturo Pulgar` cluster, held pending proof review for the bridge to `Dario Arturo Pulgar-Smith`.

Conflicts and limits:

- The Osorio passage says only `Darío Pulgar`; it does not say `Arturo`, `Pulgar-Smith`, `Smith`, a family relationship, or any CV/Habitat context.
- The Osorio context is medical/anatomy and appears historically tied to early Concepción medical teaching. The CV/Pulgar-Smith context is a separate later family/CV cluster in current local staging.
- Family context is enough to justify a future double-check, not a silent correction from `Darío Pulgar` to `Dario Arturo Pulgar-Smith`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Shared name element only; no bridge to Arturo or Pulgar-Smith. |
| conflict_severity | 0.72 | High duplicate-person risk if this medical/anatomy mention is attached to the family-supplied grandfather by name alone. |
| evidence_quality | 0.40 | Compared Pulgar-Smith/CV context is real but unrelated to this passage. |
| conversion_confidence | 0.46 | The Osorio page is held; CV identity bridges have their own holds. |
| claim_probability | 0.10 | Possible only as a broad name lead. |
| relevance | 0.86 | Required Pulgar-line comparison. |
| canonical_readiness | 0.02 | Do not attach to `Dario Arturo Pulgar-Smith` or the CV subject. |

## Hypothesis 4: Same Person As Dario Jose Pulgar-Arriagada / Dario or Darío Pulgar Arriagada

Hypothesis: the Osorio `Darío Pulgar` is the same person as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`.

Supporting evidence:

- The names share `Dario/Darío Pulgar`.
- Other local Pulgar-Arriagada materials include medical or public contexts: the 1928 `Dario Pulgar A.` passenger candidate is listed as `Medical Surgeon`; the ICRC/Geneva materials use `Dario Jose Pulgar-Arriagada` in source-title context; the canonical `Darío Pulgar Arriagada` stub carries a 2000 expropriation event.

Conflicts and limits:

- The Osorio passage does not include `Jose`, `J.`, `Arriagada`, `A.`, or any property/passenger/ICRC identity marker.
- Existing analyses warn that some Pulgar-Arriagada candidates are held for conversion QA, metadata/title-only identity, or chronology conflicts.
- If the Osorio historical teaching context is early twentieth century, it may fit an older medical candidate better than the later CV/Pulgar-Smith cluster, but that is only contextual interpretation and not a proof bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.26 | Medical/professional context makes an older Pulgar-Arriagada lead plausible, but the name is incomplete. |
| conflict_severity | 0.62 | Moderate-high risk across multiple Dario Pulgar Arriagada variants and chronology-sensitive clusters. |
| evidence_quality | 0.42 | Compared materials are staged and several are metadata-dependent or held. |
| conversion_confidence | 0.44 | This Osorio chunk and several compared clusters need QA. |
| claim_probability | 0.22 | Plausible lead, not proved. |
| relevance | 0.88 | Required by Pulgar-line conflict review. |
| canonical_readiness | 0.04 | No merge or canonical attachment supported. |

## Hypothesis 5: Same As Dario Pulgar A. Passenger Candidate

Hypothesis: the Osorio `Darío Pulgar` is the same person as the 1928 passenger-list `Dario Pulgar A.`, age 39, occupation `Medical Surgeon`.

Supporting evidence:

- The 1928 row gives a medical occupation, and the Osorio article describes `Darío Pulgar` among surgeons.
- The name overlap is close, except for the passenger-list `A.` initial.
- Existing identity analysis treats the 1928 passenger as a held older medical candidate and says `A.` may be an unexpanded maternal surname such as `Arriagada`.

Conflicts and limits:

- The Osorio passage has no age, travel, address, nationality, or full second surname.
- The 1928 passenger source image was unavailable for reread in its own staged review, and row-column alignment remains held.
- The two sources do not directly cite each other or share a unique identifier.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.36 | Name plus surgeon/medical context is suggestive, but not identity proof. |
| conflict_severity | 0.52 | Moderate risk if `A.` is expanded or merged without image QA and a bridge. |
| evidence_quality | 0.48 | Two relevant but held local source clusters. |
| conversion_confidence | 0.40 | Both the Osorio assigned chunk and 1928 passenger row have conversion/source-image issues. |
| claim_probability | 0.32 | Plausible older medical-person hypothesis only. |
| relevance | 0.76 | Useful anti-conflation comparison. |
| canonical_readiness | 0.03 | Not ready for merge or promotion. |

## Hypothesis 6: Relationship To Jose/Juana Parent Candidates

Hypothesis: the Osorio `Darío Pulgar` is directly connected to Jose/Juana parent candidates, including `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar`.

Supporting evidence:

- Existing local wiki/staged context includes Pulgar/Arriagada Jose/Juana parent candidates.
- `San Juan de Dios Hospital` includes words that could be confused with personal names if read out of context, but the source packet correctly identifies them as institutional wording.

Conflicts and limits:

- The Osorio passage states no parent, mother, father, spouse, child, household, birth registration, or family relationship.
- `Juan` and `Dios` here are not `Jose` or `Juana` parent evidence.
- Jose/Juana clusters have their own conversion conflicts and cannot bridge this Dario identity without an independent relationship-bearing source.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No same-person or relationship evidence appears in this passage. |
| conflict_severity | 0.48 | Main risk is false relationship promotion from institutional wording or surname overlap. |
| evidence_quality | 0.28 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.38 | Mixed and held across the compared register clusters. |
| claim_probability | 0.02 | No Jose/Juana relationship claim is supported here. |
| relevance | 0.58 | Required Pulgar-line checklist item. |
| canonical_readiness | 0.01 | No relationship or lineage action supported. |

## Conflict Summary

- Same-person conflict: unresolved. The assigned draft supports only a held `Darío Pulgar` surgeon candidate.
- Duplicate-person risk: high if this mention is merged into `Dario Arturo Pulgar-Smith`, staged CV `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or `Dario Pulgar A.` by name alone.
- Name-variant conflict: the literal reading is `Darío Pulgar` only. The passage does not prove `Arturo`, `Jose`, `Arriagada`, `A.`, or `Pulgar-Smith`.
- Relationship-conflict evidence: none. The passage does not support Jose/Juana parentage, spouse, child, sibling, or grandparent claims.
- Chronology-conflict evidence: none directly from the passage because it lacks age and event date for Dario; chronology remains a comparison blocker against other Dario Pulgar clusters.
- Conversion/page conflict: material. The assigned page 2 / chunk 02 reference conflicts with page 4 / printed page 652 staging, and the exact assigned chunk file is absent in this checkout.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Held surgeon-list identity candidate named `Darío Pulgar` | 0.62 | Keep staged; await conversion/page QA. |
| 2 | Duplicate/overlap with the cleaner page-4 Osorio staging | 0.70 | Reconcile through conversion QA before deduplicating or promoting claims. |
| 3 | Same as 1928 `Dario Pulgar A.` medical passenger | 0.32 | Preserve as possible older medical lead; require image reread and identity bridge. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` / `Dario/Darío Pulgar Arriagada` | 0.22 | Hold; no merge by name alone. |
| 5 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.10 | Do not attach; requires independent identity-bearing bridge. |
| 6 | Direct Jose/Juana parent-candidate connection | 0.02 | No lineage or relationship action from this source. |

## Recommended Next Action

Keep `research/_staging/identity/chunk-8daffb98e793-p0002-02-dario-pulgar-identity-candidate.md` on hold for conversion/page QA. The exact next proof-review step is to reconcile `CHUNK-8daffb98e793-P0002-02` against the rendered source page and the cleaner `CHUNK-bdfcf4d3256f-P0004-01` staging: confirm whether the assigned evidence truly belongs to source page 4 / printed page 652, verify the literal name `Darío Pulgar` in the surgeon list, and resolve the missing `page-0002-chunk-02.md` path or manifest mismatch.

After that, promote at most a narrow staged claim that `Darío Pulgar` was described as a surgeon associated with practical anatomy activities at San Juan de Dios Hospital. Do not merge with or attach to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, `Dario Pulgar A.`, or any Jose/Juana parent candidate unless a separate identity-bearing source supplies age/vital dates, full name, occupation continuity, family relationship, or another explicit bridge.
