---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525070907893
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Conversion Conflict

## Blockers First

1. Row-level conversion conflict blocks identity promotion. The staged conflict and source packet say the current chunk supports entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`. The assigned converted Markdown instead records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born in `Pellin`.

2. The father field is not proof-ready. Preserve the literal alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA decides the source-visible reading.

3. Existing canonical pages already contain partial auto-generated entry-172 evidence, but this staged draft explicitly requires `hold_for_conversion_qa` for dependent identity, claim, relationship, and parent-candidate drafts.

4. This entry does not name Dario, Arturo, Smith, Dario Jose, Dario Pulgar Arriagada, Alexander John Heinz, or any occupational/passenger/expropriation context. The Pulgar-line comparison is therefore an anti-conflation check, not a bridge.

5. Jose/Juana parent candidates remain unresolved across local Pulgar-line staging. `Juana Arriagada de Pulgar` in this entry must not be silently merged with separate `Juana de Dios Amagada de Pulgar` or `Juana de Dios Amador de Pulgar` readings from entry-513 work.

## Evidence Reviewed

- Staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md`.
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Assigned converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical pages: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/dario-arturo-pulgar-smith.md`, and `wiki/people/dar-o-pulgar-arriagada.md`.

No external research was performed. No raw source, converted Markdown, chunk Markdown, or canonical wiki page was edited.

## Literal Source Readings

Current chunk/source-packet reading:

- Entry: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk; staged draft preserves `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Mother: `Juana Arriagada de Pulgar`.
- Parents' residence: `Calle de Colipi` / `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at the birth.

Assigned converted Markdown reading:

- Entry: `172`.
- Child: `José Francisco`.
- Birth: `En veinte de Febrero ... a las diez de la noche`.
- Birth place: `En Pellin`.
- Father: `Oswaldo Gomez`.
- Mother: `Rosario de la Cruz de la Maza`.
- Informant/declarant: `Oswaldo Gomez`.

Interpretation boundary: these are not minor spelling variants. They are mutually incompatible row readings or file/conversion assignments until conversion QA resolves the controlling source row.

## Hypotheses And Scores

| Rank | Hypothesis | Evidence supporting | Conflicts / caution | identity_confidence | conflict_severity | evidence_quality | conversion_confidence | claim_probability | relevance | canonical_readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | The intended family-relevant entry-172 cluster is `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar`/`Pulgar S.` and `Juana Arriagada de Pulgar`. | Staged conflict, source packet, and current chunk agree on the Pulgar/Arriagada row; the packet labels family relevance high. | Assigned converted Markdown gives a wholly different child, parents, date, and place; father suffix unresolved. | 0.74 | 0.93 | 0.72 | 0.45 | 0.76 | 1.00 | 0.12 |
| 2 | The converted Markdown's `Jose Francisco`/`Oswaldo Gomez` row is a different row or wrong conversion/file assignment for this task. | The fields differ materially from the chunk and staged conflict; the staged conflict identifies this as row-level. | Identity analysis cannot supersede conversion QA or re-convert the image. | 0.68 | 0.94 | 0.66 | 0.42 | 0.70 | 0.96 | 0.05 |
| 3 | The father is an existing or duplicate candidate for `Jose del Carmen Pulgar`. | Current chunk/source packet name the father as `Jose del Carmen Pulgar S.` or broad `Jose del Carmen Pulgar`; canonical `jose-del-carmen-pulgar.md` exists. | Canonical stub currently shows another draft child link; `S.` is unresolved; row-level conflict blocks parent attachment. | 0.58 | 0.64 | 0.61 | 0.45 | 0.55 | 0.88 | 0.18 |
| 4 | The mother is the existing `Juana Arriagada de Pulgar` candidate. | Current chunk/source packet and canonical page use the same name; canonical page already has a probable entry-172 child link. | Canonical link is low-confidence/generated; row-level conflict blocks strengthening it. | 0.64 | 0.70 | 0.64 | 0.45 | 0.62 | 0.92 | 0.20 |
| 5 | `Juana Arriagada de Pulgar` is the same person as entry-513 `Juana de Dios Amagada/Amador de Pulgar`. | Shared Pulgar-line mother context makes this a review lead. | Different literal names and different child clusters; similarity is not identity proof. | 0.16 | 0.82 | 0.42 | 0.36 | 0.14 | 0.74 | 0.01 |
| 6 | Entry 172 directly supports `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | Pulgar surname and broader family-line context justify checking. | No Dario, Arturo, Smith, CV, grandchild, date-continuity, or relationship bridge appears. | 0.04 | 0.86 | 0.54 | 0.45 | 0.03 | 0.82 | 0.00 |
| 7 | Entry 172 directly supports `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | The Pulgar/Arriagada surname combination overlaps later local Dario clusters. | The child named here is `Jose del Carmen Segundo`, not Dario; no medical, passenger, Geneva/ICRC, or 2000 expropriation bridge appears. | 0.05 | 0.84 | 0.54 | 0.45 | 0.04 | 0.82 | 0.00 |

## Conflict Findings

- Same-person evidence: not resolved. The only plausible same-person review from this staged draft is whether the father `Jose del Carmen Pulgar`/`Pulgar S.` belongs on the existing `Jose del Carmen Pulgar` stub, after conversion QA.
- Duplicate-person risk: moderate for duplicate `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` pages; high if any Dario identity or entry-513 Juana variant is merged by name-family context alone.
- Name-variant conflict: active for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar [?]`. Separate entry-513 `Arriagada`/`Amagada`/`Amador` issues must remain separate.
- Relationship conflict: the current chunk supports a child-parent cluster, but the converted Markdown supplies a different parent pair. Relationship promotion must wait for row-level conversion QA.
- Chronology conflict: no internal chronology problem in the Pulgar/Arriagada row itself. The incompatible converted birth date/place is part of the row-level conflict, not a proven chronology conflict for one person.

## Pulgar-Line Anti-Conflation Ranking

1. `Jose del Carmen Segundo Pulgar Arriagada` as entry-172 child: probability 0.76; canonical readiness 0.12; next step is conversion QA and proof review.
2. `Juana Arriagada de Pulgar` as mother candidate: probability 0.62; canonical readiness 0.20; next step is post-QA parent-child proof review.
3. `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` as father candidate: probability 0.55; canonical readiness 0.18; next step is father-field literal QA.
4. `Juana de Dios Amagada/Amador de Pulgar` same as `Juana Arriagada de Pulgar`: probability 0.14; canonical readiness 0.01; next step is separate entry-513 comparison only after both rows are proof-reviewed.
5. `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`: probability 0.04; canonical readiness 0.00; no attachment from this draft.
6. `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith`: probability 0.03; canonical readiness 0.00; no attachment from this draft.

## Recommended Next Action

Required next step: targeted conversion QA for register page 58, entry 172. Compare the source image, assigned converted Markdown, and current chunk; decide whether the controlling row is the Pulgar/Arriagada row or the `Jose Francisco`/`Oswaldo Gomez`/`Rosario de la Cruz de la Maza` row, or whether the converted file/chunk assignment is wrong.

After QA, run proof review on the child identity, birth facts, father claim, mother claim, parent-child relationships, and comparison to existing `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` pages. Do not merge or attach Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Darío Pulgar Arriagada, or entry-513 Jose/Juana candidates without a separate identity-bearing bridge.
