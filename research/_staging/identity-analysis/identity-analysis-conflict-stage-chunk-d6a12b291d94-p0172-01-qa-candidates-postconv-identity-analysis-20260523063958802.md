---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d6a12b291d94-P0172-01-qa-candidates.md
worker: postconv-identity-analysis-20260523063958802
staged_draft: research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d6a12b291d94-P0172-01-qa-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
promotion_recommendation: hold_for_conversion_qa
---

# Identity And Conflict Analysis: CONFLICT-STAGE-CHUNK-d6a12b291d94-P0172-01

## Blockers First

- The exact staged conflict draft `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d6a12b291d94-P0172-01-qa-candidates.md` recommends `hold_for_conversion_qa`.
- Entry 515 is the controlling blocker. The converted chunk reads mother `Carmen Fuentes`, but the staged conflict draft and source packet say the available PNG is cropped before the mother field can be checked. Do not promote `Carmen Fuentes` or the entry 515 child-parent relationship until complete-row QA is done.
- Entry 515 also should not be promoted as a resolved child/father/mother trio because the image-reviewed evidence only partly supports the lower row. Preserve the derivative transcript separately from the visible-source limitation.
- Entry 513 includes Pulgar-line parent candidates, but the only literal d6a12b reading is `Jose del Carmen Pulgar` / `Jose del C. Pulgar` and `Juana de Dios Amagada de Pulgar`. Do not silently correct `Amagada` to `Arriagada` or attach the entry to broader Pulgar-line identities without a proof-reviewed bridge.
- Existing wiki context includes `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Darío Pulgar Arriagada`; this page does not name any Dario identity. These names are anti-conflation comparison targets only.

## Evidence Scope

This note uses only the assigned conflict draft, its referenced source packet, converted file, chunk, reviewed local notes already in the workspace, and existing canonical wiki pages. No external research was performed. Literal readings below are separated from interpretation.

## Hypothesis 1: Entry 515 Is A Conversion-QA Hold, Not A Canonical Identity Ready Entry

Literal evidence:

- The converted file and chunk read entry 515 as child `Rosa Elvira del Carmen`, father/declarant `Pedro Pablo Leiva`, and mother `Carmen Fuentes`.
- The staged conflict draft says the source image visibly supports the entry context and appears to support the father/declarant field, but the mother field is below the visible cropped area.
- The source packet says entry 515 is cut off at the bottom of the image and specifically warns to hold entry 515 claims depending on the cropped lower row.

Interpretation:

- The highest-confidence identity conclusion for entry 515 is negative: do not promote or merge the child, father, or mother relationship from this draft yet.
- `Pedro Pablo Leiva` is more visible than `Carmen Fuentes`, but the staged draft still ties the row to an incomplete image, so the father-child and mother-child relationships should wait for a complete page or continuation image.
- `Santiago Fuentes` appears only as a witness in the derivative transcript and should not be inferred as kin to `Carmen Fuentes` from surname alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.35 | The derivative row has names, but the lower-row source evidence is incomplete. |
| conflict_severity | 0.86 | Promoting the wrong mother or child-parent trio would create false family links. |
| evidence_quality | 0.38 | The evidence is a derivative transcription with a cropped source-image blocker. |
| conversion_confidence | 0.30 | The conflict draft directly downgrades the converted row for the mother field. |
| claim_probability | 0.40 | Possible as a transcript hypothesis, not proved enough for canonical use. |
| relevance | 0.95 | This is the main QA conflict in the assigned draft. |
| canonical_readiness | 0.02 | Not ready until complete-row proof review. |

## Hypothesis 2: Entry 513 Names Jose Del Carmen Pulgar As Father And Jose Del C. Pulgar As Declarant

Literal evidence:

- The chunk and converted file read entry 513 father as `José del Carmen Pulgar`.
- The same row reads the declarant as `José del C. Pulgar`, `Padre`, age forty-seven, agriculturist, domiciled at Calle Colon.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` is a stub with a draft child link to `Tulio Cesar Luis Jose` from the d6a12b staged relationship evidence.

Interpretation:

- Within the d6a12b row, `Jose del C. Pulgar` is probably the same person as `Jose del Carmen Pulgar`, because the role is father, the surname matches, and the middle initial expands naturally to `Carmen`.
- That same-person conclusion is internally strong for entry 513, but still should remain draft because the staged conflict draft is a QA candidate note and nearby Pulgar-line local reviews include related name-reading cautions.
- Exact next proof-review step: verify the father/declarant fields against the page image and reconcile any visible suffix or variant such as `Jose del Carmen Pulgar S.` before promotion.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Father/declarant same-person evidence is strong within the row. |
| conflict_severity | 0.58 | Mistakes would affect parentage, but this is less blocked than entry 515. |
| evidence_quality | 0.64 | Civil register row is direct, but still derivative until image proof review resolves local variants. |
| conversion_confidence | 0.66 | The d6a12b transcript is internally consistent for father/declarant. |
| claim_probability | 0.74 | Likely same person within the row. |
| relevance | 0.90 | Direct Pulgar-line parent candidate. |
| canonical_readiness | 0.42 | Review-ready, not promotion-ready. |

## Hypothesis 3: Entry 513 Mother Is Juana De Dios Amagada De Pulgar, Separate From Juana Arriagada Unless Proved Otherwise

Literal evidence:

- The converted file and chunk read entry 513 mother as `Juana de Dios Amagada de Pulgar`.
- The assigned conflict draft flags entry 513 maternal surname spelling and says it should be proof-read before canonical identity promotion.
- Existing canonical `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a stub with a draft child link to `Tulio Cesar Luis Jose`.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` is a separate stub tied to `Jose del Carmen Segundo Pulgar Arriagada` from other local entry-172 evidence.

Interpretation:

- The literal d6a12b reading supports a Juana de Dios Amagada hypothesis, not an automatic Arriagada correction.
- The broader local Pulgar context justifies a side-by-side proof-review check against `Juana Arriagada de Pulgar`, but that is a double-check lead, not identity proof.
- Exact next proof-review step: perform a crop-level reread of the entry 513 mother field and compare the confirmed letters against the separate `Juana Arriagada de Pulgar` evidence before any merge or rename.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.56 | The staged name is explicit, but the surname is specifically flagged for proof review. |
| conflict_severity | 0.78 | Amagada/Arriagada conflation would corrupt Pulgar-line parentage. |
| evidence_quality | 0.56 | Direct register evidence, but name-reading uncertainty remains. |
| conversion_confidence | 0.50 | The conflict draft rates the reading medium-high but calls for proofing. |
| claim_probability | 0.55 | Plausible literal reading, unresolved as a canonical identity. |
| relevance | 0.92 | Required Jose/Juana parent-candidate comparison. |
| canonical_readiness | 0.22 | Hold until maternal surname proof review. |

## Hypothesis 4: Entry 514 Contains A Spouse-Clue Conflict, Not A Father Reassignment

Literal evidence:

- The converted file and chunk read entry 514 child as `Rigoberto Juan Bautista`, mother/declarant as `Mercedes Riquelme`, and father as `Belisario Riquelme`.
- The same row describes Mercedes Riquelme as `Esposa de Juan Soler`.
- The staged conflict draft says `Juan Soler is spouse of declarant, not stated as the child's father in this record`.
- The staged conflict draft also notes that Belisario Riquelme has blank nationality, profession, and domicile attributes.

Interpretation:

- `Juan Soler` should remain a spouse clue for Mercedes Riquelme only. It is not father evidence for Rigoberto Juan Bautista.
- `Belisario Riquelme` can be retained as the derivative father-field reading, with blank attributes preserved as blanks. Do not infer nationality, profession, or domicile.
- Exact next proof-review step: verify entry 514 father and spouse/declarant fields against the source image before promoting a father-child relationship or spouse relationship.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | The row clearly separates father field and spouse clue in the derivative transcript. |
| conflict_severity | 0.55 | Main risk is misassigning Juan Soler as father or filling blank attributes. |
| evidence_quality | 0.62 | Direct register transcript, sparse father details. |
| conversion_confidence | 0.64 | Staged conflict draft rates the row medium-high/high, with blank fields explicit. |
| claim_probability | 0.70 | Likely spouse clue and father-field reading as transcribed, pending image QA. |
| relevance | 0.80 | Directly addresses relationship-conflict evidence in the assigned draft. |
| canonical_readiness | 0.40 | Needs ordinary proof review before relationship promotion. |

## Hypothesis 5: Witness And Official Names Are Mentions Only

Literal evidence:

- The converted file and chunk list witnesses `Benjamin Utria`, `Ignacio Jara`, `Jose D. Ramirez`, and `Santiago Fuentes`.
- The staged conflict draft says witness names are not enough for canonical identity merges.
- The converted file and chunk repeat `Emilio Lininger O. del R. C.` as official signature for the entries.
- The staged conflict draft says the official signature is official attribution, not a family relationship.

Interpretation:

- These names should remain event/record-role mentions unless independently corroborated.
- No same-person, kinship, or duplicate-person merge should be made from witness or official signature evidence alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | The names are present, but identity attributes are sparse. |
| conflict_severity | 0.25 | Low if kept as mentions; avoid surname-only inference. |
| evidence_quality | 0.45 | Witness/official mentions are minimal identity evidence. |
| conversion_confidence | 0.58 | Medium-high derivative confidence, lowered for entry 515 crop context. |
| claim_probability | 0.60 | Probable as role mentions only. |
| relevance | 0.55 | Useful to prevent over-promotion. |
| canonical_readiness | 0.00 | Do not promote as canonical people from this draft alone. |

## Required Pulgar-Line Ranking

| Rank | Identity hypothesis | Probability | Evidence and required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 513 father/declarant is the existing draft-stub candidate `Jose del Carmen Pulgar` | 0.74 | Direct d6a12b father/declarant readings. Next: image proof review of father/declarant and any suffix/variant before promotion. |
| 2 | Entry 513 mother is the existing draft-stub candidate `Juana de Dios Amagada de Pulgar` | 0.55 | Direct d6a12b mother reading, but surname requires proofing. Next: crop-level proof review of the maternal surname. |
| 3 | Entry 513 mother/child evidence is connected to `Juana Arriagada de Pulgar` and `Jose del Carmen Segundo Pulgar Arriagada` | 0.28 | Local wiki context has a separate Juana/Jose Pulgar-Arriagada cluster, but d6a12b does not literally read Arriagada or Jose del Carmen Segundo. Next: compare confirmed entry images and dates after d6a12b surname QA. |
| 4 | Entry 513 is an ancestor-line lead for `Dario Arturo Pulgar-Smith` | 0.08 | Canonical Dario Arturo Pulgar-Smith is family-supplied and warns against automatic similar-name attachment; d6a12b gives no Dario, Arturo, Smith, descendant, or lineage bridge. Next: require a proof-reviewed lineage source explicitly connecting the confirmed entry 513 family to Dario Arturo Pulgar-Smith. |
| 5 | Entry 513 is an ancestor-line lead for staged `Dario Arturo Pulgar` | 0.07 | Dario Arturo Pulgar appears in CV source-title contexts elsewhere; d6a12b does not name Dario or provide CV/occupation continuity. Next: require a reviewed lineage bridge, then compare Dario Arturo Pulgar to Dario Arturo Pulgar-Smith separately. |
| 6 | Entry 513 is the same cluster as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Darío Pulgar Arriagada` | 0.04 | Only broad Pulgar/Jose/Juana family-context overlap exists. Existing Dario Jose and Darío Pulgar Arriagada evidence is separate photo/directory/expropriation context. Next: no merge; revisit only after confirmed parentage/date/place evidence creates a real bridge. |

## Conflict Summary

- Same-person: `Jose del Carmen Pulgar` and `Jose del C. Pulgar` are probably the same person within entry 513, pending image proof review.
- Duplicate-person: `Juana de Dios Amagada de Pulgar` and `Juana Arriagada de Pulgar` must remain separate hypotheses unless the surname is proof-reviewed and corroborated.
- Name-variant: `Amagada` is a literal d6a12b reading under QA; do not normalize it to `Arriagada` or another surname from family context.
- Relationship conflict: entry 514 says Juan Soler is spouse of Mercedes Riquelme, not father of the child. Entry 515 child-parent relationships are blocked by the cropped lower row.
- Chronology conflict: no chronology conflict is proved within entries 513-515. Dario chronology comparisons are premature because this draft contains no Dario identity evidence.
- Conversion conflict: entry 515 is the active conversion/source conflict; entry 513 maternal surname is a lower-level proofing conflict; entry 514 blank father attributes must remain blank.

## Recommended Next Action

Keep `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-d6a12b291d94-P0172-01-qa-candidates.md` on `hold_for_conversion_qa`.

Exact next proof-review step: locate or generate a complete source view for page 172 that includes the lower part of entry 515, then perform side-by-side proof review of entries 513-515. For entry 513, confirm the child name, `Jose del Carmen Pulgar` / `Jose del C. Pulgar` father-declarant reading, and `Juana de Dios Amagada de Pulgar` maternal surname before comparing to Arriagada variants. For entry 514, preserve blank father attributes and verify that Juan Soler is only Mercedes Riquelme's spouse clue. For entry 515, do not promote `Carmen Fuentes` or any full child-parent relationship until the mother field is visible and proof-reviewed.

Do not merge, rename, promote, or attach this register page to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Darío Pulgar Arriagada` without a later proof-reviewed identity bridge.
