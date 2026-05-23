---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/chunk-23b2269a97df-p0001-01-identity-candidates.md
worker: postconv-identity-analysis-20260523054639519
staged_draft: research/_staging/identity/chunk-23b2269a97df-p0001-01-identity-candidates.md
source_packet: research/_staging/source-packets/chunk-23b2269a97df-p0001-01-entry-172-pulgar-arriagada.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md
chunk_id: CHUNK-23b2269a97df-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity Analysis: Entry 172 Identity Candidates

## Blockers

- The exact staged identity draft `research/_staging/identity/chunk-23b2269a97df-p0001-01-identity-candidates.md` depends on an image-reread Pulgar/Arriagada reading, while the assigned converted Markdown and assigned chunk transcribe entry 172 as a different child and different parents.
- The source packet marks `conversion_confidence: mixed` and `promotion_recommendation: hold_for_conversion_qa`. This blocks canonical promotion of every identity and relationship candidate in this draft until targeted conversion QA reconciles the source image, converted Markdown, and chunk.
- Literal source readings must remain separate from identity interpretation. The staged draft says the image reads `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and apparent informant `Oswaldo Arriagada`; this note treats those as image-reread claims under QA hold, not as corrected conversion output.
- The father exact-name form is not settled. Local notes prefer `Jose del Carmen Pulgar`, but related entry-172 material has preserved a possible suffix or additional mark. Do not merge or expand the father identity until QA records the visible form.
- The mother name is a married-style form, `Juana Arriagada de Pulgar`. Do not silently convert it to a maiden-name-only identity or merge it with `Juana de Dios ... de Pulgar` candidates from other entries.
- The staged draft does not name Dario. Existing Pulgar-line wiki context makes Dario identities relevant as a duplicate-person guardrail only; this entry should not be attached to any Dario identity by surname or Arriagada name pattern alone.

## Hypothesis 1: Image Entry 172 Identifies Jose del Carmen Segundo Pulgar Arriagada

Hypothesis: The source image for register page 58, entry 172 records the child as `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`; the converted/chunk text is a derivative mismatch.

Literal evidence:

- The staged identity draft lists `Jose del Carmen Segundo Pulgar Arriagada` as the child and says the source image child field reads that name.
- The staged source packet gives the same child reading, sex `Hombre`, registration date 7 April 1888, birth date/time 8 March 1888 at about 3 p.m., birthplace `Calle de Valdivia`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- Proof-review notes for this chunk repeatedly state that the visible source image supports a Pulgar/Arriagada birth-registration row and that the assigned conversion/chunk materially conflict with it.
- Canonical stubs already exist for `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`, but those pages are context only and do not resolve this task's conversion conflict.

Interpretation:

- This is the leading identity hypothesis for the staged draft because the draft, source packet, and proof-review notes agree on the image-reread identity cluster.
- It is not canonical-ready because the derivative transcript currently names a different child and parents for the same entry number.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.84 | Strong for the image-reread cluster, reduced by unreconciled conversion/chunk conflict. |
| conflict_severity | 0.95 | The conflict changes the child, parents, birth date/time/place, and informant context. |
| evidence_quality | 0.80 | Civil birth-register image-reread staging is high-value, but no new conversion QA was performed here. |
| conversion_confidence | 0.25 | The assigned conversion and chunk are materially unreliable for this entry identity. |
| claim_probability | 0.83 | The Pulgar/Arriagada reading is probably correct for the visible image, pending QA. |
| relevance | 0.98 | Directly controls all identity candidates in the staged draft. |
| canonical_readiness | 0.12 | Hold for conversion QA before promotion or further canonical attachment. |

## Hypothesis 2: Converted Entry 172 Identifies A Different Child And Parents

Hypothesis: The assigned converted Markdown/chunk identify the true entry 172, and the Pulgar/Arriagada staging belongs to a different row, image, or assignment.

Literal evidence:

- The assigned converted Markdown and chunk transcribe entry 172 as a non-Pulgar child, with a father and mother outside the staged Pulgar/Arriagada cluster.
- The staged conflict draft and proof-review notes preserve this as a material derivative-transcript conflict for the same source path and entry reference.

Interpretation:

- This hypothesis must remain visible because the assigned derivative artifacts exist, but it is weak for identity proof. The local reviewed notes treat the derivative row as the problem to reconcile, not as controlling evidence.
- Do not create, merge, or promote non-Pulgar identity candidates from this assigned conversion until conversion QA proves the Pulgar/Arriagada staging assignment is wrong.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.17 | Supported by conflicted derivative text only. |
| conflict_severity | 0.95 | Accepting it would replace every core staged identity. |
| evidence_quality | 0.23 | Derivative-only evidence contradicted by reviewed image-reread staging. |
| conversion_confidence | 0.18 | Very low for identity use until the mismatch is reconciled. |
| claim_probability | 0.12 | Plausible only if QA later finds a source assignment error. |
| relevance | 0.72 | Relevant as a false-promotion and duplicate-person guardrail. |
| canonical_readiness | 0.01 | Not ready; do not promote. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Jose/Juana Parent Candidates

Hypothesis: The entry-172 father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar` may be the same parent couple or same-family cluster as Jose/Juana candidates in other Pulgar-line records.

Literal evidence:

- This staged identity draft names father candidate `Jose del Carmen Pulgar` and mother candidate `Juana Arriagada de Pulgar`.
- The canonical `Jose del Carmen Pulgar` page has a drafted child link to `Tulio Cesar Luis Jose` from a separate staged relationship.
- The canonical `Juana Arriagada de Pulgar` page has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from earlier entry-172 staging.
- Local review notes for other birth-register entries mention a `Jose del Carmen Pulgar` father and a mother line beginning `Juana de Dios ... de Pulgar`; that is similar context, not a literal match to `Juana Arriagada de Pulgar`.

Interpretation:

- The father-name overlap and Pulgar/Arriagada context justify a targeted Jose/Juana parent-candidate proof review.
- They do not justify a same-person merge. The mother variants `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana de Dios Amador de Pulgar`, and any other `Juana ... de Pulgar` readings should remain separate until source-by-source identity proof explains the name forms.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Plausible same-family cluster, not proven as same persons. |
| conflict_severity | 0.62 | Premature merging could combine distinct couples or mother-name variants. |
| evidence_quality | 0.54 | Local staged and canonical context exists, but cross-record proof is incomplete. |
| conversion_confidence | 0.30 | This entry is conversion-blocked and related entries have their own QA limits. |
| claim_probability | 0.44 | Possible but not established by this identity draft. |
| relevance | 0.88 | Important for Pulgar-line parent structure. |
| canonical_readiness | 0.07 | Hold pending parent-candidate identity review. |

## Dario-Line Comparison

Ranked identity impact:

| rank | candidate | current comparison |
| ---: | --- | --- |
| 1 | `Jose del Carmen Segundo Pulgar Arriagada` | Direct subject of the staged identity draft and leading image-reread child candidate. |
| 2 | `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` | Direct parent candidates; exact father suffix and mother married-name handling remain proof-review issues. |
| 3 | Other Jose/Juana parent candidates | Relevant for later duplicate-person review, especially `Juana de Dios ... de Pulgar` variants, but not mergeable from this draft alone. |
| 4 | `Dario Arturo Pulgar-Smith` | Existing canonical family-supplied maternal-grandfather profile. This entry does not name Dario or Pulgar-Smith and provides no identity bridge. |
| 5 | `Dario Arturo Pulgar` | Staged CV context uses this document-level subject name elsewhere. This entry does not name Dario Arturo and has no CV-era bridge. |
| 6 | `Dario Jose Pulgar-Arriagada` | ICRC/photo staging names this candidate from source title or metadata elsewhere. This entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. |
| 7 | `Dario/Darío Pulgar Arriagada` | Existing canonical page has a 2000 expropriation event for `Darío Pulgar Arriagada`. This 1888 birth-entry draft does not support attachment to that person. |

Required next Dario proof-review step: none for this entry beyond a negative identity guardrail. Do not attach the entry-172 candidates to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` unless a later reviewed source provides direct bridging evidence.

## Conflicts

- Same-entry conflict: staged image-reread Pulgar/Arriagada identity cluster versus assigned converted/chunk non-Pulgar identity cluster. Severity: critical.
- Duplicate-person risk: high if the derivative non-Pulgar entry is promoted from this conversion; moderate if Jose/Juana candidates are merged across entries by name similarity.
- Name-variant conflict: `Jose del Carmen Pulgar` versus possible suffixed father form; `Juana Arriagada de Pulgar` versus other `Juana de Dios ... de Pulgar` variants. Severity: moderate.
- Relationship conflict: child-father, child-mother, and parental-pair candidates depend on the unresolved entry transcript. Severity: high.
- Chronology conflict: the competing readings imply different birth dates, times, and places for entry 172. Severity: high for this entry, low for Dario-line chronology because no Dario is named.

## Recommended Next Action

Keep the staged identity draft and dependent claims/relationships at `hold_for_conversion_qa`.

Exact next proof-review step: run targeted conversion QA for `CHUNK-23b2269a97df-P0001-01` against the source image. The QA note must decide whether the controlling entry-172 transcript is the Pulgar/Arriagada row, correct or retire the conflicting derivative transcript assignment, and settle the exact father-name form and informant-name form.

After that QA, rerun proof review for the identity draft, child birth-name claim, father-name claim, mother-name claim, informant claim, child-parent relationships, and parental-pair relationship. Separately run a Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or any `Juana de Dios ... de Pulgar` candidates across records.
