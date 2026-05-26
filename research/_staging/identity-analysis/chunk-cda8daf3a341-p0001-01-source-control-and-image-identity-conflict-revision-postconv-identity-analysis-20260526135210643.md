---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526135210643
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
- The assigned source image `V-P-HIST-03583-07A.JPG` is absent from the workspace and cannot be reread.
- The assigned source SHA-256 is `327c170fda815e9226dbef176e889611718d4ba89c088377a4092588778a6b9a`; the only same-folder JPG reported in the staged packet has SHA-256 `99541c195e4ec48320e5cafecc00e816585a4333aa495339cc5a5ad89197a8f5` and is not the controlling source.
- The converted file describes an outdoor group photograph near an ivy-covered building and a table with drinks, while the related same-folder JPG is described as an indoor assembly/Table 9 image. The latter must not be substituted for this draft.
- The converted page and chunk state that no text is present. The visual-region manifest records `identity_basis: none`.
- `Dario Jose Pulgar-Arriagada` is supported here only by source title/file identity, not by visible caption text, handwriting, roster, seat marker, or image-region labeling.
- Existing Pulgar-line context includes `Dario Arturo Pulgar-Smith`, staged CV `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, adult and child `Dario Pulgar` passenger stubs, and Jose/Juana parent candidates. This draft does not bridge those clusters.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, or canonical wiki pages were edited.

## Literal Source Reading

Literal readings from the staged draft, source packet, converted file, and chunk:

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

Interpretation kept separate: the title likely signals an intended association with `Dario Jose Pulgar-Arriagada`, but the current evidence package does not certify the controlling image, identify a person in the photograph, or support canonical attachment.

## Hypothesis 1: Metadata/Title Association With Dario Jose Pulgar-Arriagada

Evidence supporting:

- The staged draft subject is `Dario Jose Pulgar-Arriagada`.
- The source packet records `source_identity: Dario Jose Pulgar-Arriagada, named in source document title/file identity only`.
- The converted page metadata repeats the source document title and document ID `V-P-HIST-03583-07A`.

Conflicts and limits:

- The assigned source file is missing.
- The page has no visible text and no image-region identity basis.
- The evidence supports only a held metadata association, not a proved depiction or face identification.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.44 | Consistent title metadata, but no visible-page identity evidence. |
| conflict_severity | 0.72 | Wrong image substitution or face attachment would misidentify a person. |
| evidence_quality | 0.38 | Title/file metadata only; controlling image unavailable. |
| conversion_confidence | 0.74 | Strong for no-text/outdoor-photo description; weak for identity. |
| claim_probability | 0.60 | Moderate-high that metadata intends association; low that depiction is proved. |
| relevance | 0.96 | Directly controls this staged conflict. |
| canonical_readiness | 0.05 | Hold for source-control QA. |

## Hypothesis 2: Same As 1929 Dario Pulgar-Arriagada Medical/Geneva Cluster

Evidence supporting:

- Other staged source packets name `Dario Pulgar-Arriagada` in 1929 Geneva/Chile convention contexts, including medical-service or delegate-list language.
- The event context is broadly compatible with a 1929 Geneva photograph title.
- This is the strongest comparison candidate beyond the assigned title because it shares the Dario/Pulgar-Arriagada name structure and Geneva context.

Conflicts and limits:

- This draft uses `Dario Jose Pulgar-Arriagada`; the nearby listing packets reviewed in local context generally use `Dario Pulgar-Arriagada` without `Jose`.
- This draft gives no role, nationality, age, residence, caption, table/seat marker, or roster bridge.
- Event-context overlap is not a same-person proof.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.56 | Strong context/name overlap, but no explicit bridge in this draft. |
| conflict_severity | 0.54 | Moderate risk if merged or promoted before bridge review. |
| evidence_quality | 0.58 | Separate listing evidence is stronger than this photo metadata, but not controlling here. |
| conversion_confidence | 0.66 | Separate text listings may be readable; this photo identity remains weak. |
| claim_probability | 0.56 | Plausible same 1929 Pulgar-Arriagada cluster, unproved. |
| relevance | 0.88 | Required Pulgar-Arriagada comparison and likely next proof-review target. |
| canonical_readiness | 0.18 | Hold for explicit bridge review. |

## Hypothesis 3: Same Archive/Person Cluster As Separate Table 9 Photo

Evidence supporting:

- Both local source contexts name `Dario Jose Pulgar-Arriagada`.
- Both refer to 1929 Geneva Convention/ICRC photograph material.
- The same-folder JPG title includes a more specific `Table 9 Seat 2` assertion.

Conflicts and limits:

- The images have different hashes.
- The visible scene descriptions conflict: outdoor group photograph for this conversion versus indoor assembly/Table 9 for the related JPG.
- The Table 9 image cannot be imported as the controlling source for this assigned draft.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Shared metadata is meaningful, but asset control differs. |
| conflict_severity | 0.76 | Substitution would mask the source-control failure. |
| evidence_quality | 0.42 | Useful comparison only, not controlling evidence. |
| conversion_confidence | 0.50 | Different image descriptions prevent simple reconciliation. |
| claim_probability | 0.44 | Plausible same archive/person cluster, not same source proof. |
| relevance | 0.90 | Directly explains the local mismatch. |
| canonical_readiness | 0.04 | Not ready for promotion or substitution. |

## Hypothesis 4: Same As Dario/Dario Pulgar Arriagada Canonical Stub

Evidence supporting:

- The name forms share `Dario Pulgar Arriagada` / `Pulgar-Arriagada` elements.
- Canonical context includes `wiki/people/dar-o-pulgar-arriagada.md`, with a 2000 Chiguayante expropriation event for `Dario/Darío Pulgar Arriagada`.

Conflicts and limits:

- This draft provides no age, vital date, property, residence, family member, or chronology bridge.
- A 1929 Geneva photograph metadata context and a 2000 expropriation/property context may represent different people or generations.
- The canonical stub does not identify the missing assigned photograph.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Surname-form overlap only; no biographical bridge. |
| conflict_severity | 0.64 | Wrong merge would connect unrelated event contexts. |
| evidence_quality | 0.36 | Compared evidence is sparse and source-specific. |
| conversion_confidence | 0.62 | This image identity is weak; legal-notice evidence is separate. |
| claim_probability | 0.20 | Possible name-variant question only. |
| relevance | 0.78 | Required Pulgar-line comparison. |
| canonical_readiness | 0.03 | Hold; no merge or name normalization. |

## Hypothesis 5: Same As Dario Arturo Pulgar Or Dario Arturo Pulgar-Smith

Evidence supporting:

- The candidates share broad `Dario` and `Pulgar` elements.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` identifies `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather from family-supplied knowledge.
- Existing CV staging uses document-level `Dario Arturo Pulgar` and keeps the bridge to `Dario Arturo Pulgar-Smith` on hold.

Conflicts and limits:

- This draft names `Dario Jose Pulgar-Arriagada`, not `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or `Pulgar-Smith`.
- It gives no birth date, age, spouse, child, grandchild, residence, CV context, education, or relationship bridge.
- Name overlap alone is insufficient and would create a high duplicate-person risk.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Shared Dario/Pulgar elements only. |
| conflict_severity | 0.82 | High risk of collapsing distinct Pulgar-line identities. |
| evidence_quality | 0.28 | No direct evidence supports Arturo or Smith identity. |
| conversion_confidence | 0.74 | Conversion supports no text, not this bridge. |
| claim_probability | 0.08 | Very low from this staged evidence. |
| relevance | 0.86 | Required because Pulgar-Smith is the canonical family anchor. |
| canonical_readiness | 0.01 | No canonical attachment or merge supported. |

## Hypothesis 6: Connected To Jose/Juana Parent Candidates

Evidence supporting:

- Existing wiki/staged context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Some Pulgar-Arriagada register clusters preserve Jose/Juana relationship candidates, with conversion-review cautions.

Conflicts and limits:

- This staged draft names no parent, spouse, child, household member, informant, witness, or relative.
- The middle name `Jose` cannot be treated as evidence of a Jose parent.
- The Jose/Juana materials are separate and conversion-sensitive; they do not identify the assigned photo subject.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | No direct relationship or identity bridge appears here. |
| conflict_severity | 0.58 | Unsupported lineage attachment would create false relationships. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and partly held. |
| conversion_confidence | 0.48 | Mixed across separate Jose/Juana materials; this photo gives no lineage text. |
| claim_probability | 0.04 | No supported Jose/Juana connection from this draft. |
| relevance | 0.60 | Required anti-conflation context only. |
| canonical_readiness | 0.01 | No relationship promotion supported. |

## Conflict Summary

- Source-control conflict: high. The assigned source image is missing, and the available same-folder JPG is a different hash and different visual/source context.
- Conversion-vs-identity conflict: high. The conversion supports a no-text photograph description, but not identification of Dario Jose Pulgar-Arriagada in the image.
- Name-variant conflict: unresolved. `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Dario Arturo Pulgar`, and `Dario Arturo Pulgar-Smith` remain separate hypotheses pending bridge evidence.
- Duplicate-person risk: high if merged with Pulgar-Smith, CV Pulgar, Pulgar-Arriagada, passenger Dario, or Jose/Juana clusters by name alone.
- Relationship-conflict evidence: none in this draft.
- Chronology-conflict evidence: unresolved. A 1929 Geneva context may fit older Pulgar-Arriagada convention listings, but the draft gives no age or lifespan data and cannot reconcile to later CV, passenger, or 2000 expropriation contexts.

## Ranked Hypotheses

| rank | hypothesis | probability | next action |
| ---: | --- | ---: | --- |
| 1 | Metadata/title intends association with `Dario Jose Pulgar-Arriagada` | 0.60 | Hold for source-control and archive metadata reread. |
| 2 | Same as 1929 `Dario Pulgar-Arriagada` medical/Geneva listing cluster | 0.56 | Plausible comparison; require explicit bridge proof review before merge or depiction claim. |
| 3 | Same archive/person cluster as separate Table 9 photo packet | 0.44 | Do not substitute image files; compare only after conversion QA confirms each source. |
| 4 | Same as `Dario/Dario Pulgar Arriagada` canonical/expropriation stub | 0.20 | Preserve as unresolved name-variant question. |
| 5 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.08 | Do not attach; require explicit Arturo/Smith to Pulgar-Arriagada bridge. |
| 6 | Connected to Jose/Juana parent candidates | 0.04 | No relationship action; revisit only with direct relationship evidence. |

## Recommended Next Action

Keep the staged conflict draft on `hold_for_conversion_qa`. Do not promote a depiction claim, attach the photograph to a canonical gallery/person page, replace the missing assigned image with the available Table 9 JPG, merge people, rename canonical pages, or use family context to correct the name silently.

Exact next proof-review step: source-control and conversion QA must restore or locate `V-P-HIST-03583-07A.JPG` with SHA-256 `327c170fda815e9226dbef176e889611718d4ba89c088377a4092588778a6b9a`, its extracted page image, and any local ICRC/archive metadata. The follow-up proof review should reread whether `Dario Jose Pulgar-Arriagada` is identified, whether any caption/roster/table/seat marker exists, and whether the image is distinct from the Table 9 source. Any later Pulgar-line merge requires a separate identity-bridge proof review explicitly comparing Jose/Pulgar-Arriagada, Arturo/Pulgar-Smith, Dario/Dario Pulgar Arriagada, and Jose/Juana parent candidates.
