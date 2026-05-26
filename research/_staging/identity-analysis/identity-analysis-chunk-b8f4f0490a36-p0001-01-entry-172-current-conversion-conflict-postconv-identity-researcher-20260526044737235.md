---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526044644516
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: blocked
---

# Identity/Conflict Analysis: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged draft reports a controlling-row conflict for the same source and entry number. The assigned chunk/source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, while the current converted Markdown reads entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
2. This is not a name variant. The two readings conflict on child identity, sex wording, birth date/time, birth place, father, mother, informant, and downstream relationships.
3. The Pulgar/Arriagada father field is not proof-ready. Until targeted conversion QA certifies the visible field, preserve the alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
4. Existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and related b8f4f0490a36 claims are not independent corroboration here because they derive from the same disputed source cluster.
5. No same-person, duplicate-person, parent merge, Dario-line bridge, or canonical fact promotion is supported until conversion QA resolves the row and proof review is rerun.

## Evidence Reviewed

- Staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md`.
- Referenced chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Referenced converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Canonical wiki context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.
- Reviewed local notes include prior proof-review and QA notes that consistently keep this row on hold pending targeted conversion QA.

## Literal Readings Kept Separate

| Evidence layer | Literal or derivative reading |
| --- | --- |
| Assigned chunk | Entry 172: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`. |
| Source packet | Repeats the assigned chunk reading and sets `conversion_confidence: low` because the current converted Markdown gives a different entry-172 row. |
| Current converted Markdown | Entry 172: `Jose Miguel`; sex `Varon`; born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`. |
| Wiki context | Contains Pulgar/Jose/Juana pages, but the entry-172 child and mother evidence is same-cluster derivative and should not be used as independent proof. |

## Hypotheses And Ranking

| Rank | Hypothesis | Evidence supporting | Conflicts and limits | Probability | Identity confidence |
| ---: | --- | --- | --- | ---: | ---: |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk and source packet agree on child, birth date/time/place, Jose/Juana parents, and informant. Pulgar/Arriagada names make this high relevance for the local line. | Current converted Markdown contradicts every material field. Father suffix remains unresolved. Same-cluster wiki pages are not independent support. | 0.62 | 0.58 |
| 2 | Entry 172 is the converted-file Burgos/de la Cruz row for `Jose Miguel`. | Current converted Markdown directly records this row as entry 172. | It conflicts with the assigned chunk and staged source packet and has no Pulgar/Arriagada match. It may be a row/image assignment error, but that is an inference until QA decides. | 0.30 | 0.28 |
| 3 | If the Pulgar row is certified, the father is the same person as canonical `Jose del Carmen Pulgar`. | Strong name overlap; canonical Jose page has a separate draft child link in another Pulgar row. | The `S.` suffix may matter, and the canonical Jose page does not independently prove this entry-172 father. Do not merge by name alone. | 0.44 | 0.36 |
| 4 | If the Pulgar row is certified, `Juana Arriagada de Pulgar` is the entry-172 mother candidate. | Assigned chunk/source packet name her directly; wiki has a same-cluster child link to the entry-172 child. | Converted Markdown names `Concepcion de la Cruz`; same-cluster wiki evidence does not resolve the row conflict. | 0.58 | 0.52 |
| 5 | `Juana Arriagada de Pulgar` is the same person as `Juana de Dios Amagada de Pulgar` or another Juana parent candidate. | Both are Pulgar-associated mother candidates in local wiki/staging context, so they warrant later comparison. | Names and evidence clusters differ: `Arriagada` for entry 172 versus `de Dios Amagada/Amador` in entry 513 contexts. No source in this staged draft bridges them. | 0.16 | 0.12 |
| 6 | This entry bridges to `Dario Arturo Pulgar-Smith`. | Pulgar surname and family-line context justify a future anti-conflation check. | Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, or a grandparent relationship. The canonical Pulgar-Smith page is family supplied and warns against automatic merges. | 0.04 | 0.03 |
| 7 | This entry bridges to document-level `Dario Arturo Pulgar`. | Other local staged materials use that name for CV evidence. | Entry 172 names a Jose child and Jose/Juana parents; no CV, later-life, occupation-continuity, or identity-bearing bridge appears here. | 0.03 | 0.02 |
| 8 | This entry bridges to `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or canonical `Dario Pulgar Arriagada`. | The surname pair `Pulgar Arriagada` is relevant anti-conflation context. | The entry names `Jose del Carmen Segundo`, not Dario or Dario Jose. Existing Dario/Dario Pulgar Arriagada contexts are separate and do not bridge to this birth row. | 0.05 | 0.03 |

## Conflict Assessment

- Same-person conflict: high for the child identity because the row readings describe different people.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is silently folded into `Jose del Carmen Pulgar`, or if `Juana Arriagada de Pulgar` is folded into `Juana de Dios Amagada de Pulgar`, before separate proof review.
- Name-variant conflict: moderate for `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`; moderate-high for `Arriagada`, `Amagada`, and `Amador` Juana candidates because similar spelling plus family context can invite over-normalization.
- Relationship-conflict severity: high. The competing rows imply mutually exclusive parent-child relationships.
- Chronology-conflict severity: high. The Pulgar reading gives birth on 1888-03-08 at 3 p.m.; the Burgos reading gives 1888-04-06 at 10 p.m.
- Dario-line conflict severity: low as direct evidence, high as conflation risk. This staged draft supplies no Dario identity proof.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.58 for Pulgar/Arriagada row; 0.28 for Burgos/de la Cruz row | Assigned chunk/source packet cohere, but the current converted Markdown directly contradicts them. |
| Conflict severity | 0.95 | Every identity-bearing row field materially differs. |
| Evidence quality | 0.55 | The local evidence is specific and source-linked, but derivative layers conflict. |
| Conversion confidence | 0.25 | The source packet marks conversion confidence low and asks for targeted QA. |
| Claim probability | 0.62 for Pulgar/Arriagada controlling row | Best current local hypothesis, not proof-ready. |
| Relevance | 0.90 for Pulgar/Jose/Juana analysis; 0.10 for Dario bridge | Directly relevant to Pulgar/Arriagada parent candidates; only anti-conflation context for Dario identities. |
| Canonical readiness | 0.10 | Blocked until row-control QA and renewed proof review. |

## Recommended Next Action

Hold for targeted conversion QA. The exact next step is to compare the source image, assigned chunk, source packet, and current converted Markdown for `CHUNK-b8f4f0490a36-P0001-01`, then decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row. If the Pulgar row is controlling, QA must certify the father field only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review for the child identity, birth facts, father claim, mother claim, and parent-child relationship claims. Only after that should a separate Pulgar-line identity bridge review compare `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`. Do not merge or promote any of those candidates by name alone.
