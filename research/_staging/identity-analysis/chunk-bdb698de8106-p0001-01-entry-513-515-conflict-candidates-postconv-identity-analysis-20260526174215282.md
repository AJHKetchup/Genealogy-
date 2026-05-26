---
type: identity_conflict_analysis
role: identity_researcher
worker: postconv-identity-analysis-20260526174215282
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

1. Exact staged draft analyzed: `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md`.
2. The `$genealogy-proof-review` skill file was not installed in the advertised skill list for this session; this note therefore treats the staged proof-review revision, source packet, reviewed notes, converted file, chunk file, and existing canonical wiki pages as the evidence contract.
3. Entry 513 is not row-stable. The converted/chunk transcript reads child `Isolina del Carmen / José`, sex `Masculino`, father `José del Carmen Pulgar`, mother `Juana de Dios Amador de Pulgar`, and declarant `José del C. Pulgar`; the current local QA follow-up says the child-name field, birth details, and mother surname remain materially conflicted against image review.
4. The entry 513 declarant claim is comparatively strong only as a narrow appearance claim. It must not be promoted as a canonical biographical fact or parent-child relationship until conversion QA stabilizes the full row.
5. Entry 515 is bottom-cropped/partial in the reviewed evidence. The derivative transcript reads `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`, but the revised claim keeps that as unresolved and not promotion-ready.
6. Existing wiki context contains separate `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Dario Arturo Pulgar-Smith`, and `Darío Pulgar Arriagada` pages. This draft does not justify merging, renaming, or attaching any of them by name proximity.

## Hypothesis 1: Entries 513 And 515 Are Registration-Scoped Conflict Candidates

Literal evidence:

- The assigned source packet identifies page 172, entries 513-515, in an 1889 Los Angeles/La Laja civil birth-register page and recommends `hold_for_conversion_qa`.
- Entry 513 converted/chunk text includes `José del Carmen Pulgar`, `Juana de Dios Amador de Pulgar`, and `José del C. Pulgar / Padre / Edad. Cuarenta i siete Años / Prof. Agricultor / Dom. Calle Colon`.
- Entry 515 converted/chunk text includes `Rosa Elvira del Carmen` and `Pedro Pablo Leiva / Padre`.

Interpretation:

- This is the leading hypothesis. The page likely contains useful identity evidence, but the assigned draft is a conflict container, not a proof-ready identity packet.
- Keep derivative text, image-review concerns, and proof-review hold together until targeted conversion QA resolves the rows.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.58 | Real entry-level candidates are present, but exact person identities are unsettled. |
| conflict_severity | 0.90 | Core child, mother, date/time, and entry-515 identity fields conflict. |
| evidence_quality | 0.62 | Civil-register evidence is strong in type; decisive readings are unstable. |
| conversion_confidence | 0.32 | The reviewed draft and QA follow-up explicitly hold for conversion QA. |
| claim_probability | 0.66 | Probable that the page records these families; exact claims remain unproved. |
| relevance | 1.00 | Directly addresses the assigned staged conflict draft. |
| canonical_readiness | 0.05 | No canonical promotion or relationship attachment supported. |

## Hypothesis 2: Entry 513 Father/Declarant May Be Existing Jose Del Carmen Pulgar

Literal evidence:

- The converted/chunk transcript reads father `José del Carmen Pulgar` and declarant `José del C. Pulgar`.
- The revised entry-513 declarant claim has confidence `0.82` for the narrow appearance: father, age 47, farmer, domiciled Calle Colon.
- `wiki/people/jose-del-carmen-pulgar.md` exists as a stub with a draft child link to `Tulio Cesar Luis Jose`.

Interpretation:

- The same-name father/declarant match is plausible, but not proof-ready. The existing stub must not be used to force a child identity or parent-child relationship from this conflicted row.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.55 | Name and role align; row-level identity remains unsettled. |
| conflict_severity | 0.74 | Wrong attachment could propagate an incorrect child identity. |
| evidence_quality | 0.56 | Useful local evidence, but the assigned row is held. |
| conversion_confidence | 0.34 | Declarant field is stronger than the row overall, but still held. |
| claim_probability | 0.50 | Possible same parent candidate, not proved. |
| relevance | 0.92 | Direct Jose parent-candidate comparison. |
| canonical_readiness | 0.08 | Requires post-QA parent-identity proof review. |

## Hypothesis 3: Entry 513 Mother Is An Unresolved Juana Amador/Amagada/Arriagada Candidate

Literal evidence:

- The converted/chunk transcript reads `Juana de Dios Amador de Pulgar`.
- The local conversion QA follow-up says the mother surname is image-sensitive and appears closer to an `Arriagada`/`Amagada`-style reading than to converted `Amador`, but it does not replace the transcription by inference.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` exists as a separate stub with a draft child link to `Tulio Cesar Luis Jose`.
- `wiki/people/juana-arriagada-de-pulgar.md` exists separately and links to `Jose del Carmen Segundo Pulgar Arriagada` from another staged birth-register cluster.

Interpretation:

- `Amador`, `Amagada`, and `Arriagada` must remain separate literal or hypothesized readings at this proof stage. Family-context similarity justifies a double-check, not a silent correction.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.28 | Juana given-name context is present, but surname identity is the conflict. |
| conflict_severity | 0.86 | Silent surname correction could merge separate mother/child clusters. |
| evidence_quality | 0.50 | Existing stubs are useful context but do not resolve this row. |
| conversion_confidence | 0.25 | Mother surname is one of the disputed fields. |
| claim_probability | 0.24 | Plausible review lead only. |
| relevance | 0.94 | Required Jose/Juana parent-candidate comparison. |
| canonical_readiness | 0.02 | Do not merge or rename. |

## Hypothesis 4: Entry 515 Is A Leiva/Rosa Elvira Candidate

Literal evidence:

- The derivative transcript reads entry 515 as `Rosa Elvira del Carmen` with father/declarant `Pedro Pablo Leiva`.
- The revised entry-515 child-name claim has confidence `0.18` and says the partial source image does not securely support promoting `Rosa Elvira del Carmen`.

Interpretation:

- This remains a derivative reading only. Entry 515 does not support a Pulgar-line claim from this staged draft.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.20 | Name appears in derivative transcript, but image support is disputed. |
| conflict_severity | 0.82 | Promotion could create a false child/father identity. |
| evidence_quality | 0.38 | Partial row and proof-review hold. |
| conversion_confidence | 0.18 | Bottom-cropped/partial visibility is the controlling blocker. |
| claim_probability | 0.20 | Possible but unverified. |
| relevance | 0.76 | Directly part of assigned entries 513-515 conflict draft. |
| canonical_readiness | 0.00 | No promotion supported. |

## Hypothesis 5: Relevance To Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Literal evidence:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and warns not to automatically merge similarly named Pulgar source clusters.
- Local staged CV context uses document-level `Dario Arturo Pulgar`, but it is separate from this 1889 register row and does not provide a lineage bridge here.
- The assigned draft names no Dario, Arturo, Smith, grandchild, spouse, descendant, or child-of-Dario relationship.

Interpretation:

- This is only a remote Pulgar-line lead. No same-person, duplicate-person, or ancestor relationship can be inferred from surname context.
- Exact next proof step, after entry 513 QA: run a separate lineage proof review from the confirmed entry-513 child/parents to accepted Dario evidence, and separately review any bridge from staged `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct Dario evidence in this draft. |
| conflict_severity | 0.78 | Premature attachment would create unsupported lineage. |
| evidence_quality | 0.42 | Existing Dario context is local but unbridged to this row. |
| conversion_confidence | 0.32 | Underlying register row still needs QA. |
| claim_probability | 0.06 | Very low from this source alone. |
| relevance | 0.70 | Required Pulgar-line guardrail. |
| canonical_readiness | 0.00 | No canonical action. |

## Hypothesis 6: Same As Dario Jose Pulgar-Arriagada Or Dario/Dario Pulgar Arriagada

Literal evidence:

- Existing staged `Dario Jose Pulgar-Arriagada` material is separate photo, professional, medical, or metadata context and is not referenced by the assigned 1889 entry-513/515 draft.
- `wiki/people/dar-o-pulgar-arriagada.md` currently contains only a 2000-12-05 expropriation event for `Darío Pulgar Arriagada`.
- The assigned 1889 conflict draft does not contain `Dario`, `Darío`, `Dario Jose`, `Dario Pulgar A.`, or a confirmed `Arriagada` reading.

Interpretation:

- This hypothesis is not supported by the assigned draft. It is listed only to satisfy the required Pulgar-line anti-conflation comparison.
- Do not compare these Dario clusters for same-person resolution until entry 513 has a settled child name, mother surname, date/time, and parent fields.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.02 | No direct name or chronology bridge. |
| conflict_severity | 0.88 | Name-only merging would likely conflate generations or separate clusters. |
| evidence_quality | 0.36 | Compared evidence is local but outside and unbridged to this row. |
| conversion_confidence | 0.25 | Potential surname bridge is unresolved. |
| claim_probability | 0.02 | Not probable from current evidence. |
| relevance | 0.62 | Required Dario/Pulgar comparison. |
| canonical_readiness | 0.00 | Keep separate. |

## Conflicts

- Same-person conflict: unresolved. No person named or implied in the staged draft is ready for same-person matching to an existing canonical page.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar`, but blocked by child-name and mother-surname instability.
- Name-variant conflict: `Juana de Dios Amador de Pulgar` versus `Juana de Dios Amagada de Pulgar`; `Juana Arriagada de Pulgar` is only a family-context double-check lead.
- Relationship conflict: entry 513 parent-child relationship cannot be promoted because the child identity and mother surname are not settled. Entry 515 child-father relationship cannot be promoted because visible source support is partial/conflicted.
- Chronology conflict: no Dario-line chronology can be evaluated from this draft because no Dario identity appears. Entry-level birth date/time for entry 513 remains a conversion-QA issue.
- Conversion conflict: the converted text and image-reviewed notes materially disagree on identity-bearing fields for entries 513 and 515.

## Ranked Hypotheses

| rank | hypothesis | probability | next proof-review or promotion step |
|---:|---|---:|---|
| 1 | Hold entries 513 and 515 as registration-scoped conflict candidates | 0.66 | Targeted conversion QA for entries 513 and 515, then rerun proof review. |
| 2 | Entry 513 father/declarant may be existing `Jose del Carmen Pulgar` | 0.50 | After row QA, run parent-identity proof review against Jose stubs and relationship pages. |
| 3 | Entry 513 mother is an unresolved Juana Amador/Amagada/Arriagada candidate | 0.24 | After row QA, compare the three surname readings without normalization. |
| 4 | Entry 515 is a Leiva/Rosa Elvira candidate | 0.20 | Confirm the lower/partial row before any child/father claim. |
| 5 | Remote relevance to `Dario Arturo Pulgar-Smith` or staged `Dario Arturo Pulgar` | 0.06 | Requires explicit lineage bridge after entry 513 is settled. |
| 6 | Same as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar A.`, or `Dario/Darío Pulgar Arriagada` | 0.02 | Preserve separately; require direct name/date/relationship continuity before comparison. |

## Recommended Next Action

Keep the exact staged conflict draft on `hold_for_conversion_qa`. Do not promote facts, merge people, rename canonical pages, or attach entries 513/515 to any Dario/Pulgar canonical identity.

The exact next step is targeted conversion QA for the referenced source image, converted file, and chunk: settle entry 513 child full name, sex, birth date/time, father/declarant form, father age/profession/residence, and mother surname; settle whether entry 515 supports `Rosa Elvira del Carmen` and `Pedro Pablo Leiva` or must remain partial/unknown. After QA, rerun proof review on atomic claims, then run a separate parent-identity proof review comparing the confirmed entry 513 readings to `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and other Jose/Juana candidates before any broader Pulgar-line or Dario bridge review.
