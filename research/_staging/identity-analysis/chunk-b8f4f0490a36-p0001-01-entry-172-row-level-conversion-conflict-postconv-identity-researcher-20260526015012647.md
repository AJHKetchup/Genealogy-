---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: "postconv-identity-analysis-20260526014917329"
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
created: "2026-05-26"
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers

1. Exact staged draft analyzed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md`.
2. Row control is unresolved. The assigned chunk and staged source packet present entry 172 as a Pulgar/Arriagada row, while the current converted Markdown presents entry 172 as a Burgos/de la Cruz row.
3. This is a material identity and relationship conflict, not a name-variant issue. The disagreement changes child identity, parent identities, birth date/time/place, residence, and informant.
4. The father field is not promotion-ready. The next QA step must certify the visible reading as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
5. Existing wiki pages preserve related Jose/Juana/Pulgar/Dario clusters, but this note does not authorize merges, renames, canonical relationship promotion, or fact strengthening.
6. No external research was performed. Raw sources, converted Markdown, chunks, and canonical wiki pages were not edited.

## Literal Evidence

Pulgar/Arriagada reading from the staged draft, source packet, and assigned chunk:

- Entry: 172, registered 7 April 1888.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: 8 March 1888, about 3 p.m., `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the assigned chunk, with suffix still requiring QA.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth.

Burgos/de la Cruz reading from the current converted Markdown:

- Entry: 172, registered 7 April 1888.
- Child: `Jose Miguel`.
- Birth: 6 April 1888, about 10 p.m., `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

Existing wiki context reviewed:

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` contains generated entry-172 facts and a probable mother link to `Juana Arriagada de Pulgar`.
- `wiki/people/juana-arriagada-de-pulgar.md` preserves the probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- `wiki/people/jose-del-carmen-pulgar.md` preserves a separate child link to `Tulio Cesar Luis Jose`.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` preserves a separate child link to `Tulio Cesar Luis Jose`.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should attach only after identity review.
- `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/dario-pulgar-adult-passenger-age-64.md`, and `wiki/people/dario-pulgar-child-passenger-age-11.md` preserve separate Dario/Pulgar clusters.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Evidence supporting:

- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The staged source packet states the assigned chunk is highly relevant to the Pulgar/Arriagada family and identifies the current converted Markdown as the conflicting side.
- Prior local proof-review context for this row keeps the Pulgar/Arriagada reading as likely but held for targeted conversion QA.

Conflicts and limits:

- The current converted Markdown assigns the same entry number to `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The father suffix after `Jose del Carmen Pulgar` remains uncertified.
- Even if confirmed, this row supports a Jose del Carmen Segundo birth entry, not a Dario identity.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong staged chunk/source-packet support, reduced by row-control conflict. |
| conflict_severity | 0.95 | Competing rows identify different children, parents, dates, places, and informants. |
| evidence_quality | 0.82 | Civil birth-register evidence is strong, but derivative outputs disagree. |
| conversion_confidence | 0.45 | Chunk is coherent; converted Markdown materially conflicts. |
| claim_probability | 0.74 | Likely on current staged evidence, but not promotable. |
| relevance | 0.94 | Directly relevant to Pulgar/Arriagada only if QA confirms it. |
| canonical_readiness | 0.10 | Hold for conversion QA and rerun proof review. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Row

Evidence supporting:

- The current converted Markdown explicitly records entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Conflicts and limits:

- The assigned chunk and staged source packet present a different row for the same entry number.
- The staged conflict draft treats the converted Markdown row as the conflict side.
- If this hypothesis controls, the staged Pulgar/Arriagada evidence is not usable for entry 172.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Supported by one derivative conversion against the staged chunk/source packet. |
| conflict_severity | 0.95 | Acceptance would invalidate staged Pulgar entry-172 family claims. |
| evidence_quality | 0.35 | Useful conflict evidence, weak controlling evidence until QA. |
| conversion_confidence | 0.20 | Current converted file appears mismatched to the staged row. |
| claim_probability | 0.18 | Possible until row-control QA, but weak on current local evidence. |
| relevance | 0.05 | No Pulgar-line relevance if accepted. |
| canonical_readiness | 0.05 | Not ready for promotion. |

## Hypothesis 3: Jose/Juana Parent Candidates Are Duplicates Or Name Variants

Evidence supporting:

- The Pulgar-side row names father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing wiki context has `Jose del Carmen Pulgar` as a separate stub.
- Existing wiki context has both `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`, requiring an anti-conflation check.

Conflicts and limits:

- This staged draft does not mention `Tulio Cesar Luis Jose`, the separate child cluster linked to `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar`.
- This staged draft does not prove `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person.
- Row control and father suffix must be resolved before any parent identity review can be decisive.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.36 | Parent-name overlap exists, but no direct bridge in this draft. |
| conflict_severity | 0.80 | Mistaken parent merges would affect multiple child-parent clusters. |
| evidence_quality | 0.55 | Local wiki context is relevant but dependent on held register evidence. |
| conversion_confidence | 0.45 | Still blocked by row-control and father-field uncertainty. |
| claim_probability | 0.30 | Possible, not probable, pending separate proof review. |
| relevance | 0.86 | Directly relevant to the Pulgar/Arriagada parent question. |
| canonical_readiness | 0.05 | No merge, rename, or relationship promotion supported. |

## Hypothesis 4: Entry-172 Child Is Same Person As A Dario Candidate

Evidence supporting:

- If confirmed, the child would share the `Pulgar Arriagada` surname pattern with some Dario/Pulgar-Arriagada contexts.
- Existing wiki/staged context includes multiple Dario/Pulgar clusters, so comparison is required before any Pulgar-line attachment.

Required Pulgar-line comparison:

- `Dario Arturo Pulgar-Smith`: this entry does not name Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, or a family relationship to the family-supplied canonical page.
- `Dario Arturo Pulgar`: this entry does not name Dario Arturo Pulgar or provide a CV/document-subject bridge.
- `Dario Jose Pulgar-Arriagada`: this entry does not name Dario Jose. The given names `Jose del Carmen Segundo` cannot be normalized into `Dario Jose` without independent proof.
- `Dario/Dario Pulgar Arriagada` and `Darío Pulgar Arriagada`: existing local context preserves these as separate Dario/Pulgar clusters; this draft supplies no bridge.
- Passenger-list `Dario Pulgar` adult age 64 in 1953 is only a chronology hint for later review because an 1888 birth could be near age 64 in 1953; name and source context differ, and the entry-172 row is not certified.
- Passenger-list `Dario Pulgar` child age 11 in 1953 is chronologically incompatible with an 1888 birth child and should remain separate.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Surname overlap only; given names and context do not bridge. |
| conflict_severity | 0.70 | Name-only merge would contaminate separate Dario and Jose clusters. |
| evidence_quality | 0.40 | The birth row may become good evidence for Jose, not for Dario identity. |
| conversion_confidence | 0.45 | Row-control conflict still applies. |
| claim_probability | 0.05 | This entry does not prove same-person identity with any Dario candidate. |
| relevance | 0.68 | Relevant mainly as an anti-conflation checkpoint. |
| canonical_readiness | 0.00 | No Dario attachment or merge supported. |

## Conflicts

- Same-person conflict: unresolved. The staged evidence does not prove `Jose del Carmen Segundo Pulgar Arriagada` is the same person as any Dario candidate.
- Duplicate-person conflict: unresolved for Jose/Juana parent candidates. Keep `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` separate until a reviewed bridge exists.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` remain possible father readings; `Arriagada` versus `Amagada` remains a review issue, not a silent correction.
- Relationship conflict: the Pulgar/Arriagada row would support one child-parent set; the Burgos/de la Cruz row supports a completely different child-parent set.
- Chronology conflict: the Pulgar/Arriagada row gives birth on 1888-03-08 and registration on 1888-04-07; the Burgos/de la Cruz row gives birth on 1888-04-06 and registration on 1888-04-07.
- Canonical conflict: existing generated wiki evidence for entry-172 Pulgar facts should not be strengthened from this draft while the current staged recommendation remains `hold_for_conversion_qa`.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Disposition |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.74 | Hold for targeted conversion QA; likely but not canonical-ready. |
| 2 | Jose/Juana parent candidates may include duplicate or variant clusters. | 0.30 | Preserve as unresolved; compare only after row QA. |
| 3 | Entry 172 is the Burgos/de la Cruz row from current converted Markdown. | 0.18 | Treat as competing conversion reading until QA resolves. |
| 4 | Entry-172 child is same person as any Dario candidate. | 0.05 | Do not promote; use only as anti-conflation context. |

## Recommended Next Action

Run targeted conversion QA on the source image, current converted Markdown, assigned chunk, and staged source packet to certify the controlling row for entry 172 and the father field reading. The exact next proof-review step is row-control proof review that decides whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, then reruns proof review for the child name, birth facts, father, mother, informant, and any parent-child relationships.

After row-control QA passes, run a separate parent-identity proof review comparing `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` against existing child-parent clusters. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or `Darío Pulgar Arriagada` unless a later identity-bearing source explicitly bridges those persons.
