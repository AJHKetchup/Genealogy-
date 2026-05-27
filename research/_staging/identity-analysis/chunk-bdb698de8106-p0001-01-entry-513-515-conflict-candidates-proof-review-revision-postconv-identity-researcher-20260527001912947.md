---
type: identity_conflict_analysis
role: identity_researcher
worker: postconv-identity-analysis-20260527001912947
task_id: identity-analysis:research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
staged_draft: research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526232219797.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
analysis_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entries 513 And 515

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526232219797.md`.
- No external research was performed. This note uses only the assigned staged draft, its referenced source packet, referenced converted/chunk files, reviewed notes found in the workspace, and existing canonical wiki pages.
- Conversion confidence is low. The converted file and assigned chunk agree with each other, but the assigned conflict draft says proof review preserved unresolved image-reviewed disagreement in identity-controlling fields.
- Entry 513 child identity is unresolved. The derivative transcript in this assigned bdb set reads `Isolina del Carmen` / `Jose` with `Masculino`; reviewed local notes for related entry-513 work preserve competing `Pulgar Ama...` and `Jose...` readings. No child-name reading is canonical-ready.
- Entry 513 mother surname is unresolved. The derivative transcript reads `Juana de Dios Amador de Pulgar`; the proof-review concern preserves an `Amagada`-style reading. Do not normalize either to `Arriagada` from family context alone.
- Entry 513 father/declarant profession needs QA. The assigned source packet keeps `Agricultor` but also flags profession verification as a held field.
- Entry 515 is a boundary/control conflict only for this Pulgar analysis. The derivative transcript reads `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`; proof review says the partial image evidence is not secure enough for promotion and may require surname reconciliation.
- The assigned draft does not name Dario, Arturo, Smith, Pulgar-Smith, Dario Jose Pulgar-Arriagada, or Dario/Darío Pulgar Arriagada. Pulgar-line comparisons below are anti-conflation checks only.

## Hypothesis 1: Hold Entry 513 As A Registration-Scoped Pulgar Conflict Candidate

Literal evidence:

- The assigned source packet identifies page 172 of an 1889 Los Angeles/La Laja civil birth register, entries 513-515.
- Entry 513 derivative text names `Jose del Carmen Pulgar` as father and `Jose del C. Pulgar` as father/declarant, with domicile `Calle Colon`.
- Entry 513 derivative text names the mother as `Juana de Dios Amador de Pulgar`, while the conflict draft preserves an `Amagada`-style concern rather than a replacement transcription.

Interpretation:

This is the leading hypothesis. Entry 513 is likely family-relevant Pulgar evidence, but the child name, mother surname, and profession remain blocked by conversion QA. It should remain a staged conflict candidate, not a promoted person or relationship.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.58 | Father/declarant Pulgar support is useful; exact child and mother identities are unsettled. |
| conflict_severity | 0.88 | Core name and relationship fields are disputed. |
| evidence_quality | 0.60 | Civil register evidence is strong in type, but the decisive readings are not settled. |
| conversion_confidence | 0.30 | Assigned draft and source packet both mark low confidence/hold. |
| claim_probability | 0.66 | Probable that this row is Pulgar-relevant; not probable enough for exact identity promotion. |
| relevance | 0.98 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.06 | Hold for targeted conversion QA and proof review. |

## Hypothesis 2: Entry 513 Jose/Juana Pair May Match Existing Jose/Juana Amagada Stubs

Literal evidence:

- Existing `wiki/people/jose-del-carmen-pulgar.md` has a draft child link to `Tulio Cesar Luis Jose`.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` has a draft child link to `Tulio Cesar Luis Jose`.
- The assigned draft supports a father/declarant named `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, and preserves a mother-surname conflict involving `Juana de Dios Amador de Pulgar` versus an `Amagada`-style concern.

Interpretation:

This is plausible but blocked. The father name aligns with an existing stub, and the `Juana de Dios ... de Pulgar` form is close to the existing Amagada stub. The exact child identity and mother surname are the unresolved issues, so existing stubs must not be used to force a reading.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.52 | Father aligns; mother and child identities are unresolved. |
| conflict_severity | 0.76 | Premature attachment could propagate the wrong mother surname or child name. |
| evidence_quality | 0.52 | Existing pages are draft/stub context, not independent proof for this task. |
| conversion_confidence | 0.28 | The possible matching surname is conversion-sensitive. |
| claim_probability | 0.48 | Possible parent-pair match, not proved. |
| relevance | 0.92 | Direct Jose/Juana comparison is required by the assignment. |
| canonical_readiness | 0.10 | No merge, rename, or promoted fact supported. |

## Hypothesis 3: Entry 513 Is Related To The Juana Arriagada / Jose Del Carmen Segundo Cluster

Literal evidence:

- Existing `wiki/people/juana-arriagada-de-pulgar.md` links to `Jose del Carmen Segundo Pulgar Arriagada` from a separate staged entry-172 packet.
- Existing `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` preserves an 1888 birth-registration cluster with mother `Juana Arriagada de Pulgar`.
- The assigned bdb draft is an 1889 entry-513 conflict and does not confirm `Arriagada`; it preserves `Amador` versus `Amagada`-style uncertainty.

Interpretation:

Shared Pulgar/Jose/Juana/Los Angeles context justifies a later double-check, but not a same-person conclusion. `Amador`, `Amagada`, and `Arriagada` must remain separate readings until a targeted proof-review step resolves the register text and any lineage bridge.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.20 | Similar context only; no confirmed surname bridge. |
| conflict_severity | 0.82 | Merge risk across separate children, years, and surname readings. |
| evidence_quality | 0.46 | Both clusters include staged/held evidence. |
| conversion_confidence | 0.26 | The disputed surname is the possible bridge. |
| claim_probability | 0.18 | Review lead only. |
| relevance | 0.84 | Required because Jose/Juana parent candidates exist in wiki context. |
| canonical_readiness | 0.02 | Do not merge or attach. |

## Hypothesis 4: Ancestor-Line Lead For Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Literal evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic attachment of similarly named Pulgar records.
- Staged CV packets elsewhere identify a document-level `Dario Arturo Pulgar`, but this assigned entry-513/515 draft does not state Dario, Arturo, Smith, Pulgar-Smith, a descendant, or a bridge to a CV subject.

Interpretation:

This is a low-confidence lineage lead only. The exact proof step needed next is not a Dario merge; it is targeted conversion QA for entry 513, followed by proof review of any confirmed child/parent relationship. Only after that could a separate lineage proof review test a bridge to `Dario Arturo Pulgar`, and then separately to `Dario Arturo Pulgar-Smith`.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct Dario evidence in the assigned draft. |
| conflict_severity | 0.78 | Unsupported ancestor-line attachment would be misleading. |
| evidence_quality | 0.40 | Contextual only for Dario-line identities. |
| conversion_confidence | 0.30 | Register identities are not settled. |
| claim_probability | 0.07 | Very low from this source alone. |
| relevance | 0.66 | Relevant as a Pulgar-line guardrail. |
| canonical_readiness | 0.00 | No canonical action supported. |

## Hypothesis 5: Same As Dario Jose Pulgar-Arriagada Or Dario/Darío Pulgar Arriagada

Literal evidence:

- Existing `wiki/people/dar-o-pulgar-arriagada.md` has a scoped 2000 expropriation-event evidence snapshot for `Darío Pulgar Arriagada`.
- Staged `Dario Jose Pulgar-Arriagada` materials elsewhere are separate photograph/metadata/professional-context records.
- The assigned draft has no `Dario` given name and no confirmed `Arriagada` surname reading.

Interpretation:

This hypothesis is not supported by the assigned evidence. It is listed only because Pulgar-line work requires explicit comparison. The exact proof-review step needed next is to keep these identities separate until entry 513 has a settled child name, date/time, mother surname, and parent-child proof review.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.03 | No direct Dario or confirmed Arriagada evidence. |
| conflict_severity | 0.85 | Name-only merging could conflate generations and identity clusters. |
| evidence_quality | 0.36 | Compared Dario clusters are not bridged by this draft. |
| conversion_confidence | 0.26 | Possible surname bridge is unresolved. |
| claim_probability | 0.03 | Not probable from current evidence. |
| relevance | 0.58 | Relevant only as required anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not merge, rename, or promote. |

## Conflicts

- Same-person conflict: unresolved. No person in entries 513 or 515 is ready for same-person matching to an existing canonical page from this draft.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` because local stubs exist; high if those stubs are used to force the disputed child name or mother surname.
- Name-variant conflict: `Amador` versus `Amagada` is unresolved; `Arriagada` remains a family-context double-check lead only. `Isolina del Carmen` / `Jose` must not be silently replaced by a related `Pulgar...` or `Tulio...` reading without conversion QA.
- Relationship conflict: entry 513 parent-child claims cannot be promoted while the child identity and mother surname are unresolved. Entry 515 does not add Pulgar relationship evidence and remains a boundary-control conflict.
- Chronology conflict: no Dario-line chronology conflict is proved because this draft supplies no Dario chronology. Entry 513 date/time remains part of the conversion-QA hold.
- Conversion conflict: the assigned converted file/chunk agree with each other, but proof review preserves image-reviewed disagreement in identity-controlling fields.

## Ranked Hypotheses

| rank | hypothesis | probability | next action |
|---:|---|---:|---|
| 1 | Hold entry 513 as registration-scoped Pulgar conflict candidate | 0.66 | Run targeted conversion QA before identity promotion. |
| 2 | Entry 513 Jose/Juana pair may match existing Jose/Juana Amagada stubs | 0.48 | Revisit only after child and mother readings are QA-confirmed. |
| 3 | Entry 513 may be related to the Juana Arriagada / Jose del Carmen Segundo cluster | 0.18 | Preserve as a review lead; do not normalize surnames. |
| 4 | Ancestor-line lead for Dario Arturo Pulgar-Smith / Dario Arturo Pulgar | 0.07 | Requires separate lineage proof review after register QA. |
| 5 | Same as Dario Jose Pulgar-Arriagada / Dario or Darío Pulgar Arriagada | 0.03 | Keep separate; no same-person action. |

## Recommended Next Action

Keep the assigned staged draft on `hold_for_conversion_qa`. Do not promote facts, merge people, rename canonical pages, or attach this register page to any Dario/Pulgar canonical identity.

Exact next step: targeted conversion QA/proof review for page 172 entries 513 and 515. Confirm entry 513 child full name and sex, birth date/time/place, father/declarant profession, and mother surname; confirm whether entry 515's child and father/declarant fields are complete and correctly row-aligned. After QA, run a focused identity proof review comparing the confirmed entry-513 Jose/Juana/child readings against `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada` before any broader Pulgar-line comparison to Dario identities.
