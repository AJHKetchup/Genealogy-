---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260523072957430
task_id: identity-analysis:research/_staging/conflicts/CF-STAGE-CHUNK-4127185dc97c-P0172-01-conversion-conflicts.md
staged_draft: research/_staging/conflicts/CF-STAGE-CHUNK-4127185dc97c-P0172-01-conversion-conflicts.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
referenced_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
available_chunk_checked: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-4127185dc97c-P0172-01
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity And Conflict Analysis: CF-STAGE-CHUNK-4127185dc97c-P0172-01

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/CF-STAGE-CHUNK-4127185dc97c-P0172-01-conversion-conflicts.md`.
- No external research was performed. This note uses only the staged conflict draft, referenced source packet, referenced converted/chunk files where present, reviewed local notes in the workspace, and existing canonical wiki pages.
- The staged draft is a conversion-versus-source-image conflict, not an independent-source genealogical proof conflict. All affected person, relationship, and chronology claims should remain held.
- The source packet references `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md`, but that file was not present. The available chunk in that directory is `page-0001-chunk-01.md`, with a different chunk id. This citation-path mismatch blocks clean promotion.
- The staged draft says entry 513 was literally supported as `Isidoro del Carmen Diaz`, but the converted file and available chunk read entry 513 as `Isolina del Carmen / José`, father `José del Carmen Pulgar`, and mother `Juana de Dios Amador de Pulgar`; the source packet says the visible image appears closer to a `Pulgar` child surname and given names closer to `Jose Dani...`. The child identity is therefore not proof-ready.
- Entry 514 is materially conflicted: the available conversion reads father `Belisario Riquelme`, while the staged draft/source packet say the father field appears closer to `se ignora`; Mercedes Riquelme is mother/declarant context, not a silent correction of the father field.
- Entry 515 is materially conflicted: the available conversion reads `Pedro Pablo Leiva`, while the staged draft/source packet say the image appears closer to `Neira`. Do not promote Leiva/Neira identity or parentage claims from this draft.
- This staged draft contains no literal `Dario`, `Arturo`, `Smith`, `Dario Jose`, or confirmed `Arriagada` identity. Pulgar-line names in existing wiki context are anti-conflation comparison targets only.

## Evidence Scope

Literal source readings and interpretation are kept separate below. Family-context hints justify later double-checks but are not used to normalize names, merge people, or promote facts.

## Hypothesis 1: Hold Page 172 As A Conversion-QA Conflict Container

Literal evidence:

- The staged draft identifies a civil birth-register page for Los Angeles/La Laja, 1889, page 172, entries 513-515.
- The source packet says the page identity, year, and entry numbers 513-515 are supported.
- The staged draft and source packet both recommend `hold_for_conversion_qa`.
- The source packet says the visible heading appears closer to `Los Anjeles` and `La Laja` than the staged literal support's `Los Angeles` and `Julio`.

Interpretation:

This is the controlling hypothesis. Page identity is useful, but the person-name and relationship fields are unstable across derivative layers and image-reviewed notes. No same-person, duplicate-person, relationship, or chronology promotion is supported until targeted conversion QA reconciles the image with the converted file and chunk paths.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Page identity is clearer than individual identities. |
| conflict_severity | 0.92 | Core names, surnames, and parent fields conflict. |
| evidence_quality | 0.55 | Civil register is a strong source class, but current evidence is derivative and disputed. |
| conversion_confidence | 0.22 | The staged draft directly reports image/transcript conflicts and the referenced chunk path is missing. |
| claim_probability | 0.45 | Probable that the page records entries 513-515; low confidence in exact identity claims. |
| relevance | 0.99 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.02 | Hold for conversion QA. |

## Hypothesis 2: Entry 513 Is A Pulgar-Related Birth Entry, Not A Diaz Entry

Literal evidence:

- The staged draft's literal support preserves `Isidoro del Carmen Diaz`.
- The conversion QA concern says the source image appears to contain a `Pulgar` child surname rather than `Diaz`.
- The source packet says entry 513 appears to record a child with surname `Pulgar` and given names closer to `Jose Dani...`, not `Isidoro del Carmen Diaz`.
- The converted file and available chunk read father/declarant as `José del Carmen Pulgar` / `José del C. Pulgar`.

Interpretation:

The Pulgar-entry hypothesis is stronger than the Diaz-entry hypothesis, but only as a QA hypothesis. The exact child name is unresolved, and the staged evidence does not prove which Pulgar child this is. Do not create, merge, or rename a canonical child page from this draft.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Multiple local layers point toward Pulgar context, but the child reading conflicts. |
| conflict_severity | 0.88 | Diaz versus Pulgar would change the identity and family line. |
| evidence_quality | 0.58 | Image-reviewed note is useful but not a completed proof-review transcription. |
| conversion_confidence | 0.25 | Derivative readings disagree. |
| claim_probability | 0.62 | More likely a Pulgar row than a Diaz row, pending QA. |
| relevance | 0.96 | Entry 513 is the main Pulgar-line trigger. |
| canonical_readiness | 0.05 | Not ready for promotion. |

## Hypothesis 3: Jose Del Carmen Pulgar Is The Entry 513 Father/Declarant Candidate

Literal evidence:

- The converted file and available chunk read entry 513 father as `José del Carmen Pulgar`.
- The declarant field reads `José del C. Pulgar`, role `Padre`, age forty-seven, agriculturist, domiciled at Calle Colon.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` is a stub with a draft child link from separate staged evidence.

Interpretation:

Within the derivative transcript, father `José del Carmen Pulgar` and declarant `José del C. Pulgar` are probably the same row-person. This remains a draft hypothesis because the assigned conflict says the entry 513 identity fields need conversion QA, and the current task cannot silently promote the derivative reading over the source-image concern.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Father/declarant forms align in the available transcript. |
| conflict_severity | 0.70 | A wrong father/declarant reading would affect parentage. |
| evidence_quality | 0.56 | Direct register row in derivative form, but image reconciliation is incomplete. |
| conversion_confidence | 0.36 | Father/declarant is more stable than child name, but still under QA hold. |
| claim_probability | 0.64 | Plausible within entry 513 only. |
| relevance | 0.92 | Required Jose parent-candidate comparison. |
| canonical_readiness | 0.18 | Review-ready only after image proofing. |

## Hypothesis 4: Juana Mother Candidate Is Unresolved Between Amador/Amagada/Arriagada-Like Readings

Literal evidence:

- The converted file and available chunk read entry 513 mother as `Juana de Dios Amador de Pulgar`.
- Existing wiki context includes `Juana de Dios Amagada de Pulgar`, linked in draft to `Tulio Cesar Luis Jose` from related staged evidence.
- Existing wiki context also includes separate `Juana Arriagada de Pulgar`, tied to `Jose del Carmen Segundo Pulgar Arriagada` from a different source packet.
- The assigned staged draft does not provide a confirmed `Juana` reading; it only flags the row as a Pulgar-name conflict.

Interpretation:

`Amador`, `Amagada`, and `Arriagada` must remain separate reading/identity hypotheses. Family context makes `Juana de Dios Amagada de Pulgar` and `Juana Arriagada de Pulgar` worth checking after image QA, but it does not justify normalizing the mother surname in this draft.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.30 | A Juana mother is plausible from local context, but the surname bridge is unsettled. |
| conflict_severity | 0.84 | Surname normalization could conflate separate mothers and children. |
| evidence_quality | 0.44 | Compared wiki stubs are draft/probable and this draft is held. |
| conversion_confidence | 0.22 | The possible bridge is in the disputed name field. |
| claim_probability | 0.34 | Possible, not proved. |
| relevance | 0.90 | Required Juana parent-candidate comparison. |
| canonical_readiness | 0.04 | Do not merge or rename. |

## Hypothesis 5: Entry 514 Father Is Unknown Rather Than Belisario Riquelme

Literal evidence:

- The converted file and available chunk read entry 514 child as `Riquelme Juan Teodoro`, father as `Belisario Riquelme`, and mother/declarant as `Mercedes Riquelme`.
- The staged draft says entry 514 father appears closer to `se ignora`.
- The source packet says entry 514 appears to include `Rigoberto Juan Bautista`, with father field closer to `se ignora`, while mother/declarant is `Mercedes Riquelme`.
- Existing canonical `wiki/people/mercedes-riquelme.md` and `wiki/people/juan-soler.md` preserve a spouse relationship from related staged evidence, but the assigned draft does not resolve the father field.

Interpretation:

The strongest conclusion is negative: do not promote `Belisario Riquelme` as father. Mercedes Riquelme remains a likely mother/declarant candidate, but the child name and father field require image proof review before canonical use.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.42 | Mercedes context is plausible, but child and father readings conflict. |
| conflict_severity | 0.82 | Father-known versus father-unknown is a material relationship conflict. |
| evidence_quality | 0.50 | Local QA notes identify the problem but do not settle the row. |
| conversion_confidence | 0.20 | The father field is directly challenged. |
| claim_probability | 0.58 | `se ignora` is plausible enough to block Belisario promotion. |
| relevance | 0.84 | Directly addresses entry 514 conflict. |
| canonical_readiness | 0.03 | Hold. |

## Hypothesis 6: Entry 515 Is Neira-Related Rather Than Leiva-Related

Literal evidence:

- The converted file and available chunk read entry 515 as `Rosa Elvira del Carmen`, father/declarant `Pedro Pablo Leiva`.
- The staged draft says entry 515 appears to use `Neira` rather than `Leiva`.
- The source packet says entry 515 is partly visible and appears to record surnames closer to `Neira`, conflicting with the chunk's `Leiva` readings.

Interpretation:

`Neira` is a material competing surname hypothesis, but the row is not resolved enough to identify the child, father, or mother. Keep Leiva and Neira as separate literal/QA readings until the source image is proof-reviewed.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.26 | Entry 515 surname and relationship readings are disputed. |
| conflict_severity | 0.86 | Leiva versus Neira changes identity and parentage. |
| evidence_quality | 0.42 | The row is only partly supported by current local QA notes. |
| conversion_confidence | 0.18 | The converted surname is directly challenged. |
| claim_probability | 0.50 | Neira is a serious alternative, not yet proved. |
| relevance | 0.82 | Directly addresses entry 515 conflict. |
| canonical_readiness | 0.01 | Hold. |

## Required Pulgar-Line Comparison

| Rank | Identity hypothesis | Probability | Evidence and exact next step |
| ---: | --- | ---: | --- |
| 1 | Entry 513 is a Pulgar-related birth entry involving father/declarant candidate `Jose del Carmen Pulgar` | 0.62 | Local QA and derivative fields point toward Pulgar context. Next: crop-level proof review of entry 513 child, father/declarant, and mother fields against the source image before any relationship promotion. |
| 2 | Entry 513 father/declarant matches existing draft stub `Jose del Carmen Pulgar` | 0.64 | Available transcript reads `José del Carmen Pulgar` / `José del C. Pulgar`, but the assigned draft is on conversion QA hold. Next: proof-review father/declarant field and compare against the existing draft relationship evidence. |
| 3 | Entry 513 mother matches existing `Juana de Dios Amagada de Pulgar` stub | 0.34 | Similar local Pulgar/Juana context exists, but this draft's available conversion reads `Amador` and no confirmed source-image mother reading is accepted. Next: proof-review the maternal surname letter-by-letter. |
| 4 | Entry 513 is connected to `Juana Arriagada de Pulgar` / `Jose del Carmen Segundo Pulgar Arriagada` | 0.18 | Separate wiki context has an Arriagada cluster, but this draft does not confirm `Arriagada` or `Jose del Carmen Segundo`. Next: compare only after the entry 513 mother and child readings are settled. |
| 5 | Entry 513 provides an ancestor-line lead for `Dario Arturo Pulgar` | 0.08 | Dario Arturo Pulgar appears in separate CV contexts; this draft does not name Dario or establish lineage. Next: require a proof-reviewed lineage bridge from the confirmed 1889 entry to the CV subject. |
| 6 | Entry 513 provides an ancestor-line lead for canonical `Dario Arturo Pulgar-Smith` | 0.06 | Canonical page is family-supplied and explicitly warns not to attach similar Pulgar records without identity review. Next: first prove any `Dario Arturo Pulgar` bridge, then separately prove `Pulgar` equals `Pulgar-Smith`. |
| 7 | Same as `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or another Pulgar-Arriagada Dario | 0.03 | No Dario, Jose-as-Dario, Arturo, or confirmed Arriagada evidence appears in this draft. Next: no merge; keep as anti-conflation check only. |

## Conflicts

- Same-person conflict: unresolved for all persons in entries 513-515. The only internally plausible same-row match is `José del Carmen Pulgar` with `José del C. Pulgar`, pending image proof review.
- Duplicate-person risk: high if the unresolved `Juana de Dios Amador/Amagada` reading is merged into `Juana Arriagada de Pulgar`; moderate if entry 513 is attached to the existing `Jose del Carmen Pulgar` stub before source-image proofing.
- Name-variant conflict: `Diaz` versus `Pulgar` for entry 513; `Isidoro/Isolina/Jose Dani...` child readings; `Amador/Amagada/Arriagada` mother surname possibilities; `Riquelme Juan Teodoro` versus `Rigoberto Juan Bautista`; `Leiva` versus `Neira`.
- Relationship conflict: entry 514 father field is conflicted between named father and `se ignora`; entry 513 parent-child relationship cannot be promoted while the child and mother readings are unsettled; entry 515 parentage cannot be promoted while the surname conflict remains.
- Chronology conflict: no independent chronology conflict is proved. Dates on the page are not the blocker; identity and conversion readings are.
- Conversion/citation conflict: the exact staged chunk id/path is not available as cited, and the available converted/chunk layers do not agree with the staged conflict's QA concerns.

## Recommended Next Action

Keep `research/_staging/conflicts/CF-STAGE-CHUNK-4127185dc97c-P0172-01-conversion-conflicts.md` on `hold_for_conversion_qa`.

Exact next proof-review step: perform targeted side-by-side conversion QA for page 172 entries 513-515 using the source image and the current converted/chunk derivatives. First resolve the chunk citation mismatch for `CHUNK-4127185dc97c-P0172-01`. Then confirm entry 513 child surname and full given names, father/declarant form, and mother surname; confirm entry 514 child name, father field, and Mercedes Riquelme's role; and confirm entry 515 whether the surname is `Leiva`, `Neira`, or another reading. Only after that should a proof-review worker compare confirmed entry 513 Jose/Juana evidence to `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Dario Arturo Pulgar`, and `Dario Arturo Pulgar-Smith`.

Do not merge people, rename canonical pages, promote facts, or attach this page to any Dario/Pulgar identity from the current staged draft.
