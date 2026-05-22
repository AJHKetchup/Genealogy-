---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/CHUNK-3d3ab761209f-P0001-01-identity-candidates.md
staged_draft: research/_staging/identity/CHUNK-3d3ab761209f-P0001-01-identity-candidates.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk_id: CHUNK-3d3ab761209f-P0001-01
analysis_status: hold
canonical_readiness: hold
---

# Identity Analysis: CHUNK-3d3ab761209f-P0001-01

## Blockers

- The exact staged draft analyzed here is `research/_staging/identity/CHUNK-3d3ab761209f-P0001-01-identity-candidates.md`.
- The raw source image named by the staged draft and converted file, `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`, is not available in the workspace.
- The expected page image `raw/codex-conversion-jobs/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513/page-images/page-0001.png` is not available in the workspace.
- Because visible-source review is blocked, image-sensitive readings remain unresolved: record 514 witness `Benjamin Utiera`, record 514 street `Calle Sanegueso`, record 515 surname/emendation text `Neira=emendado=vale`, and page-bottom crop completeness.
- No canonical person page was found for `Jose Luis Pulgar Amagada`, `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juan Bautista Riquelme Aviles`, `Mercedes Riquelme`, `Laura de la Cruz Neira Ulloa`, `Pedro Pablo Neira`, or `Carmen Ulloa`. Existing canonical Pulgar material concerns `Dario Arturo Pulgar-Smith` and warns not to automatically merge similarly named Pulgar records.
- Do not infer a father for record 514. The converted father field says `Se ignora`.

## Hypothesis 1: Registration-Scoped Identities, No Canonical Match Yet

Hypothesis: The named children, parents, declarants, and witnesses should remain separate registration-scoped identities from this birth-register page until a later identity bridge or canonical profile comparison is available.

Literal evidence:

- Record 513 names child `Pulgar Amagada / José Luis`, father `José del Carmen Pulgar`, mother `Juana de Dios Amagada de Pulgar`, and compareciente `José del C. Pulgar / Padre`.
- Record 514 names child `Riquelme Aviles / Juan Bautista`, father `Se ignora`, mother and compareciente `Mercedes Riquelme / Madre`, and witnesses `Benjamin Utiera` and `Ignacio Soto`.
- Record 515 names child `Neira Ulloa / Laura de la Cruz`, father and compareciente `Pedro Pablo Neira / Padre`, mother `Carmen Ulloa`, and witnesses `Rosendo Ramirez H.` and `Santiago Perez`.
- The source packet, converted file, assigned chunk, identity proof review, relationship proof review, and conflict proof review all keep canonical readiness on hold.

Interpretation:

- This is the leading hypothesis. The converted register supports local identities within entries 513-515, but the current evidence does not prove duplicate-person matches to existing canonical profiles.
- The civil register is strong evidence for names and declared parent-child relationships inside the page, but identity reconciliation requires image review and comparison with corroborating records or canonical person pages.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.74 | Strong for registration-scoped identity labels; weak for broader same-person merges. |
| conflict_severity | 0.30 | No direct duplicate-person conflict found; the main risk is premature canonical attachment. |
| evidence_quality | 0.76 | Civil birth register transcription is primary-source derived, but the source image is unavailable. |
| conversion_confidence | 0.72 | Principal table entries are stable across converted file and chunk; image-sensitive readings remain unresolved. |
| claim_probability | 0.82 | High probability that the staged identities reflect the converted register text. |
| relevance | 0.90 | Directly relevant to deciding whether the staged identity candidates can move forward. |
| canonical_readiness | 0.25 | Hold pending image review and identity reconciliation. |

## Hypothesis 2: Same-Entry Parent and Declarant Equivalence

Hypothesis: The comparecientes in records 513, 514, and 515 are the same people as the named parent in the same row: `José del C. Pulgar` as `José del Carmen Pulgar`, `Mercedes Riquelme` as the mother, and `Pedro Pablo Neira` as the father.

Literal evidence:

- Record 513 father field gives `José del Carmen Pulgar`; compareciente field gives `José del C. Pulgar / Padre`, age 47, agriculturist, domiciled Calle Colon.
- Record 514 mother field gives `Mercedes Riquelme`; compareciente field gives `Mercedes Riquelme / Madre`, age 21, seamstress, domiciled Calle Sanegueso.
- Record 515 father field gives `Pedro Pablo Neira`; compareciente field gives `Pedro Pablo Neira / Padre`, age 26, agriculturist, domiciled Santiago.

Interpretation:

- Same-entry equivalence is likely for each declarant/parent pairing because name, relationship role, occupation, and domicile align within the same row.
- This does not independently prove broader identity beyond the entry. The abbreviation `José del C.` should remain interpreted as same-entry support, not as a separate proof of identity.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.82 | Same-entry role and contextual details align strongly for the parent/declarant pairs. |
| conflict_severity | 0.20 | The conflict risk is low within each row but rises if used as a broader merge proof. |
| evidence_quality | 0.78 | Evidence is direct from the converted civil register, with source-image QA still blocked. |
| conversion_confidence | 0.74 | Main names are not flagged except record 514 street context and record 515 emendation. |
| claim_probability | 0.84 | High probability for same-entry equivalence, not canonical equivalence. |
| relevance | 0.86 | Important for parent/declarant identity handling and relationship candidates. |
| canonical_readiness | 0.35 | Hold; useful as staged interpretation but not ready for canonical merge. |

## Hypothesis 3: Pulgar-Amagada May Belong Near Existing Pulgar Family Context

Hypothesis: Record 513's `Pulgar Amagada / José Luis`, `José del Carmen Pulgar`, and `Juana de Dios Amagada de Pulgar` may be relevant to the existing canonical Pulgar family context, but the current evidence does not prove a same-person, ancestor, or duplicate-person relationship with canonical `Dario Arturo Pulgar-Smith`.

Literal evidence:

- The canonical page `wiki/people/dario-arturo-pulgar-smith.md` names `Dario Arturo Pulgar-Smith` from family-supplied knowledge and explicitly says not to automatically merge similarly named source clusters.
- The canonical source `wiki/sources/user-family-knowledge-2026-05-20.md` says `Pulgar-Arriagada` is one part of the broader family history.
- The staged register candidate reads `Pulgar Amagada`, not `Pulgar-Arriagada`; the conversion does not state an identity bridge to `Dario Arturo Pulgar-Smith`.

Interpretation:

- Shared `Pulgar` context and the family note about `Pulgar-Arriagada` justify a later double-check, especially because `Amagada` could be a meaningful surname or a reading that needs image review.
- Family-context hints cannot silently correct `Amagada` to another surname and cannot attach these 1889 identities to `Dario Arturo Pulgar-Smith` without additional evidence.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.32 | Only broad surname/family-context overlap exists; no direct bridge is present. |
| conflict_severity | 0.50 | Premature merge could misattribute a nineteenth-century birth-register family to the wrong canonical line. |
| evidence_quality | 0.54 | Canonical context is family supplied; register evidence is converted text without image verification. |
| conversion_confidence | 0.68 | The `Pulgar` reading is stable, but `Amagada` needs caution before variant analysis. |
| claim_probability | 0.34 | Possible relevance, not a proved same-person or duplicate-person claim. |
| relevance | 0.72 | Relevant as a research lead for Pulgar-line reconciliation. |
| canonical_readiness | 0.10 | Not ready for canonical attachment. |

## Hypothesis 4: Distinct Persons, Witness-Only Mentions

Hypothesis: The witnesses should remain distinct, low-relevance identity leads rather than candidate canonical people or duplicate-person matches.

Literal evidence:

- Record 514 lists witnesses `Benjamin Utiera` and `Ignacio Soto`; the conversion flags `Utiera` as difficult to read.
- Record 515 lists witnesses `Rosendo Ramirez H.` and `Santiago Perez`.
- No age, residence, occupation, kinship, or repeated local context is provided for these witnesses.

Interpretation:

- Witness-only mentions are relevant for source context and identity checks but do not justify person creation or merge without corroboration.
- `Benjamin Utiera` is especially image-dependent and should not be normalized or merged until the original image is restored.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.54 | Witness names are present, but distinguishing identity data is thin and one surname is flagged. |
| conflict_severity | 0.25 | Low immediate conflict risk if held; higher if prematurely merged. |
| evidence_quality | 0.50 | Witness-only context lacks identifiers and visible-source verification. |
| conversion_confidence | 0.58 | `Utiera` is explicitly difficult; other witness names are not flagged but still unverified. |
| claim_probability | 0.62 | Probable witness mentions from converted text, not robust identities. |
| relevance | 0.45 | Low genealogical relevance absent corroborating context. |
| canonical_readiness | 0.05 | Do not promote. |

## Conflicts

- Duplicate-person conflict: none resolved. No existing canonical page directly matches any staged register identity.
- Name-variant conflict: `Pulgar Amagada` versus the broader family-context phrase `Pulgar-Arriagada` remains only a review lead. Severity: moderate because changing the surname would materially affect identity; current action is hold.
- Relationship conflict: record 514 father is explicitly unknown (`Se ignora`). Severity: high against any unsupported father assignment for Juan Bautista Riquelme Aviles, but not final disproof of a later, stronger source.
- Same-person caution: `José del Carmen Pulgar` and `José del C. Pulgar` are probably the same within record 513. Severity: low within the entry; moderate if used for broader identity merging.
- Chronology conflict: none found within the converted entries. Parent ages in records 513 and 515 are plausible relative to child birth dates; record 514 mother age 21 is not internally contradictory.
- Conversion conflict: source packet and reviews describe high confidence for principal names, but raw/page image absence prevents final QA for `Utiera`, `Sanegueso`, `Neira=emendado=vale`, and the crop completeness note.

## Recommended Next Action

Keep `research/_staging/identity/CHUNK-3d3ab761209f-P0001-01-identity-candidates.md` on hold. Do not merge people, rename canonical pages, promote facts, or attach record 513 to the canonical `Dario Arturo Pulgar-Smith` page.

Next, restore or regenerate the missing source/page image and visually verify the sensitive readings: `Pulgar Amagada`, `Benjamin Utiera`, `Calle Sanegueso`, and `Neira=emendado=vale`. After image review, reconcile child and parent identities against any relevant canonical Pulgar, Riquelme, Neira, Ulloa, Amagada, or Aviles pages; keep witness-only identities as low-priority leads unless additional corroborating records appear.
