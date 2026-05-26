---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526044220967
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged draft is a material row-level conflict for the same source and entry number. The assigned chunk/source-packet reading identifies entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, while the current converted Markdown identifies entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
2. The father field in the Pulgar/Arriagada reading is not proof-ready. It must remain open as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies the visible field.
3. Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and related b8f4f0490a36 evidence are not independent corroboration for this task because they derive from the same disputed source cluster.
4. No canonical identity merge, parent-child promotion, Dario-line bridge, name normalization, or fact promotion should occur from this staged draft until conversion QA resolves the controlling row and proof review is rerun.
5. No evidence in this staged draft names Dario. Pulgar-line context justifies later double-checking, but it does not justify attaching this entry to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or Darío Pulgar Arriagada.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Canonical wiki context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, `wiki/people/dario-arturo-pulgar-smith.md`, and `wiki/people/dar-o-pulgar-arriagada.md`.

## Literal Source Readings

| Evidence layer | Literal or derivative reading |
| --- | --- |
| Assigned chunk | Entry 172: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`. |
| Source packet | Repeats the assigned chunk reading and explicitly states conversion confidence is low because the controlling row conflicts with the converted Markdown. |
| Current converted Markdown | Entry 172: `Jose Miguel`; sex `Varon`; born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`. |
| Canonical wiki context | Contains existing pages for the Pulgar/Arriagada child and mother, but those pages are partly generated from this same disputed b8f4f0490a36 source cluster. |

## Hypotheses And Ranking

| Rank | Hypothesis | Supporting evidence | Conflicts and limits | Claim probability | Identity confidence |
| ---: | --- | --- | --- | ---: | ---: |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | The assigned chunk and staged source packet agree on the Pulgar/Arriagada child, March 8 birth date, Calle de Valdivia birth place, Jose/Juana parent fields, and Ernesto Herrera L. informant. The source packet says local source-image appearance is broadly consistent with the assigned chunk, while still not a QA certification. | The current converted Markdown for the same source and entry number gives a completely different Burgos/de la Cruz row. Father suffix is unresolved. Existing canonical evidence is same-cluster derivative. | 0.62 | 0.58 |
| 2 | Entry 172 is the converted-file Burgos/de la Cruz registration for `Jose Miguel`. | The current converted Markdown directly records this as entry 172 with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`. | It conflicts with the assigned chunk and source packet. It has no Pulgar/Arriagada relevance and may represent a row/source assignment error. | 0.30 | 0.28 |
| 3 | If the Pulgar/Arriagada row is certified, `Jose del Carmen Pulgar S.` is related to or may be the same as canonical `Jose del Carmen Pulgar`. | Name overlap is strong, and the wiki has a `Jose del Carmen Pulgar` stub with a separate draft child link to `Tulio Cesar Luis Jose`. | The final `S.` may be identity-relevant. The canonical Jose page does not independently prove this entry-172 father. Same-name evidence is not enough for a merge. | 0.44 | 0.36 |
| 4 | If the Pulgar/Arriagada row is certified, `Juana Arriagada de Pulgar` is the mother candidate for the entry-172 child. | The assigned chunk/source packet name her directly. Canonical pages preserve a same-cluster child link to `Jose del Carmen Segundo Pulgar Arriagada`. | That canonical link depends on the disputed b8f4f0490a36 cluster. The converted Markdown names `Concepcion de la Cruz`, not Juana. | 0.58 | 0.52 |
| 5 | `Juana Arriagada de Pulgar` may be the same person as `Juana de Dios Amagada de Pulgar` or another Juana parent candidate. | Both are Pulgar-associated mother-name candidates in existing local wiki context, and both warrant anti-conflation comparison after row QA. | The names differ materially: `Arriagada` versus `de Dios Amagada`. This staged draft does not provide spouse, child, residence, or chronology evidence sufficient to treat them as variants. | 0.16 | 0.12 |
| 6 | This entry bridges to Dario Arturo Pulgar-Smith. | The Pulgar surname and family-line context justify a later double-check. Canonical `Dario Arturo Pulgar-Smith` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merges with similarly named records. | The entry does not name Dario, Arturo, Smith, Alexander John Heinz, a grandparent relationship, or a bridge source. | 0.04 | 0.03 |
| 7 | This entry bridges to staged/document-level `Dario Arturo Pulgar`. | Other staged CV packets use a document-level `Dario Arturo Pulgar` identity. | Entry 172 names a Jose child and Jose/Juana parents, not Dario Arturo Pulgar. No CV, occupation, parentage, or chronology bridge appears here. | 0.03 | 0.02 |
| 8 | This entry bridges to `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | The surname form `Pulgar Arriagada` is relevant as anti-conflation context, and existing local context includes separate Dario/Darío Pulgar Arriagada clusters. | The child given names are `Jose del Carmen Segundo`, not Dario or Dario Jose. Existing `Darío Pulgar Arriagada` wiki evidence is a 2000 expropriation notice; Dario Jose photograph/delegate contexts are separate and do not bridge to this birth row. | 0.05 | 0.03 |

## Conflict Assessment

- Same-person conflict: high for the entry-172 child because the disputed readings identify entirely different children and parents.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is silently folded into `Jose del Carmen Pulgar`, or if `Juana Arriagada de Pulgar` is folded into `Juana de Dios Amagada de Pulgar`, before separate parent-candidate proof review.
- Name-variant risk: moderate for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`; moderate for `Juana Arriagada` versus `Amagada` because the strings are similar enough to invite error but different enough to require source-visible proof.
- Relationship-conflict severity: high. The two row readings imply mutually exclusive parent-child relationships.
- Chronology-conflict severity: high for the birth event because the Pulgar/Arriagada reading gives 1888-03-08 at 3 p.m., while the Burgos/de la Cruz reading gives 1888-04-06 at 10 p.m.
- Dario-line conflict severity: low in direct evidence, high in conflation risk. This draft does not name any Dario but sits in a surname cluster where later bridge mistakes are plausible.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.58 for Pulgar/Arriagada row; 0.28 for Burgos/de la Cruz row | The assigned chunk/source packet cohere internally, but the converted Markdown directly contradicts them. |
| Conflict severity | 0.95 | Child identity, birth date, birth place, parents, and informant all differ. |
| Evidence quality | 0.55 | Local staged evidence is specific and source-linked, but currently derivative and internally conflicted. |
| Conversion confidence | 0.25 for canonical use | The source packet itself sets conversion confidence low pending targeted QA. |
| Claim probability | 0.62 for Pulgar/Arriagada controlling row | Best current local hypothesis, not proof-ready. |
| Relevance | 0.90 for Pulgar/Jose/Juana analysis; 0.10 for Dario bridge | Directly relevant to Pulgar/Arriagada parent candidates; only indirect anti-conflation context for Dario-line work. |
| Canonical readiness | 0.10 | Hold. Existing canonical pages should not be expanded from this draft until QA and renewed proof review. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, current chunk, and the staged source packet. The QA note must decide whether register page 58, entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and must certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review for the child identity, birth facts, father claim, mother claim, and parent-child relationship claims. Only after those steps should a separate Pulgar-line identity bridge review compare Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, canonical Darío Pulgar Arriagada, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`. Do not merge or promote any of those candidates by name alone.
