---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-cda8daf3a341-p0001-01-source-control-and-image-identity-conflict-revision-postconv-evidence-extraction-20260526100318514.md
worker: postconv-identity-analysis-20260526140102076
staged_draft: research/_staging/conflicts/chunk-cda8daf3a341-p0001-01-source-control-and-image-identity-conflict-revision-postconv-evidence-extraction-20260526100318514.md
source_packet: research/_staging/source-packets/chunk-cda8daf3a341-p0001-01-icrc-group-photo-dario-jose-pulgar-arriagada-revision-postconv-evidence-extraction-20260526100318514.md
source: raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG
converted_file: raw/converted/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a.codex.md
chunk: raw/chunks/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a-codex/page-0001-chunk-01.md
chunk_id: CHUNK-cda8daf3a341-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: CHUNK-cda8daf3a341-P0001-01

## Blockers

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-cda8daf3a341-p0001-01-source-control-and-image-identity-conflict-revision-postconv-evidence-extraction-20260526100318514.md`.
- The assigned source file `raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG` is absent from the workspace during this review.
- The converted file's referenced extracted image `raw/codex-conversion-jobs/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a/extracted-images/page-0001/page-0001-image-01-group-at-outdoor-event-1929.png` is also absent.
- A related same-folder image exists, `Photograph of the Geneva Convention assembly (Dario Jose Pulgar-Arriagada at Table 9 Seat 2).jpg`, but the source packet states it has a different SHA-256 and visually appears to be an indoor assembly scene, not the outdoor group photograph described by the converted page. It must not be substituted as the controlling source without conversion QA.
- The converted page says `No text is present on this page` and its visual-region manifest gives `identity_basis: none`.
- The Dario association is from title/file metadata only: `Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives`.
- This staged draft contains no parent, spouse, child, sibling, grandchild, residence, birth, death, or age evidence. It therefore cannot bridge `Dario Jose Pulgar-Arriagada` to any other Pulgar-line identity.
- No external research was performed, and no raw source, converted Markdown, chunk, source-packet, claim, or canonical wiki page was edited.

## Hypothesis 1: Metadata Association With Dario Jose Pulgar-Arriagada

Hypothesis: the source title/file identity intends the image package to be associated with `Dario Jose Pulgar-Arriagada`, but the current staged evidence cannot identify a face or prove the depicted individual.

Literal evidence:

- Staged draft subject: `Dario Jose Pulgar-Arriagada`.
- Source packet `literal_support`: the source document title names `Dario Jose Pulgar-Arriagada`; the page has a single black-and-white photograph; no text is present; `identity_basis: none`.
- Converted/chunk page metadata repeats document ID `V-P-HIST-03583-07A` and the Dario Jose Pulgar-Arriagada title context.

Interpretation:

- This is the best-supported narrow reading: the metadata probably intends a Dario Jose Pulgar-Arriagada association.
- It is not a promotable visual-identity claim because the controlling image and collection metadata are not available for reread, and the converted visual region itself identifies no person.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Repeated metadata names Dario Jose Pulgar-Arriagada, but the page has no caption or face label. |
| conflict_severity | 0.68 | Premature promotion could attach an unidentified or wrong image to a person. |
| evidence_quality | 0.42 | Title/file metadata is useful but indirect; the image is unavailable for source-control verification. |
| conversion_confidence | 0.76 | High for the no-text/general-scene reading; low for person identity. |
| claim_probability | 0.54 | Moderate that the metadata intends the association; low that current evidence proves depiction. |
| relevance | 0.94 | Directly addresses the assigned staged conflict. |
| canonical_readiness | 0.08 | Hold until source-control and image-identity QA are complete. |

## Hypothesis 2: Same Person As Dario Arturo Pulgar-Smith

Hypothesis: `Dario Jose Pulgar-Arriagada` in the ICRC title metadata is the same person as canonical `Dario Arturo Pulgar-Smith`.

Literal evidence:

- `wiki/people/dario-arturo-pulgar-smith.md` identifies `Dario Arturo Pulgar-Smith` from family-supplied knowledge as Alexander John Heinz's maternal grandfather.
- That canonical page explicitly warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review.
- The assigned staged draft names `Dario Jose Pulgar-Arriagada`, not `Dario Arturo Pulgar-Smith`.
- The draft provides no family relationship, date, age, residence, occupation, or name-variant bridge to `Dario Arturo Pulgar-Smith`.

Interpretation:

- Name overlap is not enough. `Jose Pulgar-Arriagada` and `Arturo Pulgar-Smith` are materially different name forms.
- Family context justifies a future double-check, but this image-title packet cannot support merge, rename, gallery attachment, or promoted facts for `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.14 | Only broad Dario/Pulgar overlap exists. |
| conflict_severity | 0.80 | A wrong merge would contaminate the main family-supplied Dario anchor. |
| evidence_quality | 0.30 | No direct bridge evidence appears in this staged draft. |
| conversion_confidence | 0.76 | Conversion supports no visible text, not identity. |
| claim_probability | 0.12 | Low on this evidence alone. |
| relevance | 0.88 | Required Pulgar-line comparison. |
| canonical_readiness | 0.02 | No canonical action supported. |

## Hypothesis 3: Same Person As Dario Arturo Pulgar

Hypothesis: `Dario Jose Pulgar-Arriagada` in this ICRC metadata is the same person as staged CV subject `Dario Arturo Pulgar`.

Literal evidence:

- Existing staged CV contexts use `Dario Arturo Pulgar` as a document-level subject and repeatedly hold the bridge to `Dario Arturo Pulgar-Smith` for separate proof review.
- This assigned staged draft uses `Dario Jose Pulgar-Arriagada`.
- The assigned draft has no CV chronology, education, language, residence, employment, or family evidence.

Interpretation:

- The CV cluster and ICRC image-title cluster should remain separate until a proof-reviewed source explicitly ties the two name forms or biographies together.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Different middle name and surname form, with no shared biographical bridge. |
| conflict_severity | 0.74 | A merge could combine unrelated generations or professional contexts. |
| evidence_quality | 0.28 | No direct supporting evidence in this draft. |
| conversion_confidence | 0.76 | The conversion limitation is identity-specific. |
| claim_probability | 0.08 | Very low from this evidence. |
| relevance | 0.78 | Relevant as a duplicate-person guardrail. |
| canonical_readiness | 0.01 | No promotion or merge supported. |

## Hypothesis 4: Same Person As Dario/Dario Pulgar Arriagada

Hypothesis: `Dario Jose Pulgar-Arriagada` is the same person as the canonical `Darío Pulgar Arriagada` / `Dario Pulgar Arriagada` cluster.

Literal evidence:

- `wiki/people/dar-o-pulgar-arriagada.md` exists for `Darío Pulgar Arriagada` and currently records a 5 December 2000 expropriation event.
- The assigned staged draft uses the fuller metadata-derived form `Dario Jose Pulgar-Arriagada`.
- The draft provides no birth year, age, residence, property, occupation, or family relationship to connect the 1929 title context with the 2000 canonical cluster.

Interpretation:

- This is a live name-variant question because the surname form is close.
- It is not a resolved duplicate-person finding. The 1929 metadata cluster and the 2000 expropriation cluster need an explicit identity bridge before any merge or attachment.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | Surname-form overlap is stronger, but chronology and biography are missing. |
| conflict_severity | 0.64 | Wrong merge would connect separate event contexts without proof. |
| evidence_quality | 0.36 | Evidence is sparse and indirect. |
| conversion_confidence | 0.76 | Current conversion does not settle identity. |
| claim_probability | 0.22 | Possible, not demonstrated. |
| relevance | 0.82 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | Hold pending explicit identity bridge. |

## Hypothesis 5: Relationship To Jose/Juana Parent Candidates

Hypothesis: Jose/Juana parent candidates in existing Pulgar-line context connect to `Dario Jose Pulgar-Arriagada`.

Literal evidence:

- Existing canonical context includes `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada`.
- Existing wiki evidence for those pages concerns separate birth-register or relationship clusters, including held or draft relationship evidence.
- The assigned staged draft does not name `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, or any parent candidate.
- The assigned staged draft does not state any parent-child, spouse, sibling, household, witness, or informant relationship.

Interpretation:

- Jose/Juana candidates are a future lineage-check list only.
- Do not infer a relationship from the middle name `Jose`, from the Pulgar surname, or from family-context hints.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | No relationship evidence appears in this staged draft. |
| conflict_severity | 0.58 | Premature lineage attachment would create false family structure. |
| evidence_quality | 0.34 | Parent-candidate evidence is separate and partly draft/held. |
| conversion_confidence | 0.76 | This image conversion does not address lineage. |
| claim_probability | 0.05 | No supported relationship claim. |
| relevance | 0.66 | Relevant only as a Pulgar-line guardrail. |
| canonical_readiness | 0.01 | No relationship promotion supported. |

## Conflicts

- Source-control conflict: high. The assigned original JPG and extracted image are absent, while a different same-folder image exists.
- Image-identity conflict: high. The source title names Dario Jose Pulgar-Arriagada, but the converted page has no text and records `identity_basis: none`.
- Duplicate-person risk: high if merged by name alone. Current evidence favors keeping `Dario Jose Pulgar-Arriagada`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, and `Dario/Darío Pulgar Arriagada` as unresolved separate clusters.
- Name-variant conflict: moderate-high. `Dario Jose Pulgar-Arriagada` is not proved to be a variant of `Dario Arturo Pulgar-Smith` or `Dario Arturo Pulgar`; it is only a possible unresolved variant of `Dario/Darío Pulgar Arriagada`.
- Relationship-conflict evidence: none in this staged draft. No Jose/Juana parent candidate is named or implied by a source statement.
- Chronology-conflict evidence: unresolved. The title context points to 1929; other Pulgar clusters include family-supplied, CV/Habitat, passenger-list, birth-register, and 2000 property contexts. This draft has no age or lifespan evidence to reconcile them.

## Ranked Hypotheses

| rank | hypothesis | probability | next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Metadata/title intends an association with `Dario Jose Pulgar-Arriagada` | 0.54 | Conversion/source-control QA must restore or verify `V-P-HIST-03583-07A.JPG` and any ICRC metadata. |
| 2 | Same as `Dario/Darío Pulgar Arriagada` canonical cluster | 0.22 | Require an explicit identity bridge with dates, residence, occupation, or source metadata before merge. |
| 3 | Same as `Dario Arturo Pulgar-Smith` | 0.12 | Require proof that `Jose Pulgar-Arriagada` and `Arturo Pulgar-Smith` are the same person before canonical attachment. |
| 4 | Same as staged CV subject `Dario Arturo Pulgar` | 0.08 | Require a proof-reviewed source bridging the CV subject to the ICRC/Geneva metadata. |
| 5 | Connected to Jose/Juana parent candidates | 0.05 | No action; revisit only if a source states parentage or another direct relationship. |

## Recommended Next Action

Keep the staged conflict and related image/depiction claim on `hold_for_conversion_qa`.

Exact next step: a conversion-QA/proof-review worker should restore or locate the original `V-P-HIST-03583-07A.JPG` and any ICRC collection metadata, verify whether the currently present same-folder indoor assembly image is a separate source or a replacement candidate, and determine whether any source metadata identifies Dario Jose Pulgar-Arriagada in the specific image. Only after that review should any held depiction claim be revised, and any later promotion to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, or `Dario/Darío Pulgar Arriagada` must cite an explicit identity bridge.
