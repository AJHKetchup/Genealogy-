---
type: identity_conflict_analysis
role: identity_researcher
worker: postconv-identity-analysis-20260526174648032
task_id: identity-analysis:research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md
staged_draft: research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526171453486.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity And Conflict Analysis: Entries 513 And 515

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md`.
- No external research was performed. This note uses the staged draft, referenced source packet, referenced converted/chunk files, prior local reviewed notes, and existing canonical wiki pages only.
- The requested `$genealogy-proof-review` skill was not installed in this session's available skill list. This analysis therefore treats the proof-review revision draft and its referenced local evidence as the controlling evidence contract.
- Entry 513 is row-level unstable. The derivative transcript reads child `Isolina del Carmen / José`, sex `Masculino`, father `José del Carmen Pulgar`, mother `Juana de Dios Amador de Pulgar`, and declarant `José del C. Pulgar`, but the staged proof-review revision says child name, birth details, and mother surname remain unresolved against image review.
- Entry 513's declarant field is stronger than the rest of the row, but it is still blocked by the row-level conversion conflict. Do not promote father/declarant, parent-child, or child-identity claims from this draft.
- Entry 515 is bottom-cropped/partial in the reviewed evidence. The derivative reading `Rosa Elvira del Carmen` and `Pedro Pablo Leiva` is not secure enough for identity promotion.
- Existing wiki pages for `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Dario Arturo Pulgar-Smith`, and `Darío Pulgar Arriagada` are relevant comparison context only. This draft does not support merging, renaming, or attaching facts to any of them.

## Hypothesis 1: Registration-Scoped Conflict Candidates

Hypothesis: entries 513 and 515 should remain registration-scoped conflict candidates until targeted conversion QA reconciles the source image, converted transcript, chunk, and reviewed notes.

Literal evidence:

- The source packet identifies page 172 of an 1889 Los Angeles/La Laja civil birth register, entries 513-515, and recommends `hold_for_conversion_qa`.
- Entry 513 derivative text includes `José del Carmen Pulgar`, `Juana de Dios Amador de Pulgar`, and `José del C. Pulgar / Padre / Edad. Cuarenta i siete Años / Prof. Agricultor / Dom. Calle Colon`.
- Entry 515 derivative text includes `Rosa Elvira del Carmen` and `Pedro Pablo Leiva / Padre`.
- The staged conflict draft explicitly says entry 513 has unresolved conflicts in child name, birth details, and mother surname, while entry 515 is an unresolved derivative reading.

Interpretation:

- This is the leading hypothesis. The page likely contains useful identity evidence, but this staged draft is a hold container rather than a proof-ready identity packet.
- Literal derivative readings and image-review disagreement must remain together until conversion QA settles the rows.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.58 | The register entries exist as local candidates, but exact identities are unsettled. |
| conflict_severity | 0.90 | Core child, mother, date/time, and entry-515 identity fields conflict. |
| evidence_quality | 0.62 | Civil register evidence is valuable, but decisive readings are not stable. |
| conversion_confidence | 0.32 | The proof-review revision explicitly holds for conversion QA. |
| claim_probability | 0.66 | Probable that the page records these families; exact claims remain unproved. |
| relevance | 1.00 | Directly addresses the assigned staged conflict draft. |
| canonical_readiness | 0.05 | No canonical promotion or relationship attachment is supported. |

## Hypothesis 2: Entry 513 Father/Declarant May Be Existing Jose Del Carmen Pulgar

Hypothesis: the entry 513 father/declarant could be the same candidate represented by `wiki/people/jose-del-carmen-pulgar.md`.

Literal evidence:

- The converted/chunk transcript reads father `José del Carmen Pulgar`.
- The compareciente field reads `José del C. Pulgar`, role `Padre`, age forty-seven, farmer, resident at Calle Colon.
- The existing `Jose del Carmen Pulgar` wiki page is a stub and has a draft child link to `Tulio Cesar Luis Jose`.

Interpretation:

- The father/declarant match is plausible because the name and role align.
- It is not proof-ready because the child name and mother surname are exactly the disputed row fields. The existing stub cannot be used to force a relationship or normalize the row.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.55 | Name and role align, but the row remains held. |
| conflict_severity | 0.74 | Wrong attachment could propagate an incorrect child identity. |
| evidence_quality | 0.56 | Useful local evidence, but the row is not proof-reviewed for promotion. |
| conversion_confidence | 0.34 | Declarant is comparatively stronger than the rest of entry 513, not settled. |
| claim_probability | 0.50 | Possible same parent candidate, not proved. |
| relevance | 0.92 | Direct Jose parent-candidate comparison. |
| canonical_readiness | 0.08 | Requires post-QA parent-identity proof review. |

## Hypothesis 3: Entry 513 Mother Is An Unresolved Juana Amador/Amagada/Arriagada Candidate

Hypothesis: entry 513's mother line may relate to one of the local Juana candidates, but the surname must remain unresolved until QA.

Literal evidence:

- The converted/chunk transcript reads `Juana de Dios Amador de Pulgar`.
- Prior local review context and existing notes preserve `Juana de Dios Amagada de Pulgar` as an alternate image-sensitive reading.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` exists as a separate stub with a draft child link to `Tulio Cesar Luis Jose`.
- `wiki/people/juana-arriagada-de-pulgar.md` exists separately and links to `Jose del Carmen Segundo Pulgar Arriagada` from another staged birth-register cluster.

Interpretation:

- `Amador`, `Amagada`, and `Arriagada` are not interchangeable at this proof stage.
- Family-context similarity justifies a targeted double-check after conversion QA, not a silent correction or merge.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.28 | Juana context is present, but surname identity is the conflict. |
| conflict_severity | 0.86 | Silent surname normalization could merge separate mother/child clusters. |
| evidence_quality | 0.50 | Existing stubs are useful context but do not resolve the row. |
| conversion_confidence | 0.25 | Mother surname is one of the disputed fields. |
| claim_probability | 0.24 | Plausible review lead only. |
| relevance | 0.94 | Required Jose/Juana parent-candidate comparison. |
| canonical_readiness | 0.02 | Do not merge, rename, or attach. |

## Hypothesis 4: Entry 515 Is A Rosa Elvira / Pedro Pablo Leiva Candidate

Hypothesis: entry 515 may record a child `Rosa Elvira del Carmen` with father/declarant `Pedro Pablo Leiva`, but the partial image support blocks identity use.

Literal evidence:

- The derivative transcript reads entry 515 as `Rosa Elvira del Carmen`.
- The derivative transcript reads father/declarant `Pedro Pablo Leiva`.
- The staged conflict draft says entry 515 is bottom-cropped/partial and the converted identity is an unresolved derivative reading only.

Interpretation:

- Entry 515 should not be used to create or attach a child/father identity.
- It has no direct Pulgar-line value in this staged draft.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.20 | Names appear in derivative transcript, but image support is disputed. |
| conflict_severity | 0.82 | Promotion could create a false child/father identity. |
| evidence_quality | 0.38 | Partial row and proof-review hold. |
| conversion_confidence | 0.18 | Bottom-cropped/partial visibility is the controlling blocker. |
| claim_probability | 0.20 | Possible but unverified. |
| relevance | 0.76 | Directly part of the assigned entry 513-515 conflict draft. |
| canonical_readiness | 0.00 | No promotion supported. |

## Hypothesis 5: Remote Relevance To Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Hypothesis: entry 513 could eventually be relevant to the broader Pulgar line containing canonical `Dario Arturo Pulgar-Smith` or staged `Dario Arturo Pulgar` evidence.

Literal evidence:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and warns that similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records require identity review before attachment.
- Local staged CV context identifies a document-level `Dario Arturo Pulgar`, but those staged CV notes do not bridge this 1889 register row to that person.
- The assigned staged draft contains no `Dario`, `Arturo`, `Smith`, spouse, descendant, or child-of-Dario statement.

Interpretation:

- This is a remote lineage lead only. Surname context and possible Jose/Juana parent candidates are not identity proof.
- The exact next proof step, after entry 513 conversion QA, is a separate lineage proof review from the confirmed child/parents to accepted Dario evidence, and a separate bridge review from staged `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct Dario evidence appears in this draft. |
| conflict_severity | 0.78 | Premature attachment would create unsupported lineage. |
| evidence_quality | 0.42 | Existing Dario context is local but unbridged to this row. |
| conversion_confidence | 0.32 | The underlying register row still needs QA. |
| claim_probability | 0.06 | Very low from this source alone. |
| relevance | 0.70 | Required Pulgar-line guardrail. |
| canonical_readiness | 0.00 | No canonical action. |

## Hypothesis 6: Same As Dario Jose Pulgar-Arriagada Or Dario/Dario Pulgar Arriagada

Hypothesis: one of the entry 513 candidates is the same person as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar A.`, or canonical `Darío Pulgar Arriagada`.

Literal evidence:

- Existing staged `Dario Jose Pulgar-Arriagada` material is separate photo, professional, medical, or metadata context, not a direct source for this 1889 register row.
- `wiki/people/dar-o-pulgar-arriagada.md` currently contains a 2000-12-05 expropriation event for `Darío Pulgar Arriagada`.
- The assigned staged draft does not contain `Dario`, `Darío`, `Dario Jose`, `Dario Pulgar A.`, or a confirmed `Arriagada` reading.

Interpretation:

- This same-person hypothesis is not supported by the assigned draft.
- It remains listed only for the required Pulgar-line anti-conflation comparison. Keep these identities separate unless later proof-reviewed evidence supplies direct name/date/relationship continuity.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.02 | No direct name or chronology bridge. |
| conflict_severity | 0.88 | Name-only merging would likely conflate generations or separate clusters. |
| evidence_quality | 0.36 | Compared evidence is local but outside and unbridged to this row. |
| conversion_confidence | 0.25 | The possible surname bridge is unresolved. |
| claim_probability | 0.02 | Not probable from current evidence. |
| relevance | 0.62 | Required Dario/Pulgar comparison. |
| canonical_readiness | 0.00 | Keep separate. |

## Conflicts

- Same-person conflict: unresolved. No person in this staged draft is ready for same-person matching to an existing canonical page.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` because local stubs already exist; high if the disputed child name or mother surname is forced into those stubs.
- Name-variant conflict: `Juana de Dios Amador de Pulgar` versus `Juana de Dios Amagada de Pulgar`; `Juana Arriagada de Pulgar` remains only a family-context double-check lead.
- Relationship conflict: entry 513 parent-child relationships cannot be promoted while child identity, birth details, and mother surname remain unsettled. Entry 515 child-father relationship cannot be promoted while the lower row is partial/conflicted.
- Chronology conflict: no Dario-line chronology can be evaluated from this draft because no Dario identity appears. Entry 513 date/time remains part of conversion QA.
- Conversion conflict: the converted/chunk text and image-reviewed proof-review notes materially disagree on identity-bearing fields for entries 513 and 515.

## Ranked Hypotheses

| rank | hypothesis | probability | next proof-review or promotion step |
|---:|---|---:|---|
| 1 | Hold entries 513 and 515 as registration-scoped conflict candidates | 0.66 | Targeted conversion QA for entries 513 and 515, then rerun proof review. |
| 2 | Entry 513 father/declarant may be existing `Jose del Carmen Pulgar` | 0.50 | After row QA, run parent-identity proof review against Jose stubs and relationship pages. |
| 3 | Entry 513 mother is an unresolved Juana Amador/Amagada/Arriagada candidate | 0.24 | After row QA, compare the three surname readings without normalization. |
| 4 | Entry 515 is a Rosa Elvira / Pedro Pablo Leiva candidate | 0.20 | Confirm the lower/partial row before any child/father claim. |
| 5 | Remote relevance to `Dario Arturo Pulgar-Smith` or staged `Dario Arturo Pulgar` | 0.06 | Requires explicit lineage bridge after entry 513 is settled. |
| 6 | Same as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar A.`, or `Dario/Darío Pulgar Arriagada` | 0.02 | Preserve separately; require direct continuity before comparison. |

## Recommended Next Action

Keep the exact staged conflict draft on `hold_for_conversion_qa`. Do not promote facts, merge people, rename canonical pages, or attach entries 513/515 to any Dario/Pulgar canonical identity.

The exact next step is targeted conversion QA for the referenced source image, converted file, and chunk. Settle entry 513 child full name, sex, birth date/time, father/declarant form, father age/profession/residence, and mother surname; settle whether entry 515 supports `Rosa Elvira del Carmen` and `Pedro Pablo Leiva` or must remain partial/unknown. After QA, rerun proof review on atomic claims, then run a separate parent-identity proof review comparing the confirmed entry 513 readings to `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and other Jose/Juana candidates before any broader Pulgar-line or Dario bridge review.
