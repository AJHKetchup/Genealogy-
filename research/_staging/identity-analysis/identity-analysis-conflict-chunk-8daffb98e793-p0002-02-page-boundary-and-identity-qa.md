---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-8daffb98e793-p0002-02-page-boundary-and-identity-qa.md"
worker: postconv-identity-analysis-20260523080009303
staged_conflict_draft: "research/_staging/conflicts/chunk-8daffb98e793-p0002-02-page-boundary-and-identity-qa.md"
subject: "Darío Pulgar"
source_packet: "research/_staging/source-packets/chunk-8daffb98e793-p0002-02-osorio-anatomy-concepcion-pulgar.md"
source_path: "raw/sources/Osorio, H., Toro, J.C., Schorwer, K., Riveros, A., & Cardenas, J. Pioneers of a Century of Anatomical Teaching in the City of Concepción, Chile, International Journal of Morpholog.pdf"
converted_file: "raw/converted/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-cardenas-j-pioneers-of-a-century-of-anatomical-teaching-in-the-city-of-concepci-n-chile-international-journal-of-morpholog-pages-1-10.codex.md"
chunk: "raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0002-chunk-02.md"
chunk_id: "CHUNK-8daffb98e793-P0002-02"
analysis_status: hold_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
tags: [identity-analysis, conflict-review, pulgar, page-boundary-qa]
---

# Identity And Conflict Analysis: Page Boundary And Pulgar Identity QA

## Blockers First

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-8daffb98e793-p0002-02-page-boundary-and-identity-qa.md`.
- The staged draft and source packet report a page-boundary conflict: the manifest assigns the chunk to source page range 2-2, but the chunk body is described as containing `Page Metadata Page 4` and printed page `652`.
- The referenced chunk path `raw/chunks/ca3a734085-osorio-h-toro-j-c-schorw-p0001-0010-osorio-h-toro-j-c-schorwer-k-riveros-a-1cbe9f3841/page-0002-chunk-02.md` is absent in this checkout. The available same-folder chunks include `page-0002-chunk-01.md` and `page-0004-chunk-01.md`.
- The available `page-0004-chunk-01.md` contains the quoted passage and gives page metadata `Page 4` with printed page `652`, matching the conflict concern.
- The source is a secondary journal article, not a vital, civil, or relationship-bearing record.
- The literal evidence gives only `Darío Pulgar` in a list of surgeons. It gives no `Arturo`, `Jose`, `Arriagada`, `Smith`, parent, spouse, child, age, residence, birth, death, signature, or direct family relationship.
- `San Juan de Dios Hospital` is institutional wording. It is not Jose/Juana parent evidence.
- No external research was performed. No raw source, converted Markdown, chunk, staged source packet, relationship, claim, or canonical wiki page was edited.

## Literal Source Reading

The staged conflict draft quotes:

```text
accompanied by the surgeons Nicanor Durán, Darío Pulgar, Enrique González Pastor and the dentist Víctor Villalobos
```

The staged source packet gives the fuller local reading:

```text
These activities were carried out in a small room at the San Juan
de Dios Hospital, under the supervision of Dr. Gómez and
accompanied by the surgeons Nicanor Durán, Darío Pulgar,
Enrique González Pastor and the dentist Víctor Villalobos
(Solervicens, 1964).
```

Literal reading: the article names `Darío Pulgar` as one of several surgeons accompanying practical anatomy activities at San Juan de Dios Hospital.

Interpretation kept separate: this supports only a narrow source-mentioned surgeon candidate. It does not prove that this person is `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, `Dario Pulgar A.`, or a child/relative of any Jose/Juana parent candidate.

## Hypothesis 1: Held Surgeon-List Candidate

Hypothesis: the staged conflict draft should remain a held identity candidate for a source-mentioned surgeon named `Darío Pulgar`, with no canonical attachment yet.

Evidence supporting:

- The staged conflict draft and source packet agree on the literal name `Darío Pulgar`.
- The available page-4 chunk contains the same passage and locates it on page metadata `Page 4`, printed page `652`.
- The claim scope is narrow: a named person in a surgeon list connected to practical anatomy activities at San Juan de Dios Hospital.

Conflicts and limits:

- The assigned page/chunk metadata is not promotion-ready.
- The referenced `page-0002-chunk-02.md` path is missing in this checkout, so the exact assigned chunk body cannot be directly reread from that path.
- The passage provides no unique identity marker beyond name and occupational context.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | The local staged and page-4 readings agree on the name, but the page/chunk mismatch caps confidence. |
| conflict_severity | 0.32 | Low if held separately; higher if merged by name alone. |
| evidence_quality | 0.52 | Direct article text, but secondary and not identity-rich. |
| conversion_confidence | 0.42 | The page-4 chunk supports the passage, but the assigned page-2/chunk-02 reference is unresolved. |
| claim_probability | 0.62 | Probable that the article names a surgeon `Darío Pulgar`, pending page-boundary QA. |
| relevance | 1.00 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.08 | Hold until conversion/page QA and proof review are complete. |

## Hypothesis 2: Duplicate Or Overlap With Page-4 Osorio Staging

Hypothesis: `CHUNK-8daffb98e793-P0002-02` is duplicate or overlapping staging of the same Osorio article passage now visible in the available page-4 chunk.

Evidence supporting:

- The conflict draft says the assigned page-2 chunk body includes page-4 metadata and printed page `652`.
- The available page-4 chunk contains the literal passage naming `Darío Pulgar`.
- The source packet warns that all claims from this chunk should be held for conversion/page-boundary QA.

Conflicts and limits:

- This is a staging and citation problem, not a person-identity proof.
- The missing assigned chunk path prevents direct file-to-file comparison.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Same passage and same page-4/652 signal make overlap likely. |
| conflict_severity | 0.46 | Moderate citation and duplicate-claim risk. |
| evidence_quality | 0.58 | Strong local cross-check, but not independent evidence. |
| conversion_confidence | 0.46 | The page-4 chunk is coherent; the assigned staged reference is not. |
| claim_probability | 0.70 | Likely the same passage was staged under conflicting page/chunk metadata. |
| relevance | 0.94 | Central to the page-boundary QA issue. |
| canonical_readiness | 0.10 | Needs reconciliation before any claim promotion or deduplication. |

## Hypothesis 3: Same Person As Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Hypothesis: the Osorio `Darío Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith` or staged CV subject `Dario Arturo Pulgar`.

Evidence supporting:

- The names share the `Dario/Darío Pulgar` elements.
- The canonical `wiki/people/dario-arturo-pulgar-smith.md` page is the family-supplied home person context for Alexander John Heinz's maternal grandfather.
- That canonical page explicitly warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review.

Conflicts and limits:

- The Osorio passage does not state `Arturo`, `Smith`, `Pulgar-Smith`, a family relationship, birth data, death data, or any CV/Habitat context.
- Existing local CV analyses treat `Dario Arturo Pulgar` as a staged document-level subject and still require a bridge to `Dario Arturo Pulgar-Smith`.
- Name overlap alone is insufficient, especially because the Osorio context is medical/anatomy and the family/CV cluster is a different evidentiary context.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Shared name elements only; no bridge to Arturo or Pulgar-Smith. |
| conflict_severity | 0.72 | High risk if the surgeon-list mention is attached to the family-supplied grandfather by name alone. |
| evidence_quality | 0.40 | The compared canonical page is valid context, but it does not identify this Osorio person. |
| conversion_confidence | 0.46 | Both this chunk and some compared CV identity bridges are held. |
| claim_probability | 0.10 | Possible as a search lead only. |
| relevance | 0.86 | Required Pulgar-line comparison. |
| canonical_readiness | 0.02 | Do not attach or merge. |

## Hypothesis 4: Same Person As Dario Jose Pulgar-Arriagada Or Dario/Darío Pulgar Arriagada

Hypothesis: the Osorio `Darío Pulgar` is the same person as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`.

Evidence supporting:

- The names share `Dario/Darío Pulgar`.
- The canonical `wiki/people/dar-o-pulgar-arriagada.md` page records a `Darío Pulgar Arriagada` stub with a 2000 expropriation event.
- Other staged Pulgar-line work has treated `Dario Jose Pulgar-Arriagada` and `Dario/Darío Pulgar Arriagada` as comparison candidates that must not be merged by name alone.

Conflicts and limits:

- The Osorio passage does not include `Jose`, `Arriagada`, `Pulgar-Arriagada`, property context, ICRC/Geneva context, or family context.
- The canonical `Darío Pulgar Arriagada` evidence snapshot is for a 2000 legal/property event, not an early Concepción anatomy-teaching passage.
- The evidence is insufficient to resolve whether the Osorio surgeon is an older Arriagada-line medical person, a different same-name person, or merely an unrelated article mention.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.20 | Name overlap exists, but no Arriagada/Jose bridge appears in the passage. |
| conflict_severity | 0.62 | Moderate-high duplicate risk across multiple Pulgar-Arriagada variants. |
| evidence_quality | 0.38 | Compared materials are local but do not intersect this source directly. |
| conversion_confidence | 0.44 | This chunk is held; some compared Arriagada materials are also staged/limited. |
| claim_probability | 0.18 | Plausible lead only, not proof. |
| relevance | 0.88 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | No canonical merge or attachment supported. |

## Hypothesis 5: Same Person As Dario Pulgar A., Medical Surgeon Passenger

Hypothesis: the Osorio `Darío Pulgar` is the same person as the 1928 passenger-list candidate `Dario Pulgar A.`, age 39, occupation `Medical Surgeon`.

Evidence supporting:

- The passenger-list row in converted local material names `Dario Pulgar A.` and gives occupation `Medical Surgeon`.
- The Osorio passage calls `Darío Pulgar` one of the surgeons.
- This is the strongest contextual same-person lead among the non-family Pulgar candidates because both sources have a medical/surgeon occupational signal.

Conflicts and limits:

- The Osorio passage lacks the `A.` initial, age, travel context, address, nationality, or full surname.
- Existing staged review for the passenger-list material holds the candidate pending image/source QA and column-alignment review.
- Occupation plus name is suggestive but not a unique identity bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.34 | Name plus medical context is meaningful but incomplete. |
| conflict_severity | 0.54 | Moderate risk if `A.` is expanded or merged without proof. |
| evidence_quality | 0.48 | Two relevant local clusters, both with QA limitations. |
| conversion_confidence | 0.40 | The Osorio assigned chunk and passenger row both need QA before promotion. |
| claim_probability | 0.32 | Plausible older medical-person hypothesis only. |
| relevance | 0.76 | Useful comparison to prevent conflation. |
| canonical_readiness | 0.03 | No merge or promotion supported. |

## Hypothesis 6: Direct Relationship To Jose/Juana Parent Candidates

Hypothesis: the Osorio `Darío Pulgar` has a direct relationship to Jose/Juana parent candidates, including `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar`.

Evidence supporting:

- Existing wiki context includes Pulgar/Arriagada Jose/Juana candidates and staged parent-child links.
- The staged source packet correctly notes that `Juan` and `Dios` appear in `San Juan de Dios Hospital`.

Conflicts and limits:

- The Osorio passage states no parent, mother, father, spouse, child, sibling, birth registration, household, or other family relationship.
- `San Juan de Dios Hospital` is not a person-name or parent clue.
- The Jose/Juana candidate materials have their own conversion and identity conflicts and cannot bridge this Osorio mention without a separate relationship-bearing source.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | No relationship or same-person evidence appears in this passage. |
| conflict_severity | 0.48 | Main risk is false lineage inference from institutional wording or surname overlap. |
| evidence_quality | 0.28 | Parent-candidate evidence is separate from this source. |
| conversion_confidence | 0.38 | Mixed and held across compared register clusters. |
| claim_probability | 0.02 | No Jose/Juana relationship claim is supported. |
| relevance | 0.58 | Required Pulgar-line checklist item. |
| canonical_readiness | 0.01 | No lineage or relationship action supported. |

## Conflict Summary

- Same-person conflict: unresolved. The draft supports only a held `Darío Pulgar` surgeon-list candidate.
- Duplicate-person risk: high if merged with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or `Dario Pulgar A.` by name alone.
- Name-variant conflict: the literal reading is `Darío Pulgar` only. The source does not prove `Arturo`, `Jose`, `Arriagada`, `A.`, `Smith`, or `Pulgar-Smith`.
- Relationship-conflict evidence: none. The passage does not support Jose/Juana parentage, spouse, child, sibling, or grandparent claims.
- Chronology-conflict evidence: unresolved. The passage sits in an article narrative about early Concepción anatomy teaching, but gives no birth, age, or vital data for `Darío Pulgar`.
- Conversion/page conflict: material. The assigned page-2/chunk-02 reference conflicts with page-4/printed-page-652 evidence, and the exact assigned chunk path is absent.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Held source-mentioned surgeon named `Darío Pulgar` | 0.62 | Conversion/page QA must confirm the correct source page and literal wording. |
| 2 | Duplicate/overlap with available page-4 Osorio staging | 0.70 | Reconcile `CHUNK-8daffb98e793-P0002-02` against the page-4 chunk and manifest before claim deduplication. |
| 3 | Same as 1928 `Dario Pulgar A.` medical-surgeon passenger | 0.32 | Reread passenger source image/columns and find an independent full-name or chronology bridge. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` / `Dario/Darío Pulgar Arriagada` | 0.18 | Preserve separately unless a source states Jose/Arriagada or a direct identity bridge. |
| 5 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.10 | Requires independent identity-bearing bridge to Arturo/Pulgar-Smith; do not attach from this source. |
| 6 | Direct Jose/Juana parent-candidate relationship | 0.02 | No action from this source; revisit only if a relationship-bearing record appears. |

## Recommended Next Action

Hold the staged conflict draft for conversion/page-boundary QA. The exact next proof-review step is to reconcile `research/_staging/conflicts/chunk-8daffb98e793-p0002-02-page-boundary-and-identity-qa.md` and `CHUNK-8daffb98e793-P0002-02` against the available page-4 chunk/source page: confirm the correct source page, verify the visible/literal wording `Darío Pulgar` in the surgeon list, and resolve the missing `page-0002-chunk-02.md` path or manifest mismatch.

After that QA, promote at most a narrow claim that the article describes `Darío Pulgar` as one of the surgeons accompanying practical anatomy activities at San Juan de Dios Hospital. Do not merge or attach the claim to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, `Dario Pulgar A.`, or any Jose/Juana parent candidate unless a separate identity-bearing source supplies full name, age/vital dates, occupation continuity, relationship, or another explicit bridge.
