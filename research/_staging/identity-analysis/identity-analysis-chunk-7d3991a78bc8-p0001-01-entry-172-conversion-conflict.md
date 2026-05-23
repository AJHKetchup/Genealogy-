---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-7d3991a78bc8-p0001-01-entry-172-conversion-conflict.md
staged_draft: research/_staging/conflicts/chunk-7d3991a78bc8-p0001-01-entry-172-conversion-conflict.md
source_packet: research/_staging/source-packets/chunk-7d3991a78bc8-p0001-01-entry-172-image-reread-pulgar-arriagada.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md
chunk_id: CHUNK-7d3991a78bc8-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity Analysis: Entry 172 Conversion Conflict

## Blockers

- The staged conflict draft reports a material same-entry contradiction: the assigned chunk and converted Markdown read entry 172 as `Jose Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`, while the image-reread source packet reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`.
- The derivative transcript remains unreconciled. Identity conclusions can be staged only as hypotheses; no person merge, canonical attachment, or promoted relationship should be made from this entry until conversion QA either corrects or retires the Bunster/de la Maza derivative reading.
- The father reading has a smaller unresolved detail: current image-reread support is `Jose del Carmen Pulgar`; prior staging for a related derivative sometimes records a possible final `S.`. Do not expand or normalize the father beyond the literal reading until QA settles that suffix.
- The entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario. Existing wiki context contains Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, and Dario/Pulgar Arriagada clusters, but this entry alone does not bridge the child or parents to any Dario identity.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` already contain evidence generated from a prior entry-172 Pulgar/Arriagada staging. Because the current assigned derivative conflicts with that reading, any further canonical readiness must wait for conversion QA.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Hypothesis: The source image for register page 58, entry 172 records the birth of `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`; the Bunster/de la Maza text is a conversion or derivative-row error.

Literal evidence:

- The staged conflict draft states that original source image reread supports `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- The referenced source packet repeats the image-reread literal support: child name, sex `Hombre`, registration date 7 April 1888, birth date/time 8 March 1888 at 3 p.m., birthplace `Calle de Valdivia`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and official `Emilio Riquelme V.`
- Prior staged packets for entry 172 also preserve the Pulgar/Arriagada reading and identify the derivative text as unreliable until QA reconciliation.
- Canonical `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has prior reviewed evidence for birth name, sex, birth date/time, and birth place from entry 172, and `wiki/people/juana-arriagada-de-pulgar.md` has a probable child link to that person.

Interpretation:

- This is the leading identity hypothesis because the staged draft and source packet both report direct source-image support for the Pulgar/Arriagada cluster.
- It does not prove a broader family-line merge. The record supports a birth-registration identity cluster for child, father, and mother; it does not identify Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.88 | Strong for the entry-172 Pulgar/Arriagada cluster as image-read, reduced by unreconciled derivative text. |
| conflict_severity | 0.92 | The two readings name different child, parents, birth date/time, birthplace, informant, and official. |
| evidence_quality | 0.82 | Civil birth registration plus image-reread packet is strong, but this analysis did not alter or independently re-convert the source. |
| conversion_confidence | 0.35 | Low for the assigned derivative transcript because it conflicts with the image-reread packet. |
| claim_probability | 0.86 | High probability that the image-reviewed Pulgar/Arriagada reading is the correct entry-172 identity cluster. |
| relevance | 0.96 | Critical to Pulgar-line parent-child staging and to preventing false Bunster/de la Maza promotion. |
| canonical_readiness | 0.18 | Hold until conversion QA reconciles the derivative transcript. |

## Hypothesis 2: Entry 172 Is The Bunster/de la Maza Birth Registration

Hypothesis: Entry 172 records `Jose Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`, and the Pulgar/Arriagada reading belongs to another row, page, or derivative context.

Literal evidence:

- The assigned chunk and converted Markdown transcribe entry 172 as `Jose Miguel`, male, born 26 March 1888 at 10 p.m. in `En esta Subdelegacion`, father `Oswaldo Bunster`, mother `Amelia de la Maza`, informant `Oswaldo Bunster`, and official `Camilo Luis osorio`.
- The staged conflict draft explicitly preserves this as literal support from the assigned derivative text.

Interpretation:

- This hypothesis is weak because the staged draft and source packet both state that the source image at the same source path and SHA supports Pulgar/Arriagada instead.
- Do not create, merge, or promote Bunster/de la Maza people from this source unless conversion QA later determines that the image-reread packet was assigned to the wrong source, page, or row.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.22 | Supported only by the disputed derivative text. |
| conflict_severity | 0.92 | If accepted, it would replace every core identity and event detail in the Pulgar/Arriagada staging. |
| evidence_quality | 0.30 | Derivative-only support, directly contradicted by the image-reread packet. |
| conversion_confidence | 0.20 | Current conversion confidence for this reading is low. |
| claim_probability | 0.16 | Possible only if the image-reread packet/source assignment is wrong. |
| relevance | 0.70 | Relevant mainly as a false-positive guardrail. |
| canonical_readiness | 0.02 | Do not promote. |

## Hypothesis 3: Pulgar Parent Candidates Are Same As Other Jose/Juana Pulgar-Line Candidates

Hypothesis: The entry-172 father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar` may be the same Jose/Juana parent candidates appearing elsewhere in local Pulgar-line context.

Literal evidence:

- Existing `wiki/people/jose-del-carmen-pulgar.md` contains a drafted child link to `Tulio Cesar Luis Jose` from another birth-register entry, not from this entry-172 staged draft.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` contains a probable child link to `Jose del Carmen Segundo Pulgar Arriagada` from prior entry-172 staging.
- Local review notes for other entries mention father `Jose del Carmen Pulgar` and mother lines beginning with `Juana de Dios ... de Pulgar`, but those are not the same literal mother name as `Juana Arriagada de Pulgar`.

Interpretation:

- The father name overlap justifies a double-check across Pulgar-line entries, but it does not prove a same-person merge. The entry-172 record gives no age for the father in the current packet and leaves a possible suffix unresolved.
- The mother candidate `Juana Arriagada de Pulgar` should remain separate from any `Juana de Dios ... de Pulgar` candidate unless a proof review establishes name equivalence with exact source support.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.54 | Plausible for same father-name cluster; weaker for mother-name variants without a bridge. |
| conflict_severity | 0.55 | Premature merging could combine separate Jose/Juana couples or children. |
| evidence_quality | 0.58 | Local wiki and staged review context exists, but cross-entry identity proof is incomplete. |
| conversion_confidence | 0.40 | Entry-172 conversion is blocked; other entries have their own QA-sensitive readings. |
| claim_probability | 0.50 | Possible but not resolved by this conflict draft. |
| relevance | 0.84 | Important for Pulgar-line parent-child structure. |
| canonical_readiness | 0.12 | Hold; needs a targeted Jose/Juana parent-candidate proof review. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical page is family-supplied and explicitly warns not to attach similarly named Pulgar records without identity review. Entry 172 does not name Dario Arturo or Pulgar-Smith.
- `Dario Arturo Pulgar`: Existing staged CV analyses support a document-level `Dario Arturo Pulgar` name in CV metadata, with unresolved bridge to `Dario Arturo Pulgar-Smith`. Entry 172 does not name this person.
- `Dario Jose Pulgar-Arriagada`: Existing staged photo/context notes name Dario Jose Pulgar-Arriagada, but this entry names `Jose del Carmen Segundo Pulgar Arriagada`. Shared surname elements are not a proof of identity.
- `Dario/Dario Pulgar Arriagada`: Existing canonical/staged context includes `Dario Pulgar Arriagada` in a 2000 expropriation notice. Entry 172 is an 1888 birth registration for a differently named child and gives no Dario event.
- Ranked identity impact: (1) direct impact on `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; (2) indirect Pulgar-line context only for Dario clusters; (3) no present basis to merge any Dario identity with the entry-172 child or parents.

## Conflicts

- Same-entry conversion conflict: Pulgar/Arriagada image-reread cluster versus Bunster/de la Maza derivative cluster. Severity: critical.
- Duplicate-person risk: high if the derivative Bunster/de la Maza cluster is promoted as entry 172; moderate if Jose/Juana parent candidates are merged across Pulgar entries without proof review.
- Name-variant risk: moderate for `Jose del Carmen Pulgar` versus possible `Jose del Carmen Pulgar S.`; moderate for any attempted `Juana Arriagada` versus `Juana de Dios ...` equivalence; low-to-none for Dario variants within this entry because no Dario name appears.
- Relationship-conflict risk: high for parent-child claims until conversion QA confirms the controlling entry-172 reading.
- Chronology-conflict risk: low within the Pulgar/Arriagada reading; high across the two competing readings because they give different birth dates and places.

## Recommended Next Action

Keep the staged conflict draft on `hold_for_conversion_qa`. The exact next proof-review or promotion step is conversion QA reconciliation for `CHUNK-7d3991a78bc8-P0001-01`: record whether the source image controls as `Jose del Carmen Segundo Pulgar Arriagada` with parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, correct or retire the Bunster/de la Maza derivative text, and settle whether the father's final suffix is present, absent, or uncertain.

After conversion QA, run a targeted proof review of the entry-172 child-name, birth-event, father, mother, and parent-child relationship drafts. Separately, run a Jose/Juana Pulgar parent-candidate identity review before merging entry-172 parents with other Jose/Juana candidates. Do not use this entry to attach evidence to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada unless a later identity-bridging source supplies direct support.
