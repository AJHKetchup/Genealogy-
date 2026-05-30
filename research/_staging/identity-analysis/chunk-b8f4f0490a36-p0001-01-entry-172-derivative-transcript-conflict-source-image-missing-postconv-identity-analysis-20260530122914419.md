---
type: identity_conflict_analysis
status: draft
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
worker: "postconv-identity-analysis-20260530122914419"
role: identity_researcher
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_reference: "page 1; register page 58; entry 172"
conversion_confidence: "derivative_conflict_unresolved_source_image_missing"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity And Conflict Analysis: Entry 172 Derivative Transcript Conflict

## Blockers First

- Source-image row control is not certified. The conversion review states that the expected original/page image was not available, so the physical entry `172` cannot be independently reread in this worker run.
- The assigned chunk and current converted Markdown are materially different derivative transcripts, not name variants. They conflict on child, parents, birth date/time, birth place, and informant/declarant.
- Do not promote the child identity, birth facts, parent-child relationships, parent-candidate merges, Dario-line attachments, or canonical wiki updates from this evidence until targeted image-based conversion QA resolves the row.
- Do not merge `Jose del Carmen Pulgar S.` with existing `Jose del Carmen Pulgar` by name alone. The source packet allows a bounded father candidate `Jose del Carmen Pulgar`, but the suffix/terminal mark after `Pulgar` remains uncertified.
- Do not merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar`; they are separate local candidates with different staged relationship contexts.
- This entry does not name Dario. It supplies no direct identity bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, adult/child passenger `Dario Pulgar`, or any canonical Pulgar-Smith relationship.

## Literal Evidence Kept Separate

### Assigned Chunk Reading

The assigned chunk records entry `172` as a Pulgar/Arriagada birth registration:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`
- Sex: `Hombre`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `tres de la tarde`
- Birth place: `Calle de Valdivia`
- Father: `Jose del Carmen Pulgar S.`
- Mother: `Juana Arriagada de Pulgar`
- Informant/declarant: `Ernesto Herrera L.`, present at birth, age 26, employee, resident at `Calle de Valdivia`

### Current Converted Markdown Reading

The current converted Markdown records entry `172` as a Burgos/de la Cruz birth registration:

- Child: `Jose Miguel`
- Sex: `Varon`
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, about `diez de la noche`
- Birth place: `En esta`
- Father/declarant: `Oswaldo Burgos`
- Mother: `Concepcion de la Cruz`

### Existing Canonical/Reviewed Context

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` exists as a stub with auto-generated evidence from earlier reviewed material, including a probable mother link to `Juana Arriagada de Pulgar`, but that evidence traces to this same entry 172 lineage and is affected by this row-control conflict.
- `wiki/people/juana-arriagada-de-pulgar.md` exists as a stub with a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`, also dependent on this entry 172 lineage.
- `wiki/people/jose-del-carmen-pulgar.md` exists separately and currently shows a draft child link to `Tulio Cesar Luis Jose`, not a certified link to this entry 172 child.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` exists separately and currently shows a draft child link to `Tulio Cesar Luis Jose`; it is not proven to be the same person as `Juana Arriagada de Pulgar`.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic attachment of similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records.
- Existing Dario pages and staged notes preserve separate or unresolved clusters for `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose/Dario J. Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, and passenger-list `Dario Pulgar` entries.

## Ranked Hypotheses

| Rank | Hypothesis | Evidence supporting | Evidence against / conflict | Identity confidence | Conflict severity | Evidence quality | Conversion confidence | Claim probability | Relevance | Canonical readiness |
| ---: | --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| 1 | Entry `172` is currently unresolved between two different physical/derivative rows | The staged conflict, source packet, and conversion review all preserve a direct derivative conflict; the source image was missing for row-control certification. | None; this is the controlling state of the evidence. | 0.95 | high | medium derivative-only | low/unresolved | 0.95 | high | not ready |
| 2 | Entry `172` is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada` | Assigned chunk and held source packet provide a coherent row with child, parents, birth date/place, and informant; existing stubs reflect this lineage as probable/low-confidence evidence. | Current converted Markdown gives a wholly different child-parent cluster, and no image certification exists in this worker run. | 0.55 | high | medium | low/unresolved | 0.55 | high | hold |
| 3 | Entry `172` is the Burgos/de la Cruz row for `Jose Miguel` | Current converted Markdown gives a coherent row for `Jose Miguel`, father/declarant `Oswaldo Burgos`, and mother `Concepcion de la Cruz`. | Assigned chunk/source packet give a wholly different Pulgar/Arriagada row; no image certification exists in this worker run. | 0.45 | high | medium | low/unresolved | 0.45 | high | hold |
| 4 | `Jose del Carmen Pulgar S.` is the same father candidate as existing `Jose del Carmen Pulgar` | Name core matches; existing local context has a `Jose del Carmen Pulgar` stub in a Pulgar-line parent context. | The assigned father field includes an uncertified suffix/terminal mark; the existing stub's current relationship evidence is for `Tulio Cesar Luis Jose`, not this entry 172 child. | 0.35 | medium-high | low-medium | low/unresolved | 0.35 | high | not ready |
| 5 | `Juana Arriagada de Pulgar` is the mother in the Pulgar/Arriagada row | Assigned chunk reads that mother name, and the matching child surname structure supports the local family-context check. | Row control is unresolved; no independent image proof in this worker run. | 0.55 | high | medium | low/unresolved | 0.55 | high | hold |
| 6 | `Juana Arriagada de Pulgar` is the same person as `Juana de Dios Amagada de Pulgar` | Both are Juana/Pulgar parent-candidate names in local context. | Names differ materially (`Arriagada` vs `de Dios Amagada`); relationships come from different staged contexts; no reviewed bridge proves same person. | 0.12 | medium-high | low | not applicable to merge | 0.12 | medium-high | not ready |
| 7 | This entry provides a Dario-line ancestor bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` | Pulgar/Arriagada names make it a family-context lead worth checking after row-control QA. | The entry does not name Dario, Arturo, Smith, Jose as a Dario given name, Alexander John Heinz, spouse/child links to Dario, or any later identity bridge. | 0.05 | high if merged | low | low/unresolved | 0.05 | medium | not ready |

## Conflict Analysis

- Same-person conflict: unresolved only at the parent-candidate level. `Jose del Carmen Pulgar S.` may be a form of `Jose del Carmen Pulgar`, but the source-image proof step must certify the father field before any identity attachment. No same-person conclusion is available for any Dario cluster.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` is promoted while the converted Markdown still assigns entry `172` to `Jose Miguel`; high if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar` by name shape alone; high if this Pulgar/Arriagada lead is attached to Dario identities without an explicit bridge.
- Name-variant conflict: `Hombre` versus `Varon` is not material by itself, but the child/parent/date/place/informant differences make the two derivative readings different rows or assignments, not spelling variants.
- Relationship conflict: the Pulgar/Arriagada reading supports candidate parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted reading supports parents `Oswaldo Burgos` and `Concepcion de la Cruz`. These cannot both describe the same child in the same entry.
- Chronology conflict: the assigned chunk birth date/time is 8 March 1888 about 3 p.m.; the converted Markdown birth date/time is 6 April 1888 about 10 p.m. That is a material conflict for identity and source control.

## Scores

- Identity confidence: 0.95 that a material row-control conflict exists; 0.55 for the Pulgar/Arriagada row as a staged hypothesis; 0.45 for the Burgos/de la Cruz row as the competing staged hypothesis.
- Conflict severity: high. The conflict affects core identity, parents, birth chronology, place, and informant.
- Evidence quality: medium for derivative transcription comparison; low for final identity use because the source image is missing.
- Conversion confidence: low/unresolved; recorded as `derivative_conflict_unresolved_source_image_missing`.
- Claim probability: 0.55 for the Pulgar/Arriagada claims, 0.45 for the Burgos/de la Cruz claims, pending image-controlled QA.
- Relevance: high for Pulgar-line parent-candidate work; medium for Dario-line work as an anti-conflation checkpoint only.
- Canonical readiness: 0.00 / not ready.

## Recommended Next Action

Run targeted source-image conversion QA for entry `172` using the original `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` or the conversion-job page image. The proof-review step must certify whether physical entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row and, if Pulgar/Arriagada, certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control QA, rerun proof review before any canonical promotion. Only then should a separate identity-bridge review compare the confirmed Jose/Juana evidence against `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and the Dario clusters (`Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose/Dario J. Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, and passenger `Dario Pulgar` entries).
