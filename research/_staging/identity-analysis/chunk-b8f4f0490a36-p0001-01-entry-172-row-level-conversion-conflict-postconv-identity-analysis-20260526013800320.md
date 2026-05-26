---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526013800320
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
created: "2026-05-26"
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Row-control blocker: the staged conflict draft reports that the assigned chunk and source-packet image review support a Pulgar/Arriagada row for entry 172, while the current converted Markdown records a Burgos/de la Cruz row for entry 172. This blocks all canonical claims from this entry until targeted conversion QA certifies the controlling row.
2. Father-name blocker: the source packet states that the father field visibly begins `Jose del Carmen Pulgar`, but the trailing mark/suffix is not certified. Keep the father reading unresolved among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
3. Parent-identity blocker: existing canonical context has at least two Jose/Juana candidate clusters: `Jose del Carmen Pulgar` with `Juana de Dios Amagada de Pulgar` as parents of `Tulio Cesar Luis Jose`, and `Juana Arriagada de Pulgar` as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`. Do not merge these by name or surname resemblance.
4. Dario-line blocker: this entry names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. It does not bridge any Dario candidate to the entry-172 child or parents.
5. Canonical-readiness blocker: existing canonical pages already contain generated evidence from this entry, but the current staged draft requires hold-for-conversion-QA. Treat any canonical entry-172 facts as not ready for promotion or merge decisions until QA and proof review are rerun.

## Literal Evidence

From the exact staged draft:

- Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; birth `8 March 1888`, about 3 p.m., `Calle de Valdivia`; father visible start `Jose del Carmen Pulgar`; chunk reads `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at birth.
- Current converted Markdown reading: child `Jose Miguel`; birth `6 April 1888`, about 10 p.m., `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.
- Required resolution in the staged draft: targeted conversion QA must decide the controlling row and certify the father field only to visible extent.

From the referenced source packet:

- Source packet title: `Entry 172 Pulgar/Arriagada Birth Register`.
- Source packet says the assigned chunk is highly relevant to the Pulgar/Arriagada family only if certified.
- Source packet records image-reviewed evidence that the row numbered 172 on register page 58 is a Pulgar/Arriagada row, not the Burgos/de la Cruz row in the current converted Markdown.
- Source packet recommends `hold_for_conversion_qa` and explicitly says not to promote child identity, birth facts, parent names, parent-child relationships, parent merges, or Dario-line comparisons until targeted conversion QA and proof review are complete.

From the referenced chunk:

- Entry 172 appears as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at Calle de Valdivia.
- The same row reads father `Jose del Carmen Pulgar S.`, Chilean, employee, resident at Calle de Colipi, and mother `Juana Arriagada de Pulgar`, Chilean, profession `Su sexo`, resident at Calle de Colipi.
- The informant is `Ernesto Herrera L.`, present at birth, age 26, employee, resident at Calle de Valdivia.

From the current converted Markdown:

- Entry 172 instead appears as `Jose Miguel`, male, born 6 April 1888 at 10 p.m. at `En esta`, with father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

## Interpretation Guardrails

- The chunk/source-packet reading and the converted-file reading cannot both describe the same row-level facts for entry 172.
- The Pulgar/Arriagada reading is stronger for family relevance, but the conversion conflict means it is not yet canonical-ready.
- Family-context hints justify a targeted double-check of Pulgar-line identity, but do not justify silently changing the converted record, attaching facts to Dario candidates, or merging Jose/Juana candidates.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Hypothesis: the controlling row for entry 172 is the Pulgar/Arriagada row naming child `Jose del Carmen Segundo Pulgar Arriagada`, father beginning `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.

Supporting evidence:

- The assigned chunk transcribes entry 172 as the Pulgar/Arriagada row.
- The source packet reports image-reviewed support for the Pulgar/Arriagada row on register page 58.
- The staged draft says the assigned chunk and source image support the Pulgar/Arriagada row.

Conflicts and limits:

- The current converted Markdown records a different entry-172 row: Burgos/de la Cruz.
- The father suffix after `Jose del Carmen Pulgar` is not certified.
- This hypothesis supports an entry-level identity candidate for `Jose del Carmen Segundo Pulgar Arriagada`, not a Dario-line merge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong chunk/source-packet support for this row, reduced by unresolved converted-file conflict. |
| conflict_severity | 0.95 | Row-control conflict changes child, parents, date, place, and informant. |
| evidence_quality | 0.82 | Civil birth-register evidence with image-reviewed source packet, but QA not completed. |
| conversion_confidence | 0.45 | Assigned chunk is strong, current converted Markdown is materially contradictory. |
| claim_probability | 0.74 | Probable as the correct row, but held pending targeted QA. |
| relevance | 0.92 | Directly relevant to Pulgar/Arriagada family candidates and parentage. |
| canonical_readiness | 0.10 | Not ready until conversion QA and proof review rerun. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Hypothesis: the current converted Markdown correctly controls entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Supporting evidence:

- The current converted Markdown records entry 172 in this form.

Conflicts and limits:

- The staged conflict draft directly rejects this as inconsistent with the assigned chunk and source image.
- The source packet says visual review supports the Pulgar/Arriagada row, not the Burgos/de la Cruz row.
- This hypothesis has no Pulgar-line relevance if accepted.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Supported only by the current converted Markdown against chunk/source-packet image review. |
| conflict_severity | 0.95 | Same row-control conflict as Hypothesis 1. |
| evidence_quality | 0.35 | Converted text is useful as conflict evidence, not reliable as controlling evidence here. |
| conversion_confidence | 0.20 | The converted-file row appears materially mismatched to the assigned chunk/source packet. |
| claim_probability | 0.18 | Unlikely on current local evidence, but not discarded until QA resolves row control. |
| relevance | 0.05 | Minimal to Pulgar-line identity if this row controls. |
| canonical_readiness | 0.05 | Not ready; contradicted by staged QA evidence. |

## Hypothesis 3: Child Is Same Person As An Existing Dario Candidate

Hypothesis: `Jose del Carmen Segundo Pulgar Arriagada` from the Pulgar/Arriagada row is the same person as one of the Dario candidates: `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

Supporting evidence:

- The child shares the surname elements `Pulgar Arriagada` with some Pulgar-Arriagada contexts.
- Local canonical and staged context contains multiple Dario/Pulgar/Pulgar-Arriagada identity clusters, so this entry is relevant as an anti-conflation checkpoint.

Conflicts and limits:

- The entry-172 child is named `Jose del Carmen Segundo`, not Dario.
- The entry does not state `Arturo`, `Smith`, `Dario Jose`, `Dario J.`, `Dario Pulgar A.`, or any relationship to Alexander John Heinz.
- `Dario Arturo Pulgar-Smith` is represented by family-supplied canonical knowledge as Alexander John Heinz's maternal grandfather and explicitly requires identity review before attaching Dario/Pulgar/Pulgar-Arriagada records.
- `Dario Arturo Pulgar` is currently a document-level CV subject in other staged materials and still requires an identity bridge to `Dario Arturo Pulgar-Smith`.
- `Dario Jose Pulgar-Arriagada` appears in local staged image/metadata contexts that require source/image identity QA and are not bridged here.
- Canonical `Dario Pulgar Arriagada` is tied to a 5 December 2000 Chiguayante expropriation notice, with no bridge from this 1888 birth entry.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Name/surname overlap only; given names and proof context do not match. |
| conflict_severity | 0.70 | A premature merge would contaminate several Pulgar-line clusters. |
| evidence_quality | 0.40 | The birth entry may be good evidence after QA, but it is poor evidence for a Dario identity. |
| conversion_confidence | 0.45 | Still affected by row-control conflict. |
| claim_probability | 0.05 | Very low that this entry alone proves same-person identity with any Dario candidate. |
| relevance | 0.65 | Relevant chiefly as an anti-conflation checkpoint. |
| canonical_readiness | 0.00 | No Dario attachment should be promoted from this entry. |

## Hypothesis 4: Jose/Juana Parent Candidates Are Duplicates Or Variants

Hypothesis: `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` from this entry may overlap with existing canonical parent candidates such as `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar`.

Supporting evidence:

- Existing canonical `Jose del Carmen Pulgar` has a draft parent relationship to `Tulio Cesar Luis Jose`.
- Existing canonical `Juana Arriagada de Pulgar` has a probable child relationship to `Jose del Carmen Segundo Pulgar Arriagada`.
- Existing canonical `Juana de Dios Amagada de Pulgar` has a draft child relationship to `Tulio Cesar Luis Jose`.
- The names `Arriagada` and `Amagada` are close enough to require deliberate QA, especially in handwritten Spanish-register contexts.

Conflicts and limits:

- This staged draft does not mention `Tulio Cesar Luis Jose`.
- This staged draft does not prove that `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person.
- This staged draft does not prove that the father of entry-172 child and the father of Tulio are the same `Jose del Carmen Pulgar`.
- The father suffix in entry 172 is not certified.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.36 | Plausible family/name overlap, but no direct bridge within this staged draft. |
| conflict_severity | 0.80 | Parent-merge error would affect multiple child-parent relationships. |
| evidence_quality | 0.55 | Local canonical snapshots exist, but entry-172 evidence is still held. |
| conversion_confidence | 0.45 | Affected by row-control and father-suffix uncertainty. |
| claim_probability | 0.30 | Possible, not probable, pending QA and proof review across both child-parent clusters. |
| relevance | 0.85 | Directly relevant to Pulgar/Arriagada parentage. |
| canonical_readiness | 0.05 | Not ready for merge, rename, or relationship promotion. |

## Conflict Summary

- Same-person conflict: unresolved; this draft does not prove same-person identity between `Jose del Carmen Segundo Pulgar Arriagada` and any Dario candidate.
- Duplicate-person conflict: unresolved for Jose/Juana parent candidates; preserve `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` separately until a proof-reviewed bridge exists.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` remain unresolved father readings; `Arriagada` versus `Amagada` remains an anti-conflation watch, not a correction.
- Relationship conflict: the Pulgar/Arriagada row would support a child-parent relationship for Jose del Carmen Segundo, Jose del Carmen Pulgar, and Juana Arriagada de Pulgar, but the current converted Markdown supports a different child-parent set. This blocks all entry-172 relationship promotion.
- Chronology conflict: Pulgar/Arriagada row gives birth on 8 March 1888 and registration on 7 April 1888; converted Burgos/de la Cruz row gives birth on 6 April 1888 and registration on 7 April 1888. This is a row-control conflict, not a mere date variant.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Disposition |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada` | 0.74 | Hold for targeted conversion QA; likely but not canonical-ready. |
| 2 | Jose/Juana parent candidates may include duplicate or name-variant clusters | 0.30 | Preserve as unresolved; compare only after row QA and separate proof review. |
| 3 | Entry 172 is the Burgos/de la Cruz row from current converted Markdown | 0.18 | Treat as competing conversion reading until QA resolves. |
| 4 | Entry-172 child is same person as a Dario candidate | 0.05 | Reject for promotion; keep only as anti-conflation checkpoint. |

## Recommended Next Action

Run targeted conversion QA on `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, the current converted Markdown, and `CHUNK-b8f4f0490a36-P0001-01` to certify the controlling row for entry 172 and the father field reading. The exact proof-review step needed next is a row-control proof review that explicitly decides whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, then reruns proof review for child name, birth facts, father, mother, and informant.

After row-control QA passes, perform a separate parent-identity proof review comparing `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` against the existing child-parent clusters. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` unless a later identity-bearing source explicitly bridges those persons.
