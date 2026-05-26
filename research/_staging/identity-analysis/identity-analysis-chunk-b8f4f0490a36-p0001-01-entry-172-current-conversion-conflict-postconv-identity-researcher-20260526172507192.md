---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526172507192
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: hold
---

# Identity And Conflict Analysis: Entry 172 Current Conversion Conflict

## Blockers First

- Row-level conversion conflict blocks all identity promotion. The assigned chunk and held source packet read register page 58, entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown reads the same entry number as a Burgos/de la Cruz birth row.
- Father-field blocker remains unresolved. If the Pulgar/Arriagada row controls, the visible father field must be certified only as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`; do not silently normalize the suffix away.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` appear to contain generated evidence from the same entry-172 cluster. They are context, not independent resolution of the current conversion conflict.
- Entry 172 does not literally name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or `Dario Pulgar Arriagada`. Any Dario-line comparison here is an anti-conflation check only.
- `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and other Jose/Juana parent candidates must remain separate unless later proof review establishes identity continuity.

## Literal Evidence Reviewed

### Staged Conflict Draft

The staged conflict draft at `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md` says the assigned chunk and source image support entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 about 3 p.m. at Calle de Valdivia, father `Jose del Carmen Pulgar` with a possible trailing `S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.

The same draft says the current converted Markdown reads entry `172` as child `Jose Miguel`, registered 7 April 1888, born 6 April 1888 at 10 p.m. in `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

### Held Source Packet And Assigned Chunk

The held source packet repeats the Pulgar/Arriagada row and explicitly recommends `hold_for_conversion_qa`. It states that the source image shows entry 172 as the Pulgar/Arriagada row and that the father field reads `Jose del Carmen Pulgar` with a trailing mark compatible with `S.`, pending targeted QA.

The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.

### Current Converted Markdown

The current converted Markdown transcribes entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`. This is not a name variant of the Pulgar/Arriagada row; it is a different family row under the same entry number.

### Existing Canonical Context

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has generated probable evidence for the entry-172 child and a probable mother link to `Juana Arriagada de Pulgar`.
- `wiki/people/juana-arriagada-de-pulgar.md` has generated evidence naming her as mother of `Jose del Carmen Segundo Pulgar Arriagada`.
- `wiki/people/jose-del-carmen-pulgar.md` is a sparse stub whose generated child link currently points to `Tulio Cesar Luis Jose` from a separate entry-513 cluster, not this entry-172 row.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate stub tied to the entry-513 `Tulio Cesar Luis Jose` cluster.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and warns against automatic attachment of Dario/Pulgar/Pulgar-Arriagada records without identity review.
- `wiki/people/dar-o-pulgar-arriagada.md` is a stub for `Dario Pulgar Arriagada` with a 2000 expropriation event, not a proved 1888 birth or parent bridge.

## Hypotheses And Scores

| Rank | Hypothesis | Supporting Evidence | Conflicts / Limits | Identity Confidence | Conflict Severity | Evidence Quality | Conversion Confidence | Claim Probability | Relevance | Canonical Readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The controlling row is the Pulgar/Arriagada birth of `Jose del Carmen Segundo Pulgar Arriagada`. | Staged conflict draft, held source packet, and assigned chunk all agree on the Pulgar/Arriagada row. | Current converted Markdown gives a complete Burgos/de la Cruz row for the same entry number; father suffix not certified. | 0.68 | 0.95 | 0.70 | 0.55 | 0.64 | 0.98 | hold |
| 2 | The controlling row is the current conversion's Burgos/de la Cruz birth of `Jose Miguel`. | Current converted Markdown gives a complete row for entry 172. | Staged conflict draft, source packet, and assigned chunk all reject this as the controlling row for entry 172; family relevance to Pulgar line would be absent. | 0.30 | 0.95 | 0.55 | 0.40 | 0.30 | 0.20 | hold |
| 3 | The Pulgar/Arriagada child matches the existing canonical stub `Jose del Carmen Segundo Pulgar Arriagada`. | Exact name match and existing generated evidence from the same entry-172 cluster. | Canonical evidence depends on the disputed row cluster and cannot override conversion QA. | 0.62 | 0.75 | 0.60 | 0.55 | 0.58 | 0.95 | hold |
| 4 | `Jose del Carmen Pulgar S.` / `Jose del Carmen Pulgar` in entry 172 is the existing canonical `Jose del Carmen Pulgar`. | Core name match; separate local context has a Jose del Carmen Pulgar parent/declarant candidate. | The suffix is unresolved; canonical page currently reflects a separate entry-513 child cluster. | 0.40 | 0.70 | 0.55 | 0.50 | 0.38 | 0.90 | hold |
| 5 | `Juana Arriagada de Pulgar` in entry 172 is the existing canonical `Juana Arriagada de Pulgar`. | Exact name match and generated evidence from the same entry-172 cluster. | Still depends on row QA; married-style name does not prove maiden identity or same-person continuity beyond this row. | 0.60 | 0.65 | 0.62 | 0.55 | 0.58 | 0.95 | hold |
| 6 | `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are the same person under variant readings. | Both are Juana-with-Pulgar parent candidates in local context. | Literal surnames and clusters differ; entry 172 supplies no direct identity bridge to the entry-513 Juana candidate. | 0.20 | 0.72 | 0.45 | 0.50 | 0.18 | 0.70 | hold |
| 7 | Entry 172 bridges to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | Pulgar/Arriagada family-context terms may later justify a lineage double-check if the row is certified. | Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, a child/spouse/grandchild, or a lineage bridge. | 0.03 | 0.88 | 0.35 | 0.50 | 0.02 | 0.65 | blocked |
| 8 | Entry 172 is same-person evidence for `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or `Dario Pulgar Arriagada`. | The disputed Pulgar/Arriagada row contains the Pulgar and Arriagada surnames. | The child is `Jose del Carmen Segundo`, not Dario; canonical `Dario Pulgar Arriagada` currently has a 2000 event and no bridge to this 1888 birth entry. | 0.02 | 0.88 | 0.35 | 0.50 | 0.02 | 0.60 | blocked |

## Conflicts

- Same-person conflict: unresolved for the entry-172 father-name reading versus canonical `Jose del Carmen Pulgar`; unresolved for `Juana Arriagada de Pulgar` versus other Juana parent candidates.
- Duplicate-person conflict: possible only after row QA for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; current canonical stubs may duplicate staged candidates but are not proof-ready resolution.
- Name-variant conflict: `Jose del Carmen Pulgar S.` must remain distinct from a certified `Jose del Carmen Pulgar` reading until targeted QA; `Arriagada` must not be silently corrected to `Amagada` or `Amador`.
- Relationship conflict: the current conversion's parents `Oswaldo Burgos` and `Concepcion de la Cruz` are incompatible with the Pulgar/Arriagada parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- Chronology conflict: the Pulgar/Arriagada row gives birth on 8 March 1888 at about 3 p.m.; the current conversion gives birth on 6 April 1888 at 10 p.m. These are different event readings, not a minor date variant.
- Dario-line conflict: no reviewed evidence here supports merging or attaching this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.

## Recommended Next Action

Run targeted conversion QA against the source image, current converted Markdown, assigned chunk, and held source packet. The QA note must decide the controlling row for register page 58, entry 172; explain the Burgos/de la Cruz versus Pulgar/Arriagada divergence; and certify the father field only as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review for the child identity, birth facts, parent names, and parent-child relationships. Only after those pass should a separate identity-bridge review compare this Jose/Juana cluster with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or `Dario Pulgar Arriagada`. No merge, rename, canonical promotion, or Dario-line attachment should occur from this note.
