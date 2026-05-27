---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527031854638
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
conflict_type: row_level_conversion_conflict
canonical_readiness: hold
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged conflict draft and targeted QA note identify physical row `172` on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, but the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The source packet and QA note certify the father field only as `Jose del Carmen Pulgar`; the chunk's terminal `S.` after `Pulgar` remains unresolved and is not promotion-ready.
- This staged draft does not name or bridge any Dario identity. It cannot attach the entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.
- Existing wiki context has separate Jose/Juana parent candidates, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`. This staged draft alone does not prove same-person identity for those parent candidates.
- Canonical claims, parent-child relationships, parent-pair promotion, duplicate-person merges, and Dario-line attachment should remain held until proof review accepts the row-control QA and conversion-control reconciles the derivative conflict.

## Literal Source Readings

Image-reviewed staged reading from the source packet and targeted QA note:

- Entry number: `172`, physical row on left page/register page 58.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar`; suffix unresolved.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employed, resident at Calle de Valdivia.

Conflicting derivative reading from the current converted Markdown:

- Entry `172`: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at ten at night.

## Hypotheses And Scores

| Hypothesis | Rank | Identity confidence | Conflict severity | Evidence quality | Conversion confidence | Claim probability | Relevance | Canonical readiness |
| --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| H1: Physical row `172` is the Pulgar/Arriagada birth entry | 1 | 0.91 | high | 0.88 | 0.90 for image-reviewed row control; 0.55 overall because derivatives conflict | 0.92 | 0.99 | hold |
| H2: The converted Markdown Burgos/de la Cruz entry is controlling for this task | 2 | 0.12 | high | 0.35 | 0.20 | 0.10 | 0.95 | blocked |
| H3: 1888 father `Jose del Carmen Pulgar` is the same person as an existing Jose parent candidate | 3 | 0.62 | medium | 0.76 | 0.70 | 0.55 | 0.90 | not ready |
| H4: 1888 mother `Juana Arriagada de Pulgar` is the same person as `Juana de Dios Amagada de Pulgar` | 4 | 0.38 | medium | 0.62 | 0.76 for the literal 1888 name; lower for cross-record identity | 0.30 | 0.88 | not ready |
| H5: The 1888 child is a direct bridge to Dario-line identities | 5 | 0.08 | high if used for merge | 0.20 | 0.00 for Dario linkage | 0.05 | 0.80 | blocked |

## Evidence By Hypothesis

### H1: Pulgar/Arriagada Row Controls

Supporting evidence:

- The staged conflict draft states that the visible row number `172` aligns with the Pulgar/Arriagada row on the left page.
- The source packet says direct image review found the child name, sex, registration date, birth date/time, place, mother, informant, and official signature agree with the assigned chunk.
- The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.

Conflicting evidence:

- The current converted Markdown records a different entry `172` for the Burgos/de la Cruz family.

Interpretation:

- The source-image-reviewed staging controls the identity analysis, but the derivative conflict keeps canonical readiness at hold.

### H2: Burgos/de la Cruz Conversion Controls

Supporting evidence:

- The current converted Markdown is a derivative file for the same source path and labels the Burgos/de la Cruz row as entry `172`.

Conflicting evidence:

- The assigned chunk and targeted conversion QA note both support the Pulgar/Arriagada row as physical entry `172`.
- The staged conflict draft explicitly says to preserve the Burgos/de la Cruz text as a derivative conversion conflict, not merge it into the Pulgar/Arriagada person or family record.

Interpretation:

- Treat the Burgos/de la Cruz reading as stale, row-shifted, or otherwise unresolved derivative evidence for this task.

### H3: Jose Parent Candidate Bridge

Supporting evidence:

- The 1888 staged row names father `Jose del Carmen Pulgar`, with Chilean nationality, employed occupation, and Calle de Colipi residence.
- Existing canonical context includes `wiki/people/jose-del-carmen-pulgar.md`, currently a stub with a draft child link to `Tulio Cesar Luis Jose`.
- Reviewed 1889 identity context also supports a father `Jose del Carmen Pulgar` in a Los Anjeles birth-register row, but with different surrounding family evidence.

Conflicting or limiting evidence:

- The staged conflict draft says not to merge `Jose del Carmen Pulgar` with any existing father candidate from this entry alone.
- The 1888 row's father suffix is unresolved.
- This pass did not perform a fresh proof-review comparison of the 1888 and 1889 source images.

Interpretation:

- Same-person identity is plausible but not proved. The next proof step must compare age, residence, occupation, spouse/mother form, child chronology, and the unresolved suffix across the 1888 and 1889 entries.

### H4: Juana Parent Variant Bridge

Supporting evidence:

- The 1888 staged row names mother `Juana Arriagada de Pulgar`.
- Existing canonical context includes `wiki/people/juana-arriagada-de-pulgar.md` and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.
- Both Juana candidates appear in Pulgar parent contexts and use a married-name form ending `de Pulgar`.

Conflicting or limiting evidence:

- `Arriagada` and `Amagada` are materially different literal readings, and `de Dios` appears only in one candidate form.
- The staged conflict draft says not to equate `Juana Arriagada de Pulgar` with any other Juana variant from this entry alone.
- No explicit same-person bridge appears in the staged draft or canonical pages reviewed here.

Interpretation:

- Preserve these as separate candidate identities or name variants until a proof review resolves whether the differences are transcription variants, source errors, or distinct people.

### H5: Dario-Line Bridge

Supporting evidence:

- The child surname `Pulgar Arriagada` overlaps with later Pulgar-line names in the workspace.

Conflicting or limiting evidence:

- The 1888 entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.
- The canonical `Dario Arturo Pulgar-Smith` page is family-supplied and explicitly warns against automatic merging of similarly named Pulgar records.
- Existing staged CV context supports only document-level `Dario Arturo Pulgar` attribution unless separately bridged to the canonical `Dario Arturo Pulgar-Smith`.
- Existing `Dario Jose Pulgar-Arriagada` and `Dario/Darío Pulgar Arriagada` contexts do not supply a parent-child bridge to this 1888 entry in the materials reviewed for this task.

Interpretation:

- This entry is relevant as a Pulgar-line caution point, not as Dario identity proof.

## Required Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: Canonical page is family-supplied as Alexander John Heinz's maternal grandfather. No reviewed evidence from this staged conflict links him to the 1888 child or parents.
- `Dario Arturo Pulgar`: CV-related staged evidence identifies a document-level subject but requires a separate bridge before attachment to `Dario Arturo Pulgar-Smith`. No parentage bridge appears here.
- `Dario Jose Pulgar-Arriagada`: Existing staged photograph/source-packet context is a separate identity cluster and does not connect this 1888 entry to that person.
- `Dario/Darío Pulgar Arriagada`: Existing canonical/staged references are name/event contexts without parentage linking to entry 172.
- Jose/Juana candidates: `Jose del Carmen Pulgar` is a plausible cross-entry parent candidate, but not merge-ready. `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` must remain separate literal readings until proof review resolves the variant.

## Conflict Summary

- Same-person conflict: unresolved for `Jose del Carmen Pulgar` across parent contexts; weak and unresolved for Juana variants.
- Duplicate-person conflict: possible future duplicate handling for Jose/Juana parent candidates, but this entry alone is insufficient.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`; `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar`.
- Relationship conflict: converted Burgos/de la Cruz child-parent set conflicts with image-reviewed Pulgar/Arriagada child-parent set.
- Chronology conflict: none inside the image-reviewed Pulgar/Arriagada row; no chronology bridge to Dario identities is established.

## Recommended Next Action

1. Run proof review on the exact staged conflict draft, source packet, and targeted conversion QA note to accept or reject the row-control finding.
2. Have conversion-control reconcile, supersede, or annotate the current converted Markdown so entry `172` is not silently represented as Burgos/de la Cruz when the image-reviewed row-control finding supports Pulgar/Arriagada.
3. After row control is accepted, run a focused parent-identity proof review comparing the 1888 `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` entry with the 1889 Jose/Juana parent contexts.
4. Keep `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Dario/Darío Pulgar Arriagada` separate until a dedicated identity-bridge review supplies explicit connecting evidence.
