---
type: identity_conflict_analysis
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/CONFLICT-STAGE-CHUNK-c136e7acf00f-P0001-01-source-image-missing-qa.md"
worker: postconv-identity-analysis-20260523080352067
staged_draft: "research/_staging/conflicts/CONFLICT-STAGE-CHUNK-c136e7acf00f-P0001-01-source-image-missing-qa.md"
subject: "Highland Loch passenger list, Pulgar rows"
source_packet: "research/_staging/source-packets/SP-STAGE-CHUNK-c136e7acf00f-P0001-01-highland-loch-pulgar-passenger-list.md"
source_path: "raw/sources/Passenger List, Pacific Steam Navigation Co., Official Number 143667, 8th July 1928..png"
converted_file: "raw/converted/cadfbbb3a3-passenger-list-pacific-s-passenger-list-pacific-steam-navigation-co-official-number-143667-8th-july-1928.codex.md"
chunk: "raw/chunks/cadfbbb3a3-passenger-list-pacific-s-passenger-list-pacific-steam-navigation-co-offici-bf75a09294/page-0001-chunk-01.md"
chunk_id: "CHUNK-c136e7acf00f-P0001-01"
page_reference: "page 1; right page P.M. 26; rows 55-56 and 65"
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Source Image Missing For Highland Loch Pulgar Rows

## Blockers First

- The exact staged conflict draft analyzed here is `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-c136e7acf00f-P0001-01-source-image-missing-qa.md`.
- The original PNG recorded at `raw/sources/Passenger List, Pacific Steam Navigation Co., Official Number 143667, 8th July 1928..png` is not present in this workspace. Current `Test-Path` returned false.
- The controller and staged conflict draft both flag this as `qc:reread-page`; therefore row readings, ditto marks, and dense table column alignment remain conversion-dependent.
- This is not yet an independent genealogical conflict. It is a conversion QA blocker that prevents promotion of derivative passenger-list claims.
- The converted text supports only `Dario Pulgar A.`, not an expanded `Dario Pulgar Arriagada`, `Dario Jose Pulgar-Arriagada`, `Dario Arturo Pulgar`, or `Dario Arturo Pulgar-Smith`.
- The row for `Dorothy Pulgar` follows `Dario Pulgar A.`, but the source has no relationship column or explicit spouse/kinship wording.
- `Luis Lopez de Romana` appears in row 65, but this page does not state any Pulgar-family connection.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged drafts, or canonical wiki pages were edited.

## Literal Source Readings

Converted row 55 reads:

```text
| 55 | Valparaiso | " | Dario Pulgar A. | c/o Anglo South American Bank Ltd. London | 1 | Medical Surgeon | 39 | ... | Chile | Chile | ... | France [handwritten diamond symbol] |
```

Converted row 56 reads:

```text
| 56 | " | " | Dorothy Pulgar | do | 1 | -- | | 25 | ... | do | do | ... | do |
```

Converted row 65 reads:

```text
| 65 | Mollendo | " | Luis Lopez de Romana | London E.C. 2. | 1 | Mining Engineer | 25 | ... | Peru | Peru | ... | " |
```

Interpretation kept separate: row 55 may be a Pulgar-Arriagada medical identity candidate, row 56 may be a travel-party or family clue, and row 65 may be family-relevant only by later evidence. None of those interpretations is proved by this converted page alone.

## Hypothesis 1: This Draft Is A Conversion QA Blocker, Not A Genealogical Conflict

Hypothesis: The staged conflict should remain a source-image-missing QA blocker attached to the Highland Loch passenger-list claims.

Evidence:

- The staged conflict draft states no direct genealogical conflict is identified within the converted chunk.
- The source packet gives `conversion_confidence: medium from converted text; source image unavailable locally for required reread`.
- The research-task note directs the next step to locate or restore the original PNG and reread rows 55, 56, and 65.
- Current workspace check confirms the stated source path is still absent.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.10 | The conflict draft is about source availability, not a resolved identity. |
| conflict_severity | 0.72 | Promotion before image reread could spread incorrect row facts or column alignments. |
| evidence_quality | 0.58 | Local derivative evidence is consistent, but the controlling image is absent. |
| conversion_confidence | 0.48 | Medium converted-text confidence reduced by missing reread. |
| claim_probability | 0.86 | Very likely that the current issue is a QA blocker rather than a source conflict. |
| relevance | 1.00 | Directly answers the assigned staged draft. |
| canonical_readiness | 0.02 | Do not promote while the source-image blocker remains. |

## Hypothesis 2: Row 55 Is A Held 1928 Identity Candidate For `Dario Pulgar A.`

Hypothesis: Row 55 should be preserved as a staged identity candidate for `Dario Pulgar A.` only.

Evidence:

- The source packet and chunk both transcribe row 55 as `Dario Pulgar A.`, age 39, occupation `Medical Surgeon`.
- The staged identity candidate records possible identity `Dario Pulgar Arriagada`, but its own uncertainty says the `A.` is not spelled out.
- The existing identity analysis for this same row ranks the held 1928 passenger candidate as the strongest limited conclusion.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.70 | Multiple local derivatives agree on the literal candidate name, but no image reread is available. |
| conflict_severity | 0.34 | Low if held separately; higher if merged by surname and initial. |
| evidence_quality | 0.62 | Direct converted table evidence, not yet image-verified. |
| conversion_confidence | 0.50 | Matches staged medium confidence and missing-source concern. |
| claim_probability | 0.74 | Probable row reading, not promotion-ready. |
| relevance | 0.96 | Direct Pulgar identity candidate in the conflict draft. |
| canonical_readiness | 0.10 | Hold for conversion QA and proof review. |

## Hypothesis 3: Same Person As Adult 1953 `Dario Pulgar`

Hypothesis: The 1928 `Dario Pulgar A.`, age 39 and medical surgeon, may be the same person as the 1953 adult `PULGAR Dario`, age 64 and occupation/calling `Medical`.

Evidence:

- Existing staged analysis of the 1953 Andes passenger list records an adult `PULGAR Dario`, age 64, `Medical`, Chile/Chile.
- The age chronology is compatible: 39 in July 1928 and 64 in August 1953.
- Both records use a medical occupation, but the 1953 row does not include `A.`, `Arriagada`, `Jose`, parentage, or a direct bridge.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.58 | Age and occupation align, but full identity is absent. |
| conflict_severity | 0.56 | Premature merge could collapse separate adult Pulgar clusters. |
| evidence_quality | 0.58 | Relevant local staged evidence, with QA limits. |
| conversion_confidence | 0.56 | 1953 structure is stronger; 1928 image remains missing. |
| claim_probability | 0.54 | Plausible, not proved. |
| relevance | 0.90 | Important duplicate-person comparison. |
| canonical_readiness | 0.14 | Hold for targeted bridge proof review. |

## Hypothesis 4: Same Person As `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada`

Hypothesis: `Dario Pulgar A.` belongs to the same older medical Pulgar-Arriagada cluster as staged `Dario Jose Pulgar-Arriagada` or `Dario J. Pulgar Arriagada`.

Evidence:

- Row 55 gives `Dario Pulgar A.` and `Medical Surgeon`.
- Local staged packets include title or file-context evidence for `Dario Jose Pulgar-Arriagada` in a Geneva photograph cluster.
- Local staged material also includes a `Dario J. Pulgar Arriagada` medical-title context.
- Those compared clusters remain partly metadata-dependent or conversion-sensitive, and this row does not expand `A.` to `Arriagada` or `J.` to `Jose`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.36 | Suggestive name-shape and professional overlap, no explicit bridge. |
| conflict_severity | 0.64 | Metadata or initial expansion could create a false merge. |
| evidence_quality | 0.42 | Compared evidence is local but still staged and held. |
| conversion_confidence | 0.48 | 1928 image is missing and comparison clusters are not fully settled. |
| claim_probability | 0.32 | Possible older Pulgar-Arriagada cluster, unresolved. |
| relevance | 0.88 | Required Pulgar-line name-variant comparison. |
| canonical_readiness | 0.06 | Not ready to merge or promote. |

## Hypothesis 5: Same Person As Canonical `Darío Pulgar Arriagada`

Hypothesis: `Dario Pulgar A.` is the same person as canonical `wiki/people/dar-o-pulgar-arriagada.md`.

Evidence:

- The 1928 row gives `Dario Pulgar A.`, age 39.
- The canonical `Darío Pulgar Arriagada` page currently carries a reviewed life fact from a 5 December 2000 Serviu Región del Bío Bío expropriation resolution.
- If the 1928 passenger and 2000 legal-notice person were the same person, the 1928 age would imply about 111 years old in 2000.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.16 | Initial/surname possibility is outweighed by missing bridge and chronology concern. |
| conflict_severity | 0.84 | A merge would create a serious chronology problem. |
| evidence_quality | 0.46 | The canonical fact supports its own person, not the 1928 bridge. |
| conversion_confidence | 0.56 | Both clusters must keep their separate QA limits. |
| claim_probability | 0.12 | Low without vital-date or property-continuity proof. |
| relevance | 0.82 | Required due to possible `A.`/Arriagada expansion. |
| canonical_readiness | 0.03 | Do not attach to the canonical Arriagada stub. |

## Hypothesis 6: Same Person As `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith`

Hypothesis: `Dario Pulgar A.` is the same person as staged CV subject `Dario Arturo Pulgar` or canonical `Dario Arturo Pulgar-Smith`.

Evidence:

- The canonical page identifies `Dario Arturo Pulgar-Smith` from family-supplied knowledge as Alexander John Heinz's maternal grandfather and warns not to merge similar Pulgar records without identity review.
- Existing CV analyses treat `Dario Arturo Pulgar` as a document-level CV subject, with the bridge to `Dario Arturo Pulgar-Smith` still on hold.
- The 1928 row names `Dario Pulgar A.`, not `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith`.
- Existing local analysis treats the 1928 age-39 medical passenger as more consistent with an older professional-generation cluster than with the later CV/Habitat Dario cluster.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.10 | Broad name overlap only; surname form and chronology do not bridge. |
| conflict_severity | 0.78 | Wrong attachment would contaminate the family-supplied Dario anchor. |
| evidence_quality | 0.40 | Family context is real but not identity-bridging for this row. |
| conversion_confidence | 0.48 | This row and the CV bridge are both held for separate reasons. |
| claim_probability | 0.08 | Low on current local evidence. |
| relevance | 0.90 | Required Pulgar-Smith comparison. |
| canonical_readiness | 0.01 | No canonical attachment supported. |

## Hypothesis 7: Dorothy Pulgar Is Spouse Or Relative Of Dario Pulgar A.

Hypothesis: Row 56 `Dorothy Pulgar` is a spouse or relative of row 55 `Dario Pulgar A.`.

Evidence:

- Rows 55 and 56 are consecutive and share the Pulgar surname.
- Row 56 uses `do`/ditto marks for some fields.
- The staged relationship draft explicitly says no relationship column or kinship wording is present.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.52 | Association clue only, not an exact relationship. |
| conflict_severity | 0.46 | Unsupported spouse/family promotion would create a relationship conflict. |
| evidence_quality | 0.50 | Adjacency is direct; kinship is inferred. |
| conversion_confidence | 0.48 | Ditto marks and table alignment need image reread. |
| claim_probability | 0.60 | Probable travel-party association; exact kinship unproved. |
| relevance | 0.74 | Relevant relationship-conflict review. |
| canonical_readiness | 0.02 | No relationship promotion supported. |

## Hypothesis 8: Jose/Juana Parent Candidates Connect This Dario To A Lineage

Hypothesis: Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, Juana de Dios Amagada de Pulgar, or related Jose/Juana candidates connect this 1928 Dario to a proven lineage.

Evidence:

- Existing local context includes Jose/Juana parent candidates in separate birth-register clusters.
- Those clusters are themselves partly held for conversion/proof-review questions, including father suffix, child name, and maternal surname readings.
- The 1928 passenger row does not name Jose, Juana, parents, birthplace, or any relationship.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct relationship or identity evidence appears in this draft. |
| conflict_severity | 0.62 | Unsupported lineage attachment would create serious relationship conflicts. |
| evidence_quality | 0.34 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.38 | Both the 1928 row and Jose/Juana clusters carry QA limits. |
| claim_probability | 0.04 | No Jose/Juana connection is supported here. |
| relevance | 0.62 | Required Pulgar-line anti-conflation context. |
| canonical_readiness | 0.01 | No lineage action supported. |

## Conflicts

- Source-availability conflict: high. The original Highland Loch PNG is absent, blocking the requested reread.
- Conversion-confidence conflict: medium-high. Local derivatives agree on the rows, but row facts remain dependent on unverified conversion of a dense table.
- Name-variant conflict: moderate-high. `Dario Pulgar A.` does not prove `Arriagada`, `Jose`, `Arturo`, or `Pulgar-Smith`.
- Duplicate-person risk: high if this row is merged into `Dario Arturo Pulgar-Smith`, staged CV `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or canonical `Darío Pulgar Arriagada` by name alone.
- Relationship-conflict evidence: none stated. Dorothy Pulgar is adjacent but not explicitly identified as spouse or kin.
- Chronology-conflict evidence: 1928 age 39 aligns with a possible 1953 adult age 64 medical passenger, but conflicts with a direct unsupported merge to later CV/Habitat Dario context and creates an age-about-111 caution for the 2000 `Darío Pulgar Arriagada` legal-notice cluster.
- Luis relevance conflict: low-to-medium. `Luis Lopez de Romana` is present in row 65, but no Pulgar relationship or family relevance is stated on this page.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | The assigned draft is a conversion QA blocker, not a promotable genealogical conflict | 0.86 | Keep as source-image-missing QA hold. |
| 2 | Row 55 is a held 1928 passenger identity candidate for `Dario Pulgar A.` | 0.74 | Preserve staged; do not expand the name. |
| 3 | Same person as 1953 adult `Dario Pulgar`, age 64, medical | 0.54 | Hold for targeted bridge proof review after image reread. |
| 4 | Dorothy Pulgar is a travel-party associate of Dario Pulgar A. | 0.60 for association; lower for exact kinship | Do not promote spouse or family relationship. |
| 5 | Same older cluster as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` | 0.32 | Preserve as unresolved; require explicit full-name or metadata bridge. |
| 6 | Same person as canonical `Darío Pulgar Arriagada` | 0.12 | Treat as anti-conflation until chronology is bridged. |
| 7 | Same person as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.08 | Do not attach to CV or Pulgar-Smith canonical cluster. |
| 8 | Connected to Jose/Juana parent candidates | 0.04 | No lineage action from this draft. |
| 9 | `Luis Lopez de Romana` is family-relevant through this page | 0.10 | Hold as a broad name lead only unless independent relationship evidence appears. |

## Recommended Next Action

Keep `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-c136e7acf00f-P0001-01-source-image-missing-qa.md` on hold as a conversion QA blocker. Do not promote the conflict, do not promote row-derived facts, do not merge `Dario Pulgar A.` with any canonical person, do not expand `A.` to `Arriagada`, and do not infer a Dorothy relationship.

The exact next proof-review step is source-availability and page-image conversion QA for `CHUNK-c136e7acf00f-P0001-01`: restore or locate the original Highland Loch PNG and reread rows 55, 56, and 65 against the image. Verify the row 55 name, age, medical occupation, citizenship/residence/destination columns, row 56 ditto marks, and row 65 identity/relevance. Only after that should a targeted identity-bridge proof review compare the confirmed 1928 row first to the 1953 adult medical `Dario Pulgar`, then separately to `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Arturo Pulgar`, and `Dario Arturo Pulgar-Smith`. Jose/Juana parent candidates require separate parent-identity proof review before they can bridge any Dario identity.
