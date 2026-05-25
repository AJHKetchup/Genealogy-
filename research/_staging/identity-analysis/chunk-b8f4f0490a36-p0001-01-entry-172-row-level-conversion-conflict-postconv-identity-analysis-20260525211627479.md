---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525211541369
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
created: 2026-05-25
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The assigned converted Markdown and assigned chunk disagree at the row level for entry 172. The converted file records `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the chunk and source packet record `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- This is not a same-person spelling variation. It is an incompatible child/parent cluster conflict for the same entry number and source assignment.
- The source packet reports image-review support for the Pulgar/Arriagada row, but this identity analysis does not correct the converted Markdown or promote claims. The controlling row still needs targeted conversion QA.
- Father-field normalization is not settled. The held literal field is `Jose del Carmen Pulgar S.`; possible normalized readings are `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Existing canonical stubs already contain some claims from the Pulgar/Arriagada reading, but those pages do not remove the current conversion blocker. They should be treated as context pending proof review, not as independent confirmation.
- No current evidence in this assigned draft proves an identity bridge to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío/Dario Pulgar Arriagada`.

## Evidence Boundary

Literal evidence from the assigned chunk:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at `tres de la tarde`, place `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.`; Chilean; occupation `Empleado`; domicile `Calle de Colipí`.
- Mother field: `Juana Arriagada de Pulgar`; Chilean; profession/status `Su sexo`; domicile `Calle de Colipí`.
- Compareciente: `Ernesto Herrera L.`, present at birth, age twenty-six, employee, domicile `Calle de Valdivia`.

Literal evidence from the assigned converted Markdown:

- Entry number: `172`.
- Child: `José Miguel`; sex `Varon`.
- Birth date/place: `El seis de Abril de mil ochocientos ochenta i ocho`, `a las diez de la noche`, `En esta`.
- Father: `Oswaldo Burgos`; mother: `Concepcion de la Cruz`.
- Compareciente: `Oswaldo Burgos`.

Interpretation:

- The two derivative readings cannot both be the same entry 172 family. The Pulgar/Arriagada row and Burgos/de la Cruz row differ on child name, birth date, birth place, father, mother, compareciente, domicile, and surrounding page context.
- If targeted conversion QA accepts the chunk/source-packet reading, the Jose/Juana parent-child claims become strong register evidence, subject to father-field suffix QA.
- If targeted conversion QA accepts the converted Markdown reading, the Pulgar/Arriagada claims for this source assignment should be rejected or reassigned to the correct source/chunk before any identity work continues.

## Hypotheses

### 1. Entry 172 Is The Pulgar/Arriagada Birth Row

Hypothesis: the controlling entry 172 row records child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.

Supporting evidence:

- The assigned chunk gives a complete row-level transcription for entry 172 on page 58 with the Pulgar/Arriagada family.
- The source packet says direct image context supports the Pulgar/Arriagada row rather than the Burgos/de la Cruz row.
- Existing canonical stubs for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` already reflect held/probable evidence from this chunk family, showing this is an already tracked local identity cluster.

Conflicts:

- The assigned converted Markdown directly contradicts this row with a Burgos/de la Cruz family.
- The father suffix `S.` remains unresolved and should not be silently dropped.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Strong if the chunk/source-packet row controls, but row assignment is unresolved. |
| conflict_severity | 0.95 | Full child/parent cluster conflict. |
| evidence_quality | 0.78 | Civil birth register row is high-quality evidence, but current evidence is derivative and blocked by conversion disagreement. |
| conversion_confidence | 0.35 | Source packet explicitly marks conversion confidence low because derivative outputs conflict. |
| claim_probability | 0.68 | More likely than the converted-file reading based on chunk plus image-review note, but not ready to promote. |
| relevance | 0.90 | Directly relevant to Pulgar/Arriagada parent-child identity work. |
| canonical_readiness | 0.20 | Hold until conversion QA and proof review. |

### 2. Entry 172 Is The Burgos/de la Cruz Birth Row

Hypothesis: the controlling entry 172 row records child `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.

Supporting evidence:

- The assigned converted Markdown explicitly records entry 172 with the Burgos/de la Cruz family.

Conflicts:

- The assigned chunk and source packet both reject this as the controlling row for the source assignment.
- The source packet reports image-review support for the Pulgar/Arriagada row.
- This hypothesis has no Pulgar-line relevance unless conversion QA later shows the converted Markdown is correct and the Pulgar/Arriagada row belongs elsewhere.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.30 | Supported by one derivative file only. |
| conflict_severity | 0.95 | Mutually exclusive family cluster with the chunk/source packet. |
| evidence_quality | 0.40 | Derivative converted Markdown conflicts with the chunk and image-review note. |
| conversion_confidence | 0.35 | Overall conversion confidence remains low. |
| claim_probability | 0.25 | Possible, but currently weaker than the Pulgar/Arriagada hypothesis. |
| relevance | 0.15 | Low Pulgar-line relevance unless QA reverses the assignment. |
| canonical_readiness | 0.05 | Not ready for canonical use from this conflicted packet. |

### 3. Existing Jose/Juana Parent Candidate Cluster

Hypothesis: if the Pulgar/Arriagada row is confirmed, the child and parents may correspond to existing canonical stubs `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`.

Supporting evidence:

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has the same preferred child name and already cites staged claims/source packet material from this chunk family.
- `wiki/people/juana-arriagada-de-pulgar.md` has the same preferred mother name and an evidence snapshot naming `Jose del Carmen Segundo Pulgar Arriagada` as probable child.
- `wiki/people/jose-del-carmen-pulgar.md` exists as a separate stub and may be the normalized father candidate if `Jose del Carmen Pulgar S.` is accepted as this person.

Conflicts and cautions:

- The father field in this assigned row includes `S.`; the canonical stub uses `Jose del Carmen Pulgar` without the suffix.
- A separate existing page, `wiki/people/tulio-cesar-luis-jose.md`, contains draft parent links to `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` from a different entry 513 context. That does not prove the same parents here.
- `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` should not be silently merged or corrected by surname similarity.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Existing stubs align with the Pulgar/Arriagada reading, but the row itself remains blocked. |
| conflict_severity | 0.70 | Moderate-to-high risk of duplicate/variant confusion among Jose/Juana parent candidates. |
| evidence_quality | 0.66 | Canonical stubs are auto-generated/held context, not independent proof. |
| conversion_confidence | 0.35 | Inherits row-level conversion blocker. |
| claim_probability | 0.58 | Plausible after QA, not currently promotable. |
| relevance | 0.95 | Directly relevant to the named Pulgar/Arriagada family cluster. |
| canonical_readiness | 0.18 | Existing pages should remain held/probable until QA and proof review settle the row. |

### 4. Connection To Dario Arturo Pulgar-Smith Or Document-Level Dario Arturo Pulgar

Hypothesis: this 1888 Pulgar/Arriagada birth row may be relevant to the broader Pulgar line that includes canonical `Dario Arturo Pulgar-Smith` or staged CV subject `Dario Arturo Pulgar`.

Supporting evidence:

- The surnames `Pulgar` and `Arriagada` are locally relevant to Pulgar-line work.
- Canonical `Dario Arturo Pulgar-Smith` exists as a family-supplied maternal-grandfather profile and explicitly warns against automatic merging of similarly named Dario/Pulgar/Pulgar-Arriagada records.
- Staged CV materials elsewhere use document-level `Dario Arturo Pulgar`, but those materials require their own identity bridge to `Dario Arturo Pulgar-Smith`.

Conflicts and cautions:

- This assigned draft names no `Dario`, `Arturo`, `Smith`, grandchild, spouse, descendant, CV, occupation continuity, or later-life bridge.
- A birth for `Jose del Carmen Segundo Pulgar Arriagada` in 1888 cannot be treated as Dario Arturo Pulgar-Smith or Dario Arturo Pulgar by name or surname context alone.
- Family-context hints justify a future double-check, not a silent correction or merge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | No direct Dario identity evidence in this entry. |
| conflict_severity | 0.75 | High risk if used to force a Pulgar-line ancestry bridge. |
| evidence_quality | 0.25 | Only surname/context relevance, no direct bridge. |
| conversion_confidence | 0.35 | Underlying row still blocked. |
| claim_probability | 0.08 | Possible future lineage relevance only. |
| relevance | 0.45 | Relevant as a review lead, not as proof. |
| canonical_readiness | 0.00 | Not ready for any Dario canonical attachment. |

### 5. Connection To Dario Jose Pulgar-Arriagada, Darío/Dario Pulgar Arriagada, Or Dario Pulgar A.

Hypothesis: the confirmed Pulgar/Arriagada family may eventually connect to separate Pulgar-Arriagada identity clusters such as `Dario Jose Pulgar-Arriagada`, canonical `Darío Pulgar Arriagada`, or `Dario Pulgar A.`.

Supporting evidence:

- Existing local context includes `Darío Pulgar Arriagada` as a canonical stub with a 2000 expropriation event.
- Existing staged/proof-review notes elsewhere preserve `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar A.`, and similar forms as unresolved Pulgar-line candidates.
- The surname pair `Pulgar Arriagada` overlaps with the child name in the chunk reading.

Conflicts and cautions:

- The assigned entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.
- No vital-date continuity, parentage bridge, profession, property, spouse, or later-life event links this 1888 child to any Dario candidate.
- Do not merge `Jose del Carmen Segundo Pulgar Arriagada` with any Dario candidate by surname pattern alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No direct same-person evidence. |
| conflict_severity | 0.80 | Very high conflation risk if surname overlap is overused. |
| evidence_quality | 0.20 | Context-only comparison. |
| conversion_confidence | 0.35 | Underlying row still blocked. |
| claim_probability | 0.04 | Preserve only as anti-conflation review context. |
| relevance | 0.40 | Relevant because the assignment requires Pulgar-line comparison. |
| canonical_readiness | 0.00 | Not ready for canonical attachment or merge. |

## Conflict Summary

- Same-person conflict: none proved. The evidence does not prove any same-person relationship between the entry 172 child and any Dario candidate.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar S.` versus existing `Jose del Carmen Pulgar`; moderate for `Juana Arriagada de Pulgar` versus similarly named/nearby Juana candidates; high if any Dario cluster is merged from this entry.
- Name-variant conflict: `Jose del Carmen Pulgar S.` cannot be normalized to `Jose del Carmen Pulgar` without father-field QA; `Juana Arriagada` cannot be corrected to or merged with `Juana de Dios Amagada` without separate proof.
- Relationship conflict: child-parent relationships are blocked by the row-level conflict until targeted conversion QA decides whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row.
- Chronology conflict: no internal chronology problem if the Pulgar/Arriagada row controls; registration on 1888-04-07 for an 1888-03-08 birth is plausible. The converted-file reading has a different 1888-04-06 birth and a different family, creating a row conflict rather than a chronology-only conflict.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth row | 0.68 | Targeted conversion QA against the source image, converted Markdown, chunk, and source packet. |
| 2 | Existing Jose/Juana stubs are the correct local candidates if the Pulgar row controls | 0.58 | After row QA, run proof review for child, father, mother, and relationship claims, including the father suffix. |
| 3 | Entry 172 is the Burgos/de la Cruz birth row | 0.25 | Conversion QA must explain why the chunk/source-packet Pulgar row is not controlling for this source assignment. |
| 4 | The row is a future ancestor-line lead for Dario Arturo Pulgar-Smith / Dario Arturo Pulgar | 0.08 | Require explicit lineage evidence after row QA; then separately bridge `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`. |
| 5 | The row is same-person evidence for Dario Jose Pulgar-Arriagada / Darío Pulgar Arriagada / Dario Pulgar A. | 0.04 | Preserve as anti-conflation context only; require direct continuity evidence before comparison can advance. |

## Recommended Next Action

Keep this conflict and all dependent claims at `hold_for_conversion_qa`. The exact next proof-review/promotion sequence should be:

1. Targeted conversion QA: decide the controlling row for entry 172 by comparing the source image, assigned converted Markdown, assigned chunk, and source packet.
2. Father-field QA: record whether the father reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. If the Pulgar/Arriagada row is confirmed, run proof review for the child identity, birth date/place, father relationship, mother relationship, and parent candidate matching against existing `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada`.
4. Only after that, run a separate Pulgar-line identity bridge review before connecting this family cluster to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío/Dario Pulgar Arriagada`, or `Dario Pulgar A.`.

No canonical merge, page rename, fact promotion, or relationship promotion is ready from this conflicted draft.
