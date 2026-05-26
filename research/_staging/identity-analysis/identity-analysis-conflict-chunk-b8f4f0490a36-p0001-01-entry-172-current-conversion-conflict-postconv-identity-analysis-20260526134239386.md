---
type: identity_conflict_analysis
role: identity_researcher
status: draft
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-evidence-extraction-20260526095657171.md
worker: postconv-identity-analysis-20260526134239386
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-evidence-extraction-20260526095657171.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: page 1; register page 58; entry 172
analysis_status: hold_for_conversion_qa
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Current Conversion Conflict

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-held-postconv-evidence-extraction-20260526095657171.md`.
- The current referenced converted Markdown and the current referenced chunk disagree at the row level for register page 58, entry 172.
- The chunk/source-packet reading identifies a Pulgar/Arriagada birth row; the current converted Markdown identifies a Burgos/de la Cruz row. This is not a spelling variant, name variant, or normal identity ambiguity.
- The father field is not promotion-ready. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet only certifies the field to `Jose del Carmen Pulgar` with any final initial or mark unresolved.
- Existing canonical pages already contain auto-generated or reviewed-looking evidence for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`; this note does not promote, edit, merge, or correct those pages.
- The staged draft does not name any Dario person. Dario-line context is relevant only as an anti-conflation check and cannot bridge this entry to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Darío/Dario Pulgar Arriagada.

## Literal Source Readings

### Chunk/Source-Packet Reading

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father in chunk: `Jose del Carmen Pulgar S.`, Chilean, employed, resident at `Calle de Colipí`.
- Father as certified by source packet: `Jose del Carmen Pulgar` with the trailing mark unresolved.
- Mother: `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident at `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at `Calle de Valdivia`.

### Current Converted Markdown Reading

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `José Miguel`.
- Sex: `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birth place: `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant: `Oswaldo Burgos`.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Row

Interpretation: the source image and chunk/source packet identify entry 172 as the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, but all dependent claims must remain held until conversion QA reconciles the row-level derivative conflict.

Evidence supporting:

- The staged conflict draft explicitly says the image/current-chunk-supported reading is the Pulgar/Arriagada row.
- The source packet says image review supports the Pulgar/Arriagada row rather than the Burgos/de la Cruz row in the converted Markdown.
- The referenced chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` contain evidence snapshots tied to this b8f4 source-packet family cluster, showing this row has already been treated locally as family-relevant but still with low/probable status.

Evidence against or limiting:

- The current converted Markdown for the exact referenced file does not contain the Pulgar row for entry 172.
- The father suffix cannot yet be certified as `S.` or ignored as a non-name mark.
- Parent-child relationships rely on accepting the Pulgar row as controlling after QA.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.82 | Strong local support from staged draft, source packet, and chunk; reduced by current converted-file contradiction. |
| conflict_severity | 0.95 | The conflict changes child, parents, birth date, birth place, and informant. |
| evidence_quality | 0.78 | Civil birth-register row is high-quality evidence if correctly transcribed; current derivative disagreement lowers usable quality. |
| conversion_confidence | 0.42 | Chunk and packet align, but the main converted Markdown is materially inconsistent. |
| claim_probability | 0.82 | More likely than the converted row on the currently staged image/chunk evidence, but not ready for promotion. |
| relevance | 0.98 | Directly relevant to the staged Pulgar/Arriagada conflict. |
| canonical_readiness | 0.10 | Hold for targeted conversion QA and renewed proof review. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Row In The Current Converted Markdown

Interpretation: the current converted Markdown could represent the controlling row only if targeted QA shows that the chunk/source packet is attached to the wrong image, row, or version. Current local evidence favors treating this as a conversion/file-assignment conflict.

Evidence supporting:

- The current converted Markdown explicitly records entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The converted Markdown is a referenced artifact in the staged draft and cannot be ignored.

Evidence against or limiting:

- The staged conflict draft says the image and current chunk support the Pulgar/Arriagada row.
- The source packet records image review supporting the Pulgar/Arriagada row.
- The converted row names no Pulgar, Arriagada, Jose del Carmen Segundo, Jose del Carmen Pulgar, or Juana Arriagada de Pulgar.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Supported only by the conflicted converted artifact. |
| conflict_severity | 0.95 | Accepting this row would displace the entire Pulgar/Arriagada identity cluster. |
| evidence_quality | 0.16 | Derivative text under active dispute. |
| conversion_confidence | 0.12 | The conversion is the artifact being challenged. |
| claim_probability | 0.07 | Possible as a file/version problem, unlikely as the correct family-relevant row on current staged evidence. |
| relevance | 0.82 | Highly relevant as the competing reading and false-promotion risk. |
| canonical_readiness | 0.00 | Do not create or promote Burgos/de la Cruz identities from this conflict. |

## Hypothesis 3: Jose/Juana Parent Candidates May Connect Across Pulgar Entries

Interpretation: `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are plausible Pulgar-line parent candidates, but this entry alone does not prove they are the same as any other Jose/Juana candidates in the wiki.

Evidence supporting:

- This entry, under the Pulgar-row hypothesis, names father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` contains a drafted child link to `Tulio Cesar Luis Jose` from another staged relationship, indicating a separate Jose del Carmen Pulgar candidate exists in the local wiki.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` is directly tied to this entry as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`.
- Other local reviewed notes mention separate Juana readings such as `Juana de Dios Amagada de Pulgar` / related surname variants in nearby Pulgar-line work.

Evidence against or limiting:

- The staged draft for this task does not provide a cross-entry bridge between the entry-172 parents and the other Jose/Juana candidates.
- `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` are materially different literal readings and must not be silently corrected into one person.
- The father suffix/mark issue could affect whether `Jose del Carmen Pulgar S.` should be treated as the same canonical person as `Jose del Carmen Pulgar`.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | The parent names are relevant, but cross-entry identity is not proved here. |
| conflict_severity | 0.68 | Premature merging could combine distinct parents or preserve a mistranscribed mother surname. |
| evidence_quality | 0.48 | Local candidate evidence exists, but the direct bridge is absent and this entry is conversion-blocked. |
| conversion_confidence | 0.30 | Depends on resolving the entry-172 row and father suffix. |
| claim_probability | 0.35 | Plausible lead only. |
| relevance | 0.86 | Important for Pulgar-line structure after QA. |
| canonical_readiness | 0.05 | Hold for separate Jose/Juana proof review after conversion QA. |

## Hypothesis 4: Entry 172 Bridges To A Dario Identity

Interpretation: no Dario identity is supported by this staged draft. Dario-line names must remain separate or unresolved until a later reviewed source provides a direct lineage or identity bridge.

Required Pulgar-line comparisons:

- `Dario Arturo Pulgar-Smith`: canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to attach similarly named Pulgar records without identity review. This entry does not name him.
- `Dario Arturo Pulgar`: staged CV context uses this document-level name form elsewhere. This 1888 birth entry does not name Dario Arturo and gives no CV-era bridge.
- `Dario Jose Pulgar-Arriagada`: local staged context elsewhere uses this form for separate medical/ICRC-type clusters. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose.
- `Dario/Darío Pulgar Arriagada`: canonical `wiki/people/dar-o-pulgar-arriagada.md` currently contains a narrow 2000 expropriation event. Entry 172 has no Dario name and no 2000-era continuity.
- Jose/Juana parent candidates: this entry may eventually help a lineage proof only after conversion QA and separate parent-candidate proof review. It does not itself bridge to any Dario identity.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.01 | No Dario person appears in the staged draft, chunk, packet, or converted reading. |
| conflict_severity | 0.80 | A surname-only Dario attachment would be a serious identity conflation. |
| evidence_quality | 0.05 | Only anti-conflation context exists for this hypothesis. |
| conversion_confidence | 0.20 | Even a resolved Pulgar row would not by itself name Dario. |
| claim_probability | 0.01 | Unsupported by this evidence set. |
| relevance | 0.55 | Relevant as an explicit Pulgar-line guardrail. |
| canonical_readiness | 0.00 | Do not attach this entry to a Dario canonical page. |

## Conflicts

- Same-person conflict: no same-person merge is supported. The child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and converted-row people `Jose Miguel`, `Oswaldo Burgos`, and `Concepcion de la Cruz` should remain distinct pending QA.
- Duplicate-person risk: high if the converted Markdown row is promoted as if it were the same entry as the Pulgar row; moderate if `Jose del Carmen Pulgar` is merged across entries before the suffix and cross-entry evidence are reviewed.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` is unresolved. Treat `S.` as a literal uncertainty, not a normalized identity conclusion.
- Relationship conflict: child-father and child-mother claims are likely under the Pulgar-row hypothesis but blocked because the controlling row is not yet QA-certified.
- Chronology conflict: Pulgar-row birth is 8 March 1888 at 3 p.m.; converted-row birth is 6 April 1888 at 10 p.m. This is a material event conflict, not a date variant.
- Dario-line conflict: none is directly evidenced; the risk is false attachment by surname or assumed lineage.

## Ranked Hypotheses

| rank | hypothesis | probability | disposition |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.82 | Hold for conversion QA, then proof-review child identity, birth facts, and parent relationships. |
| 2 | The entry-172 parents are related to other Jose/Juana Pulgar-line candidates. | 0.35 | Preserve as a lead; require separate cross-entry Jose/Juana proof review. |
| 3 | Entry 172 is the Burgos/de la Cruz row in the current converted Markdown. | 0.07 | Treat as conversion/file-assignment conflict unless QA proves otherwise. |
| 4 | Entry 172 bridges to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Darío Pulgar Arriagada. | 0.01 | Reject for this draft; use only as anti-conflation context. |

## Recommended Next Action

Keep this staged conflict and all dependent identity, relationship, and claim work at `hold_for_conversion_qa`.

Exact next proof-review or promotion step: run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the original image, current chunk, source packet, and current converted Markdown. QA must decide the controlling entry-172 row and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review on the child birth name, sex, birth date/time, birth place, registration date, father field, mother field, informant role, and child-parent relationships. Only after that should a separate Jose/Juana parent-candidate proof review compare `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and any other local Jose/Juana candidates. No Dario-line page should receive this evidence without a later reviewed lineage or identity bridge.
