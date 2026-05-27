---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527222753668
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-rowcert-postconv-evidence-extraction-20260527221218880.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
conflict_type: conversion_row_control
canonical_readiness: hold
promotion_recommendation: promote_after_review
---

# Identity Analysis: Entry 172 Derivative Row Conflict

## Blockers First

- The exact staged conflict draft says physical row `172` is the Pulgar/Arriagada birth registration, while the current converted Markdown labels entry `172` as a Burgos/de la Cruz row. This is a high-severity derivative row-control conflict.
- The source packet is image-reviewed row-control evidence, but the converted Markdown still conflicts. Canonical promotion needs proof review and an explicit conversion-control reconciliation or superseding note.
- The father field is staged only as `Jose del Carmen Pulgar`. The possible trailing `S.` or mark after `Pulgar` remains unresolved and must not be promoted as a suffix.
- This staged draft does not name or directly bridge `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.
- Existing wiki context has separate Jose/Juana parent candidates. This note does not merge `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar`.

## Literal Source Readings

Image-reviewed staged row reading from the assigned chunk and source packet:

- Entry number: `172`, register page 58, physical row on the left page.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at `tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar`; possible following suffix/mark not certified.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age twenty-six, employed, resident at Calle de Valdivia.

Conflicting derivative reading from the current converted Markdown:

- Entry `172`: `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at ten at night.

Interpretation kept separate: the staged image-reviewed packet likely corrects a derivative conversion row error, but identity promotion should wait for proof review because two local derivatives disagree.

## Hypotheses And Scores

| Rank | Hypothesis | Identity confidence | Conflict severity | Evidence quality | Conversion confidence | Claim probability | Relevance | Canonical readiness |
| ---: | --- | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | Physical entry `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.92 | high | 0.89 | 0.90 for image-reviewed row control; 0.58 overall while derivative conversion conflicts | 0.93 | 0.99 | hold pending proof review |
| 2 | The Burgos/de la Cruz converted-Markdown row controls this task's entry `172`. | 0.10 | high | 0.35 | 0.20 | 0.08 | 0.95 | blocked |
| 3 | The father `Jose del Carmen Pulgar` in this 1888 entry is the same person as the existing wiki `Jose del Carmen Pulgar` parent candidate. | 0.55 | medium | 0.70 | 0.70 | 0.50 | 0.88 | not ready |
| 4 | The mother `Juana Arriagada de Pulgar` is a name variant or duplicate of `Juana de Dios Amagada de Pulgar`. | 0.28 | medium | 0.58 | 0.76 for the 1888 literal name; lower for cross-record identity | 0.24 | 0.82 | not ready |
| 5 | This entry directly bridges to `Dario Arturo Pulgar-Smith` or staged `Dario Arturo Pulgar`. | 0.07 | high if merged | 0.18 | 0.00 for Dario linkage | 0.04 | 0.70 | blocked |
| 6 | This entry directly bridges to `Dario Jose Pulgar-Arriagada` or `Dario/Darío Pulgar Arriagada`. | 0.06 | high if merged | 0.18 | 0.00 for Dario linkage | 0.03 | 0.70 | blocked |

## Evidence Supporting Each Hypothesis

### H1: Pulgar/Arriagada Row Controls

Supporting evidence:

- The exact staged conflict draft states that the original image and assigned chunk identify physical row `172` as the Pulgar/Arriagada birth registration.
- The source packet states that on register page 58, physical row `172` is the Pulgar/Arriagada row, not the Burgos/de la Cruz row in current converted Markdown.
- The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.

Limiting evidence:

- The converted Markdown for the same source path gives a different row/person under entry `172`.
- The father-field suffix is unresolved.

Interpretation:

- H1 is the best-supported identity reading for this staged task, but it remains a proof-review candidate, not a canonical fact.

### H2: Burgos/de la Cruz Conversion Controls

Supporting evidence:

- The current converted Markdown is a local derivative tied to the same source path and labels `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, as entry `172`.

Conflicting evidence:

- The newer source packet explicitly treats the current converted Markdown as the conflict, not as the controlling row.
- The assigned chunk and staged conflict draft agree on the Pulgar/Arriagada physical row.

Interpretation:

- H2 should be preserved as the conflicting derivative reading only. Do not attach the Burgos/de la Cruz family to the Pulgar/Arriagada person.

### H3: Jose Parent Candidate

Supporting evidence:

- The staged row names father `Jose del Carmen Pulgar`, Chilean, employed, resident at Calle de Colipi.
- Existing canonical context has `wiki/people/jose-del-carmen-pulgar.md`, a stub with a draft child link to `Tulio Cesar Luis Jose`.
- Other staged identity-analysis notes for Pulgar birth-register rows preserve `Jose del Carmen Pulgar` as a parent candidate requiring later comparison.

Limiting evidence:

- This 1888 row does not state the father's age.
- The possible `S.` after `Pulgar` is not certified.
- The existing wiki Jose page does not yet carry this entry's father claim in its evidence snapshot.

Interpretation:

- Same-person identity is plausible but not ready. The next proof-review step must compare source-reviewed names, ages if present, residences, occupations, spouse/mother forms, and child chronology across the 1888 and later Jose parent contexts.

### H4: Juana Parent Variant Candidate

Supporting evidence:

- The 1888 row names mother `Juana Arriagada de Pulgar`.
- Existing canonical context has `wiki/people/juana-arriagada-de-pulgar.md`, with a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- Existing canonical context also has `wiki/people/juana-de-dios-amagada-de-pulgar.md`, with a draft child link in another Pulgar parent context.

Limiting evidence:

- `Arriagada` and `Amagada` are materially different literal readings.
- `Juana de Dios` appears in the separate candidate, not in this 1888 staged row.
- No reviewed bridge in this task proves that the two Juana forms are the same woman.

Interpretation:

- Preserve separate hypotheses: `Juana Arriagada de Pulgar` is the literal 1888 mother reading; `Juana de Dios Amagada de Pulgar` remains a separate parent candidate until targeted proof review resolves whether this is a variant, transcription error, or distinct person.

### H5: Dario Arturo Pulgar-Smith / Dario Arturo Pulgar Bridge

Supporting evidence:

- The surname pattern `Pulgar Arriagada` is relevant to the broader Pulgar-line research context.
- Canonical `Dario Arturo Pulgar-Smith` exists as a family-supplied maternal-grandfather profile.
- Staged CV contexts use document-level `Dario Arturo Pulgar` and repeatedly call for a separate bridge to `Dario Arturo Pulgar-Smith`.

Limiting evidence:

- This staged draft names `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; it does not name Dario or Smith.
- The canonical `Dario Arturo Pulgar-Smith` page explicitly warns against automatic merging with similarly named Pulgar records.

Interpretation:

- Do not attach this entry to `Dario Arturo Pulgar-Smith` or `Dario Arturo Pulgar`. A later lineage proof review would first need accepted parent-child links from this row and then explicit bridge evidence outward to the Arturo/Smith identity.

### H6: Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada Bridge

Supporting evidence:

- The 1888 child's maternal surname pattern overlaps with later `Pulgar Arriagada` name forms in local staged and wiki context.
- Existing local context includes a canonical `Darío Pulgar Arriagada` stub and staged `Dario Jose Pulgar-Arriagada` materials.

Limiting evidence:

- This staged draft contains no `Dario`, `Dario Jose`, `Darío J.`, medical-title, Geneva, expropriation, age, residence, or spouse evidence.
- The child in this row is `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.

Interpretation:

- This entry is only a potential family-line context clue. It is not a same-person or duplicate-person bridge to any Dario Pulgar Arriagada candidate.

## Conflict Summary

- Same-person conflict: unresolved for `Jose del Carmen Pulgar` across parent contexts; unresolved and weaker for Juana variants.
- Duplicate-person conflict: possible future duplicate review for Jose/Juana parent candidates, but no merge is justified by this draft alone.
- Name-variant conflict: `Jose del Carmen Pulgar` versus uncertified `Jose del Carmen Pulgar S.`; `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: high. The converted Burgos/de la Cruz child-parent set conflicts with the staged image-reviewed Pulgar/Arriagada child-parent set for entry `172`.
- Chronology conflict: none inside the Pulgar/Arriagada row; no chronology bridge to Dario identities is established.
- Conversion conflict: high row-control conflict between current converted Markdown and the staged image-reviewed row packet.

## Required Pulgar-Line Comparison

| Candidate | Current comparison result | Next proof-review or promotion step |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Not linked by this draft. Existing canonical page is family-supplied and warns against name-only merging. | Require a dedicated lineage/identity-bridge proof review after accepted parent-child evidence connects this 1888 row to the Arturo/Smith line. |
| `Dario Arturo Pulgar` | Not linked by this draft. Existing staged CV evidence is document-level and still needs a bridge to `Dario Arturo Pulgar-Smith`. | Keep separate; proof-review the CV subject bridge independently before any use of this row as context. |
| `Dario Jose Pulgar-Arriagada` | Not linked by this draft. No Dario/Jose-Arriagada identity evidence appears in entry 172. | Require explicit Dario Jose source-control and identity-bridge proof review before comparison to this family row. |
| `Dario/Darío Pulgar Arriagada` | Not linked by this draft. Name pattern overlap is not evidence of sameness. | Preserve as separate; compare only after a proof-reviewed lineage or identity record supplies age, parent, spouse, residence, or event continuity. |
| `Jose del Carmen Pulgar` | Literal father candidate in this staged row; plausible overlap with existing wiki parent stub. | After row-control proof review, run focused parent-identity review across Jose parent records, comparing residence, occupation, spouse/mother forms, and chronology. |
| `Juana Arriagada de Pulgar` | Literal mother candidate in this staged row and existing wiki page with probable child link. | After row-control proof review, promote only the literal 1888 mother reading if accepted; do not normalize to other Juana variants. |
| `Juana de Dios Amagada de Pulgar` | Separate wiki/staged parent candidate; not proved same as `Juana Arriagada de Pulgar`. | Run targeted Juana variant proof review after row-control is settled; preserve `Arriagada` and `Amagada` as separate readings until accepted evidence reconciles them. |

## Recommended Next Action

1. Proof-review this exact staged conflict draft and source packet to accept or reject the image-reviewed row-control conclusion for entry `172`.
2. Ask conversion-control to reconcile, supersede, or annotate the current converted Markdown so the Burgos/de la Cruz derivative row is not silently treated as the controlling entry `172` for this image.
3. If row control is accepted, proof-review the atomic Pulgar/Arriagada claims and parent-child relationships using the father boundary `Jose del Carmen Pulgar` only.
4. Only after that, run a focused Jose/Juana parent identity review; keep all Dario candidates separate until a dedicated identity-bridge proof review supplies direct connecting evidence.
