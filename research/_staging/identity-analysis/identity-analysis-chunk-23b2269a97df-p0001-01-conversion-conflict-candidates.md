---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-23b2269a97df-p0001-01-conversion-conflict-candidates.md
worker: postconv-identity-analysis-20260523053152351
staged_draft: research/_staging/conflicts/chunk-23b2269a97df-p0001-01-conversion-conflict-candidates.md
source_packet: research/_staging/source-packets/chunk-23b2269a97df-p0001-01-entry-172-pulgar-arriagada.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md
chunk_id: CHUNK-23b2269a97df-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Conversion Conflict

## Blockers

- The exact staged draft `research/_staging/conflicts/chunk-23b2269a97df-p0001-01-conversion-conflict-candidates.md` reports a material same-source, same-entry contradiction. The image-reread support says entry 172 is `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`; the assigned converted Markdown and chunk instead read entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The referenced source packet marks `conversion_confidence: mixed` and `promotion_recommendation: hold_for_conversion_qa`. No identity, relationship, or chronology claim from this entry is canonical-ready until targeted conversion QA reconciles the image-visible row with the derivative transcript.
- The father's exact name remains detail-blocked. Local reread notes say the image appears to read `Jose del Carmen Pulgar`, while prior derivative material in related entry-172 staging has included a possible suffix. Do not normalize to a longer father identity or merge father candidates until QA records the exact visible form.
- The informant exact name is unresolved. The conflict draft says the image appears to read `Oswaldo Arriagada`; the converted/chunk text gives `Oswaldo Burgos`. This is evidence of conversion conflict, not a basis to infer one informant identity.
- The entry does not name Dario. Existing Dario-line context is relevant as a guardrail only; this record must not be attached to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada by surname similarity.
- Existing canonical pages already contain related Pulgar/Arriagada stub evidence from earlier entry-172 staging. This note does not revise those pages and does not promote additional facts from the conflicted derivative transcript.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Hypothesis: The source image for register page 58, entry 172 records the birth of `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`; the Burgos/de la Cruz transcript is a derivative conversion mismatch.

Literal evidence:

- The staged conflict draft says the source image reads child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- The source packet gives the same image-supported child and parent readings, with registration date 7 April 1888, birth date/time 8 March 1888 at about 3 p.m., and birthplace `Calle de Valdivia`.
- The proof-review revision note for this chunk preserves the same image-reviewed reading and specifically says the assigned converted Markdown and chunk remain inconsistent with the source image.
- Existing canonical stubs include `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`, but their presence is context rather than fresh proof of this conflict's resolution.

Interpretation:

- This is the leading hypothesis because it is supported by the staged conflict draft, source packet, and proof-review revision note, all tied to the same source path/SHA and entry reference.
- The record supports an entry-level Pulgar/Arriagada identity cluster only. It does not prove that these people are the same as other Jose/Juana parent candidates, and it does not bridge to any Dario identity.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.86 | Strong for the image-reread Pulgar/Arriagada cluster, reduced by unreconciled derivative text. |
| conflict_severity | 0.95 | Competing readings change the child, both parents, birth date/time, birthplace, and informant. |
| evidence_quality | 0.82 | Civil birth registration image-reread staging is high value, but this note did not perform a new conversion or edit the transcript. |
| conversion_confidence | 0.32 | Low for the assigned converted/chunk text because it contradicts the image-reread staging. |
| claim_probability | 0.84 | High probability that the Pulgar/Arriagada reading is the correct identity cluster, pending QA reconciliation. |
| relevance | 0.97 | Directly relevant to Pulgar-line parent-child evidence and to blocking false derivative promotion. |
| canonical_readiness | 0.16 | Hold for conversion QA before promotion or canonical attachment. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Birth Registration

Hypothesis: Entry 172 records `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and the Pulgar/Arriagada image-reread belongs to another row, page, or assignment.

Literal evidence:

- The assigned converted Markdown transcribes entry 172 as `José Francisco` in one visible derivative row with father `Oswaldo Gomez` and mother `Emilia de la Cruz`; the staged conflict draft and proof-review revision preserve a related conflicting derivative summary as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The assigned chunk at the path named in this task reflects the same derivative-conversion problem rather than the image-reread Pulgar/Arriagada row.
- The staged conflict draft treats this derivative reading as literal support from converted/chunk text, not as a source-image conclusion.

Interpretation:

- This hypothesis must be preserved because the derivative files are the assigned converted artifacts, but it is weak as identity evidence for this source image. The local staging repeatedly says the image-visible entry is Pulgar/Arriagada.
- Do not create or promote Burgos/de la Cruz/Gomez/de la Cruz people from this entry unless conversion QA proves the Pulgar/Arriagada source-packet assignment is wrong.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Supported only by conflicted derivative text. |
| conflict_severity | 0.95 | Accepting it would displace every core Pulgar/Arriagada identity and event detail. |
| evidence_quality | 0.24 | Derivative-only support, directly contradicted by image-reread staging. |
| conversion_confidence | 0.18 | Very low for identity use until the conversion mismatch is reconciled. |
| claim_probability | 0.12 | Plausible only if the image-reread/source-packet assignment is later shown to be wrong. |
| relevance | 0.68 | Relevant chiefly as a false-positive guardrail. |
| canonical_readiness | 0.01 | Do not promote. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Pulgar-Line Parent Candidates

Hypothesis: The entry-172 father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar` may be the same Jose/Juana parent candidates appearing elsewhere in local Pulgar-line staging and wiki context.

Literal evidence:

- The image-reread staging for this entry names father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` contains a drafted child link to `Tulio Cesar Luis Jose` from another staged relationship, not from this task's entry 172.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` contains a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from earlier entry-172 staging.
- Local review notes for other Pulgar birth-register entries mention similar father-name evidence and a mother line beginning `Juana de Dios ... de Pulgar`; that is not the same literal name as `Juana Arriagada de Pulgar`.

Interpretation:

- The father name overlap is a reason for a targeted parent-candidate proof review, not a merge.
- The mother candidates `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and any other Jose/Juana variants should remain separate hypotheses until source-by-source identity proof explains the name forms and relationships.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.50 | Plausible same-family cluster, but unresolved across entries. |
| conflict_severity | 0.60 | Premature merging could combine separate couples, children, or mother-name variants. |
| evidence_quality | 0.55 | Local wiki and staged review evidence exists but does not complete cross-entry identity proof. |
| conversion_confidence | 0.34 | This entry is conversion-blocked; related entries have independent QA issues. |
| claim_probability | 0.46 | Possible, not established by this conflict draft. |
| relevance | 0.86 | Important to Pulgar-line structure and downstream identity review. |
| canonical_readiness | 0.08 | Hold pending targeted Jose/Juana parent-candidate proof review. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical context identifies him from family-supplied knowledge as Alexander John Heinz's maternal grandfather and warns not to merge similarly named Pulgar records without identity review. Entry 172 does not name him.
- `Dario Arturo Pulgar`: Staged CV context uses this as a document-level subject name. Entry 172 does not name Dario Arturo and provides no CV-era bridge.
- `Dario Jose Pulgar-Arriagada`: Staged ICRC/Geneva photograph context names Dario Jose Pulgar-Arriagada from source titles or metadata. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, a different given-name cluster.
- `Dario/Dario Pulgar Arriagada`: Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` has a 2000 expropriation event for `Darío Pulgar Arriagada`. Entry 172 is an 1888 birth-registration conflict for a non-Dario child.
- Ranked impact: (1) direct impact on `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; (2) indirect Jose/Juana parent-candidate review; (3) no current basis to attach the entry to any Dario identity.

## Conflicts

- Same-entry conflict: Pulgar/Arriagada source-image reread versus Burgos/de la Cruz or Gomez/de la Cruz derivative converted/chunk text. Severity: critical.
- Name-variant conflict: `Jose del Carmen Pulgar` versus possible father suffix in related derivative staging. Severity: moderate.
- Relationship conflict: child-father, child-mother, and parental-pair claims are not canonical-ready until conversion QA identifies the controlling transcript. Severity: high.
- Duplicate-person risk: high if derivative Burgos/de la Cruz claims are promoted from this mismatched conversion; moderate if Jose/Juana candidates are merged across Pulgar-line entries without proof review.
- Chronology conflict: the competing readings carry different birth dates/times and places. Severity: high for entry 172; low for Dario chronology because no Dario is named.

## Recommended Next Action

Keep the staged conflict draft and all dependent claims/relationships at `hold_for_conversion_qa`.

Exact next proof-review step: perform targeted conversion QA for `CHUNK-23b2269a97df-P0001-01` against the source image or authoritative page image. The QA note must state whether entry 172's controlling transcript is the Pulgar/Arriagada row, retire or correct the derivative Burgos/de la Cruz/Gomez/de la Cruz row assignment, and settle whether the father field reads `Jose del Carmen Pulgar`, a suffixed form, or an uncertain form.

After conversion QA, rerun proof review for the entry-172 child birth-name, sex, birth date/time/place, registration date, father, mother, informant, child-parent relationships, and parental-pair relationship. Separately run a Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or any `Juana de Dios ... de Pulgar` candidate across records. Do not attach this entry to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada unless a later identity-bridging source provides direct support.
