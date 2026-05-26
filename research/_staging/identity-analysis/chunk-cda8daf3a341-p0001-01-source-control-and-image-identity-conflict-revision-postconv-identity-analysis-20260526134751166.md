---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526134751166
task_id: identity-analysis:research/_staging/conflicts/chunk-cda8daf3a341-p0001-01-source-control-and-image-identity-conflict-revision-postconv-evidence-extraction-20260526100318514.md
staged_draft: research/_staging/conflicts/chunk-cda8daf3a341-p0001-01-source-control-and-image-identity-conflict-revision-postconv-evidence-extraction-20260526100318514.md
subject: Dario Jose Pulgar-Arriagada
source_packet: research/_staging/source-packets/chunk-cda8daf3a341-p0001-01-icrc-group-photo-dario-jose-pulgar-arriagada-revision-postconv-evidence-extraction-20260526100318514.md
source: raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG
converted_file: raw/converted/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a.codex.md
chunk: raw/chunks/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a-codex/page-0001-chunk-01.md
chunk_id: CHUNK-cda8daf3a341-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Source Control And Image Identity

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-cda8daf3a341-p0001-01-source-control-and-image-identity-conflict-revision-postconv-evidence-extraction-20260526100318514.md`.
- The assigned source file `raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG` is absent in the current workspace.
- The assigned source SHA-256 is `327c170fda815e9226dbef176e889611718d4ba89c088377a4092588778a6b9a`. The only same-folder JPG found is `Photograph of the Geneva Convention assembly (Dario Jose Pulgar-Arriagada at Table 9 Seat 2).jpg`, with SHA-256 `99541c195e4ec48320e5cafecc00e816585a4333aa495339cc5a5ad89197a8f5`.
- The converted file points to an extracted outdoor-group image path, but that extracted image is also absent locally. The available same-folder JPG must not be substituted because it is a different hash and a different Table 9/indoor-assembly source context.
- The converted page and chunk state that the page has no text. The visual-region manifest records `identity_basis: none`.
- `Dario Jose Pulgar-Arriagada` is named only in source document title/file identity for this packet, not by a visible caption, roster, handwriting, page text, or image-region label.
- Existing local context contains multiple Pulgar-line candidates: `Dario Arturo Pulgar-Smith`, staged/CV `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, adult and child `Dario Pulgar` passenger stubs, and Jose/Juana parent candidates. This draft does not bridge them.
- No external research was performed. No raw sources, converted Markdown, chunks, reviewed notes, source packets, or canonical wiki pages were edited.

## Literal Source Reading

Literal support from the staged draft, source packet, converted file, and chunk:

```text
Source document title: Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives
```

```text
The page consists of a single black and white photograph, occupying the entire page. There is no text or other content on the page.
```

```text
No text is present on this page.
```

```text
identity_basis: none
```

Literal reading: the evidence package describes a no-text photograph whose source title names `Dario Jose Pulgar-Arriagada`.

Interpretation kept separate: the title may indicate an intended association with Dario Jose Pulgar-Arriagada, but the current evidence does not certify the controlling image, identify a face, or support a canonical attachment.

## Hypothesis 1: Metadata/Title Intends Dario Jose Pulgar-Arriagada

Hypothesis: the missing assigned source image was intended by local source title/file identity to be associated with `Dario Jose Pulgar-Arriagada`.

Evidence supporting:

- The staged draft subject is `Dario Jose Pulgar-Arriagada`.
- The source packet and converted page repeat the source title naming `Dario Jose Pulgar-Arriagada`.
- The source packet states `source_identity: Dario Jose Pulgar-Arriagada, named in source document title/file identity only`.

Conflicts and limits:

- The assigned source file is absent and cannot be reread.
- The page has no visible text and no image-region identity basis.
- The strongest current support is metadata/title evidence, not direct page text or face identification.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.44 | Title metadata consistently names Dario Jose Pulgar-Arriagada, but no visible-page evidence identifies him. |
| conflict_severity | 0.72 | Wrong source substitution or face attachment would misidentify a photograph and person. |
| evidence_quality | 0.38 | Source-title evidence only; controlling image is missing. |
| conversion_confidence | 0.74 | High for no-text/outdoor-photo conversion statement, low for person identity. |
| claim_probability | 0.52 | Moderate that metadata intends association; low that this package proves depiction. |
| relevance | 0.96 | Directly relevant to the staged source-control conflict. |
| canonical_readiness | 0.05 | Hold for source-control and metadata QA. |

## Hypothesis 2: Same As Separate Table 9 Dario Jose Pulgar-Arriagada Photo Cluster

Hypothesis: the missing outdoor `V-P-HIST-03583-07A.JPG` source and the present same-folder `Table 9 Seat 2` JPG are separate photographs connected to the same Dario Jose Pulgar-Arriagada Geneva Convention source cluster.

Evidence supporting:

- Both local source contexts name `Dario Jose Pulgar-Arriagada`.
- Both refer broadly to the 1929 Geneva Convention/ICRC photograph context.
- The present same-folder JPG title contains a more specific Table 9/Seat 2 assertion.

Conflicts and limits:

- The two files have different hashes.
- The assigned converted chunk describes an outdoor group near an ivy-covered building and table with drinks; the same-folder JPG is a different indoor/table context.
- This assigned draft cannot import the Table 9 source as controlling evidence for `V-P-HIST-03583-07A.JPG`.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Shared source naming and event context are meaningful, but the images are different assets and both depend on metadata for identity. |
| conflict_severity | 0.76 | Treating the Table 9 JPG as the assigned source would erase the source-control conflict. |
| evidence_quality | 0.42 | Useful local comparison, but not a controlling source match. |
| conversion_confidence | 0.50 | The assigned conversion and Table 9 file context describe different images. |
| claim_probability | 0.44 | Plausible same archive/person cluster, unproved same image or same person depiction. |
| relevance | 0.90 | Directly explains the same-folder mismatch. |
| canonical_readiness | 0.04 | Not ready for promotion or substitution. |

## Hypothesis 3: Same As 1929 Dario Pulgar-Arriagada Medical/Geneva Cluster

Hypothesis: `Dario Jose Pulgar-Arriagada` in the photograph title is the same person as staged 1929 Geneva/medical-service references to `Dario Pulgar-Arriagada`.

Evidence supporting:

- Existing staged notes and source-packet context contain older medical/Geneva Pulgar-Arriagada candidates, including `Dario Pulgar-Arriagada`.
- The 1929 Geneva context is broadly compatible with the photograph source title.
- This is the strongest same-person hypothesis beyond the assigned title itself because it shares event period, surname compound, and Dario/Pulgar name elements.

Conflicts and limits:

- This assigned draft uses `Dario Jose Pulgar-Arriagada`; the separate Geneva/medical contexts do not, in this package, provide a direct full-name bridge.
- The assigned photo evidence gives no role, nationality, age, residence, table/seat marker, or caption.
- Event-context similarity is not enough to merge persons or promote a depiction claim.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.62 | Strong name/event-context overlap, but no explicit bridge in the assigned draft. |
| conflict_severity | 0.54 | Moderate risk if promoted as same person without bridge evidence. |
| evidence_quality | 0.60 | Separate listing/name evidence is stronger than this photo metadata, but it is not controlling here. |
| conversion_confidence | 0.66 | High for separate text listings where reviewed; low for this photo identity. |
| claim_probability | 0.58 | Plausible same 1929 Geneva/Pulgar-Arriagada cluster, not proved by this draft. |
| relevance | 0.88 | Required Pulgar-Arriagada comparison and likely next-review target. |
| canonical_readiness | 0.18 | Hold for explicit bridge review. |

## Hypothesis 4: Same As Dario Arturo Pulgar Or Dario Arturo Pulgar-Smith

Hypothesis: `Dario Jose Pulgar-Arriagada` in this source-title cluster is the same person as staged/CV `Dario Arturo Pulgar` or canonical family-supplied `Dario Arturo Pulgar-Smith`.

Evidence supporting:

- The candidates share broad `Dario` and `Pulgar` name elements.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` represents Dario Arturo Pulgar-Smith as Alexander John Heinz's maternal grandfather from family-supplied knowledge.
- That canonical page explicitly warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review.

Conflicts and limits:

- This assigned draft says `Dario Jose Pulgar-Arriagada`, not `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or `Pulgar-Smith`.
- It gives no birth date, age, spouse, child, grandchild, residence, CV context, education, or family relationship.
- Existing CV/Pulgar-Smith staging keeps the bridge from `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith` on proof-review hold, and does not support a merge with Pulgar-Arriagada by name alone.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Shared Dario/Pulgar elements only; middle name and surname form are unbridged. |
| conflict_severity | 0.82 | High risk of collapsing distinct Pulgar-line identities and misattributing a photo. |
| evidence_quality | 0.28 | No direct evidence in this draft supports Arturo or Smith identity. |
| conversion_confidence | 0.74 | Conversion supports that the page has no text; it does not support this bridge. |
| claim_probability | 0.08 | Very low from this staged evidence. |
| relevance | 0.86 | Required because Pulgar-Smith is the canonical family anchor. |
| canonical_readiness | 0.01 | No canonical attachment or merge supported. |

## Hypothesis 5: Same As Dario/Dario Pulgar Arriagada Canonical Stub

Hypothesis: `Dario Jose Pulgar-Arriagada` in this photo metadata is the same person as canonical `wiki/people/dar-o-pulgar-arriagada.md`, currently represented by a 2000 Chiguayante expropriation event.

Evidence supporting:

- The name forms share `Dario Pulgar Arriagada` / `Pulgar-Arriagada` elements.
- Existing local identity-analysis context preserves this as a possible name-variant comparison.

Conflicts and limits:

- This assigned draft provides no age, vital date, property, residence, family member, or chronology bridge.
- A 1929 Geneva photograph/title context and a 2000 expropriation/property context could represent different generations or same-name persons.
- The canonical stub's current evidence does not add independent support for the missing assigned image.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Surname-form overlap is real, but no chronology or biographical bridge appears. |
| conflict_severity | 0.64 | Wrong merge would connect a 1929 photo-metadata cluster to a 2000 property event without proof. |
| evidence_quality | 0.36 | Compared evidence is sparse and source-specific. |
| conversion_confidence | 0.62 | This image identity is weak; the legal-notice cluster is separate. |
| claim_probability | 0.20 | Possible name-variant question only. |
| relevance | 0.78 | Required Pulgar-line comparison. |
| canonical_readiness | 0.03 | Hold; no merge or name normalization. |

## Hypothesis 6: Connected To Jose/Juana Parent Candidates

Hypothesis: Jose/Juana parent candidates in local Pulgar-line context explain or connect `Dario Jose Pulgar-Arriagada`.

Evidence supporting:

- Existing wiki/staged context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Some local Pulgar-Arriagada register clusters preserve Jose/Juana relationship candidates, with conversion-review cautions.

Conflicts and limits:

- This assigned staged draft names no parent, spouse, child, household member, informant, witness, or relative.
- The middle name `Jose` cannot be treated as evidence of a Jose parent.
- The Jose/Juana materials are separate, partly held or low-confidence, and do not identify the assigned photo subject.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No direct relationship or identity bridge appears in this staged draft. |
| conflict_severity | 0.58 | Unsupported lineage attachment would create false parent/child or ancestor links. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.48 | Mixed across the separate Jose/Juana materials; this photo gives no lineage text. |
| claim_probability | 0.04 | No supported Jose/Juana connection from this draft. |
| relevance | 0.60 | Relevant only as required Pulgar-line anti-conflation context. |
| canonical_readiness | 0.01 | No relationship promotion supported. |

## Conflict Summary

- Source-control conflict: high. The assigned `V-P-HIST-03583-07A.JPG` is missing, and the present same-folder JPG has a different SHA-256 and different visual/source context.
- Conversion-vs-identity conflict: high. The converted page can support a no-text photograph description, but it cannot identify Dario Jose Pulgar-Arriagada in the image.
- Duplicate-person risk: high if `Dario Jose Pulgar-Arriagada` is merged with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario/Dario Pulgar Arriagada`, adult/child passenger Dario entries, or Jose/Juana clusters by name alone.
- Name-variant conflict: unresolved. `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Dario Arturo Pulgar`, and `Dario Arturo Pulgar-Smith` remain separate hypotheses pending bridge evidence.
- Relationship-conflict evidence: none. This staged draft states no parent, spouse, child, sibling, or grandchild relationship.
- Chronology-conflict evidence: unresolved. A 1929 Geneva context may fit an older medical/Geneva Pulgar-Arriagada cluster, but this draft supplies no age or lifespan data and cannot be reconciled to the 1953 child/adult passenger stubs.

## Ranked Hypotheses

| rank | hypothesis | probability | next action |
| ---: | --- | ---: | --- |
| 1 | Metadata/title intends association with `Dario Jose Pulgar-Arriagada` | 0.52 | Hold for source-control and ICRC/archive metadata reread. |
| 2 | Same as 1929 `Dario Pulgar-Arriagada` medical/Geneva cluster | 0.58 | Plausible but not proved here; require a bridge review before merge or depiction claim. |
| 3 | Same archive/person cluster as the separate Table 9 photo packet | 0.44 | Do not substitute image files; compare only after conversion QA confirms each source. |
| 4 | Same as `Dario/Dario Pulgar Arriagada` canonical/expropriation stub | 0.20 | Preserve as unresolved name-variant question. |
| 5 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.08 | Do not attach; require explicit Arturo/Smith to Pulgar-Arriagada bridge. |
| 6 | Connected to Jose/Juana parent candidates | 0.04 | No relationship action; revisit only with direct relationship evidence. |

## Recommended Next Action

Keep the staged conflict draft on `hold_for_conversion_qa`. Do not promote a depiction claim, do not attach the photograph to a canonical gallery/person page, do not replace the missing assigned image with the available Table 9 JPG, and do not merge `Dario Jose Pulgar-Arriagada` with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario/Dario Pulgar Arriagada`, passenger-list Dario candidates, or Jose/Juana parent candidates.

Exact next proof-review step: perform source-control and conversion QA for `V-P-HIST-03583-07A.JPG` by restoring or locating the original image with SHA-256 `327c170fda815e9226dbef176e889611718d4ba89c088377a4092588778a6b9a`, its extracted page image, and any local ICRC/archive metadata. Then reread the image/metadata to determine whether `Dario Jose Pulgar-Arriagada` is identified, whether any caption/roster/table/seat marker exists, and whether the image is distinct from the Table 9 source. Any later Pulgar-line merge requires a separate identity-bridge proof review naming the exact bridge between Jose/Pulgar-Arriagada, Arturo/Pulgar-Smith, Dario/Dario Pulgar Arriagada, and any Jose/Juana relationship candidates.
