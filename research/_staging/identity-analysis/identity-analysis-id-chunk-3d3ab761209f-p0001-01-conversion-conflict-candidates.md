---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/id-chunk-3d3ab761209f-p0001-01-conversion-conflict-candidates.md
staged_draft: research/_staging/identity/id-chunk-3d3ab761209f-p0001-01-conversion-conflict-candidates.md
source_packet: research/_staging/source-packets/sp-chunk-3d3ab761209f-p0001-01-los-angeles-birth-register-page-172.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md
chunk_id: CHUNK-3d3ab761209f-P0001-01
analysis_status: hold
canonical_readiness: hold
---

# Identity Analysis: id-chunk-3d3ab761209f-p0001-01

## Blockers

- Exact staged draft analyzed: `research/_staging/identity/id-chunk-3d3ab761209f-p0001-01-conversion-conflict-candidates.md`.
- This note uses only staged drafts, referenced converted/chunk/source files, reviewed notes, and existing canonical wiki pages. No external research was performed.
- The assigned chunk, assembled converted Markdown, source packet, and proof-review revision disagree on identity-bearing fields for entries 513-515. Principal conflicts include entry 513 child name, entry 513 mother surname, entry 513 birth date/time, entry 514 father field, entry 514 child/place/witness readings, and entry 515 mother field.
- Entry 513 is Pulgar-line relevant but not promotion-ready. The source packet says the image supports father `Jose del Carmen Pulgar`, male sex, domicile `Calle Colon`, and mother line beginning `Juana de Dios ... de Pulgar`; the child given-name line and maternal surname remain image-sensitive.
- Existing wiki context contains separate Pulgar-related pages: `Dario Arturo Pulgar-Smith`, `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada`. These pages do not by themselves prove that the entry 513 people are the same as any Dario or Pulgar-Arriagada cluster.
- Do not merge people, rename pages, promote facts, infer `Amagada` as `Arriagada`, or attach this register page to `Dario Arturo Pulgar-Smith` until targeted conversion QA and a later identity proof review resolve the literal readings.

## Hypothesis 1: Registration-Scoped Identities Only

Hypothesis: Entries 513-515 should remain staged registration-scoped identity candidates, not canonical same-person matches.

Literal evidence:

- Entry 513 candidate: child surname/given-name line currently held as `Pulgar Amagada` with given name only securely beginning `Jose ...`; father/declarant `Jose del Carmen Pulgar` / `Jose del C. Pulgar`; mother `Juana de Dios Amagada de Pulgar` as best current image-reviewed reading, but surname still sensitive.
- Entry 514 candidate: child `Juan Bautista Riquelme`, mother/declarant `Mercedes Riquelme`; father field supported locally as `Se ignora`, not a named father.
- Entry 515 candidate: child `Laura de la Cruz Neira Ulloa`; father/declarant `Pedro Pablo Neira`; mother staged as `Carmen Ulloa`, with the lower mother field requiring caution.

Interpretation:

- This is the leading hypothesis. The page supports local candidates and same-entry parent/declarant links, but the conversion conflicts prevent canonical promotion.
- The civil-register context is strong for eventual identity work, but current derivative disagreement makes normalized names unsafe.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.72 | Good for registration-scoped labels; insufficient for broader same-person matches. |
| conflict_severity | 0.62 | Identity-bearing fields conflict materially across derivative layers. |
| evidence_quality | 0.70 | Civil birth-register image and reviewed notes exist, but several readings need targeted crop QA. |
| conversion_confidence | 0.48 | Assigned chunk and assembled converted Markdown disagree on principal names and relationships. |
| claim_probability | 0.76 | Probable that these are real entry-level people; exact normalized names remain held. |
| relevance | 0.92 | Directly relevant to the assigned identity/conflict draft. |
| canonical_readiness | 0.18 | Hold for conversion QA and proof review. |

## Hypothesis 2: Entry 513 Jose/Juana Pair Matches Existing Jose/Juana Canonical Stubs

Hypothesis: Entry 513's `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` may correspond to existing stubs `wiki/people/jose-del-carmen-pulgar.md` and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

Literal evidence:

- Existing `Jose del Carmen Pulgar` page has a draft child link to `Tulio Cesar Luis Jose`.
- Existing `Juana de Dios Amagada de Pulgar` page has a draft child link to `Tulio Cesar Luis Jose`.
- The current staged draft instead describes entry 513 child as a Pulgar-Amagada child with the given-name line unresolved, and the source packet says only `Jose ...` is secure.

Interpretation:

- A same-person match for the parent names is plausible because the names align closely and the 1889 register is the same type of Pulgar parent context.
- The child-name mismatch or unresolved child reading is a blocker. Do not use the stubs to correct this staged draft, and do not treat `Tulio Cesar Luis Jose`, `Jose Luis`, `Isidoro del Carmen Jose`, or another reading as settled until conversion QA reconciles the entry.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.58 | Parent names align, but child and surname readings are unstable. |
| conflict_severity | 0.68 | A premature merge could propagate a wrong child identity or maternal surname. |
| evidence_quality | 0.56 | Existing stubs rely on draft evidence; this staged draft is explicitly held. |
| conversion_confidence | 0.42 | The exact entry 513 child and mother readings are unresolved. |
| claim_probability | 0.54 | Possible parent-stub correspondence, not proved. |
| relevance | 0.86 | Important for Pulgar-line conflict handling. |
| canonical_readiness | 0.12 | Hold; no canonical update. |

## Hypothesis 3: Entry 513 Is Related To Juana Arriagada / Jose del Carmen Segundo Pulgar Arriagada Cluster

Hypothesis: Entry 513's `Pulgar Amagada`/`Juana de Dios Amagada` readings might be a conversion or reading variant near the existing `Juana Arriagada de Pulgar` and `Jose del Carmen Segundo Pulgar Arriagada` cluster.

Literal evidence:

- Existing `Juana Arriagada de Pulgar` page links to `Jose del Carmen Segundo Pulgar Arriagada` as a probable child from a separate staged entry.
- Existing `Jose del Carmen Segundo Pulgar Arriagada` page records birth on 1888-03-08 at Calle de Valdivia, Los Angeles, based on a different source packet.
- The current staged draft is an 1889 page 172, entries 513-515, and says entry 513 source image only securely supports `Pulgar Ama...` and a given-name line beginning `Jose ...`.

Interpretation:

- The overlap in Pulgar, Jose, Juana, and Los Angeles register context justifies a double-check.
- The dates, entry/source context, and surname readings do not allow a same-person merge. `Amagada` must not be silently corrected to `Arriagada`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.26 | Shared family-name context only; separate source/date context. |
| conflict_severity | 0.74 | Merging could collapse distinct children or mothers. |
| evidence_quality | 0.50 | Both clusters have staged or held evidence and unresolved transcript issues. |
| conversion_confidence | 0.40 | The decisive surname and child-name readings are image-sensitive. |
| claim_probability | 0.24 | Possible review lead, low same-person probability. |
| relevance | 0.78 | Relevant because Pulgar-line instructions require comparison. |
| canonical_readiness | 0.04 | Do not merge or attach. |

## Hypothesis 4: Entry 513 Connects To Dario Arturo Pulgar-Smith / Dario Arturo Pulgar

Hypothesis: The 1889 Pulgar entry may be an ancestor-line lead for canonical `Dario Arturo Pulgar-Smith` or staged `Dario Arturo Pulgar` CV records.

Literal evidence:

- Canonical `Dario Arturo Pulgar-Smith` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to automatically merge similarly named Pulgar records.
- Staged CV analyses support a document-level `Dario Arturo Pulgar`, not a proven bridge to `Pulgar-Smith`.
- The current staged draft contains no Dario, Arturo, Smith, CV, grandparent, spouse, child-of-Dario, or descendant statement.

Interpretation:

- This hypothesis is a low-confidence family-context lead only. The presence of `Pulgar` and possible Jose/Juana parent candidates is not an identity bridge to Dario.
- Exact next proof step: after conversion QA, compare the verified entry 513 parents/child against evidence-grade lineage records that explicitly connect a verified Pulgar child or parent to `Dario Arturo Pulgar` and then separately to `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.08 | No direct Dario or Pulgar-Smith evidence in this staged draft. |
| conflict_severity | 0.70 | Premature attachment would create unsupported ancestor-line claims. |
| evidence_quality | 0.42 | This hypothesis rests on family context and surname overlap only. |
| conversion_confidence | 0.48 | Register conversion conflicts still unresolved. |
| claim_probability | 0.10 | Very low from this source alone. |
| relevance | 0.66 | Relevant only as a guarded Pulgar-line lead. |
| canonical_readiness | 0.01 | No canonical action supported. |

## Hypothesis 5: Same Person As Dario Jose Pulgar-Arriagada / Dario or Darío Pulgar Arriagada

Hypothesis: The entry 513 Pulgar child or parents are the same identity cluster as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`.

Literal evidence:

- Existing `Darío Pulgar Arriagada` page currently records a 2000 expropriation event only.
- Other staged Pulgar-Arriagada analyses describe held ICRC/Geneva and related records for `Dario Jose Pulgar-Arriagada` or `Dario Pulgar-Arriagada`, but those are separate adult/professional contexts.
- The current 1889 register staged draft has no `Dario` given name and no settled `Arriagada` reading.

Interpretation:

- This is not supported as a same-person hypothesis. It is a name-cluster guardrail: preserve separately until an explicit lineage or identity bridge is reviewed.
- Exact next proof step: only after entry 513's literal child and mother names are QA-confirmed should a Pulgar-Arriagada proof review compare dates, parents, occupations, and source contexts against the Dario Jose / Dario Arriagada clusters.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.04 | No Dario or confirmed Arriagada evidence in the assigned draft. |
| conflict_severity | 0.82 | Name-only merging would likely conflate separate generations or clusters. |
| evidence_quality | 0.38 | Compared Dario clusters are outside this entry and often held for their own QA. |
| conversion_confidence | 0.40 | The only possible bridge, `Amagada`/`Arriagada`, is not settled. |
| claim_probability | 0.04 | Not probable from current evidence. |
| relevance | 0.62 | Relevant as a required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Do not merge, rename, or promote. |

## Conflicts

- Same-person conflict: unresolved. No staged candidate from this draft can be safely merged with an existing canonical person.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` because similarly named stubs exist; high if the unresolved child name is used to force a match.
- Name-variant conflict: `Amagada` versus `Amador` in derivative layers, and possible family-context temptation to read `Arriagada`; treat all as unresolved literal-reading issues.
- Relationship conflict: entry 514 father should remain negative evidence only for that registration. The local reviewed evidence supports `Se ignora`; the converted Markdown's named father should not be promoted.
- Chronology conflict: none proved inside the assigned entries. Cross-cluster Dario comparisons are not mature enough for chronology resolution because this draft lacks Dario identity evidence.
- Conversion conflict: severe enough to block promotion. Entry 513 child/mother/date-time, entry 514 father/child/place/witness, and entry 515 mother readings require targeted QA.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Registration-scoped identities only | 0.76 | Hold staged identities pending conversion QA. |
| 2 | Entry 513 Jose/Juana pair may match existing Jose/Juana Amagada stubs | 0.54 | Revisit only after child and mother readings are QA-confirmed. |
| 3 | Entry 513 may be near Juana Arriagada / Jose del Carmen Segundo Pulgar Arriagada cluster | 0.24 | Preserve as review lead; do not correct `Amagada` to `Arriagada`. |
| 4 | Ancestor-line lead for Dario Arturo Pulgar-Smith / Dario Arturo Pulgar | 0.10 | Requires explicit lineage bridge after register QA. |
| 5 | Same as Dario Jose Pulgar-Arriagada / Dario or Darío Pulgar Arriagada | 0.04 | Keep separate; compare only after literal entry QA. |

## Recommended Next Action

Keep `research/_staging/identity/id-chunk-3d3ab761209f-p0001-01-conversion-conflict-candidates.md` on hold. Do not promote facts, merge people, rename canonical pages, or attach this page to any Dario/Pulgar canonical identity.

The exact next step is targeted conversion QA/proof review for the source image and derivative transcripts: confirm entry 513 child full name, entry 513 mother surname, entry 513 birth date/time, entry 514 father field, entry 514 child/place/witness readings, and entry 515 mother field. After that, run a focused identity proof review comparing the confirmed entry 513 Jose/Juana/child readings against the existing `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada` pages before any Pulgar-line promotion.
