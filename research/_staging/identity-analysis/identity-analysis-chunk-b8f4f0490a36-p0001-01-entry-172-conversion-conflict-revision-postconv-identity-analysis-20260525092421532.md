---
type: identity_conflict_analysis
status: hold_for_conversion_qa
worker: postconv-identity-analysis-20260525092421532
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525082133967.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525082133967.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Entry 172 Conversion Conflict

## Blockers First

- Material row-level or file-assignment conflict blocks identity, relationship, chronology, and canonical promotion from this entry. The current chunk reads entry 172 as a Pulgar/Arriagada birth registration, while the assigned converted Markdown reads entry 172 as a Gomez/de la Cruz birth registration.
- Targeted conversion QA must reconcile the source image, assigned converted Markdown, current chunk, and source packet before any fact, relationship, duplicate-person merge, or Pulgar-line bridge can be used.
- The father field is not settled. Preserve all literal-reading candidates: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` contain earlier b8f4-derived evidence snapshots. Those pages are cautionary context, not independent confirmation of this conflicted row.
- This staged draft does not name or bridge `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`.

## Literal Evidence Reviewed

- Staged conflict draft: identifies a high-confidence row-level conversion conflict for entry 172 and recommends `hold_for_conversion_qa`.
- Current chunk/source packet reading: entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`; father rendered as `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; parents resident at `Calle de Colipí`; informant `Ernesto Herrera L.`.
- Assigned converted Markdown reading: entry 172 records `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born 26 March 1888 at 10 p.m. in `En esta`; informant/father `Oswaldo Gomez`.

Interpretation: if the current chunk is certified by source-image QA, it would support a separate birth-registration identity candidate for `Jose del Carmen Segundo Pulgar Arriagada` and parent candidates `Jose del Carmen Pulgar [S./?]` and `Juana Arriagada de Pulgar`. Until then, the row conflict prevents canonical readiness.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Supporting evidence:

- The current chunk and source packet both identify entry 172 on page 58 as `Jose del Carmen Segundo Pulgar Arriagada`.
- The current chunk gives internally coherent parent and residence fields: father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, both at `Calle de Colipí`.
- The source packet marks Pulgar/Arriagada family relevance high if the current chunk row is confirmed.

Conflicts and limits:

- The assigned converted Markdown gives a different child, parents, birth date, place, informant, and official.
- The father-name ending after `Pulgar` is unresolved.
- Existing wiki snapshots appear to rely on the same b8f4 evidence cluster and cannot resolve the conflict independently.

Scores: identity confidence 0.45 now, 0.80 if visually certified; conflict severity 0.95; evidence quality 0.55; conversion confidence 0.35; claim probability 0.58; relevance 0.95; canonical readiness 0.05.

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Supporting evidence:

- The assigned converted Markdown records entry 172 as `José Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`.
- The converted file is the derivative transcript referenced by the chunk front matter.

Conflicts and limits:

- The current chunk and source packet contradict the converted Markdown and identify a Pulgar/Arriagada row.
- This reading has no Pulgar-line relevance unless QA shows that the chunk/source packet is assigned to the wrong row or source.

Scores: identity confidence 0.25 for this Pulgar-line task; conflict severity 0.95; evidence quality 0.45; conversion confidence 0.35; claim probability 0.42; relevance 0.10; canonical readiness 0.00.

## Hypothesis 3: Father Candidate Is Jose del Carmen Pulgar / Jose del Carmen Pulgar S.

Supporting evidence:

- The current chunk reads the father field for the Pulgar/Arriagada row as `Jose del Carmen Pulgar S.`.
- Existing canonical context has a `Jose del Carmen Pulgar` stub, but its visible evidence snapshot concerns another child, `Tulio Cesar Luis Jose`.

Conflicts and limits:

- The father suffix is unsettled: `Pulgar`, `Pulgar S.`, or `Pulgar [?]`.
- No same-person bridge proves that this father candidate is the same person as the existing canonical stub.
- No evidence in this staged draft connects this father candidate to a Dario-line identity.

Scores: same-person confidence with `wiki/people/jose-del-carmen-pulgar.md` 0.30; relationship confidence as father of `Jose del Carmen Segundo Pulgar Arriagada` 0.45 pending QA; evidence quality 0.50; claim probability 0.52; canonical readiness 0.05.

## Hypothesis 4: Mother Candidate Is Juana Arriagada de Pulgar

Supporting evidence:

- The current chunk reads the mother field as `Juana Arriagada de Pulgar`.
- Existing canonical context has a `Juana Arriagada de Pulgar` page with earlier b8f4-derived child evidence for `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts and limits:

- The same row-level conflict blocks the mother-child relationship until the Pulgar/Arriagada row is certified.
- The canonical mother page appears dependent on this same conflicted evidence cluster, so it does not supply independent corroboration.
- No direct evidence in this staged draft connects this Juana candidate to Dario-line identities or broader Juana/Jose parent clusters.

Scores: same-person confidence with `wiki/people/juana-arriagada-de-pulgar.md` 0.40; relationship confidence as mother of `Jose del Carmen Segundo Pulgar Arriagada` 0.45 pending QA; evidence quality 0.55; claim probability 0.58; canonical readiness 0.05.

## Pulgar-Line Candidate Comparison

Candidates compared: `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, and the Jose/Juana parent candidates.

Supporting context:

- If confirmed, the current chunk would add an 1888 Los Angeles birth-registration candidate with Pulgar and Arriagada surnames.
- Existing local context separately preserves `Dario Arturo Pulgar-Smith` as family-supplied, `Dario Arturo Pulgar` as a staged CV document-level subject, `Dario Jose`/`Dario J.` Pulgar-Arriagada source clusters, and canonical `Darío Pulgar Arriagada` from a 2000 expropriation notice.

Conflicts and limits:

- This staged draft does not name Dario, Arturo, Smith, `Dario Jose`, a spouse, child, grandchild, birth-to-death chronology, or any relationship tying entry 172 to a Dario candidate.
- The 1888 birth date, if confirmed, belongs to `Jose del Carmen Segundo Pulgar Arriagada`, not to a named Dario candidate.
- Name and surname overlap alone would create a high duplicate-person and same-person conflation risk.

Ranked hypotheses:

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 172, if certified, supports a separate `Jose del Carmen Segundo Pulgar Arriagada` birth-registration identity candidate with Jose/Juana parent candidates. | 0.58 | Targeted source-image row QA against the converted Markdown and chunk. |
| 2 | The father is the same person as existing `Jose del Carmen Pulgar`. | 0.30 | After conversion QA, run parent identity proof review comparing accepted Jose del Carmen Pulgar records. |
| 3 | The mother is the same person as existing `Juana Arriagada de Pulgar`. | 0.40 | After conversion QA, run parent identity proof review and determine whether existing evidence is independent or b8f4-derived. |
| 4 | The confirmed entry is an indirect clue for later Dario Arturo Pulgar / Pulgar-Smith lineage work. | 0.20 | Require a proof-reviewed lineage bridge from this child or parents to a Dario candidate. |
| 5 | Same-person merge with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | 0.02 | Do not merge; require direct identity-bearing evidence or a documented relationship chain. |

## Conflict Types

- Same-person conflict: unresolved only for possible Jose/Juana parent candidates. No same-person merge is supported.
- Duplicate-person risk: high if earlier b8f4-derived wiki pages are treated as independent evidence; moderate for reuse of the `Jose del Carmen Pulgar` stub; high for any Dario merge by name alone.
- Name-variant conflict: father suffix `S.` is unresolved; keep `Pulgar`, `Pulgar S.`, and `Pulgar [?]` as separate literal readings.
- Relationship conflict: parent-child relationships for `Jose del Carmen Segundo Pulgar Arriagada` with `Jose del Carmen Pulgar [S./?]` and `Juana Arriagada de Pulgar` are held until row QA.
- Chronology conflict: none established internally if the Pulgar row is confirmed; current conflict is row/source identity, not date inconsistency.

## Overall Scores

| Score | Value | Reason |
| --- | ---: | --- |
| identity_confidence | 0.45 | The Pulgar child and parent names are clear in the current chunk but contradicted by the assigned converted transcript. |
| conflict_severity | 0.95 | Child, parents, birth details, place, informant, and source row differ materially. |
| evidence_quality | 0.55 | The staged/chunk evidence is useful but not stable because derivative artifacts disagree. |
| conversion_confidence | 0.35 | Entry 172 needs targeted source-image QA before use. |
| claim_probability | 0.58 | The Pulgar/Arriagada reading is plausible from the current chunk/source packet, but not promotion-ready. |
| relevance | 0.95 | If confirmed, this directly concerns Pulgar/Arriagada identity and parent candidates. |
| canonical_readiness | 0.05 | Hold all dependent claims, relationships, parent merges, and Dario-line bridges. |

## Recommended Next Action

Run targeted conversion QA for the specific source image and row. The QA note must decide whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz row, reconcile the source image with the assigned converted Markdown and current chunk, and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, run proof review before promoting parent-child claims for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar [S./?]`, and `Juana Arriagada de Pulgar`. A separate identity-bridge proof review is required before connecting this evidence to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, or any broader Jose/Juana parent candidate.
