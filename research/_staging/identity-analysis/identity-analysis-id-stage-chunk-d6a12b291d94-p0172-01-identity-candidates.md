---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-d6a12b291d94-P0172-01-identity-candidates.md
worker: postconv-identity-analysis-20260523063027247
staged_draft: research/_staging/identity/ID-STAGE-CHUNK-d6a12b291d94-P0172-01-identity-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: CHUNK-d6a12b291d94-P0172-01

## Blockers First

- The staged identity draft itself recommends `hold_for_conversion_qa`; do not promote entry 515 identities from this packet until a complete lower-row image or continuation image is checked.
- Entry 515 has a source-image crop problem. The source packet says the mother field for `Carmen Fuentes` is not visible in the reviewed PNG area, and the full child name is only partly supported.
- Entry 513 has a Pulgar-line name-reading conflict across local staged/reviewed materials. This d6a12b chunk reads child `Tulio Cesar Luis Jose` and mother `Juana de Dios Amagada de Pulgar`; other reviewed notes for related entry 513 material report that the image-sensitive child line begins closer to `Pulgar Ama...` plus `Jose ...`, and that the mother surname conflicts with `Amador`/`Amagada`.
- Entry 514 father evidence is not stable across local staged materials. This d6a12b chunk reads father `Belisario Riquelme`; another local page-172 review says the derivative father field is unreliable and the image is closer to an unknown/ignored father notation. Preserve the d6a12b literal reading but hold any father merge until proof review resolves the register image.
- The staged draft and existing wiki context include Pulgar-line names. Nothing in this page names `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío Pulgar Arriagada`; those identities are anti-conflation context only for this task.

## Evidence Scope

This note reviews only the staged draft `research/_staging/identity/ID-STAGE-CHUNK-d6a12b291d94-P0172-01-identity-candidates.md`, its referenced source packet and chunk, related local staged claims/relationships/review notes surfaced in this workspace, and existing canonical wiki pages. No external research was used.

Literal readings below preserve what the d6a12b staged materials say. Interpretation is separated from those readings.

## Hypothesis 1: Entry 513 Names A Child Tulio Cesar Luis Jose With Parents Jose Del Carmen Pulgar And Juana De Dios Amagada De Pulgar

Literal evidence:

- The d6a12b chunk reads entry 513 as `Nombre. Tulio Cesar Luis José`, `Sexo Masculino`.
- The same row reads `Nombre del padre. José del Carmen Pulgar`, Chilean, agriculturist, domiciled at Calle Colon.
- The same row reads `Nombre de la madre. Juana de Dios Amagada de Pulgar`, Chilean, housework, domiciled at Calle Colon.
- The declarant field reads `José del C. Pulgar`, `Padre`, age forty-seven, agriculturist, Calle Colon.
- Existing canonical stubs already contain draft links among `wiki/people/tulio-cesar-luis-jose.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

Interpretation:

- Within this exact d6a12b staged draft, the father and declarant are probably the same person: `Jose del C. Pulgar` is an abbreviation of `Jose del Carmen Pulgar`, and the declarant is explicitly marked father.
- The parent-child relationship is plausible from the d6a12b table, but not canonical-ready because other local reviewed materials flag the child-name line and mother surname as image-sensitive.
- `Juana de Dios Amagada de Pulgar` should not be silently merged with `Juana Arriagada de Pulgar`; they may be distinct readings/persons, or one may be a conversion/proofing error. The next action is targeted image proof review of the entry 513 child and mother fields.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Father/declarant identity is internally strong; child and mother exact-name readings are disputed locally. |
| conflict_severity | 0.74 | Entry 513 conflicts affect Pulgar-line parent-child attachment and canonical person creation. |
| evidence_quality | 0.62 | Civil register evidence is valuable, but this packet depends on derivative transcription plus image-sensitive readings. |
| conversion_confidence | 0.58 | The d6a12b chunk is confident, but reviewed notes identify competing readings. |
| claim_probability | 0.66 | Probable that a Jose del Carmen Pulgar father entry exists; lower for exact child/mother names as staged here. |
| relevance | 0.95 | Directly relevant to this staged identity draft and existing Pulgar-line wiki stubs. |
| canonical_readiness | 0.35 | Hold until targeted proof review resolves child name and maternal surname. |

## Hypothesis 2: Entry 513 Is Related To The Jose Del Carmen Segundo Pulgar Arriagada / Juana Arriagada De Pulgar Cluster

Literal evidence:

- Existing canonical pages include `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, with probable/draft evidence from other local staged entry-172 materials.
- Local review notes for related entry-172 work report child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- The d6a12b staged draft for entry 513 does not literally name `Jose del Carmen Segundo Pulgar Arriagada` or `Juana Arriagada de Pulgar`.

Interpretation:

- This is a competing/local-context hypothesis, not a merge instruction. The shared father name `Jose del Carmen Pulgar`, similar mother married-name form, and page-172/register context justify a double-check.
- The d6a12b staged reading `Tulio Cesar Luis Jose` plus `Juana de Dios Amagada de Pulgar` should remain separate from `Jose del Carmen Segundo Pulgar Arriagada` plus `Juana Arriagada de Pulgar` until proof review determines whether these are different entries, duplicate conversions, or misread portions of the same register page.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Overlap is contextual and partly name-based; d6a12b does not name this child/mother pair. |
| conflict_severity | 0.82 | A mistaken merge would corrupt Pulgar-line parentage. |
| evidence_quality | 0.55 | Based on reviewed local notes and canonical stubs, but not resolved against this exact source image here. |
| conversion_confidence | 0.42 | Multiple local conversion/proof-review variants exist. |
| claim_probability | 0.38 | Possible duplicate/conflicting identity cluster, not proven. |
| relevance | 0.88 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.10 | Not ready for merge or promotion. |

## Hypothesis 3: Entry 514 Names Rigoberto Juan Bautista, Mother Mercedes Riquelme, Spouse-Clue Juan Soler, And Possible Father Belisario Riquelme

Literal evidence:

- The d6a12b chunk reads entry 514 as `Nombre. Rigoberto Juan Bautista`, `Sexo. Masculino`.
- The d6a12b father field reads `Belisario Riquelme`, with blank nationality/profession/domicile details.
- The mother and declarant field names `Mercedes Riquelme`; she is marked `Madre`, `Esposa de Juan Soler`, age twenty-one, seamstress, domiciled at Calle San Joaquin.
- The staged draft correctly warns not to conflate Juan Soler with the child's father.
- Existing canonical pages for `Mercedes Riquelme` and `Juan Soler` contain draft spouse links from this staging area.

Interpretation:

- Mercedes Riquelme as mother/declarant and Juan Soler as her spouse are stronger than the d6a12b father-field identity.
- `Juan Soler` is relationship context for Mercedes Riquelme, not father evidence for Rigoberto Juan Bautista.
- `Belisario Riquelme` should be held as a possible father named in this d6a12b derivative reading, because related local review notes question the father field.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Child, mother/declarant, and spouse clue are internally coherent in d6a12b. |
| conflict_severity | 0.57 | Main risk is over-promoting an unstable father reading or treating Juan Soler as father. |
| evidence_quality | 0.64 | Register row is direct evidence, but father attributes are sparse and locally disputed. |
| conversion_confidence | 0.63 | Good for mother/declarant; lower for father. |
| claim_probability | 0.76 | Mother/declarant and spouse clue probable; father lower. |
| relevance | 0.82 | Directly relevant to staged identities and relationship conflict handling. |
| canonical_readiness | 0.46 | Mother/spouse clue may proceed after proof review; father should remain held. |

## Hypothesis 4: Entry 515 Names Rosa Elvira Del Carmen With Father Pedro Pablo Leiva And Mother Carmen Fuentes

Literal evidence:

- The d6a12b chunk reads entry 515 as `Nombre. Rosa Elvira del Carmen`, `Sexo. Femenino`.
- The d6a12b father/declarant field reads `Pedro Pablo Leiva`, Chilean, day laborer, domiciled at Calle San Joaquin.
- The d6a12b mother field reads `Carmen Fuentes`, Chilean, housework, domiciled at Calle San Joaquin.
- The source packet says the image crop only partially supports the lower entry and that `Carmen Fuentes` is not visible in the reviewed image area.
- Other local staged notes for entry 515 report competing image-visible possibilities such as `Neira`/`Ulloa`/`Laura de la Cruz`, conflicting with `Rosa Elvira del Carmen`, `Pedro Pablo Leiva`, and `Carmen Fuentes`.

Interpretation:

- Entry 515 is not canonical-ready. The only safe identity action from this packet is to preserve the derivative reading as a hypothesis pending complete-row proof review.
- The father/declarant reading is stronger than the mother reading, but both should remain held because the child identity and lower row are cropped or disputed.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.44 | Partial image support and competing local readings prevent firm identity resolution. |
| conflict_severity | 0.79 | Promoting the wrong child/parent trio would create duplicate or false family links. |
| evidence_quality | 0.42 | Derivative transcription with cropped source-image limitation. |
| conversion_confidence | 0.34 | Source packet explicitly downgrades entry 515, especially mother field. |
| claim_probability | 0.41 | Possible but not sufficiently verified. |
| relevance | 0.86 | Directly relevant to staged identities and conversion QA. |
| canonical_readiness | 0.05 | Hold for complete image/continuation proof review. |

## Hypothesis 5: Witness-Only Names Are Separate Identity Mentions

Literal evidence:

- Entry 514 witness area names `Benjamin Utria` and `Ignacio Jara`.
- Entry 515 witness area names `Jose D. Ramirez` and `Santiago Fuentes`.

Interpretation:

- These are witness-only mentions. They should not be merged with canonical persons or used as family relationships without corroborating evidence.
- `Santiago Fuentes` should not be inferred as related to `Carmen Fuentes` from surname alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.50 | Names are present as witness labels, but no independent identity attributes are provided. |
| conflict_severity | 0.30 | Low if kept as witness mentions; higher only if merged by surname/name. |
| evidence_quality | 0.48 | Sparse witness-only register data. |
| conversion_confidence | 0.58 | D6a12b chunk reads them clearly, but entry 515 remains cropped. |
| claim_probability | 0.62 | Probable as mentions, not as relationships. |
| relevance | 0.58 | Useful to prevent witness-only merges. |
| canonical_readiness | 0.00 | Do not promote as people from this packet alone. |

## Required Pulgar-Line Anti-Conflation

The staged draft contains Pulgar-line names (`Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`) and existing wiki context includes broader Pulgar candidates. The comparison below is anti-conflation evidence only.

| Rank | Hypothesis | Probability | Evidence and next step |
| ---: | --- | ---: | --- |
| 1 | d6a12b entry 513 father/declarant is `Jose del Carmen Pulgar`; same as existing `wiki/people/jose-del-carmen-pulgar.md` draft stub | 0.66 | Exact name plus abbreviated declarant/father role in the same row. Next: targeted entry 513 image proof review and reconcile with `Jose del Carmen Pulgar S.` variants before promotion. |
| 2 | d6a12b entry 513 mother is `Juana de Dios Amagada de Pulgar`; same as existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` draft stub | 0.52 | Exact staged name exists, but mother surname is image-sensitive and conflicts with `Amador` in related material. Next: crop-level proof review of the mother field. |
| 3 | d6a12b entry 513 connects to `Juana Arriagada de Pulgar` / `Jose del Carmen Segundo Pulgar Arriagada` cluster | 0.38 | Shared Pulgar/Jose context and local entry-172 variants, but d6a12b literal names differ. Next: side-by-side proof review of the relevant page-172 entry images/chunks. |
| 4 | d6a12b entry 513 has any direct connection to canonical `Dario Arturo Pulgar-Smith` | 0.08 | Existing canonical Dario page is family-supplied and warns against automatic Pulgar merges; d6a12b does not name Dario, Arturo, Smith, grandchild, spouse, or occupation. Next: no Dario attachment from this page; revisit only with lineage evidence. |
| 5 | d6a12b entry 513 has any direct connection to `Dario Arturo Pulgar` CV cluster | 0.06 | No Dario/Arturo/CV evidence on this page. Next: none from this packet. |
| 6 | d6a12b entry 513 has any direct connection to `Dario Jose Pulgar-Arriagada` / `Dario Pulgar Arriagada` / `Darío Pulgar Arriagada` | 0.05 | Broad surname overlap only; no Dario, Jose-as-Dario, Arriagada-as-Dario, medical, Geneva, expropriation, or chronology bridge in the d6a12b page. Next: preserve as separate/unresolved; do not merge by name alone. |

## Conflict Summary

- Same-person conflict: `Jose del Carmen Pulgar` father and `Jose del C. Pulgar` declarant are probably the same person within entry 513, but proof review should confirm before promotion.
- Duplicate-person conflict: high risk if `Juana de Dios Amagada de Pulgar` is merged with `Juana Arriagada de Pulgar` or if the entry 513 child is merged with `Jose del Carmen Segundo Pulgar Arriagada` by contextual similarity rather than image proof.
- Name-variant conflict: `Amagada` versus `Amador` versus `Arriagada` remains unresolved; `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` remains unresolved in related local notes.
- Relationship conflict: entry 514 names Juan Soler only as spouse of Mercedes Riquelme, not father of Rigoberto Juan Bautista. Entry 515 mother/father relationship is blocked by the cropped row.
- Chronology conflict: no direct chronology conflict appears within d6a12b entries 513-515. Cross-cluster Dario/Pulgar chronology is irrelevant without a lineage bridge.
- Conversion/source conflict: entry 515 is the clearest conversion/source blocker; entry 513 and entry 514 have local competing proof-review readings that require targeted QA before canonical attachment.

## Recommended Next Action

Hold this staged identity draft for conversion QA and targeted proof review.

Exact next proof-review step: create or locate a complete source image/continuation image for page 172 and perform a side-by-side crop-level review of entries 513, 514, and 515. For entry 513, verify the child-name line, `Jose del Carmen Pulgar` father/declarant abbreviation, any `S.` suffix in related variants, and the mother surname (`Amagada`/`Amador`/`Arriagada`). For entry 514, verify whether the father field truly reads `Belisario Riquelme` or is blank/ignored/otherwise uncertain, while preserving Juan Soler only as Mercedes Riquelme's spouse clue. For entry 515, verify the full child name, father/declarant, and mother field from a complete row before any person or relationship promotion.

Do not merge or attach this page to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío Pulgar Arriagada` without a later reviewed identity bridge.
