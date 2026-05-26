---
type: identity_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526173959405
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
created: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged conflict draft reports a material row-level conversion conflict for entry `172`. The assigned chunk and staged source packet read the entry as a Pulgar/Arriagada birth row; the current converted Markdown reads the same entry number as a Burgos/de la Cruz birth row.
2. This is not a same-person, duplicate-person, or spelling-variant issue. The competing readings change the child, birth date/time/place, father, mother, informant, and every dependent relationship candidate.
3. The Pulgar/Arriagada father field is not certified at proof precision. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA records the visible source reading.
4. Existing canonical Pulgar pages are context only. This staged draft cannot promote, merge, rename, or repair pages for `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, or any Juana candidate.
5. The next required step is targeted conversion QA for row control and father-field certification, followed by proof review before any canonical update.

## Literal Evidence

From the assigned staged draft and source packet:

- Entry: `172`, Los Angeles birth register, 1888; register page 58.
- Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`, male; born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`; father `Jose del Carmen Pulgar` with unresolved trailing `S.` or mark; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at birth.
- Current converted Markdown reading: child `Jose Miguel`, male; born 6 April 1888 at about 10 p.m. at `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

From the assigned chunk:

- Entry `172` is transcribed as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`

Existing wiki context checked:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns against automatic merges with similar Pulgar clusters.
- `wiki/people/dar-o-pulgar-arriagada.md` is a separate `Darío Pulgar Arriagada` stub with a 5 December 2000 expropriation event and no entry-172 parent bridge.
- `wiki/people/jose-del-carmen-pulgar.md` has a separate draft child link to `Tulio Cesar Luis Jose`; it does not prove the entry-172 father identity.
- `wiki/people/juana-arriagada-de-pulgar.md` and `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` contain entry-172 evidence snapshots, but those snapshots are derivative of the same conflicted cluster and are not independent corroboration.

## Ranked Hypotheses

| Rank | Hypothesis | Evidence supporting | Conflicts and limits | Identity confidence | Claim probability | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk and source packet give a coherent row with child, birth facts, parents, and informant. | Current converted Markdown gives a wholly different row; father suffix remains unresolved. | 0.64 | 0.66 | hold_for_conversion_qa |
| 2 | Entry `172` is the Burgos/de la Cruz birth registration for `Jose Miguel`. | Current converted Markdown gives a complete alternate row. | Contradicted by assigned chunk and staged source packet; likely row-control or conversion-file conflict. | 0.28 | 0.30 | hold_for_conversion_qa |
| 3 | The Pulgar-row father is a `Jose del Carmen Pulgar [?]` candidate compatible with existing `Jose del Carmen Pulgar` context. | Base name appears in the chunk/source packet; existing wiki has a Jose del Carmen Pulgar stub. | The suffix/mark is unresolved, and cross-entry identity is not proved by name alone. | 0.46 | 0.44 | hold_for_field_qa |
| 4 | The Pulgar-row mother is compatible with existing `Juana Arriagada de Pulgar`. | Exact name appears in the chunk/source packet and an existing stub. | Stub evidence depends on this same conflicted entry; do not conflate with other Juana candidates. | 0.55 | 0.52 | hold_for_conversion_qa |
| 5 | Entry 172 bridges to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | Pulgar/Arriagada family context justifies later comparison. | No Dario, Arturo, Smith, CV, grandchild, spouse, or identity bridge appears in this source. | 0.05 | 0.04 | not_ready |
| 6 | Entry 172 bridges to `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`. | Surname cluster overlaps with broader Pulgar-Arriagada work. | Entry names a Jose-named child if the Pulgar row controls; no Dario Jose or Dario Pulgar Arriagada bridge is present. | 0.03 | 0.02 | not_ready |
| 7 | Entry 172 resolves broader Jose/Juana parent candidates from other register clusters. | `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are relevant comparison names. | Other clusters are separate and conversion-sensitive; no spouse, duplicate-person, or parent-merge proof is supplied here. | 0.18 | 0.16 | not_ready |

## Conflict Assessment

- Same-person conflict severity: high. `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` have different names, parents, birth dates, birth places, and informants.
- Duplicate-person risk: high for premature merging of `Jose del Carmen Pulgar S.` with `Jose del Carmen Pulgar`, and for broad Juana/Pulgar candidate merging before row and field QA.
- Name-variant risk: moderate-high. `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is a transcription issue, not a proved variant. `Pulgar`, `Pulgar Arriagada`, `Pulgar-Smith`, and Dario-name clusters are not interchangeable.
- Relationship conflict severity: high. The competing rows name different parent pairs: `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar` versus `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Chronology conflict severity: high. The Pulgar/Arriagada row gives birth on 8 March 1888; the converted Burgos/de la Cruz row gives birth on 6 April 1888.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.64 | Highest for the Pulgar/Arriagada row because assigned chunk/source packet agree, but row-control conflict blocks proof-level use. |
| Conflict severity | 0.95 | The conflict changes the entire identity and family structure of entry 172. |
| Evidence quality | 0.70 | Local evidence includes source packet, chunk, converted Markdown, reviewed notes, and wiki context, but derivatives disagree. |
| Conversion confidence | 0.35 | Low for canonical use until targeted conversion QA reconciles the current converted Markdown with the assigned chunk/source packet. |
| Claim probability | 0.66 | The Pulgar/Arriagada row is probable if the assigned chunk/source-packet reading is certified. |
| Relevance | 0.95 | Directly relevant to Pulgar/Arriagada parent candidates and required Dario-line anti-conflation review. |
| Canonical readiness | 0.10 | No identity, event, relationship, merge, or canonical attachment is ready. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, current converted Markdown, staged source packet, and exact staged conflict draft referenced above. The QA note must decide which row controls entry `172` and certify the father field only to the visible extent as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, duplicate-person decision, parent merge, or canonical attachment. The next Pulgar-line proof-review step should explicitly compare certified entry-172 evidence against `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and other Jose/Juana parent candidates while preserving separate hypotheses unless a direct bridge is found.
