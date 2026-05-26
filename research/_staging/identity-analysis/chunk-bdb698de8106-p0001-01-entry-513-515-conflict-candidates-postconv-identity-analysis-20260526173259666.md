---
type: identity_conflict_analysis
role: identity_researcher
worker: postconv-identity-analysis-20260526173259666
task_id: identity-analysis:research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md
staged_draft: research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526171453486.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
analysis_status: hold
canonical_readiness: not_ready
---

# Identity And Conflict Analysis: Entries 513 And 515

## Blockers

1. Entry 513 is not row-stable. The converted/chunk transcript reads child `Isolina del Carmen / José`, father `José del Carmen Pulgar`, mother `Juana de Dios Amador de Pulgar`, and declarant `José del C. Pulgar`; image-review notes preserve conflicting indicators for the child name, birth date/time, and mother surname, including `Juana de Dios Amagada de Pulgar`.
2. The entry 513 declarant/father reading is comparatively strong, but it remains part of a disputed row. Do not promote the declarant claim or parent-child relationship until conversion QA supplies a settled child and mother reading.
3. Entry 515 is partial/conflicted. The derivative transcript reads `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`, while reviewed notes warn that the bottom-cropped image does not securely support that identity. Treat entry 515 as a hold-only conflict indicator.
4. Existing wiki context already has separate Jose/Juana and Dario/Pulgar clusters. The staged draft does not prove that `Juana de Dios Amador de Pulgar`, `Juana de Dios Amagada de Pulgar`, or `Juana Arriagada de Pulgar` are the same person.
5. The staged draft does not name Dario, Arturo, Smith, Arriagada, Pulgar-Smith, `Dario Jose Pulgar-Arriagada`, or `Darío Pulgar Arriagada`. Any Dario-line comparison is an anti-conflation check only.

## Hypothesis 1: Hold Entries 513 And 515 As Registration-Scoped Conflict Candidates

Literal evidence:

- The exact staged draft is `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526171453486.md`.
- The revised source packet identifies page 1/register page 172, entries 513-515, and recommends `hold_for_conversion_qa`.
- Entry 513 literal converted support includes `José del Carmen Pulgar`, `Juana de Dios Amador de Pulgar`, and `José del C. Pulgar / Padre / Edad. Cuarenta i siete Años / Prof. Agricultor / Dom. Calle Colon`.
- Entry 515 literal converted support includes `Rosa Elvira del Carmen` and `Pedro Pablo Leiva / Padre`.

Interpretation:

- This is the leading hypothesis. The page is relevant and probably contains real identity evidence, but the staged draft is a conflict container, not a proof-ready identity packet.
- The literal conversion readings and image-review conflict indicators must travel together until targeted conversion QA resolves the rows.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.58 | Page-level identity candidates are real, but exact person identities are unsettled. |
| conflict_severity | 0.90 | Core child, mother, date/time, and entry-515 identity readings conflict. |
| evidence_quality | 0.62 | Civil-register evidence is strong in type, but decisive readings are not stable. |
| conversion_confidence | 0.32 | Current review explicitly says hold for conversion QA. |
| claim_probability | 0.66 | Probable that the page records the named families; not probable enough for exact claims. |
| relevance | 1.00 | Directly addresses the assigned staged conflict draft. |
| canonical_readiness | 0.05 | No canonical promotion, merge, or relationship attachment supported. |

## Hypothesis 2: Entry 513 Father/Declarant May Be The Existing Jose Del Carmen Pulgar Stub

Literal evidence:

- The bdb converted/chunk transcript reads father `José del Carmen Pulgar` and declarant `José del C. Pulgar`.
- The current conversion review note says the declarant-column reading is comparatively strong but blocked by row-level conflict.
- `wiki/people/jose-del-carmen-pulgar.md` exists as a separate stub with a draft child link to `Tulio Cesar Luis Jose` from a related staged relationship.

Interpretation:

- The father/declarant match is plausible, but not ready. The staged draft does not settle whether the child is `Isolina del Carmen José`, a `Pulgar Ama... / José` form, `Tulio Cesar Luis Jose`, or another corrected reading.
- Do not use the existing stub to force a parent-child relationship from this conflicted bdb row.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.55 | Same name and role align, but the row is not proof-ready. |
| conflict_severity | 0.74 | Wrong attachment could propagate an incorrect child identity. |
| evidence_quality | 0.56 | Good local evidence type; current draft is held. |
| conversion_confidence | 0.34 | Declarant is stronger than the row overall, but still held. |
| claim_probability | 0.50 | Possible same parent candidate, not proved. |
| relevance | 0.92 | Direct Jose parent-candidate comparison. |
| canonical_readiness | 0.08 | Requires post-QA parent-identity proof review. |

## Hypothesis 3: Entry 513 Mother Is A Juana Candidate, But Amador/Amagada/Arriagada Must Stay Separate

Literal evidence:

- The bdb converted/chunk transcript reads `Juana de Dios Amador de Pulgar`.
- The entry-513 image reconciliation note preserves `Juana de Dios Amagada de Pulgar [surname reading uncertain]` as a conflict indicator.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` exists as a separate stub with a draft child link to `Tulio Cesar Luis Jose`.
- `wiki/people/juana-arriagada-de-pulgar.md` exists separately and links to `Jose del Carmen Segundo Pulgar Arriagada` from a different local staged source.

Interpretation:

- `Amador`, `Amagada`, and `Arriagada` are not interchangeable at this proof stage. Family context justifies a double-check, not normalization.
- The most defensible action is to preserve all three as separate or unresolved hypotheses pending conversion QA and a dedicated parent-identity review.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.28 | Juana given-name context is present, but surname identity is the conflict. |
| conflict_severity | 0.86 | A silent surname correction could merge separate mother/child clusters. |
| evidence_quality | 0.50 | Existing stubs are useful context but do not resolve this row. |
| conversion_confidence | 0.25 | Mother surname is one of the disputed fields. |
| claim_probability | 0.24 | Plausible review lead only. |
| relevance | 0.94 | Required Jose/Juana parent-candidate comparison. |
| canonical_readiness | 0.02 | Do not merge or rename. |

## Hypothesis 4: Entry 515 Is A Leiva/Rosa Elvira Candidate

Literal evidence:

- The derivative transcript reads entry 515 as `Rosa Elvira del Carmen` with father/declarant `Pedro Pablo Leiva`.
- The staged conflict draft says entry 515 is bottom-cropped/partial and conflicts with converted child-name and father/declarant readings.

Interpretation:

- This hypothesis is possible only as a derivative transcription reading. It is not proof-ready identity evidence.
- Entry 515 does not support the Pulgar line from this staged draft.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.20 | Name appears in derivative transcript, but image support is explicitly disputed. |
| conflict_severity | 0.82 | Promoting could create a false child/father identity. |
| evidence_quality | 0.38 | Partial row and conflict-review hold. |
| conversion_confidence | 0.18 | Bottom-cropped/partial visibility is the main blocker. |
| claim_probability | 0.20 | Treat as possible but unverified. |
| relevance | 0.76 | Directly part of assigned entries 513-515 conflict draft. |
| canonical_readiness | 0.00 | No promotion supported. |

## Hypothesis 5: Relevance To Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Literal evidence:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to merge similarly named source clusters automatically.
- Staged CV identity candidates refer to document-level `Dario Arturo Pulgar`, but those records are separate CV-context material and do not cite this 1889 birth-register row.
- The assigned conflict draft names no Dario, Arturo, Smith, spouse, child, grandchild, or lineage bridge.

Interpretation:

- This is only a remote Pulgar-line lead. No same-person, duplicate-person, or ancestor relationship can be inferred from surname context.
- Exact next proof step, after entry 513 QA: run a separate lineage proof review from the confirmed entry-513 child/parents to accepted Dario evidence, and separately review any bridge from staged `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct Dario evidence in this draft. |
| conflict_severity | 0.78 | Premature attachment would create unsupported lineage. |
| evidence_quality | 0.42 | Existing Dario context is local but unbridged to this row. |
| conversion_confidence | 0.32 | Underlying register row still needs QA. |
| claim_probability | 0.06 | Very low from this source alone. |
| relevance | 0.70 | Required Pulgar-line guardrail. |
| canonical_readiness | 0.00 | No canonical action. |

## Hypothesis 6: Same As Dario Jose Pulgar-Arriagada Or Dario/Darío Pulgar Arriagada

Literal evidence:

- A staged claim for `Dario Jose Pulgar-Arriagada` is a source-path/context photograph lead and says the person is not named in visible image text.
- `wiki/people/dar-o-pulgar-arriagada.md` contains a reviewed 2000 expropriation event for `Darío Pulgar Arriagada`.
- The assigned 1889 conflict draft does not contain `Dario`, `Darío`, `Dario Jose`, or a confirmed `Arriagada` surname reading.

Interpretation:

- This hypothesis is not supported by the assigned draft. It remains listed only to make the anti-conflation comparison explicit.
- Do not compare these Dario Arriagada clusters for same-person resolution until entry 513 has a settled child name, mother surname, date, and parent fields.

Scores:

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
- Duplicate-person conflict: possible for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar`, but blocked by child-name and mother-surname instability.
- Name-variant conflict: `Juana de Dios Amador de Pulgar` versus `Juana de Dios Amagada de Pulgar`; `Juana Arriagada de Pulgar` is only a family-context double-check lead. Do not silently correct one to another.
- Relationship conflict: entry 513 parent-child relationship cannot be promoted because the child identity and mother surname are not settled. Entry 515 child-father relationship cannot be promoted because the visible source support is partial/conflicted.
- Chronology conflict: no Dario-line chronology can be evaluated from this draft because no Dario identity appears. Entry-level birth date/time for entry 513 remains a conversion-QA issue.
- Conversion conflict: the current bdb chunk path is present, but the converted text and image-reviewed notes still materially disagree on identity-bearing fields.

## Ranked Hypotheses

| rank | hypothesis | probability | next proof-review or promotion step |
|---:|---|---:|---|
| 1 | Hold entries 513 and 515 as registration-scoped conflict candidates | 0.66 | Targeted conversion QA for entries 513 and 515, then rerun proof review. |
| 2 | Entry 513 father/declarant may be existing `Jose del Carmen Pulgar` | 0.50 | After row QA, run parent-identity proof review against the Jose stub and relationship pages. |
| 3 | Entry 513 mother is an unresolved Juana Amador/Amagada/Arriagada candidate | 0.24 | After row QA, compare `Amador`, `Amagada`, and `Arriagada` variants without normalization. |
| 4 | Entry 515 is a Leiva/Rosa Elvira candidate | 0.20 | Confirm the lower/partial row before any child/father claim. |
| 5 | Remote relevance to `Dario Arturo Pulgar-Smith` or staged `Dario Arturo Pulgar` | 0.06 | Requires explicit lineage bridge after entry 513 is settled. |
| 6 | Same as `Dario Jose Pulgar-Arriagada` or `Dario/Darío Pulgar Arriagada` | 0.02 | Preserve separately; require direct name/date/relationship continuity before comparison. |

## Recommended Next Action

Keep the exact staged conflict draft on `hold_for_conversion_qa`. Do not promote facts, merge people, rename canonical pages, or attach entries 513/515 to any Dario/Pulgar canonical identity.

The exact next step is targeted conversion QA for the referenced source image, converted file, and chunk: settle entry 513 child full name, birth date/time, father/declarant form, and mother surname; settle whether entry 515 supports `Rosa Elvira del Carmen` and `Pedro Pablo Leiva` or must remain partial/unknown. After QA, rerun proof review on atomic claims, then run a separate parent-identity proof review comparing the confirmed entry 513 readings to `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and any other Jose/Juana candidates before any broader Pulgar-line or Dario bridge review.
