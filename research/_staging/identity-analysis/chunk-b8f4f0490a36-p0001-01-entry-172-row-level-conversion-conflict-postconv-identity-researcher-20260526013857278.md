---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: "postconv-identity-analysis-20260526013800814"
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-26
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers

- The same entry number, page reference, source image, converted file, and chunk are represented by two incompatible readings. The assigned chunk/source packet read entry 172 as a Pulgar/Arriagada child. The current converted Markdown reads entry 172 as a Burgos/de la Cruz child.
- This is a row-control conflict before it is a person-identity conflict. Until targeted conversion QA decides which row controls entry 172, no canonical birth fact, parent-child relationship, identity merge, name variant, or Dario-line bridge should be promoted from this record.
- The father field in the Pulgar/Arriagada reading remains uncertified at the final character level: possible readings include `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical wiki context already contains low-confidence Pulgar/Arriagada claims from this chunk, but those should not be strengthened while the derivative row conflict remains unresolved.

## Literal Evidence

From the staged conflict draft and source packet:

- Assigned chunk reading for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; born 8 March 1888 about 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at birth.
- Current converted Markdown reading for entry 172: child `Jose Miguel`; born 6 April 1888 about 10 p.m. at `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.
- The referenced chunk file itself contains the Pulgar/Arriagada row for entry 172 and surrounding rows 171-176 that differ materially from the current converted Markdown.

## Existing Wiki Context Reviewed

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has a stub person with probable mother `Juana Arriagada de Pulgar` and life facts derived from the same chunk/source-packet cluster.
- `wiki/people/juana-arriagada-de-pulgar.md` has a stub person with probable child `Jose del Carmen Segundo Pulgar Arriagada` from the same chunk/source-packet cluster.
- `wiki/people/jose-del-carmen-pulgar.md` exists separately and has a draft child link to `Tulio Cesar Luis Jose` from a different staged relationship.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` exists separately and has a draft child link to `Tulio Cesar Luis Jose` from a different staged relationship.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merge with similarly named Dario/Pulgar clusters.
- `wiki/people/dar-o-pulgar-arriagada.md` is a separate stub for a person named in a 2000 expropriation resolution.
- `wiki/people/dario-pulgar-adult-passenger-age-64.md` and `wiki/people/dario-pulgar-child-passenger-age-11.md` are separate passenger-list clusters.

## Hypotheses Ranked

| Rank | Hypothesis | Evidence supporting | Evidence against / limits | Probability |
| ---: | --- | --- | --- | ---: |
| 1 | Entry 172 is a Pulgar/Arriagada birth row for Jose del Carmen Segundo Pulgar Arriagada. | The assigned chunk and source packet agree on the Pulgar/Arriagada row; the staged conflict draft summarizes the same literal reading. | The current converted Markdown gives a completely different Burgos/de la Cruz row for the same entry number; source image QA is still required. | 0.62 |
| 2 | Entry 172 is a Burgos/de la Cruz birth row for Jose Miguel. | The current converted Markdown explicitly records entry 172 as Jose Miguel, son of Oswaldo Burgos and Concepcion de la Cruz. | The assigned chunk and staged source packet for the same source image and chunk read a different row; the current converted Markdown may be stale or row-shifted. | 0.30 |
| 3 | The Pulgar/Arriagada row exists in the image but may be mis-numbered or misaligned relative to entry 172. | The row data in the chunk appears internally coherent and includes neighboring rows that diverge from the current converted Markdown. | No permitted evidence reviewed here resolves whether this is a numbering, page, or conversion-version mismatch. | 0.08 |

## Identity And Relationship Analysis

### Child Candidate

- Literal reading if the Pulgar row controls: `Jose del Carmen Segundo Pulgar Arriagada`.
- Interpretation: this can support a child identity only after row-control QA. It should not be merged with any Dario Pulgar person by surname or Arriagada association alone.
- Identity confidence now: 0.45 because the name is clear in one derivative transcription, but the controlling row is disputed.

### Father Candidate

- Literal reading if the Pulgar row controls: `Jose del Carmen Pulgar S.` with father attributes `Chileno`, `Empleado`, resident at Calle de Colipi.
- Interpretation: this may be the same person as canonical `wiki/people/jose-del-carmen-pulgar.md`, but the father-field suffix and row control both need review. A same-person claim with the `Tulio Cesar Luis Jose` father candidate is not ready.
- Identity confidence now: 0.35 for attachment to canonical `Jose del Carmen Pulgar`; 0.55 for a distinct local father candidate named Jose del Carmen Pulgar pending QA.

### Mother Candidate

- Literal reading if the Pulgar row controls: `Juana Arriagada de Pulgar`, Chilena, `Su sexo`, resident at Calle de Colipi.
- Interpretation: this may support the existing canonical stub `Juana Arriagada de Pulgar`, but it should not be silently corrected to or merged with `Juana de Dios Amagada de Pulgar`. Those are separate Jose/Juana parent-candidate clusters until a reviewed source bridges them.
- Identity confidence now: 0.45 for attachment to canonical `Juana Arriagada de Pulgar`; 0.10 for same-person with `Juana de Dios Amagada de Pulgar`.

### Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: family-supplied maternal grandfather page. No reviewed evidence in this entry names Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, spouse, child, or grandchild. Same-person or ancestor bridge probability from this entry alone: 0.05.
- `Dario Arturo Pulgar`: appears in local CV-oriented staged context, but this entry does not name Dario Arturo Pulgar or provide a CV/person bridge. Same-person or lineage bridge probability from this entry alone: 0.05.
- `Dario Jose Pulgar-Arriagada`: not named in this staged draft or reviewed entry-172 literal evidence. If later context proposes a Dario Jose Pulgar-Arriagada born to Jose/Juana, this entry can only be a family-context hint after row QA, not proof of that Dario identity. Probability from this entry alone: 0.03.
- `Dario/Dario Pulgar Arriagada`: existing canonical `Darío Pulgar Arriagada` is a 2000 expropriation cluster and not bridged to this 1888 birth entry. Probability from this entry alone: 0.03.
- Passenger-list `Dario Pulgar` adult age 64 and child age 11: no bridge from this entry. The adult passenger age 64 in 1953 implies an approximate 1888-1889 birth window, but this entry names Jose del Carmen Segundo, not Dario, and row control is unresolved. Chronology hint only; probability from this entry alone: 0.12 for future double-check, not promotion.

## Conflicts

- Same entry number conflict: Pulgar/Arriagada row versus Burgos/de la Cruz row.
- Identity conflict: the same staged source cluster has already produced canonical/stub Pulgar claims, while the current converted Markdown would support unrelated Burgos/de la Cruz identities.
- Relationship conflict: parent candidates differ entirely between readings, so father, mother, informant, and child relationships cannot be accepted together.
- Chronology conflict: Pulgar reading gives birth 8 March 1888; Burgos reading gives birth 6 April 1888.
- Place conflict: Pulgar reading gives Calle de Valdivia and parent residence Calle de Colipi; Burgos reading gives `En esta` and different parent context.
- Name-variant risk: `Jose del Carmen Pulgar S.` must not be normalized to `Jose del Carmen Pulgar` or merged with other Jose Pulgar candidates until the visible father field is certified.

## Scores

| Metric | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.40 | One derivative path provides a coherent Pulgar family row, but the controlling row is disputed. |
| Conflict severity | 0.95 | The conflict changes child identity, parents, dates, places, and informant. |
| Evidence quality | 0.58 | The staged chunk/source packet are detailed, but the evidence is derivative and conflicts with the converted Markdown. |
| Conversion confidence | 0.30 | Two local conversion products disagree on the same row. |
| Claim probability | 0.20 | Canonical Pulgar claims are blocked until QA; conditional Pulgar-row facts are plausible but not promotable. |
| Relevance | 0.85 | The Pulgar/Arriagada reading is highly relevant to Pulgar-line research if certified. |
| Canonical readiness | 0.05 | Not ready for canonical promotion, merge, or relationship strengthening. |

## Recommended Next Action

Hold for targeted conversion QA. The next proof-review or promotion step should compare the source image directly against the converted Markdown, assigned chunk, and source packet, then certify:

- which row controls entry 172;
- whether the child is `Jose del Carmen Segundo Pulgar Arriagada` or `Jose Miguel`;
- whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`;
- whether existing canonical stub claims derived from this chunk should remain, be downgraded, or be marked conversion-conflicted.

After conversion QA, rerun proof review before any canonical claim, relationship, name variant, same-person decision, duplicate-person merge, or Dario-line comparison is promoted.
