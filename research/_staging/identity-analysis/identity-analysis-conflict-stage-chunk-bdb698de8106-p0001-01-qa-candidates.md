---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md
staged_draft: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
analysis_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Identity And Conflict Analysis: bdb698de8106 QA Candidates

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md`.
- No external research was performed. This analysis uses the staged conflict draft, referenced source packet, available converted/chunk files, reviewed notes, and existing canonical wiki pages only.
- Revision on 2026-05-25: the staged conflict draft and source packet cite `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, and that file is now present as manifest chunk `CHUNK-bdb698de8106-P0001-01`. The citation-path mismatch is not the controlling blocker for this bdb task.
- Entry 513 has a material child-identity conflict across derivative layers: the conflict draft says the converted text reads `Isolina del Carmen José`; the current converted file and d6a12 chunk read `Tulio Cesar Luis José`; another available chunk reads `Pulgar Amagada / José Luis`; reviewed notes say the visible image appears to begin with `Pulgar...` and end with a `José` line. None is proof-ready for canonical child identity.
- Entry 513 mother surname remains unresolved: staged conflict evidence preserves `Juana de Dios Amador de Pulgar` versus possible `Juana de Dios Amagada de Pulgar`. Similarity to canonical `Juana Arriagada de Pulgar` is only a double-check lead, not a correction.
- Entries 514 and 515 have material name, father, street, witness, and completeness conflicts. Do not promote `Belisario Riquelme`, `Pedro Pablo Leiva`, or entry-515 full identity claims from this packet.
- The bdb draft contains no Dario, Arturo, Smith, or confirmed Arriagada child identity. It must not be attached to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío Pulgar Arriagada` by surname or family context alone.

## Hypothesis 1: Hold As Registration-Scoped Conflict Candidates

Literal evidence:

- The staged draft identifies page 172 of an 1889 Los Anjeles/La Laja birth register with entries 513, 514, and 515.
- The source packet says the heading, page, and entry numbers are reliable, but person-name and relationship readings are low confidence.
- Entry 513 has consistent row-level support for a Pulgar father/declarant, `José del Carmen Pulgar` / `José del C. Pulgar`, male sex, and Calle Colon context, while the child and mother surname remain unstable.
- Entry 514 and 515 image-reviewed notes conflict with the converted names and father fields.

Interpretation:

This is the leading hypothesis. The page is relevant evidence, but this staged draft is a conflict container. Identity and relationship claims should remain staged until conversion QA reconciles the source image, converted file, chunk paths, and reviewed notes.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.60 | Strong page identity, weak exact person identity. |
| conflict_severity | 0.90 | Core names and parent relationships conflict. |
| evidence_quality | 0.62 | Civil register and local review notes are useful, but decisive readings are unsettled. |
| conversion_confidence | 0.32 | The cited bdb chunk path is present again, but competing transcriptions remain unresolved. |
| claim_probability | 0.68 | Probable that the page records the families, not that exact identities are settled. |
| relevance | 0.98 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.06 | Hold for conversion QA. |

## Hypothesis 2: Entry 513 Jose/Juana Pair May Match Existing Jose/Juana Amagada Stubs

Literal evidence:

- Entry 513 father/declarant evidence supports `José del Carmen Pulgar` / `José del C. Pulgar` in the same row.
- The mother line is held as `Juana de Dios Amador de Pulgar` versus possible `Juana de Dios Amagada de Pulgar`.
- Existing canonical stubs `wiki/people/jose-del-carmen-pulgar.md` and `wiki/people/juana-de-dios-amagada-de-pulgar.md` already contain draft links to `Tulio Cesar Luis Jose` from related staged evidence.

Interpretation:

The parent-pair match is plausible, especially for the father/declarant. It is not ready for merge or promotion because the child identity and mother surname are exactly the disputed fields.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.54 | Father aligns; mother and child are unresolved. |
| conflict_severity | 0.76 | Premature match could propagate a wrong child or maternal surname. |
| evidence_quality | 0.54 | Existing stubs are draft-backed and this task is held. |
| conversion_confidence | 0.28 | The bdb conversion layer is unstable for identity fields. |
| claim_probability | 0.50 | Possible, not proved. |
| relevance | 0.92 | Direct Jose/Juana comparison required. |
| canonical_readiness | 0.10 | No canonical edit supported. |

## Hypothesis 3: Entry 513 Is Related To, But Not Same As, The Juana Arriagada Cluster

Literal evidence:

- `wiki/people/juana-arriagada-de-pulgar.md` links to `Jose del Carmen Segundo Pulgar Arriagada` from a separate staged birth-register packet.
- That separate cluster records an 1888 birth, Calle de Valdivia context, and mother `Juana Arriagada de Pulgar`.
- The bdb conflict draft concerns an 1889 entry with mother held as `Juana de Dios Amador/Amagada de Pulgar`, not confirmed `Arriagada`.

Interpretation:

Shared Pulgar/Jose/Juana/Los Angeles context justifies later comparison, but it does not justify normalizing `Amagada` or `Amador` to `Arriagada`. Treat as a review lead only.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.22 | Similar context, no settled surname bridge. |
| conflict_severity | 0.82 | Merge risk across separate children and entries. |
| evidence_quality | 0.48 | Both clusters include staged or held evidence. |
| conversion_confidence | 0.26 | The disputed surname is the possible bridge. |
| claim_probability | 0.20 | Possible family-context lead only. |
| relevance | 0.84 | Required because Jose/Juana parent candidates exist in wiki context. |
| canonical_readiness | 0.02 | Do not merge or attach. |

## Hypothesis 4: Ancestor-Line Lead For Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Literal evidence:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merge with similarly named Pulgar clusters.
- Staged CV packets identify a document-level `Dario Arturo Pulgar`, but they do not bridge this 1889 birth-register entry to that identity.
- The bdb conflict draft contains no direct `Dario`, `Arturo`, `Smith`, spouse, descendant, or parent-of-Dario statement.

Interpretation:

This is a low-confidence lineage lead only. The exact next proof step is targeted conversion QA for entry 513, then a separate lineage proof review linking any confirmed child or parent pair to `Dario Arturo Pulgar`, and only then to `Dario Arturo Pulgar-Smith` if evidence supports it.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.06 | No direct Dario evidence in this draft. |
| conflict_severity | 0.78 | Unsupported ancestor-line attachment would be misleading. |
| evidence_quality | 0.40 | Contextual only. |
| conversion_confidence | 0.28 | Register identities are not settled. |
| claim_probability | 0.08 | Very low from this source alone. |
| relevance | 0.66 | Relevant as a Pulgar-line guardrail. |
| canonical_readiness | 0.00 | No canonical action. |

## Hypothesis 5: Same As Dario Jose Pulgar-Arriagada Or Darío Pulgar Arriagada

Literal evidence:

- Existing `wiki/people/dar-o-pulgar-arriagada.md` currently has a 2000 expropriation event only.
- Staged `Dario Jose Pulgar-Arriagada` photograph/metadata packets are separate identity-review contexts.
- The bdb conflict draft has no `Dario` given name and no confirmed `Arriagada` reading for entry 513.

Interpretation:

This hypothesis is not supported. It is listed because Pulgar-line instructions require explicit comparison. Keep these identities separate until entry 513 has a settled child name, date/time, mother surname, and proof-reviewed citation path.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.03 | No direct Dario or confirmed Arriagada evidence. |
| conflict_severity | 0.85 | Name-only merging could conflate generations. |
| evidence_quality | 0.36 | Compared Dario clusters are not bridged by this draft. |
| conversion_confidence | 0.26 | Possible surname bridge is unresolved. |
| claim_probability | 0.03 | Not probable from current evidence. |
| relevance | 0.58 | Relevant only as required comparison. |
| canonical_readiness | 0.00 | Do not merge, rename, or promote. |

## Conflicts

- Same-person conflict: unresolved. No candidate in the bdb conflict draft is ready for same-person matching to an existing canonical page.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` because local stubs exist; high if those stubs are used to force the disputed child name or maternal surname.
- Name-variant conflict: `Isolina del Carmen José`, `Tulio Cesar Luis José`, `Pulgar Amagada / José Luis`, and `Pulgar... / ... José` remain competing child-name readings; `Amador`, `Amagada`, and the context-only `Arriagada` remain separate until QA.
- Relationship conflict: entry 513 parent-child relationship is not promotable while the child identity is unresolved; entry 514 father field conflicts between `Belisario Riquelme` and `Se ignora`; entry 515 conflicts between Leiva/Fuentes and Neira/Ulloa readings.
- Chronology conflict: no proved Dario-line chronology conflict from this draft. Entry-level dates and times still require conversion QA.
- Conversion/citation conflict: the cited bdb chunk path is present, but available chunks for the same source have different chunk IDs and transcriptions.

## Ranked Hypotheses

| rank | hypothesis | probability | next action |
|---:|---|---:|---|
| 1 | Hold as registration-scoped conflict candidates | 0.68 | Run targeted conversion QA before identity work. |
| 2 | Entry 513 Jose/Juana pair may match Jose/Juana Amagada stubs | 0.50 | Revisit after child and mother readings are confirmed. |
| 3 | Entry 513 may be related to the Juana Arriagada cluster | 0.20 | Preserve as a review lead; do not normalize surname. |
| 4 | Ancestor-line lead for Dario Arturo Pulgar-Smith / Dario Arturo Pulgar | 0.08 | Requires separate lineage proof review after register QA. |
| 5 | Same as Dario Jose Pulgar-Arriagada / Darío Pulgar Arriagada | 0.03 | Keep separate; no same-person action. |

## Recommended Next Action

Keep `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md` on `hold_for_conversion_qa`. Do not promote facts, merge people, rename canonical pages, or attach this register page to any Dario/Pulgar canonical identity.

Exact next step: targeted conversion QA/proof review for page 172 and the bdb derivative set. Confirm entry 513 child full name, sex, birth date/time, father/declarant form, and mother surname; confirm entry 514 child, father field, mother/declarant, street, and witnesses; and confirm whether entry 515 is complete enough for identity extraction. After QA, run a focused identity proof review comparing the confirmed entry 513 Jose/Juana/child readings against `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada` before any broader Dario-line comparison.
