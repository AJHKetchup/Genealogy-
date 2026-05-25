---
type: identity_conflict_analysis
status: hold_for_conversion_qa
worker: postconv-identity-analysis-20260525092213644
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525081514407.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Entry 172 Conversion Conflict

## Blockers First

- Material row-level or file-assignment conflict blocks all identity, relationship, and chronology promotion from this entry. The current chunk reads entry 172 as a Pulgar/Arriagada birth registration, while the assigned converted Markdown reads entry 172 as a Gomez/de la Cruz birth registration.
- The controlling source reading is not settled for identity use. Targeted conversion QA must reconcile the source image, converted Markdown, current chunk, and source packet before any canonical fact, relationship, duplicate-person merge, or Pulgar-line bridge is accepted.
- The father field has an unresolved literal-reading issue. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as possible readings until QA certifies the exact form.
- Existing canonical wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` contain earlier b8f4-derived evidence snapshots. Because this task's staged draft identifies the b8f4 conversion as conflicted, those wiki entries are context for caution, not a reason to promote or merge.
- No direct evidence in this staged draft links the child or parents to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. Those candidates remain anti-conflation checkpoints only.

## Literal Evidence Reviewed

From the staged draft and source packet:

- Current chunk entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`; male; registered 7 April 1888; born 8 March 1888 at 3 p.m.; birthplace `Calle de Valdivia`; father rendered in the chunk as `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; parents resident at `Calle de Colipí`; informant `Ernesto Herrera L.`.
- Assigned converted Markdown entry 172: child `José Francisco`; father `Oswaldo Gomez`; mother `Emilia de la Cruz`; born 26 March 1888 at 10 p.m.; place `En esta`; informant/father `Oswaldo Gomez`.
- The staged conflict draft classifies this as `row_level_conversion_conflict` with `confidence: high` and `promotion_recommendation: hold_for_conversion_qa`.

Interpretation kept separate: if the current chunk is confirmed by source-image QA, it would support a distinct birth-registration identity candidate for `Jose del Carmen Segundo Pulgar Arriagada` and parent candidates `Jose del Carmen Pulgar [S./?]` and `Juana Arriagada de Pulgar`. Until then, the conversion conflict prevents canonical readiness.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Evidence supporting:

- The current chunk and source packet both identify entry 172 on page 58 as `Jose del Carmen Segundo Pulgar Arriagada`.
- The same current chunk gives internally coherent family fields: father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, shared residence `Calle de Colipí`, and a birth date of 8 March 1888.
- The source packet marks family relevance high if the current chunk's row is confirmed.

Evidence against or limiting:

- The assigned converted Markdown for the same converted file and entry number gives a completely different child and parents.
- The father suffix after `Pulgar` is not certified.
- The existing wiki snapshot uses b8f4-derived claims, but the current task shows that b8f4 evidence is not conversion-stable.

Assessment:

- Claim probability: 0.58 pending targeted image/row QA.
- Identity confidence: 0.45 for canonical use now; 0.80 if the current chunk is visually certified.
- Evidence quality: 0.55 now because source-derived artifacts conflict.
- Conversion confidence: 0.35 overall; high concern despite a clear current chunk reading.
- Relevance: 0.95 if confirmed, because it directly names Pulgar/Arriagada persons.
- Canonical readiness: hold_for_conversion_qa.

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Evidence supporting:

- The assigned converted Markdown records entry 172 as `José Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`.
- The converted file is the derivative transcript referenced by the chunk front matter.

Evidence against or limiting:

- The current chunk and source packet for this task explicitly disagree and identify a Pulgar/Arriagada row.
- The staged conflict draft says the disagreement is not a spelling variant.
- This hypothesis has no Pulgar-line family relevance unless conversion QA shows the current chunk is assigned to the wrong source or row.

Assessment:

- Claim probability: 0.42 pending targeted image/row QA.
- Identity confidence: 0.25 for this task's Pulgar-line analysis.
- Evidence quality: 0.45 because it is a derivative transcript contradicted by the staged chunk.
- Conversion confidence: 0.35 overall.
- Relevance: 0.10 to Pulgar identity research unless it explains the assignment conflict.
- Canonical readiness: not_ready.

## Hypothesis 3: Father Candidate Is Jose del Carmen Pulgar / Jose del Carmen Pulgar S.

Evidence supporting:

- The current chunk reads the father field for the Pulgar/Arriagada row as `Jose del Carmen Pulgar S.`.
- Existing canonical context has a separate `Jose del Carmen Pulgar` page, but its visible evidence snapshot concerns another child, `Tulio Cesar Luis Jose`; it does not by itself prove this entry's father is the same person.

Evidence against or limiting:

- The exact father-name ending is unresolved: `Pulgar`, `Pulgar S.`, or `Pulgar [?]`.
- No direct same-person bridge connects this father candidate to the existing `Jose del Carmen Pulgar` canonical stub or to any Dario-line person.

Assessment:

- Claim probability: 0.52 that the current chunk names a father in the Jose del Carmen Pulgar name cluster.
- Same-person confidence with existing `wiki/people/jose-del-carmen-pulgar.md`: 0.30.
- Relationship confidence as father of `Jose del Carmen Segundo Pulgar Arriagada`: 0.45 now; dependent on conversion QA.
- Evidence quality: 0.50.
- Canonical readiness: hold_for_conversion_qa_and_parent_identity_review.

## Hypothesis 4: Mother Candidate Is Juana Arriagada de Pulgar

Evidence supporting:

- The current chunk reads the mother field as `Juana Arriagada de Pulgar`.
- Existing canonical context has a `Juana Arriagada de Pulgar` page with earlier b8f4-derived child evidence for `Jose del Carmen Segundo Pulgar Arriagada`.

Evidence against or limiting:

- The same b8f4 row-level conflict blocks promotion of the mother-child relationship until QA confirms the Pulgar/Arriagada row.
- No direct evidence in this staged draft connects this Juana candidate to Dario-line candidates or other Juana/Jose parent clusters beyond the entry itself.

Assessment:

- Claim probability: 0.58 that the current chunk names this mother.
- Same-person confidence with existing `wiki/people/juana-arriagada-de-pulgar.md`: 0.40, because that page appears to rely on the same conflicted b8f4 evidence cluster.
- Relationship confidence as mother of `Jose del Carmen Segundo Pulgar Arriagada`: 0.45 now; dependent on conversion QA.
- Evidence quality: 0.55.
- Canonical readiness: hold_for_conversion_qa_and_parent_identity_review.

## Hypothesis 5: Same Person Or Lineal Bridge To Dario Candidates

Candidates compared as required: `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, and canonical `Darío Pulgar Arriagada`.

Evidence supporting:

- The potential child name `Jose del Carmen Segundo Pulgar Arriagada` and parent surnames `Pulgar` and `Arriagada` are family-context hints worth preserving for later Pulgar-line review if the row is confirmed.
- Existing local context separately preserves a family-supplied `Dario Arturo Pulgar-Smith`, staged/document-level `Dario Arturo Pulgar` CV clusters, `Dario Jose Pulgar-Arriagada` source-context/image clusters, and canonical `Darío Pulgar Arriagada` tied to a 2000 expropriation notice.

Evidence against or limiting:

- This entry does not name Dario, Arturo, Smith, Jose as a Dario middle-name variant, a spouse, a child, a grandchild, or any direct relationship to the Dario candidates.
- The birth year 1888 for `Jose del Carmen Segundo Pulgar Arriagada`, if confirmed, is not enough to infer identity with later Dario candidates or to infer parentage/ancestry by surname.
- The canonical `Dario Arturo Pulgar-Smith` page explicitly warns not to automatically merge similarly named Pulgar records without identity review.
- The canonical `Darío Pulgar Arriagada` page currently supports only a 2000 expropriation mention and supplies no bridge to this 1888 birth entry.

Ranked assessment:

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | The entry, if confirmed, creates/updates a separate `Jose del Carmen Segundo Pulgar Arriagada` birth-registration identity candidate with Jose/Juana parent candidates. | 0.58 | Targeted conversion QA of source image against converted Markdown and chunk. |
| 2 | The father is the same person as the existing `Jose del Carmen Pulgar` stub. | 0.30 | After conversion QA, run parent identity proof review comparing all accepted Jose del Carmen Pulgar records. |
| 3 | The mother is the same person as the existing `Juana Arriagada de Pulgar` stub. | 0.40 | After conversion QA, run parent identity proof review and verify whether existing wiki evidence is independent or b8f4-derived. |
| 4 | The confirmed entry supplies a later indirect clue for the Dario Arturo Pulgar / Pulgar-Smith line. | 0.20 | Require an explicit, proof-reviewed lineage bridge from the child or parents to a Dario candidate. |
| 5 | Same-person merge with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | 0.02 | Do not merge; require direct identity-bearing evidence naming the same person or a documented relationship chain. |

## Conflict Types

- Same-person conflict: unresolved only for possible future parent candidates. No same-person merge is supported now.
- Duplicate-person risk: high if earlier b8f4-derived wiki pages are treated as independent confirmation; moderate for `Jose del Carmen Pulgar` father-candidate reuse; low for direct Dario identity because the entry does not name Dario.
- Name-variant conflict: father surname suffix `S.` is unresolved; `Pulgar`, `Pulgar S.`, and `Pulgar [?]` must remain separate literal readings until QA.
- Relationship conflict: parent-child relationships for `Jose del Carmen Segundo Pulgar Arriagada` with `Jose del Carmen Pulgar [S./?]` and `Juana Arriagada de Pulgar` are held because the controlling row is conflicted.
- Chronology conflict: none established internally if the Pulgar row is confirmed; the conflict is source-row identity, not a date inconsistency. Do not use the 1888 birth date to infer Dario-line chronology without a bridge.

## Scores

| Score | Value | Reason |
| --- | ---: | --- |
| identity_confidence | 0.45 | The Pulgar child/parent identities are clear in the current chunk but blocked by a contradictory converted transcript. |
| conflict_severity | 0.95 | Child, parents, birth date, place, informant, and likely row all differ. |
| evidence_quality | 0.55 | Useful staged/chunk evidence exists, but derivative artifacts conflict. |
| conversion_confidence | 0.35 | The conversion set is materially unstable for entry 172 until row-level QA. |
| claim_probability | 0.58 | The Pulgar/Arriagada reading is plausible from the current chunk/source packet, not ready for promotion. |
| relevance | 0.95 | If confirmed, this directly concerns Pulgar/Arriagada family candidates. |
| canonical_readiness | 0.05 | Hold all dependent facts, relationships, and identity merges. |

## Recommended Next Action

Run targeted conversion QA for the specific source image and row: compare the source image, assigned converted Markdown, current chunk, and source packet for entry 172; decide whether the controlling row is the Pulgar/Arriagada entry or the Gomez/de la Cruz entry; and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

Only after that QA passes should proof review consider parent-child relationship claims for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar [S./?]`, and `Juana Arriagada de Pulgar`. A separate identity-bridge proof review is required before any connection to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, or any Jose/Juana parent candidate is promoted.
