---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: "postconv-identity-analysis-20260526014144513"
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

## Blockers

1. Row-control blocker: the exact staged draft reports that the assigned chunk and source image support a Pulgar/Arriagada row for entry 172, while the current converted Markdown records a Burgos/de la Cruz row for the same entry number.
2. Conversion-confidence blocker: the referenced converted file and referenced chunk cannot both be treated as controlling for entry 172 without targeted conversion QA. This blocks canonical birth, parent, residence, informant, and relationship claims from this draft.
3. Father-field blocker: the staged draft and source packet say the Pulgar father field visibly begins `Jose del Carmen Pulgar`, while the chunk reads `Jose del Carmen Pulgar S.`. Certify only one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` after image QA.
4. Jose/Juana parent-candidate blocker: existing wiki context has separate `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` pages or clusters. This draft does not prove those are duplicates or variants.
5. Dario-line blocker: this draft does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío/Dario Pulgar Arriagada`. Any Dario comparison is an anti-conflation check only.
6. Canonical-readiness blocker: existing wiki pages already contain generated entry-172 Pulgar/Arriagada facts, but this later staged draft places the row on hold for conversion QA. Do not strengthen, merge, rename, or promote those facts from this analysis.

## Literal Evidence Reviewed

From the exact staged draft:

- Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; birth `8 March 1888`, about 3 p.m., `Calle de Valdivia`; father visible start `Jose del Carmen Pulgar`; chunk reads `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at birth.
- Converted Markdown reading: child `Jose Miguel`; birth `6 April 1888`, about 10 p.m., `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.
- Required resolution: targeted conversion QA must decide the controlling row and certify the father field only to the visible extent.

From the referenced source packet:

- The assigned chunk is described as highly relevant to the Pulgar/Arriagada family only if certified.
- Image-reviewed evidence in the packet says row 172 on register page 58 is a Pulgar/Arriagada row, not the Burgos/de la Cruz row in the current converted Markdown.
- The packet recommends `hold_for_conversion_qa` and says not to promote child identity, birth facts, parent names, parent-child relationships, parent merges, or Dario-line comparisons until targeted conversion QA and proof review are complete.

From the referenced chunk:

- Entry 172 is transcribed as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at Calle de Valdivia.
- Father is transcribed as `Jose del Carmen Pulgar S.`, Chilean, employee, resident at Calle de Colipi.
- Mother is transcribed as `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident at Calle de Colipi.
- Informant is transcribed as `Ernesto Herrera L.`, present at birth, age 26, employee, resident at Calle de Valdivia.

From the current converted Markdown:

- Entry 172 is transcribed instead as `Jose Miguel`, male, born 6 April 1888 at 10 p.m. at `En esta`, with father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

## Existing Wiki Context

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` contains generated life facts and a probable mother link derived from the entry-172 Pulgar/Arriagada cluster.
- `wiki/people/juana-arriagada-de-pulgar.md` contains a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` and mother-attribute facts from the same cluster.
- `wiki/people/jose-del-carmen-pulgar.md` exists as a separate stub and has a draft child link to `Tulio Cesar Luis Jose` from another relationship cluster.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` exists as a separate stub and has a draft child link to `Tulio Cesar Luis Jose`.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records require identity review before attachment.
- `wiki/people/dar-o-pulgar-arriagada.md` is a separate canonical stub tied to a 5 December 2000 Chiguayante expropriation resolution.
- `wiki/people/dario-pulgar-adult-passenger-age-64.md` and `wiki/people/dario-pulgar-child-passenger-age-11.md` are separate passenger-list clusters with no bridge supplied by this draft.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Hypothesis: the controlling row for entry 172 is the Pulgar/Arriagada row naming child `Jose del Carmen Segundo Pulgar Arriagada`, father beginning `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.

Evidence supporting:

- The assigned chunk transcribes entry 172 as the Pulgar/Arriagada row.
- The source packet reports image-reviewed support for the Pulgar/Arriagada row on register page 58.
- The staged draft states that the assigned chunk and source image support a Pulgar/Arriagada row.

Conflicts and limits:

- The current converted Markdown records a different entry-172 row for `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The final father suffix or mark after `Jose del Carmen Pulgar` is not certified.
- This hypothesis supports an entry-level identity candidate for `Jose del Carmen Segundo Pulgar Arriagada`; it does not prove any Dario-line identity.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong chunk/source-packet support for this row, reduced by unresolved converted-file contradiction. |
| conflict_severity | 0.95 | The conflict changes child, parents, date, place, residence, and informant. |
| evidence_quality | 0.82 | Civil birth-register evidence and image-reviewed packet are strong, but QA has not resolved the row-control disagreement. |
| conversion_confidence | 0.45 | The assigned chunk is coherent, but the current converted Markdown is materially contradictory. |
| claim_probability | 0.74 | Probable as the correct row on current local evidence, but not promotable. |
| relevance | 0.92 | Directly relevant to Pulgar/Arriagada parentage if certified. |
| canonical_readiness | 0.10 | Hold until conversion QA and proof review rerun. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Hypothesis: the current converted Markdown controls entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Evidence supporting:

- The current converted Markdown explicitly records entry 172 in this form.

Conflicts and limits:

- The staged draft states that the assigned chunk and source image support the Pulgar/Arriagada row instead.
- The source packet says visual review supports the Pulgar/Arriagada row, not the Burgos/de la Cruz row.
- This hypothesis has no Pulgar-line relevance if accepted.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Supported only by current converted Markdown against source-packet/chunk review. |
| conflict_severity | 0.95 | Same row-control conflict; acceptance would overturn all Pulgar entry-172 facts. |
| evidence_quality | 0.35 | Useful as conflict evidence, weak as controlling evidence against the staged packet. |
| conversion_confidence | 0.20 | The converted row appears mismatched to the assigned chunk/source packet. |
| claim_probability | 0.18 | Possible until QA resolves the row, but unlikely on current local evidence. |
| relevance | 0.05 | Minimal relevance to Pulgar-line research. |
| canonical_readiness | 0.05 | Contradicted by staged QA evidence and not ready for promotion. |

## Hypothesis 3: Jose/Juana Parent Candidates Are Duplicates Or Variants

Hypothesis: the entry-172 father/mother candidates may overlap with existing Jose/Juana parent candidates in the wiki or staged record clusters.

Evidence supporting:

- Entry-172 Pulgar reading names father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing wiki context includes `Jose del Carmen Pulgar` as a separate person stub.
- Existing wiki context includes both `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`, making `Arriagada` versus `Amagada` a legitimate identity-watch issue.

Conflicts and limits:

- This staged draft does not mention `Tulio Cesar Luis Jose`, the other child cluster connected to `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar`.
- This staged draft does not prove that `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person.
- The father suffix and row control are still unresolved.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.36 | Plausible parent-name overlap, but no direct bridge in this draft. |
| conflict_severity | 0.80 | A mistaken parent merge would affect multiple child-parent clusters. |
| evidence_quality | 0.55 | Local wiki context is relevant, but entry-172 evidence is currently held. |
| conversion_confidence | 0.45 | Still affected by row-control and father-field uncertainty. |
| claim_probability | 0.30 | Possible, not probable, pending row QA and separate parent-identity proof review. |
| relevance | 0.85 | Directly relevant to Pulgar/Arriagada parentage. |
| canonical_readiness | 0.05 | Not ready for merge, rename, or relationship promotion. |

## Hypothesis 4: Entry-172 Child Is Same Person As A Dario Candidate

Hypothesis: `Jose del Carmen Segundo Pulgar Arriagada` from the Pulgar/Arriagada row is the same person as one of the Dario candidates.

Evidence supporting:

- The child shares `Pulgar Arriagada` surname elements with some Pulgar-Arriagada contexts.
- Local context contains multiple Dario/Pulgar/Pulgar-Arriagada clusters, so this entry is relevant as an anti-conflation checkpoint.

Conflicts and limits:

- `Dario Arturo Pulgar-Smith`: this entry does not name Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, spouse, child, grandchild, or any kinship bridge to the canonical family-supplied page.
- `Dario Arturo Pulgar`: this entry does not name Dario Arturo Pulgar or provide any CV/document-subject bridge.
- `Dario Jose Pulgar-Arriagada`: this entry does not name Dario Jose. The given names `Jose del Carmen Segundo` cannot be converted into `Dario Jose` without independent identity proof.
- `Darío/Dario Pulgar Arriagada`: existing canonical context ties that name to a 2000 expropriation cluster, with no bridge to this 1888 birth entry.
- Passenger-list `Dario Pulgar` adult age 64 in 1953 has a rough chronology that could prompt a later double-check, but this entry names a different child and is not row-control certified.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Surname overlap only; given-name and context bridges are absent. |
| conflict_severity | 0.70 | A premature merge would contaminate Dario, Pulgar-Arriagada, and Jose/Juana clusters. |
| evidence_quality | 0.40 | The birth row may become good evidence after QA, but it is weak evidence for Dario identity. |
| conversion_confidence | 0.45 | The row-control conflict still applies. |
| claim_probability | 0.05 | This entry alone does not prove same-person identity with any Dario candidate. |
| relevance | 0.65 | Relevant mainly to prevent name-only conflation. |
| canonical_readiness | 0.00 | No Dario attachment should be promoted from this draft. |

## Conflict Summary

- Same-person conflict: unresolved; this draft does not prove `Jose del Carmen Segundo Pulgar Arriagada` is the same person as any Dario candidate.
- Duplicate-person conflict: unresolved for Jose/Juana parent candidates; keep `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` separate until reviewed bridge evidence exists.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` remain unresolved father readings; `Arriagada` versus `Amagada` remains an anti-conflation watch, not a silent correction.
- Relationship conflict: the Pulgar/Arriagada row would support one child-parent set; the converted Burgos/de la Cruz row supports a completely different child-parent set.
- Chronology conflict: the Pulgar/Arriagada row gives birth on 8 March 1888 and registration on 7 April 1888; the Burgos/de la Cruz row gives birth on 6 April 1888 and registration on 7 April 1888.
- Place/residence conflict: Pulgar/Arriagada row gives Calle de Valdivia and parent residence Calle de Colipi; Burgos/de la Cruz row gives `En esta` and different parent context.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Disposition |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.74 | Hold for targeted conversion QA; likely but not canonical-ready. |
| 2 | Jose/Juana parent candidates may include duplicate or name-variant clusters. | 0.30 | Preserve as unresolved; compare only after row QA and separate proof review. |
| 3 | Entry 172 is the Burgos/de la Cruz row from current converted Markdown. | 0.18 | Treat as competing conversion reading until QA resolves. |
| 4 | Entry-172 child is same person as a Dario candidate. | 0.05 | Reject for promotion; keep only as anti-conflation checkpoint. |

## Recommended Next Action

Run targeted conversion QA on the source image, current converted Markdown, and `CHUNK-b8f4f0490a36-P0001-01` to certify the controlling row for entry 172 and the father field reading. The exact next proof-review step is a row-control proof review that decides whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, then reruns proof review for child name, birth facts, father, mother, and informant.

After row-control QA passes, run a separate parent-identity proof review comparing `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` against existing child-parent clusters. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío/Dario Pulgar Arriagada` unless a later identity-bearing source explicitly bridges those persons.
