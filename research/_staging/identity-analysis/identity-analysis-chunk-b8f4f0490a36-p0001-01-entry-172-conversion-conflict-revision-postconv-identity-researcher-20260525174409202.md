---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525174409202
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525171911545.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525171911545.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525171911545.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
created: 2026-05-25
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Conversion Conflict

## Blockers

- The assigned staged conflict draft reports a row-level conversion conflict for entry 172. The assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth registration, while the assigned converted Markdown reads entry 172 as a Gomez/de la Cruz de la Maza birth registration.
- This is not a same-person, duplicate-person, or spelling-variant issue. The competing rows have different child names, parents, birth dates, places, informants, and register context.
- No canonical merge, parent-child promotion, Dario-line attachment, or Jose/Juana candidate merge is ready until targeted conversion QA reconciles the source image, converted Markdown, chunk, and source packet.
- The father field in the Pulgar/Arriagada reading remains unresolved after `Pulgar`. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as literal-reading alternatives until source-image QA certifies the field.
- The staged draft does not name Dario, Arturo, Smith, Dario Jose, or any later Dario professional/property/passenger context. Any Dario-line bridge would be interpretive and currently unsupported.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525171911545.md`.
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525171911545.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Assigned converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical wiki context for `Dario Arturo Pulgar-Smith`, `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and `Darío Pulgar Arriagada`.
- Local staged Dario context found in staged tasks/reviews for `Dario Arturo Pulgar`, `Darío J. Pulgar Arriagada`, `Dario Pulgar A.`, and related identity-bridge holds.

## Literal Source-Layer Readings

### Chunk And Source Packet Reading

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father: chunk reads `Jose del Carmen Pulgar S.`; staged conflict requires proof-review alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employee, resident at `Calle de Valdivia`.

### Converted Markdown Reading

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `José Francisco`; sex `Hombre`.
- Birth: `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En Pellin`.
- Father: `Oswaldo Gomez`.
- Mother: `Rosario de la Cruz de la Maza`.
- Informant: `Oswaldo Gomez`; age 26; profession `Empleado`; residence `Pellin`.

## Hypotheses And Scores

| Rank | Hypothesis | Interpretation | Claim probability | Identity confidence | Evidence quality | Conversion confidence | Conflict severity | Relevance | Canonical readiness |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | The assigned row is a Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | Plausible from chunk/source-packet agreement, but blocked by converted-file contradiction. | 0.68 | 0.62 | 0.55 | 0.35 | 0.90 | 0.90 | 0.08 |
| 2 | The assigned row is a Gomez/de la Cruz de la Maza birth registration for `Jose Francisco`. | Plausible from the assigned converted Markdown alone, but contradicted by chunk/source packet and staged conflict draft. | 0.34 | 0.30 | 0.45 | 0.30 | 0.90 | 0.20 | 0.05 |
| 3 | The Pulgar/Arriagada and Gomez/de la Cruz rows are the same person or duplicate-person evidence. | Not supported; the differences are material, not variant spellings. | 0.02 | 0.02 | 0.20 | 0.20 | 0.95 | 0.05 | 0.00 |
| 4 | `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` are alternative readings of the same father field in the Pulgar row. | Reasonable as a field-reading problem, not a resolved identity merge. | 0.55 | 0.45 | 0.50 | 0.35 | 0.55 | 0.75 | 0.08 |
| 5 | `Juana Arriagada de Pulgar` is the mother in the Pulgar/Arriagada row. | Plausible if the Pulgar row is certified; not promotable while the row conflict remains. | 0.66 | 0.58 | 0.55 | 0.35 | 0.75 | 0.85 | 0.08 |
| 6 | `Juana Arriagada de Pulgar` is the same person as `Juana de Dios Amagada de Pulgar` or another Juana candidate. | Not proved. Existing wiki context keeps these as separate candidates attached to different staged child contexts. | 0.12 | 0.10 | 0.30 | 0.30 | 0.70 | 0.45 | 0.02 |
| 7 | Entry 172 supplies a direct identity bridge to a Dario-line person. | Not supported; the assigned draft and source layers do not name Dario. | 0.05 | 0.05 | 0.25 | 0.25 | 0.65 | 0.45 | 0.01 |

## Pulgar-Line Comparison

| Candidate | Local evidence context | Comparison to this staged draft | Hypothesis rank |
| --- | --- | --- | ---: |
| `Dario Arturo Pulgar-Smith` | Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns against automatic merges with similar Pulgar records. | Entry 172 does not name Dario, Arturo, Smith, Alexander, or a family relationship to the canonical person. A bridge remains unproved. | Low: 0.05 |
| `Dario Arturo Pulgar` | Staged CV contexts treat this as a document-level subject and repeatedly require a separate identity bridge before attaching to `Dario Arturo Pulgar-Smith`. | Entry 172 does not name `Dario Arturo Pulgar`; surname overlap alone is insufficient. | Low: 0.05 |
| `Dario Jose Pulgar-Arriagada` | Local staged context flags Dario Jose/Pulgar-Arriagada as a comparison candidate requiring proof-reviewed bridge evidence. | Entry 172 names a possible `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose`; no age, occupation, residence continuity, parentage bridge, or later-life context is supplied. | Very low: 0.03 |
| `Darío J. Pulgar Arriagada` | Local staged task notes a 1918 medical-title mention under `Médicos-Cirujanos`. | If the 1888 Pulgar row is certified, the chronology could make a later adult professional identity possible in the abstract, but no source currently bridges `Jose del Carmen Segundo` to `Darío J.` or explains the given-name difference. | Low lead only: 0.10 |
| `Dario/Darío Pulgar Arriagada` | Existing canonical stub has a 2000 legal-notice/expropriation event. | The 2000 notice is far removed from an 1888 birth entry and has no parentage or same-person bridge here. | Very low: 0.03 |
| `Dario Pulgar A.` | Local staged context treats this as an identity-bridge/QA candidate in separate source material. | `A.` could theoretically abbreviate Arriagada, but this draft supplies no Dario name and no continuity evidence. | Low lead only: 0.08 |

## Jose And Juana Parent-Candidate Comparison

- `Jose del Carmen Pulgar`: existing canonical page currently has a draft child link to `Tulio Cesar Luis Jose`, not a certified link to this entry-172 child. The entry-172 father reading cannot be merged into that page until the Pulgar row and father suffix are proof-reviewed.
- `Jose del Carmen Pulgar S.`: preserve as the literal chunk reading for the father field, with the final `S.` unresolved. Do not normalize away the suffix.
- `Jose del Carmen Pulgar [?]`: preserve as an uncertainty label if source-image QA cannot certify the final mark.
- `Juana Arriagada de Pulgar`: existing canonical stub already has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`, but this remains weak and should stay held because the controlling row is under conversion conflict.
- `Juana de Dios Amagada de Pulgar`: existing canonical stub has a separate draft child link to `Tulio Cesar Luis Jose`. This staged draft does not prove she is `Juana Arriagada de Pulgar`; do not silently correct `Amagada` to `Arriagada`.

## Conflict Findings

- Same-person conflict: no same-person merge is supported between the Pulgar/Arriagada child and the Gomez/de la Cruz child, or between the entry-172 child and any Dario candidate.
- Duplicate-person conflict: possible duplicate Jose/Juana pages are not resolvable from this draft because the controlling row and father-field ending are unsettled.
- Name-variant conflict: `Jose del Carmen Pulgar S.` is a literal-reading uncertainty, not yet a proved name variant of `Jose del Carmen Pulgar`. `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are not interchangeable.
- Relationship conflict: the Pulgar/Arriagada parent-child reading conflicts directly with the converted Markdown's Gomez/de la Cruz parent-child reading for the same entry number.
- Chronology conflict: the Pulgar row gives birth on 8 March 1888 at 3:00 p.m.; the converted Markdown row gives birth on 20 February 1888 at 10:00 p.m.
- Place conflict: the Pulgar row gives `Calle de Valdivia`; the converted Markdown row gives `Pellin`.

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image and all derivative files. The proof-reviewer must decide whether entry 172 is the Pulgar/Arriagada row or the Gomez/de la Cruz de la Maza row, and must certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that, rerun proof review before promoting any child, birth, place, parent, or source-packet claims. A separate identity-bridge proof-review step is required before linking certified entry-172 evidence to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, `Jose del Carmen Pulgar` from other staged contexts, or any Juana parent candidate.
