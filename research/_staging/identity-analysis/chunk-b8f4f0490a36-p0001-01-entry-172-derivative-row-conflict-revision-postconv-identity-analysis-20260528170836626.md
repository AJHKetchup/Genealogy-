---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260528170836626
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-evidence-extraction-20260528133324374.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-evidence-extraction-20260528133324374.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260528133324374.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
analysis_status: hold
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: blocked
---

# Identity/Conflict Analysis: Entry 172 Derivative Row Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-revision-postconv-evidence-extraction-20260528133324374.md`.
- The controlling issue is not a normal name variant. The assigned converted Markdown records entry `172` as a Burgos/de la Cruz birth, while the assigned chunk and source packet support physical row `172` as a Pulgar/Arriagada birth registration.
- No child identity, parent-child relationship, Dario-line attachment, parent merge, canonical fact, canonical relationship, or wiki rename should proceed until row-level conversion QA accepts the controlling row and proof review reruns on the corrected evidence set.
- The father field must remain bounded to `Jose del Carmen Pulgar`; the chunk's terminal `S.` is not certified by the current source packet.
- Existing canonical pages already contain low-confidence or family-supplied Pulgar-line material, but this staged draft must not be used to silently normalize or merge `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or `Darío Pulgar Arriagada`.

## Literal Source Readings

- Staged conflict draft: original image and assigned chunk support the Pulgar/Arriagada row as physical entry `172`; assigned converted Markdown instead gives a Burgos/de la Cruz row for entry `172`.
- Source packet literal chunk support: `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, at `Calle de Valdivia`.
- Source packet parent readings: father visible to current certified level as `Jose del Carmen Pulgar`; mother as `Juana Arriagada de Pulgar`; both associated with `Calle de Colipi`.
- Source packet declarant reading: `Ernesto Herrera L.`, present at birth, age twenty-six, employee, domiciled `Calle de Valdivia`.
- Converted Markdown conflict reading: entry `172` is `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888. This is a derivative-row conflict against the assigned image/chunk.

## Hypotheses And Evidence

| rank | hypothesis | evidence supporting | conflicts/limits | identity confidence | conflict severity | evidence quality | conversion confidence | claim probability | relevance | canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Physical entry `172` is a Pulgar/Arriagada registration for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk and source packet agree on the Pulgar/Arriagada row, child name, male sex, birth event, parents, and declarant. | Assigned converted Markdown gives a different entry `172`; row control still requires conversion QA acceptance. | 0.78 | 0.88 | 0.72 | 0.35 | 0.76 | 1.00 | 0.18 |
| 2 | Assigned converted Markdown entry `172` is the controlling row: `José Miguel`, Burgos/de la Cruz. | Converted Markdown explicitly labels this as entry `172`. | It conflicts with the assigned chunk, source packet, and image-reviewed row-control note for this task; no Pulgar-line support follows if this controls. | 0.22 | 0.88 | 0.50 | 0.35 | 0.20 | 0.55 | 0.02 |
| 3 | `Jose del Carmen Pulgar` is the recorded father of the Pulgar/Arriagada child. | Source packet and current father claim preserve father only as `Jose del Carmen Pulgar`; existing wiki has a separate `Jose del Carmen Pulgar` stub. | Terminal `S.` is not certified; father identity must not be merged with any other Jose candidate by name alone. | 0.70 | 0.64 | 0.68 | 0.35 | 0.70 | 0.95 | 0.16 |
| 4 | `Juana Arriagada de Pulgar` is the recorded mother of the Pulgar/Arriagada child. | Source packet and current mother claim read `Juana Arriagada de Pulgar`; existing wiki has a separate stub with this name. | Depends on row-control acceptance; do not merge with `Juana de Dios Amagada de Pulgar` or other Juana candidates. | 0.70 | 0.66 | 0.68 | 0.35 | 0.70 | 0.95 | 0.16 |
| 5 | Entry 172 child is the same person as `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | Broad Pulgar-line family context only; canonical Pulgar-Smith is family supplied and flagged for identity review. | Entry 172 child is recorded as `Jose del Carmen Segundo`, born 1888; no `Dario`, `Arturo`, `Smith`, grandchild link, CV facts, or later-life bridge appears here. | 0.03 | 0.86 | 0.44 | 0.35 | 0.02 | 0.70 | 0.00 |
| 6 | Entry 172 child is the same person as `Dario Jose Pulgar-Arriagada` / `Darío J. Pulgar Arriagada` / `Darío Pulgar Arriagada`. | Shared Pulgar/Arriagada surname cluster; local staged context includes 1918 medical title, photograph/source-title, and later legal-notice candidates. | Entry 172 literal given names are `Jose del Carmen Segundo`, not Dario; no middle-name bridge, occupation, image metadata bridge, or continuity evidence connects them. | 0.08 | 0.78 | 0.48 | 0.35 | 0.06 | 0.80 | 0.01 |
| 7 | `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are duplicate/variant mother candidates. | Both are Pulgar-line mother/wife-style names in existing wiki context and both involve a Jose del Carmen Pulgar cluster. | They come from different entry clusters with separate conversion conflicts; current entry 172 supports only `Juana Arriagada de Pulgar`. | 0.18 | 0.72 | 0.46 | 0.35 | 0.16 | 0.72 | 0.02 |

## Conflict Analysis

- Same-person conflict: no same-person merge is supported between entry 172 child `Jose del Carmen Segundo Pulgar Arriagada` and any Dario candidate. The literal given names do not match, and no bridge evidence is present.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` because existing stubs and staged relationship records exist, but this draft cannot update them until row QA and proof review accept the evidence.
- Name-variant conflict: `Jose del Carmen Pulgar S.` remains unproven as a normalized father name. Use `Jose del Carmen Pulgar` unless a proof-review reread certifies the suffix.
- Relationship conflict: parent-child claims are plausible within the Pulgar row but blocked by the converted Markdown disagreement. The Burgos/de la Cruz row, if treated as controlling, would invalidate the Pulgar parent-child claims for this source.
- Chronology conflict: entry 172 birth in 1888 does not fit same-person identity with the later `Dario Arturo Pulgar` / Pulgar-Smith CV and 1942-born clusters. It could be chronologically closer to the 1918/1928 physician Pulgar-Arriagada cluster only by surname context, but the given name conflict blocks same-person treatment.
- Canonical conflict: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` and `wiki/people/juana-arriagada-de-pulgar.md` already contain evidence snapshots from earlier promoted or staged material. This note does not revise those pages and recommends no further promotion from the current derivative-conflict draft.

## Ranked Conclusion

1. Most likely row reading after current staging: physical entry `172` is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`, but it is not promotion-ready because the converted Markdown disagrees.
2. Most likely parent readings if the Pulgar row is accepted: father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`, with father suffix unresolved.
3. Low-confidence contextual lead only: the entry 172 family may belong somewhere in the broader Pulgar/Arriagada family context.
4. Not supported as same person: `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, and Dario passenger candidates.
5. Not supported as duplicate mother: `Juana Arriagada de Pulgar` should not be merged with `Juana de Dios Amagada de Pulgar` from entry 513 context.

## Recommended Next Action

Run targeted conversion QA on the exact source image, assigned chunk, and assigned converted Markdown for entry `172`. The QA decision must identify the controlling physical row, explain why the converted Markdown and chunk disagree, and certify the father field as one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, rerun proof review on the current revision source packet, atomic claims, and relationships. Only then consider narrow canonical promotion for the child identity, birth event, registration date, father-name claim, mother-name claim, and parent-child relationships. A separate identity-bridge proof-review task is required before comparing or attaching this evidence to any Dario/Pulgar-Arriagada/Pulgar-Smith candidate.
