---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-aeb680c662f4-p0001-01-source-availability-and-identity-qa.md"
worker: postconv-identity-analysis-20260523115513149
staged_conflict_draft: "research/_staging/conflicts/chunk-aeb680c662f4-p0001-01-source-availability-and-identity-qa.md"
subject: "Dario Jose Pulgar-Arriagada in V-P-HIST-01820-01"
source_packet: "research/_staging/source-packets/chunk-aeb680c662f4-p0001-01-v-p-hist-01820-01-geneva-convention-photograph.md"
converted_file: "raw/converted/ca58706dfd-v-p-hist-01820-01-1-v-p-hist-01820-01-1.codex.md"
chunk: "raw/chunks/ca58706dfd-v-p-hist-01820-01-1-v-p-hist-01820-01-1-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-aeb680c662f4-P0001-01"
analysis_status: hold
promotion_recommendation: do_not_promote
canonical_readiness: hold_for_source_availability_and_metadata_review
tags: [identity-analysis, conflict-review, source-availability, pulgar]
---

# Identity And Conflict Analysis: V-P-HIST-01820-01

## Blockers First

- The exact staged conflict draft reviewed here is `research/_staging/conflicts/chunk-aeb680c662f4-p0001-01-source-availability-and-identity-qa.md`.
- The recorded original source image is absent in this checkout: `raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-01820-01 (1).JPG`.
- The extracted-images directory recorded by the converted file is also absent: `raw/codex-conversion-jobs/ca58706dfd-v-p-hist-01820-01-1-v-p-hist-01820-01-1/extracted-images`.
- The converted page describes a formal assembly photograph and transcribes faint date/desk-number markings, but it does not visibly name `Dario Jose Pulgar-Arriagada`.
- The visual-region manifest records `identity_basis: "none"`. The Dario identification comes from local source path/title context, not from visible caption text, a roster, handwriting, face labeling, or a region-level identification.
- This staged draft supplies no birth date, death date, age, occupation, nationality, residence, parent, spouse, child, grandchild, or household relationship.
- Existing Pulgar-line context contains multiple similarly named candidates: `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario J. Pulgar Arriagada`, adult and child `Dario Pulgar` passenger clusters, and Jose/Juana parent candidates. This photograph draft does not bridge them.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, or canonical wiki pages were edited.

## Literal Source Reading

The converted page literally supports only a photograph setting and visible markings:

```text
The page consists of a single, large black and white photograph depicting a formal assembly or conference.
```

```text
1.H.J.U.L.I.S. - 1929
15.09.1929
```

```text
1
7
13
19
3
9
15
25
```

The source packet and converted metadata give the local source path:

```text
raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-01820-01 (1).JPG
```

Interpretation kept separate: the local source-folder/title context probably intends an association with `Dario Jose Pulgar-Arriagada`, but the current converted page does not identify any person in the photograph by visible text.

## Hypothesis 1: Source Metadata Intends Dario Jose Pulgar-Arriagada

Hypothesis: the local source title/path intends `V-P-HIST-01820-01` to be associated with `Dario Jose Pulgar-Arriagada`, but the present evidence cannot identify him in the image.

Supporting evidence:

- The staged conflict draft names the subject as `Dario Jose Pulgar-Arriagada in V-P-HIST-01820-01`.
- The source packet source path is inside a folder titled as photographs of the 1929 Geneva Convention showing `Dario Jose Pulgar-Arriagada`.
- The converted file repeats that source path and describes a 1929 formal assembly/conference photograph.
- The date `15.09.1929` is visibly transcribed and is consistent with the staged Geneva Convention photograph context.

Conflicts and limits:

- The converted page contains no visible personal name.
- The visual region has `identity_basis: "none"`.
- The original image and extracted crop are unavailable for local reread.
- The source packet says the family identification comes from source path/title context and recommends holding for conversion QA.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.44 | Metadata consistently points to Dario Jose Pulgar-Arriagada, but no visible page evidence identifies him. |
| conflict_severity | 0.68 | Premature promotion could attach an unidentified group photograph to the wrong person or face. |
| evidence_quality | 0.40 | Evidence is path/title metadata plus a converted visual description, not direct identity evidence. |
| conversion_confidence | 0.72 | Conversion is usable for general photograph/date markings, but weak for personal identification. |
| claim_probability | 0.52 | Moderate that metadata intends the association; low that current evidence proves a depicted individual. |
| relevance | 0.96 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.07 | Hold until original image and archive/source metadata are reviewed. |

## Hypothesis 2: Same Person As `Dario/Darío Pulgar Arriagada`

Hypothesis: title-derived `Dario Jose Pulgar-Arriagada` is the same person as the canonical/staged `Dario/Darío Pulgar Arriagada` cluster.

Supporting evidence:

- The names share `Dario/Darío` and the `Pulgar Arriagada` surname elements.
- Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` preserves a separate `Darío Pulgar Arriagada` stub.

Conflicts and limits:

- The canonical `Darío Pulgar Arriagada` stub currently reflects a 2000-12-05 Chiguayante expropriation notice, while this staged draft concerns a 1929 Geneva Convention photograph.
- The photograph draft has no age, occupation, residence, property, relationship, or lifespan evidence connecting the 1929 and 2000 contexts.
- The middle name `Jose` appears only in the photograph source-path/title context and is not visible on the converted image.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.24 | The surname-form overlap is meaningful, but there is no biographical bridge. |
| conflict_severity | 0.66 | A wrong merge would connect separate event contexts across 71 years. |
| evidence_quality | 0.34 | Compared evidence is sparse and context-dependent. |
| conversion_confidence | 0.62 | The image conversion does not settle identity; the expropriation cluster has separate QA limits. |
| claim_probability | 0.22 | Possible name-variant question, not demonstrated. |
| relevance | 0.84 | Required Pulgar-Arriagada comparison. |
| canonical_readiness | 0.04 | Not ready for merge, variant control, or attachment. |

## Hypothesis 3: Same Person As `Dario J. Pulgar Arriagada`

Hypothesis: `Dario Jose Pulgar-Arriagada` in the photograph metadata is the same person as the staged 1918 medical-title candidate `Dario J. Pulgar Arriagada`.

Supporting evidence:

- `J.` could stand for `Jose`, and both forms share `Dario` plus `Pulgar Arriagada`.
- A 1918 medical-title context and a 1929 Geneva Convention photograph context are chronologically possible for one adult.

Conflicts and limits:

- The 1918 source does not expand `J.` to `Jose`.
- This photograph draft does not state profession, age, nationality, delegate role, or any medical identity marker.
- Prior local analysis keeps the 1918 line on conversion QA/proof-review hold.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.38 | Name and chronology are plausible, but no direct bridge appears. |
| conflict_severity | 0.58 | Expanding `J.` to Jose from metadata alone risks conflating staged clusters. |
| evidence_quality | 0.42 | Both sides need proof-review or metadata support before linkage. |
| conversion_confidence | 0.50 | The 1918 item and this photograph identity are both held for QA. |
| claim_probability | 0.34 | Possible, not proved. |
| relevance | 0.88 | Direct middle-name/name-variant comparison. |
| canonical_readiness | 0.06 | Do not merge or promote as a controlled variant. |

## Hypothesis 4: Same Person As `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith`

Hypothesis: the photograph metadata person `Dario Jose Pulgar-Arriagada` is the same person as staged CV subject `Dario Arturo Pulgar` or canonical family-supplied `Dario Arturo Pulgar-Smith`.

Supporting evidence:

- All forms share the broad `Dario` and `Pulgar` elements.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is the family-supplied Dario anchor for Alexander John Heinz's maternal line.
- The canonical Pulgar-Smith page explicitly warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records should be attached only after identity review.

Conflicts and limits:

- This staged draft uses `Dario Jose Pulgar-Arriagada` in source metadata, not `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or `Pulgar-Smith`.
- It provides no CV, Habitat, Chile/Canada, child-passenger, family-supplied, or grandparent bridge.
- The 1929 Geneva photograph context is not enough to connect to the later CV/Pulgar-Smith cluster.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Shared given name and paternal surname only; middle and surname forms differ. |
| conflict_severity | 0.80 | Wrong attachment would misattribute a photograph and collapse distinct Pulgar-line identities. |
| evidence_quality | 0.28 | No direct bridge supports the Arturo or Pulgar-Smith hypothesis. |
| conversion_confidence | 0.72 | Conversion describes the image but cannot support this identity link. |
| claim_probability | 0.08 | Very low from this staged draft alone. |
| relevance | 0.88 | Required because Pulgar-Smith is the canonical family anchor. |
| canonical_readiness | 0.01 | No canonical action supported. |

## Hypothesis 5: Same Person As Adult Or Child `Dario Pulgar` Passenger Clusters

Hypothesis: `Dario Jose Pulgar-Arriagada` in the 1929 photograph metadata is the same person as either the adult `Dario Pulgar` passenger or the child `Dario Pulgar` passenger preserved in local 1953 passenger-list context.

Supporting evidence:

- The adult 1953 row has been analyzed locally as `Dario Pulgar`, age 64, occupation/calling `Medical`, which could be chronologically compatible with an adult present in 1929.
- The child 1953 row has been analyzed locally as `Dario Pulgar`, age 11, which is not compatible with being a 1929 adult but is relevant as an anti-conflation candidate.

Conflicts and limits:

- This photograph draft gives no age, occupation, passenger-list details, family group, `Arturo`, `Smith`, `Jose`, or full surname bridge.
- The child passenger cannot be the 1929 conference adult if the child age-11 reading is correct.
- The adult passenger remains at most a possible older medical Pulgar comparison, not a same-person proof.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Some chronological plausibility for the adult passenger; none for the child as a 1929 adult. |
| conflict_severity | 0.70 | High duplicate-person risk if passenger clusters are merged by name alone. |
| evidence_quality | 0.38 | Passenger evidence is separate and does not bridge this image. |
| conversion_confidence | 0.56 | The photograph identity and some passenger-row details remain held for targeted QA. |
| claim_probability | 0.16 | Possible for adult passenger only; unsupported overall. |
| relevance | 0.72 | Useful Pulgar-line anti-conflation context. |
| canonical_readiness | 0.03 | No merge or attachment supported. |

## Hypothesis 6: Related To Jose/Juana Parent Candidates

Hypothesis: Jose/Juana parent candidates explain or connect `Dario Jose Pulgar-Arriagada` to the broader Pulgar line.

Supporting evidence:

- Existing wiki context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- `Jose del Carmen Segundo Pulgar Arriagada` shares the `Pulgar Arriagada` surname combination, and Jose/Juana clusters are relevant Pulgar-line checklist items.

Conflicts and limits:

- This staged draft does not name any Jose or Juana parent candidate.
- It states no parent, spouse, child, sibling, household, informant, witness, grandparent, or lineage relationship.
- `Jose` as a possible middle name cannot be treated as evidence for a Jose parent or any Juana mother.
- Related Jose/Juana register clusters have their own conversion and relationship QA cautions.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No direct same-person or kinship bridge appears. |
| conflict_severity | 0.58 | Unsupported lineage attachment would create false relationship claims. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.42 | Jose/Juana materials remain mixed; this image does not address lineage. |
| claim_probability | 0.04 | This draft supports no relationship claim. |
| relevance | 0.66 | Required Pulgar-line checklist only. |
| canonical_readiness | 0.01 | No relationship promotion supported. |

## Conflict Summary

- Source-availability conflict: high. The original source image and extracted-images directory are absent, blocking independent local reread.
- Conversion-vs-identity conflict: high. The conversion supports a formal 1929 assembly photograph and visible desk/date markings; it does not visibly identify Dario Jose Pulgar-Arriagada.
- Name-variant conflict: moderate-high. `Dario Jose Pulgar-Arriagada` is not proved to be a variant of `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario/Darío Pulgar Arriagada`, or `Dario J. Pulgar Arriagada`.
- Duplicate-person risk: high if merged by name alone. Current evidence supports a held metadata/title association only.
- Relationship-conflict evidence: none in this staged draft. No Jose/Juana parent, spouse, child, sibling, household, grandparent, or maternal-line relationship is stated.
- Chronology-conflict evidence: unresolved. A 1929 photograph context might fit an older Pulgar-Arriagada medical cluster, but the draft gives no age, role, or lifespan evidence. It does not fit the 1953 child passenger as the same adult subject.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Source metadata/title intends association with `Dario Jose Pulgar-Arriagada` | 0.52 | Hold for original image and ICRC/archive metadata reread. |
| 2 | Same as `Dario J. Pulgar Arriagada` medical-title candidate | 0.34 | Preserve as possible; require proof-reviewed bridge for `J.`/`Jose`, role, and chronology. |
| 3 | Same as `Dario/Darío Pulgar Arriagada` name cluster | 0.22 | Preserve as unresolved name-variant question; no merge. |
| 4 | Same as adult `Dario Pulgar` passenger cluster | 0.16 | Keep as a weak adult medical-cluster comparison only. |
| 5 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.08 | Do not attach; require explicit bridge from Jose/Pulgar-Arriagada to Arturo/Pulgar-Smith. |
| 6 | Related to Jose/Juana parent candidates | 0.04 | No lineage action; revisit only with direct relationship evidence. |
| 7 | Same as 1953 child `Dario Pulgar` passenger | 0.01 | Treat as anti-conflation; age chronology conflicts with 1929 adult-conference context. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-aeb680c662f4-p0001-01-source-availability-and-identity-qa.md` on hold and do not promote a canonical conflict, person merge, gallery item, event-presence claim, seat-location claim, or family relationship from this evidence.

The exact next proof-review step is source-availability and metadata QA: restore or locate the original `V-P-HIST-01820-01 (1).JPG`, the extracted page image, and any local ICRC/archive metadata for the item. Then reread the image and metadata to determine whether they explicitly identify `Dario Jose Pulgar-Arriagada` and whether any image region, caption, roster, table/seat information, or archive description identifies the person. Only after that should proof review decide whether a narrow held photograph-association claim is ready. Any later merge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario/Darío Pulgar Arriagada`, `Dario J. Pulgar Arriagada`, or any Jose/Juana parent cluster must cite an explicit identity or relationship bridge.
