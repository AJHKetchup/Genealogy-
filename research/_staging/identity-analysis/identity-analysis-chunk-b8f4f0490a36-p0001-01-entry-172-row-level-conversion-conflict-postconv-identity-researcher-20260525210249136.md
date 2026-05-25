---
type: identity_conflict_analysis
status: draft
role: identity_researcher
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
worker: postconv-identity-analysis-20260525210249136
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md"
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Targeted conversion QA is required before any identity, birth, parent-child relationship, or canonical attachment is promoted. The assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth, while the assigned converted Markdown reads the same entry number as a Burgos/de la Cruz birth.
- The father field in the Pulgar/Arriagada row is not promotion-ready. The current chunk reads `Jose del Carmen Pulgar S.`, and the source packet requires QA to decide whether the visible field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and related b8f4 relationships appear to depend on earlier b8f4 entry-172 staging. They are context, not independent corroboration while this row-level conversion conflict is open.
- No same-person merge should be made between the entry-172 child or parents and any Dario-line person. The staged draft does not name Dario, and the only Dario comparison comes from existing Pulgar-line wiki/staging context.

## Literal Evidence Boundary

The staged conflict draft says the assigned chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, while the assigned converted Markdown records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.

The assigned chunk literal table reads entry 172 as registered on 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`, male; born 8 March 1888 at 3 p.m. on Calle de Valdivia; father `Jose del Carmen Pulgar S.`, Chilean, employee, resident on Calle de Colipi; mother `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident on Calle de Colipi; declarant/witness context includes Ernesto Herrera L.

The assigned converted Markdown literal section for entry 172 instead reads child `Jose Miguel`, male; born 6 April 1888 at 10 p.m.; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; declarant `Oswaldo Burgos`.

Interpretation: these are incompatible row/family clusters for the same assigned entry number, not spelling variants.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Row

Evidence supporting:

- The assigned chunk for `CHUNK-b8f4f0490a36-P0001-01` explicitly transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`.
- The source packet states that direct image inspection during extraction supported the Pulgar/Arriagada row on register page 58, entry 172.
- The source packet marks family relevance high and matched terms `Arriagada` and `Pulgar`.
- Existing wiki stubs preserve the same child and mother names, but those pages appear b8f4-derived and should not be counted as independent support.

Conflicts and weaknesses:

- The assigned converted Markdown for the same source/entry number gives a wholly different Burgos/de la Cruz family.
- The father suffix or abbreviation after `Pulgar` remains uncertain.
- Prior canonical/staged b8f4 facts may have been generated before the current row-level conflict was isolated.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Strong chunk/source-packet support, blocked by direct converted-file contradiction. |
| conflict_severity | 0.95 | Different child, father, mother, birth date, and family cluster. |
| evidence_quality | 0.62 | Civil-register row is strong in principle, but current evidence is derivative/staged and requires row QA. |
| conversion_confidence | 0.35 | Source packet itself marks conversion confidence low due to row-level conflict. |
| claim_probability | 0.60 | Pulgar row is plausible and image-reviewed per packet, but not certified. |
| relevance | 0.90 | Directly relevant to Pulgar/Arriagada parent-child identity if certified. |
| canonical_readiness | 0.05 | Hold until targeted conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Row

Evidence supporting:

- The assigned converted Markdown explicitly labels entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The converted Markdown includes a complete entry-172 narrative with date, parents, declarant, and page context.

Conflicts and weaknesses:

- The assigned chunk for the same converted source and chunk id reads a different row for entry 172.
- The source packet says image-reviewed context supports the Pulgar/Arriagada row rather than the Burgos/de la Cruz row.
- No canonical wiki page or staged identity context found in this review independently anchors `Oswaldo Burgos`, `Concepcion de la Cruz`, or `Jose Miguel` to this task.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Supported only by the conflicting converted Markdown in the reviewed set. |
| conflict_severity | 0.95 | Same row number is assigned to incompatible families. |
| evidence_quality | 0.45 | Complete derivative transcription, but contradicted by chunk and source packet. |
| conversion_confidence | 0.30 | Current conversion is specifically challenged by post-conversion extraction. |
| claim_probability | 0.30 | Possible file/row assignment error or older conversion error. |
| relevance | 0.70 | Relevant as the competing row-control hypothesis, not as Pulgar-line evidence. |
| canonical_readiness | 0.00 | Do not promote from this conflict state. |

## Hypothesis 3: Father Candidate Is Jose del Carmen Pulgar / Jose del Carmen Pulgar S.

Evidence supporting:

- The Pulgar/Arriagada chunk reads the father field as `Jose del Carmen Pulgar S.`, Chilean, employee, resident on Calle de Colipi.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` has a stub for `Jose del Carmen Pulgar`.

Conflicts and weaknesses:

- The canonical `Jose del Carmen Pulgar` visible evidence snapshot concerns a draft child link to `Tulio Cesar Luis Jose`, not this entry-172 child.
- The suffix `S.` could be a name part, abbreviation, or uncertain reading; the exact father name is not certified.
- Same-person identity between the entry-172 father and canonical `Jose del Carmen Pulgar` is name-based only at this stage.

Scores: identity confidence with canonical `Jose del Carmen Pulgar` 0.28; relationship confidence as father of `Jose del Carmen Segundo Pulgar Arriagada` 0.45 pending row QA; evidence quality 0.55; conversion confidence 0.35; claim probability 0.50; relevance 0.85; canonical readiness 0.05.

## Hypothesis 4: Mother Candidate Is Juana Arriagada de Pulgar

Evidence supporting:

- The Pulgar/Arriagada chunk reads the mother field as `Juana Arriagada de Pulgar`, Chilean, resident on Calle de Colipi.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` has the same preferred name and a b8f4-derived child link to `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts and weaknesses:

- The existing canonical child link appears dependent on the same conflicted b8f4 entry-172 evidence; it is not independent support.
- Existing wiki context also has `Juana de Dios Amagada de Pulgar`, with a separate draft child link to `Tulio Cesar Luis Jose`. That Juana candidate is not named in this staged draft and should not be merged with `Juana Arriagada de Pulgar`.

Scores: identity confidence with canonical `Juana Arriagada de Pulgar` 0.42; relationship confidence as mother of `Jose del Carmen Segundo Pulgar Arriagada` 0.48 pending row QA; evidence quality 0.58; conversion confidence 0.35; claim probability 0.55; relevance 0.90; canonical readiness 0.05.

## Dario-Line Comparison Required By Pulgar Context

Candidates compared: `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.

Evidence supporting a Dario connection:

- Only broad Pulgar-line context supports a double-check. The entry-172 child has Pulgar/Arriagada surnames if the Pulgar row controls.
- Canonical `Dario Arturo Pulgar-Smith` exists as a family-supplied maternal-grandfather page and explicitly warns not to merge similarly named source clusters automatically.
- Canonical `Darío Pulgar Arriagada` exists as a separate stub tied to a 5 December 2000 expropriation event.
- Local staged context elsewhere preserves document-level `Dario Arturo Pulgar` CV evidence and `Dario Jose Pulgar-Arriagada`/ICRC clusters separately.

Evidence against a Dario merge:

- This staged draft and the entry-172 literal row do not name any Dario.
- If the Pulgar row is certified, the named child is `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888, not Dario Arturo, Dario Jose, or Darío Pulgar Arriagada.
- No reviewed source in this task provides a parent-child, grandparent, spouse, age, occupation, residence, or chronology bridge from the entry-172 child or parents to any Dario candidate.

Ranked Dario/Pulgar hypotheses:

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Entry 172, if certified, supports a separate `Jose del Carmen Segundo Pulgar Arriagada` child identity with Jose/Juana parent candidates. | 0.60 | Targeted conversion QA for source image versus chunk versus converted Markdown; then proof review of child and parent claims. |
| 2 | The father is the same person as canonical `Jose del Carmen Pulgar`. | 0.28 | After row QA, run parent identity proof review comparing accepted Jose del Carmen Pulgar records and suffix/name variants. |
| 3 | The mother is the same person as canonical `Juana Arriagada de Pulgar`. | 0.42 | After row QA, run parent identity proof review and separate b8f4-derived evidence from independent evidence. |
| 4 | Entry 172 is an indirect clue for later Dario Arturo Pulgar / Pulgar-Smith / Dario Jose Pulgar-Arriagada lineage work. | 0.18 | Require a documented relationship chain from a proof-reviewed Pulgar/Arriagada person to a Dario candidate. |
| 5 | Same-person merge with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | 0.02 | Do not merge; require direct identity-bearing evidence or a proof-reviewed lineage bridge with compatible chronology. |

## Conflict Types

- Same-person conflict: unresolved for the entry-172 father versus canonical `Jose del Carmen Pulgar`, and for the entry-172 mother versus canonical `Juana Arriagada de Pulgar`; both are held pending row QA and independent identity proof review.
- Duplicate-person risk: high if b8f4-derived wiki stubs are treated as independent proof; high if Dario/Pulgar identities are merged by surname or family context alone.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` requires field-level QA; `Juana Arriagada de Pulgar` must remain separate from `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: the parent-child claims for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar [S./?]`, and `Juana Arriagada de Pulgar` conflict with the converted-file `Jose Miguel`/`Oswaldo Burgos`/`Concepcion de la Cruz` family cluster.
- Chronology conflict: Pulgar row gives birth 8 March 1888 and registration 7 April 1888; Burgos row gives birth 6 April 1888 and registration 7 April 1888. These cannot both describe the same child.

## Recommended Next Action

Run targeted conversion QA for `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, the assigned converted Markdown, and `CHUNK-b8f4f0490a36-P0001-01`. The QA note must decide whether the controlling entry-172 row is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and it must certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth, parent-child relationship, or canonical wiki attachment. A separate identity-bridge proof review is required before connecting this evidence to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, or any broader Jose/Juana parent candidate.
