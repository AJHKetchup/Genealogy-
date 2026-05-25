---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-bdb698de8106-P0001-01-identity-candidates.md
staged_draft: research/_staging/identity/ID-STAGE-CHUNK-bdb698de8106-P0001-01-identity-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
analysis_status: hold
canonical_readiness: hold
---

# Identity Analysis: ID-STAGE-CHUNK-bdb698de8106-P0001-01

## Revision Note

- Exact staged draft analyzed: `research/_staging/identity/ID-STAGE-CHUNK-bdb698de8106-P0001-01-identity-candidates.md`.
- This note uses only staged drafts, referenced converted/chunk/source files, reviewed notes, and existing canonical wiki pages. No external research was performed.
- Revision on 2026-05-25: the assigned chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is now present and matches the bdb manifest. The citation-path mismatch should no longer be treated as the controlling blocker for this bdb task.

## Blockers

- Entry 513 has a material child-name conflict. The bdb staged draft reports the converted reading `Isolina del Carmen José`, while reviewed local notes and related chunks variously point to a Pulgar-family row, including `Pulgar...` with a `José` line, `Pulgar Amagada / José Luis`, or `Tulio Cesar Luis José`. None of these complete child-name readings is proof-ready from this task.
- Entry 513 mother surname is unresolved: converted/chunk evidence in this bdb task says `Juana de Dios Amador de Pulgar`, while image-reviewed local conflict indicators lean toward `Juana de Dios Amagada de Pulgar`; family-context similarity to `Arriagada` is only a double-check lead, not a correction.
- Entries 514 and 515 have material derivative-vs-image conflicts for child name, father field, street/place, witnesses, and record completeness. Do not promote `Belisario Riquelme`, a two-parent relationship for entry 514, or `Pedro Pablo Leiva` for entry 515 from this held draft.
- Pulgar-line context is relevant, but the assigned page does not name Dario. It must not be attached to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` by surname or family context alone.

## Hypothesis 1: Registration-Scoped Candidates Only

Hypothesis: Entries 513-515 should remain staged registration-scoped candidates, with no canonical same-person merge or promoted relationship until conversion QA reconciles the source image, converted file, and chunk paths.

Literal evidence:

- The source packet identifies a civil birth-register page, `Páj. 172`, for Los Anjeles/La Laja, with entries 513, 514, and 515.
- Entry 513 has father/declarant support for `José del Carmen Pulgar` / `José del C. Pulgar`, male sex, and Calle Colon context, but the child name and mother surname remain unstable.
- Entry 514 is locally held because the converted record names `Belisario Riquelme` as father while image-reviewed notes say the father field appears to read `Se ignora`.
- Entry 515 is locally held because the converted record gives `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`, while image-reviewed notes point toward a Neira/Ulloa child and `Pedro Pablo Neira`.

Interpretation:

- This is the leading hypothesis. The source is valuable for identity work, but this staged bdb draft is a conflict container, not a proof-ready identity packet.
- Literal source readings must remain separated from interpretation. The image-reviewed alternatives are conflict indicators until targeted QA creates a settled transcription.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.62 | Good that the page contains real entry-level candidates; low for exact normalized person identities. |
| conflict_severity | 0.88 | Core names and relationships conflict across derivative layers. |
| evidence_quality | 0.60 | Civil-register source and local review notes are strong in type, but the decisive readings are unsettled. |
| conversion_confidence | 0.34 | The assigned bdb chunk path is present again, but the conversion still conflicts with image-reviewed notes. |
| claim_probability | 0.70 | Probable that the page records these families, but not probable enough for exact promotion. |
| relevance | 0.96 | Directly addresses the assigned staged identity draft. |
| canonical_readiness | 0.08 | Hold for conversion QA and later proof review. |

## Hypothesis 2: Entry 513 Jose/Juana Pair Matches Existing Jose/Juana Amagada Stubs

Hypothesis: Entry 513's father `José del Carmen Pulgar` and mother line `Juana de Dios ... de Pulgar` may correspond to existing canonical stubs `wiki/people/jose-del-carmen-pulgar.md` and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

Literal evidence:

- The bdb father claim records `José del Carmen Pulgar`; the declarant field abbreviates this as `José del C. Pulgar`.
- The bdb mother claim preserves a conflict between `Juana de Dios Amador de Pulgar` and image-reviewed `Juana de Dios Amagada de Pulgar`.
- Existing `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` pages contain draft child links to `Tulio Cesar Luis Jose`, based on related staged evidence for the same 1889 register source family context.

Interpretation:

- The parent-stub match is plausible but blocked. The exact child identity and mother surname must be fixed before any merge or evidence attachment.
- Do not use the existing stubs to force the bdb draft into a preferred reading.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.56 | Father name aligns; mother surname and child identity remain unresolved. |
| conflict_severity | 0.72 | A premature match could propagate the wrong child name or maternal surname. |
| evidence_quality | 0.52 | Existing stubs are draft-backed, and this task is explicitly held. |
| conversion_confidence | 0.28 | The bdb conversion/chunk layer is unstable for exact identity fields. |
| claim_probability | 0.52 | Possible same parent pair, not proved. |
| relevance | 0.90 | Direct Pulgar/Jose/Juana comparison required by the task. |
| canonical_readiness | 0.10 | No canonical edit or promotion supported. |

## Hypothesis 3: Entry 513 Is Near The Juana Arriagada / Jose del Carmen Segundo Pulgar Arriagada Cluster

Hypothesis: Entry 513 may be related to, but is not yet the same as, the existing `Juana Arriagada de Pulgar` and `Jose del Carmen Segundo Pulgar Arriagada` cluster.

Literal evidence:

- Existing `Juana Arriagada de Pulgar` links to `Jose del Carmen Segundo Pulgar Arriagada` from a separate staged entry-172 packet.
- Existing `Jose del Carmen Segundo Pulgar Arriagada` records an 1888 birth and Calle de Valdivia context from a different staged source packet.
- The assigned bdb draft concerns 1889 register page 172, entry 513, with a mother line currently held as `Juana de Dios Amador/Amagada de Pulgar`, not confirmed `Arriagada`.

Interpretation:

- Shared Pulgar/Jose/Juana/Los Angeles context justifies a later double-check.
- Same-person probability is low at this stage. `Amagada` or `Amador` must not be silently normalized to `Arriagada`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.22 | Similar family context only; no settled same-person bridge. |
| conflict_severity | 0.80 | Merging could collapse separate children, mothers, or entries. |
| evidence_quality | 0.48 | Both clusters rely on staged or held evidence with unresolved conversion issues. |
| conversion_confidence | 0.26 | The exact surname bridge is one of the disputed readings. |
| claim_probability | 0.20 | Review lead only. |
| relevance | 0.82 | Required because existing wiki context contains Jose/Juana parent candidates. |
| canonical_readiness | 0.02 | Do not merge or attach. |

## Hypothesis 4: Ancestor-Line Lead For Dario Arturo Pulgar-Smith / Dario Arturo Pulgar

Hypothesis: Entry 513 may eventually prove relevant to the Pulgar line containing `Dario Arturo Pulgar-Smith` or staged `Dario Arturo Pulgar` records.

Literal evidence:

- Canonical `Dario Arturo Pulgar-Smith` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to merge similarly named Pulgar records automatically.
- Local staged CV packets identify a document-level `Dario Arturo Pulgar`, but they do not establish a parentage bridge from this 1889 entry.
- The bdb staged draft contains no Dario, Arturo, Smith, spouse, child-of-Dario, grandparent, or descendant statement.

Interpretation:

- This is only a low-confidence lineage lead. Surname overlap plus a possible Jose/Juana parent pair is not identity proof.
- Exact next proof step: after conversion QA confirms entry 513's child and parents, run a dedicated lineage proof review looking for evidence-grade links from that verified child or parent pair to `Dario Arturo Pulgar`, and separately from `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.06 | No direct Dario evidence in this draft. |
| conflict_severity | 0.76 | Premature attachment would create unsupported ancestor-line claims. |
| evidence_quality | 0.40 | This hypothesis rests on context, not direct statements. |
| conversion_confidence | 0.30 | Register identities are not yet settled. |
| claim_probability | 0.08 | Very low from this source alone. |
| relevance | 0.66 | Relevant as a Pulgar-line guardrail. |
| canonical_readiness | 0.00 | No canonical action supported. |

## Hypothesis 5: Same As Dario Jose Pulgar-Arriagada / Dario Or Darío Pulgar Arriagada

Hypothesis: The bdb entry 513 child or parent candidates are the same person as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`.

Literal evidence:

- Existing `Darío Pulgar Arriagada` currently has a 2000 expropriation event only.
- Staged `Dario Jose Pulgar-Arriagada` records are separate metadata/photo or professional-context records and have their own identity-review holds.
- The assigned bdb staged draft has no `Dario` given name and no confirmed `Arriagada` surname reading.

Interpretation:

- This hypothesis is not supported. It remains listed only because Pulgar-line instructions require explicit comparison.
- Exact next proof step: do not compare against Dario Jose/Darío Pulgar Arriagada for same-person resolution until entry 513 has a settled child name, mother surname, date, and source citation path.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.03 | No direct Dario or confirmed Arriagada evidence. |
| conflict_severity | 0.84 | Name-only merging would likely conflate separate generations or identity clusters. |
| evidence_quality | 0.36 | Compared Dario clusters are outside this source and not bridged by this draft. |
| conversion_confidence | 0.26 | The possible surname bridge is unresolved. |
| claim_probability | 0.03 | Not probable from current evidence. |
| relevance | 0.58 | Relevant only as required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Do not merge, rename, or promote. |

## Conflicts

- Same-person conflict: unresolved. No candidate in the bdb staged draft is ready for same-person matching to an existing canonical page.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` because local stubs already exist; high if the unresolved child name is used to force the match.
- Name-variant conflict: `Amador` versus `Amagada` for entry 513 mother, with `Arriagada` as family-context temptation only; `Isolina del Carmen José`, `Pulgar... José`, `Pulgar Amagada / José Luis`, and `Tulio Cesar Luis José` remain competing child-name readings across layers.
- Relationship conflict: entry 513 parentage cannot be promoted while the child identity is unresolved; entry 514 father should remain a conversion conflict because image-reviewed notes support `Se ignora`, not `Belisario Riquelme`.
- Chronology conflict: none proved for Dario-line identities because this draft supplies no Dario chronology. Entry-level date/time readings still require conversion QA.
- Conversion/citation conflict: the assigned bdb chunk path is present, but related chunks for the same source have different chunk IDs and different transcriptions.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Registration-scoped candidates only | 0.70 | Hold all identities and relationships pending conversion QA. |
| 2 | Entry 513 Jose/Juana pair may match existing Jose/Juana Amagada stubs | 0.52 | Revisit only after child and mother readings are QA-confirmed. |
| 3 | Entry 513 may be near Juana Arriagada / Jose del Carmen Segundo Pulgar Arriagada cluster | 0.20 | Preserve as a review lead; do not normalize surnames. |
| 4 | Ancestor-line lead for Dario Arturo Pulgar-Smith / Dario Arturo Pulgar | 0.08 | Requires explicit lineage proof after register QA. |
| 5 | Same as Dario Jose Pulgar-Arriagada / Dario or Darío Pulgar Arriagada | 0.03 | Keep separate; no same-person action. |

## Recommended Next Action

Keep `research/_staging/identity/ID-STAGE-CHUNK-bdb698de8106-P0001-01-identity-candidates.md` on hold. Do not promote facts, merge people, rename pages, or attach this register page to any Dario/Pulgar canonical identity.

The exact next step is targeted conversion QA/proof review for the source image and derivative files: confirm entry 513 child full name, birth date/time, father/declarant form, and mother surname; confirm entry 514 child, father field, mother/declarant, street, and witnesses; and confirm the visible portion of entry 515. Only after that should a focused identity proof review compare the confirmed entry 513 Jose/Juana/child readings against `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada`, before any broader Pulgar-line comparison to Dario identities.
