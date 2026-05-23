---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260523081206386
task_id: identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-4127185dc97c-P0172-01-person-identity-candidates.md
staged_draft: research/_staging/identity/ID-STAGE-CHUNK-4127185dc97c-P0172-01-person-identity-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
referenced_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
available_chunk_checked: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-4127185dc97c-P0172-01
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity And Conflict Analysis: ID-STAGE-CHUNK-4127185dc97c-P0172-01

## Blockers First

- Exact staged draft analyzed: `research/_staging/identity/ID-STAGE-CHUNK-4127185dc97c-P0172-01-person-identity-candidates.md`.
- No external research was performed. This note uses the staged identity draft, referenced source packet, referenced converted/chunk files, reviewed local notes already in the workspace, and existing canonical wiki pages.
- The staged identity draft is not proof-ready. It says entries 513-515 are derivative-transcript identities and recommends `hold_for_conversion_qa`.
- The cited chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md` is not present. The available file in that directory is `page-0001-chunk-01.md`, with chunk id `CHUNK-bdb698de8106-P0001-01`.
- Entry 513 is materially conflicted: the staged draft literal support says `Isidoro del Carmen Diaz`, while the converted/available chunk reads `Isolina del Carmen / José`, father `José del Carmen Pulgar`, and mother `Juana de Dios Amador de Pulgar`; the source packet says image review points closer to a `Pulgar` child with given names closer to `Jose Dani...`.
- Entry 514 is materially conflicted: the staged draft literal support says `Rigoberto Juan Bautista`, while the converted/available chunk reads `Riquelme Juan Teodoro`; the source packet says the father field appears closer to `se ignora`, conflicting with the converted `Belisario Riquelme`.
- Entry 515 is materially conflicted: the staged draft literal support says `Rosa Elvira del Carmen`, while the source packet and reviewed notes say the image appears closer to `Neira` readings, conflicting with the converted `Leiva` fields.
- Do not merge any page-172 person into Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío Pulgar Arriagada, Jose del Carmen Pulgar, Juana de Dios Amagada de Pulgar, or Juana Arriagada de Pulgar from this draft alone.

## Evidence Scope

Literal source readings and interpretation are separated below. Family-context hints only justify later proof-review checks; they are not used here to correct names or relationships.

## Hypothesis 1: Entries 513-515 Are Identity Candidates Only After Conversion QA

Literal evidence:

- The staged draft identifies page 172, entries 513-515, with candidate names `Isidoro del Carmen Diaz`, `Rigoberto Juan Bautista`, and `Rosa Elvira del Carmen`.
- The same staged draft says overall confidence is low, with entries 513 and 515 materially conflicting with direct image review.
- The source packet supports page identity and entry numbers 513-515 but recommends holding person names, parentage, street names, and jurisdiction wording for conversion QA.

Interpretation:

This is the strongest conclusion. Page 172 probably contains entries 513-515, but the individual identities are not ready for same-person matching, duplicate detection, relationship promotion, or chronology use.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.30 | Page identity is stronger than individual person identity. |
| conflict_severity | 0.92 | Core given names, surnames, and parent fields disagree. |
| evidence_quality | 0.54 | Civil register is strong, but current usable evidence is disputed derivative transcription plus local QA notes. |
| conversion_confidence | 0.20 | The draft itself flags low confidence and the cited chunk path is missing. |
| claim_probability | 0.44 | Likely page/entry frame; low confidence in exact identity claims. |
| relevance | 1.00 | Directly analyzes the assigned staged identity draft. |
| canonical_readiness | 0.02 | Hold. |

## Hypothesis 2: Entry 513 Is A Pulgar-Related Birth, Not A Diaz Identity

Literal evidence:

- Staged draft literal support preserves `513 ... Isidoro del Carmen Diaz`.
- Converted/available chunk reads entry 513 child as `Isolina del Carmen / José`, father/declarant as `José del Carmen Pulgar` / `José del C. Pulgar`, and mother as `Juana de Dios Amador de Pulgar`.
- Source packet says direct image review appears closer to a child with surname `Pulgar` and given names closer to `Jose Dani...`, not `Isidoro del Carmen Diaz`.
- Reviewed notes in `research/_staging/tasks/` for related page-172 QA report entry 513 as a Pulgar-family row, while still leaving child given name and maternal surname image-sensitive.

Interpretation:

The Pulgar-row hypothesis is stronger than the Diaz-row hypothesis, but only as a conversion-QA hypothesis. The exact child name and maternal surname remain unresolved, so no child page or parent relationship should be promoted from this draft.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Several local layers point toward Pulgar, but not to a settled child identity. |
| conflict_severity | 0.90 | Diaz versus Pulgar would change the person and family. |
| evidence_quality | 0.58 | Local image-review notes are useful but not a finalized proof transcription. |
| conversion_confidence | 0.24 | Derivative readings disagree. |
| claim_probability | 0.62 | Pulgar row is plausible and stronger than Diaz, pending QA. |
| relevance | 0.98 | Entry 513 is central to this identity draft. |
| canonical_readiness | 0.05 | Not ready. |

## Hypothesis 3: Jose Del Carmen Pulgar Is The Entry 513 Father/Declarant Candidate

Literal evidence:

- Converted/available chunk reads father as `José del Carmen Pulgar`.
- Declarant is read as `José del C. Pulgar`, role `Padre`, age forty-seven, agriculturist, domiciled at Calle Colon.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` is a stub with a draft child link to `Tulio Cesar Luis Jose` from separate staged evidence.

Interpretation:

Within the available derivative row, father `José del Carmen Pulgar` and declarant `José del C. Pulgar` are probably the same row-person. This does not prove the existing canonical stub is the same person, because the row is under conversion QA hold and the child/mother readings are unsettled.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Father/declarant forms align internally in the derivative transcript. |
| conflict_severity | 0.70 | A wrong father reading would affect parentage. |
| evidence_quality | 0.56 | Register-row evidence is direct in kind but not proof-reviewed here. |
| conversion_confidence | 0.35 | More stable than child name, still subject to QA. |
| claim_probability | 0.63 | Plausible row-person only. |
| relevance | 0.92 | Required Jose parent-candidate comparison. |
| canonical_readiness | 0.16 | Hold pending field-level image proof. |

## Hypothesis 4: Juana Mother Candidate Is Unresolved Across Amador, Amagada, And Arriagada Readings

Literal evidence:

- Converted/available chunk reads entry 513 mother as `Juana de Dios Amador de Pulgar`.
- Existing canonical `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a stub with a draft child link to `Tulio Cesar Luis Jose`.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` is a separate stub with a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from different evidence.
- The assigned staged draft does not provide a settled Juana reading; it only flags entry 513 as a material identity/conversion problem.

Interpretation:

`Amador`, `Amagada`, and `Arriagada` must remain separate reading and identity hypotheses. Do not normalize these surnames by family context.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.29 | Juana mother context is plausible but surname identity is unresolved. |
| conflict_severity | 0.84 | Surname normalization could conflate distinct mothers and children. |
| evidence_quality | 0.43 | Compared wiki pages are stubs/draft/probable, and this row is held. |
| conversion_confidence | 0.21 | The surname is one of the disputed fields. |
| claim_probability | 0.34 | Possible, not proved. |
| relevance | 0.90 | Required Juana parent-candidate comparison. |
| canonical_readiness | 0.04 | Hold. |

## Hypothesis 5: Entry 514 Has Mother/Declarant Mercedes Riquelme, But Father And Child Name Are Unsettled

Literal evidence:

- Staged draft literal support gives `Rigoberto Juan Bautista`.
- Converted/available chunk gives child `Riquelme Juan Teodoro`, father `Belisario Riquelme`, mother/declarant `Mercedes Riquelme`, and says she is wife of `Juan Soler`.
- Source packet says the image appears to include `Rigoberto Juan Bautista`, father field closer to `se ignora`, and mother/declarant `Mercedes Riquelme`.

Interpretation:

Mercedes Riquelme is a likely row participant, but `Belisario Riquelme` should not be promoted as father while the field may read `se ignora`. The child-name conflict also blocks identity promotion.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.42 | Mother/declarant context is plausible; child and father are conflicted. |
| conflict_severity | 0.82 | Known father versus unknown father is a material relationship conflict. |
| evidence_quality | 0.50 | Local QA identifies the problem but does not settle it. |
| conversion_confidence | 0.20 | The challenged father field is central. |
| claim_probability | 0.57 | `se ignora` is plausible enough to block father promotion. |
| relevance | 0.84 | Direct entry 514 conflict. |
| canonical_readiness | 0.03 | Hold. |

## Hypothesis 6: Entry 515 May Be Neira-Related Rather Than Leiva-Related

Literal evidence:

- Staged draft literal support gives `Rosa Elvira del Carmen`.
- Converted/available chunk reads father/declarant as `Pedro Pablo Leiva`.
- Source packet says the partly visible entry appears closer to `Neira`, conflicting with the chunk's `Leiva` readings.
- Reviewed page-172 notes report `Neira=emendado= / vale=` and `Pedro Pablo Neira` as image-supported or likely readings, while preserving lower-field uncertainty.

Interpretation:

`Neira` is a serious competing surname hypothesis, but the row is not settled enough to identify the child, father, or mother. Keep Leiva and Neira as separate literal/QA readings.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.26 | Entry 515 name and relationship readings are disputed. |
| conflict_severity | 0.86 | Leiva versus Neira changes identity and parentage. |
| evidence_quality | 0.42 | Local QA is useful but the row is partly visible/uncertain. |
| conversion_confidence | 0.18 | Converted surname is directly challenged. |
| claim_probability | 0.50 | Neira is plausible, not proved by this note. |
| relevance | 0.82 | Direct entry 515 conflict. |
| canonical_readiness | 0.01 | Hold. |

## Required Pulgar-Line Comparison

| Rank | Identity hypothesis | Probability | Evidence and exact next proof-review step |
| ---: | --- | ---: | --- |
| 1 | Entry 513 is a Pulgar-related birth row involving father/declarant candidate `Jose del Carmen Pulgar` | 0.62 | Source packet and local reviewed notes point toward a Pulgar row. Next: targeted crop-level proof review of entry 513 child, father/declarant, and mother fields against the source image. |
| 2 | Entry 513 father/declarant is same row-person as existing `wiki/people/jose-del-carmen-pulgar.md` | 0.60 | Name and role align with the derivative transcript, but the canonical page is a stub and this draft is held. Next: after image proof, compare age, residence, spouse/mother context, and child evidence before linking. |
| 3 | Entry 513 mother is `Juana de Dios Amagada de Pulgar` | 0.34 | Existing wiki has this draft mother candidate, but current derivative conversion reads `Amador`. Next: letter-by-letter maternal surname proof review. |
| 4 | Entry 513 mother is `Juana Arriagada de Pulgar` or connects to `Jose del Carmen Segundo Pulgar Arriagada` | 0.18 | Separate canonical/staged context exists, but this draft does not confirm `Arriagada` or `Jose del Carmen Segundo`. Next: compare only after entry 513 child and mother readings are settled. |
| 5 | Entry 513 provides an ancestor-line lead for `Dario Arturo Pulgar` | 0.08 | No Dario or Arturo appears in the assigned draft. Next: require a proof-reviewed lineage bridge from a confirmed 1889 row to the CV subject. |
| 6 | Entry 513 connects to canonical `Dario Arturo Pulgar-Smith` | 0.06 | Canonical page is family-supplied and warns against attaching similar Pulgar records without identity review. Next: first prove any `Dario Arturo Pulgar` bridge, then prove the `Pulgar`/`Pulgar-Smith` identity variant. |
| 7 | Entry 513 is evidence for `Dario Jose Pulgar-Arriagada` or `Darío Pulgar Arriagada` | 0.03 | This draft has no `Dario`, `Jose` as a Dario name, `Arturo`, or confirmed `Arriagada` evidence. Next: no merge; use only as an anti-conflation check. |

## Conflicts

- Same-person conflict: unresolved for all named children in entries 513-515. The only internally plausible same-row match is `José del Carmen Pulgar` with `José del C. Pulgar`, pending proof review.
- Duplicate-person risk: high if `Juana de Dios Amador/Amagada` is merged into `Juana Arriagada de Pulgar`; moderate if entry 513 is attached to `Jose del Carmen Pulgar` before source-image proofing; high if any Pulgar row is used as a Dario bridge by surname alone.
- Name-variant conflict: `Diaz` versus `Pulgar`; `Isidoro`/`Isolina`/`Jose Dani...`; `Amador`/`Amagada`/`Arriagada`; `Rigoberto Juan Bautista` versus `Riquelme Juan Teodoro`; `Leiva` versus `Neira`.
- Relationship conflict: entry 514 father is conflicted between named father and `se ignora`; entry 513 parent-child relationship cannot be promoted while child and mother readings are unresolved; entry 515 parentage cannot be promoted while surname and lower-row readings remain disputed.
- Chronology conflict: none independently established. The page dates are not the blocker; identity and conversion readings are.
- Conversion/citation conflict: the staged draft's referenced `CHUNK-4127185dc97c-P0172-01` path is missing, while the available chunk file has a different chunk id and derivative readings that conflict with local image-review notes.

## Recommended Next Action

Keep `research/_staging/identity/ID-STAGE-CHUNK-4127185dc97c-P0172-01-person-identity-candidates.md` on `hold_for_conversion_qa`.

Exact next proof-review step: run targeted side-by-side conversion QA for page 172 entries 513-515 using the source image, the converted Markdown, the available chunk, and reviewed page-172 notes. First resolve the chunk citation mismatch for `CHUNK-4127185dc97c-P0172-01`. Then confirm entry 513 child surname/full given names, father/declarant form, and mother surname; confirm entry 514 child name, father field, and Mercedes Riquelme's role; and confirm entry 515 whether the surname is `Leiva`, `Neira`, or another reading. Only after that should a proof-review worker compare confirmed entry 513 Jose/Juana evidence to `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Dario Arturo Pulgar`, and `Dario Arturo Pulgar-Smith`.

Do not merge people, rename canonical pages, promote facts, or attach this page to any Dario/Pulgar identity from the current staged identity draft.
