---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526015109623
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: blocked
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Row-control blocker: the assigned chunk and source packet present entry 172 on register page 58 as a Pulgar/Arriagada birth row, while the current converted Markdown presents entry 172 as a Burgos/de la Cruz row. This blocks promotion of child identity, birth details, parent-child relationships, parent merges, and Dario-line bridge claims.
- Father-field blocker: the Pulgar row father field is not yet certified past the visible start `Jose del Carmen Pulgar`. The staged source packet permits only `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted conversion QA.
- Canonical conflict blocker: existing canonical pages already contain low-confidence/probable evidence for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` from earlier entry-172 materials, but this new conflict draft says current conversion control is disputed. Existing pages should not be treated as resolved proof.
- Pulgar-line anti-conflation blocker: no reviewed evidence in this staged conflict proves that `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar` is the same person as, parent of, child of, or direct bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.

## Literal Source Readings

- Staged conflict draft: entry 172 Pulgar/Arriagada reading lists child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth on 8 March 1888 about 3 p.m. at Calle de Valdivia, father visible as `Jose del Carmen Pulgar` with possible suffix, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- Source packet: assigned chunk, page 58, entry 172 reads `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, father and mother residence Calle de Colipi, and informant Ernesto Herrera L. present at the birth.
- Source packet image review: the visible row numbered 172 is a Pulgar/Arriagada row, not the Burgos/de la Cruz row, but the father suffix remains uncertified.
- Current converted Markdown: entry 172 reads child `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth 6 April 1888 about 10 p.m., place `En esta`, informant Oswaldo Burgos.
- Assigned chunk: entry 172 reads the Pulgar/Arriagada row and differs materially from the current converted file for entries 171-176.

## Existing Wiki Context Read

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has a stub person with probable mother `Juana Arriagada de Pulgar` at confidence 1 and life facts from entry 172. These facts depend on the same disputed entry-172 evidence family and should remain held until row QA.
- `wiki/people/juana-arriagada-de-pulgar.md` has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` at confidence 1 and mother attributes from entry 172. This is not sufficient for merge or promotion while row control is disputed.
- `wiki/people/jose-del-carmen-pulgar.md` has a separate draft child link to `Tulio Cesar Luis Jose`, not a proven link to the entry-172 child in this staged conflict.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` has a separate draft child link to `Tulio Cesar Luis Jose`; this is not the same literal mother name as `Juana Arriagada de Pulgar`.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to attach similar Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review.
- `wiki/people/dar-o-pulgar-arriagada.md` records a 2000 event for `Darío Pulgar Arriagada`; it does not provide a parent, birth, or bridge to entry 172.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Interpretation: the assigned chunk and source-packet image review correctly control entry 172, and the current converted Markdown row is from a wrong row/image state or earlier conversion error.

Supporting evidence:

- The assigned chunk gives a full row for entry 172 with coherent Pulgar/Arriagada child, parents, birth date, residence, and informant fields.
- The source packet states that visual review of the source image shows the row numbered 172 as Pulgar/Arriagada.
- The staged conflict draft classifies this as high-confidence row-level conversion conflict and recommends `hold_for_conversion_qa`, not rejection of the Pulgar reading.

Conflicts and limits:

- The current converted Markdown gives a completely different entry 172: Burgos/de la Cruz, different child, different parents, different birth date/time/place, and different informant.
- The father suffix after `Pulgar` remains unresolved.
- This hypothesis can support a targeted QA task but not canonical promotion yet.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong staged chunk/source-packet support for the Pulgar row, but current conversion conflicts. |
| conflict_severity | 0.95 | Row control changes every material person and relationship in entry 172. |
| evidence_quality | 0.72 | Civil birth register evidence is high value; current evidence is staged and internally conflicting. |
| conversion_confidence | 0.35 | Converted Markdown and chunk disagree materially. |
| claim_probability | 0.74 | Pulgar reading is probable as the row to recheck, not ready as a final claim. |
| relevance | 0.92 | Directly relevant to Pulgar/Arriagada family candidates. |
| canonical_readiness | 0.10 | Blocked pending targeted conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Interpretation: the current converted Markdown controls entry 172, and the assigned chunk/source-packet Pulgar row is misaligned.

Supporting evidence:

- The converted Markdown explicitly labels entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.

Conflicts and limits:

- The assigned chunk and source-packet image review both contradict this reading.
- The source packet says the visible row numbered 172 is Pulgar/Arriagada.
- This hypothesis does not explain why the assigned chunk has a coherent Pulgar entry 172 with matching page and source metadata.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Supported by current converted Markdown only, against staged image-reviewed evidence. |
| conflict_severity | 0.95 | If true, it excludes all Pulgar/Arriagada claims from entry 172. |
| evidence_quality | 0.45 | Converted file is direct but contradicted by chunk and source packet. |
| conversion_confidence | 0.35 | Same row-control conflict. |
| claim_probability | 0.20 | Less likely on current staged record; still must be checked by QA. |
| relevance | 0.15 | Low Pulgar-line relevance if this is the controlling row. |
| canonical_readiness | 0.05 | Not ready because row control is contested. |

## Hypothesis 3: Jose del Carmen Segundo Pulgar Arriagada Is A Child Of Jose del Carmen Pulgar And Juana Arriagada de Pulgar

Interpretation: if the Pulgar row is certified, entry 172 supports a child-parent relationship between the named child and parents.

Supporting evidence:

- Assigned chunk names child `Jose del Carmen Segundo Pulgar Arriagada`.
- Assigned chunk names father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Source packet image review supports the child and mother name and visible father start `Jose del Carmen Pulgar`.
- Existing wiki pages already hold this mother-child cluster only at low/probable confidence.

Conflicts and limits:

- Father suffix is unresolved; do not merge `Jose del Carmen Pulgar S.` with the canonical `Jose del Carmen Pulgar` page or other Jose del Carmen Pulgar candidates by name alone.
- Mother `Juana Arriagada de Pulgar` must not be silently corrected to, or merged with, `Juana de Dios Amagada de Pulgar`.
- Relationship is blocked until row-control QA certifies the Pulgar row.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Coherent if Pulgar row controls; unresolved father suffix and row conflict lower confidence. |
| conflict_severity | 0.88 | Affects parent-child identities and possible duplicate parent pages. |
| evidence_quality | 0.70 | Birth register is strong relationship evidence once row control is certified. |
| conversion_confidence | 0.35 | Row-level conversion conflict remains. |
| claim_probability | 0.62 | Probable but conditional on QA. |
| relevance | 0.95 | Directly relevant to Pulgar/Arriagada line. |
| canonical_readiness | 0.12 | Hold for conversion QA and proof review. |

## Hypothesis 4: Entry 172 Provides A Bridge To Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Interpretation: the Pulgar/Arriagada child or parents may belong somewhere in the broader Dario Pulgar family context.

Supporting evidence:

- The surname cluster `Pulgar` and `Arriagada` is relevant to the workspace's Pulgar-line research.
- Canonical `Dario Arturo Pulgar-Smith` is a family-supplied maternal-line person, and staged Pulgar materials repeatedly warn that Dario/Pulgar/Pulgar-Arriagada records require identity review.

Conflicts and limits:

- Entry 172 does not name `Dario`, `Arturo`, `Smith`, `Pulgar-Smith`, `Dario Arturo Pulgar`, or Alexander John Heinz.
- No relationship in the staged conflict connects the 1888 child or parents to canonical `Dario Arturo Pulgar-Smith`.
- A same-person or ancestor bridge would require separate proof-reviewed records connecting identities across generations.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | No direct identity bridge in this entry. |
| conflict_severity | 0.80 | Premature bridge would contaminate the Dario line. |
| evidence_quality | 0.25 | Only family-context relevance, not identity proof. |
| conversion_confidence | 0.35 | Underlying row still disputed. |
| claim_probability | 0.07 | Possible research lead only. |
| relevance | 0.55 | Worth tracking after QA, but not actionable now. |
| canonical_readiness | 0.00 | Not ready. |

## Hypothesis 5: Same As Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, Or Dario/Darío Pulgar Arriagada

Interpretation: the Pulgar/Arriagada names in entry 172 might relate to later Pulgar-Arriagada persons such as Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or canonical Darío Pulgar Arriagada.

Supporting evidence:

- Existing staged and wiki context includes Pulgar-Arriagada name clusters, including `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, and `Darío Pulgar Arriagada`.
- Entry 172, if Pulgar-controlled, supplies a Pulgar/Arriagada family-context lead in Los Angeles, Chile in 1888.

Conflicts and limits:

- Entry 172's child is `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario`.
- The existing canonical `Darío Pulgar Arriagada` page has a 2000 event and no birth/parent bridge to entry 172.
- Staged Dario Jose/Dario J. materials are separate source clusters and cannot be merged with Jose del Carmen Segundo by surname pattern or family-context hunch.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No shared given-name evidence; only surname-family context. |
| conflict_severity | 0.85 | High risk of false merge across different Pulgar-Arriagada people. |
| evidence_quality | 0.20 | No direct bridge evidence in this staged conflict. |
| conversion_confidence | 0.35 | Entry 172 row still disputed. |
| claim_probability | 0.04 | Preserve only as a research caution. |
| relevance | 0.50 | Useful for anti-conflation and future bridge review. |
| canonical_readiness | 0.00 | Not ready. |

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada row, with child `Jose del Carmen Segundo Pulgar Arriagada`. | 0.74 | Targeted conversion QA must certify row control against the source image, converted file, and chunk. |
| 2 | Conditional parent-child claim: child of `Jose del Carmen Pulgar`/possible `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. | 0.62 | After row QA, proof review must certify father field and mother field before relationship promotion. |
| 3 | Entry 172 is the Burgos/de la Cruz row from current converted Markdown. | 0.20 | QA must explain and resolve why converted Markdown conflicts with assigned chunk/source-packet image review. |
| 4 | Entry 172 helps bridge to `Dario Arturo Pulgar-Smith` or `Dario Arturo Pulgar`. | 0.07 | Requires separate identity-bridge proof review using records that explicitly connect the Dario identity to this Jose/Juana/Pulgar-Arriagada cluster. |
| 5 | Entry 172 person is same as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Darío Pulgar Arriagada`. | 0.04 | Preserve as separate or unresolved; do not merge without explicit name, date, place, parent, or relationship bridge evidence. |

## Conflict Types

- Same-person conflict: no same-person conclusion is supported between entry-172 persons and any Dario identity.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` versus a possible `Jose del Carmen Pulgar S.` candidate; high if father suffix is ignored.
- Name-variant conflict: `Juana Arriagada de Pulgar` is not proven to be a variant of `Juana de Dios Amagada de Pulgar`; `Jose del Carmen Segundo Pulgar Arriagada` is not a Dario name variant.
- Relationship conflict: parent-child claims are blocked by row-control conflict and father-field uncertainty.
- Chronology conflict: no direct chronology conflict is proven, but any linkage from an 1888 birth row to 1918/1929/2000 Dario Pulgar-Arriagada clusters would require exact bridge evidence.

## Recommended Next Action

Keep all entry-172 Pulgar/Arriagada claims on hold. The exact next proof-review step is targeted conversion QA for `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, comparing the row numbered 172 against the current converted Markdown and the assigned chunk, and certifying the father field as only one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review for the child identity and parent-child relationships. Only after those steps should a separate identity-bridge review compare this Jose/Juana/Pulgar-Arriagada cluster with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, and `Dario/Darío Pulgar Arriagada`.
