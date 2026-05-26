---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260526135632869
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

# Identity/Conflict Analysis: ICRC Photograph Source Control

## Blockers First

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-cda8daf3a341-p0001-01-source-control-and-image-identity-conflict-revision-postconv-evidence-extraction-20260526100318514.md`.
- The assigned source image is absent in the current workspace: `raw/sources/Photographs of the 1929 Geneva Convention showing Dario Jose Pulgar-Arriagada ICRC Audiovisual archives_files/V-P-HIST-03583-07A.JPG`.
- The assigned source SHA-256 is `327c170fda815e9226dbef176e889611718d4ba89c088377a4092588778a6b9a`. The available same-folder JPG is `Photograph of the Geneva Convention assembly (Dario Jose Pulgar-Arriagada at Table 9 Seat 2).jpg`, SHA-256 `99541c195e4ec48320e5cafecc00e816585a4333aa495339cc5a5ad89197a8f5`, and is not the controlling source for this chunk.
- The converted file references extracted visual crops under `raw/codex-conversion-jobs/ca327c170f-v-p-hist-03583-07a-v-p-hist-03583-07a/extracted-images`, but that extracted-images directory is absent in the current workspace.
- The converted page and chunk say the page is a no-text photograph. The visual-region manifest records `identity_basis: none`.
- The source packet reports a visual/content mismatch: this conversion describes an outdoor group near an ivy-covered building and table with drinks, while the related same-folder JPG is described as an indoor assembly/Table 9 source.
- The name `Dario Jose Pulgar-Arriagada` is supported here only by source-title/file metadata, not by visible page text, caption, roster, face label, seat marker, or image-region identification.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, claims, or canonical wiki pages were edited.

## Literal Source Readings

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

Interpretation kept separate: the local title likely intends an association with `Dario Jose Pulgar-Arriagada`, but the current evidence package does not prove which source image controls, whether he is depicted, or which person in any image is him.

## Hypothesis 1: Metadata Association With Dario Jose Pulgar-Arriagada

Evidence supporting:

- The staged draft subject is `Dario Jose Pulgar-Arriagada`.
- The source packet states `source_identity: Dario Jose Pulgar-Arriagada, named in source document title/file identity only`.
- The converted file repeats the source document title and document ID `V-P-HIST-03583-07A`.

Conflicts and limits:

- The assigned source file and extracted image are missing.
- The page itself has no visible text, and the visual-region manifest says `identity_basis: none`.
- This supports only a held metadata/title association, not a promoted depiction or face identification.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.44 | Title metadata is consistent, but no visible identity evidence exists. |
| conflict_severity | 0.74 | Promoting the image could misidentify a person or substitute a noncontrolling source. |
| evidence_quality | 0.38 | Source-title metadata only; controlling image unavailable. |
| conversion_confidence | 0.74 | High for the no-text/outdoor-photo description; low for person identity. |
| claim_probability | 0.58 | Moderate that the metadata intends this association; low that depiction is proved. |
| relevance | 0.97 | Directly controls this staged conflict. |
| canonical_readiness | 0.05 | Hold for source-control QA. |

## Hypothesis 2: Same As 1918/1929 Pulgar-Arriagada Medical Or Geneva Cluster

Evidence supporting:

- Local reviewed/staged context includes `Darío J. Pulgar Arriagada` in a 1918 medical-surgeon title-conferral source and other Pulgar-Arriagada/Geneva comparison notes.
- The 1929 Geneva photograph-title context is broadly compatible with a professional or delegate identity, if later bridged.
- The name structure overlaps with `Dario Jose Pulgar-Arriagada` if a future source proves `J.` expands to `Jose`.

Conflicts and limits:

- This draft does not contain `Darío J. Pulgar Arriagada`, medical title language, age, nationality, role, table/seat identification, or a roster.
- No source read for this task expands `J.` to `Jose`.
- Event-context and name-shape overlap are not same-person proof.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.52 | Plausible name/context overlap, but no explicit bridge in this draft. |
| conflict_severity | 0.55 | Moderate risk if clusters are merged before proof review. |
| evidence_quality | 0.56 | Separate text evidence is stronger than this image metadata but is not controlling here. |
| conversion_confidence | 0.64 | Separate listings may be readable; this photo identity remains weak. |
| claim_probability | 0.52 | Plausible same cluster, unproved. |
| relevance | 0.88 | Required Pulgar-Arriagada comparison. |
| canonical_readiness | 0.18 | Hold for identity-bridge proof review. |

## Hypothesis 3: Same Archive Cluster As Separate Table 9 JPG

Evidence supporting:

- The available same-folder JPG title names `Dario Jose Pulgar-Arriagada at Table 9 Seat 2`.
- Both the assigned source and the available same-folder JPG appear to belong to local 1929 Geneva Convention/ICRC photograph material.

Conflicts and limits:

- The hashes differ: assigned source `327c170f...`; available JPG `99541c...`.
- The source packet reports conflicting visual contexts: outdoor group photograph for this chunk versus indoor assembly/Table 9 for the available JPG.
- The Table 9 file cannot be substituted as the source for this staged draft without conversion QA.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Shared local metadata is meaningful, but source control differs. |
| conflict_severity | 0.78 | Substitution would hide the source-control failure. |
| evidence_quality | 0.42 | Useful comparison source only, not controlling evidence. |
| conversion_confidence | 0.50 | Different image descriptions block simple reconciliation. |
| claim_probability | 0.44 | Plausible same archive/person cluster, not same-source proof. |
| relevance | 0.92 | Directly explains the local mismatch. |
| canonical_readiness | 0.04 | Not ready for promotion or substitution. |

## Hypothesis 4: Same As Dario/Darío Pulgar Arriagada Canonical Stub

Evidence supporting:

- The names share the `Dario/Darío Pulgar Arriagada` structure.
- Existing canonical context includes `wiki/people/dar-o-pulgar-arriagada.md`, whose evidence snapshot records a 2000 Chiguayante expropriation event for `Darío Pulgar Arriagada`.

Conflicts and limits:

- This draft provides no birth date, age, death date, occupation, residence, property, or relationship bridge.
- A 1929 Geneva photo-title context and a 2000 expropriation context may represent different people or generations.
- The canonical stub does not identify the missing assigned photograph.

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Surname-form overlap only; no biographical bridge. |
| conflict_severity | 0.66 | Wrong merge would connect unrelated event contexts. |
| evidence_quality | 0.36 | Compared evidence is sparse and source-specific. |
| conversion_confidence | 0.62 | This image identity is weak; legal-notice evidence is separate. |
| claim_probability | 0.20 | Possible name-variant question only. |
| relevance | 0.78 | Required Pulgar-line comparison. |
| canonical_readiness | 0.03 | Hold; no merge or name normalization. |

## Hypothesis 5: Same As Dario Arturo Pulgar Or Dario Arturo Pulgar-Smith

Evidence supporting:

- These candidates share broad `Dario` and `Pulgar` elements.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` identifies `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather from family-supplied knowledge and warns against automatic merging with similarly named Pulgar records.
- Existing staged CV context uses document-level `Dario Arturo Pulgar` and keeps the bridge to `Dario Arturo Pulgar-Smith` on hold.

Conflicts and limits:

- This staged draft names `Dario Jose Pulgar-Arriagada`, not `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, or `Pulgar-Smith`.
- It gives no birth date, spouse, child, grandchild, residence, CV context, education, occupation, or direct family bridge.
- Name overlap alone is insufficient and would create high duplicate-person risk.

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

- Existing local context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
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
| relevance | 0.62 | Required anti-conflation context only. |
| canonical_readiness | 0.01 | No relationship promotion supported. |

## Conflict Summary

- Source-control conflict: high. The assigned source image and extracted image are absent, and the available same-folder JPG is a different hash with a different reported visual context.
- Conversion-vs-identity conflict: high. The conversion supports a no-text photograph description but not identification of Dario Jose Pulgar-Arriagada in the image.
- Same-person and duplicate-person conflict: unresolved. `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Arturo Pulgar`, and `Dario Arturo Pulgar-Smith` remain separate hypotheses pending bridge evidence.
- Name-variant conflict: unresolved. This draft does not prove that `Jose`, `J.`, `Arturo`, `A.`, `Arriagada`, or `Pulgar-Smith` forms refer to one person.
- Relationship-conflict evidence: none in this draft.
- Chronology-conflict evidence: unresolved. A 1929 Geneva context may fit an older Pulgar-Arriagada medical/delegate cluster, but the draft gives no age or lifespan data and cannot reconcile later CV, I-94, passenger, or 2000 expropriation contexts.

## Ranked Hypotheses

| rank | hypothesis | probability | next action |
| ---: | --- | ---: | --- |
| 1 | Metadata/title intends association with `Dario Jose Pulgar-Arriagada` | 0.58 | Hold for source-control and archive metadata reread. |
| 2 | Same as a 1918/1929 `Dario/Darío J. Pulgar Arriagada` medical/Geneva cluster | 0.52 | Require explicit bridge proof review before merge or depiction claim. |
| 3 | Same archive/person cluster as separate Table 9 JPG | 0.44 | Do not substitute image files; compare only after conversion QA confirms each source. |
| 4 | Same as canonical `Dario/Darío Pulgar Arriagada` expropriation stub | 0.20 | Preserve as unresolved name-variant question. |
| 5 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.08 | Do not attach; require explicit Arturo/Smith to Pulgar-Arriagada bridge. |
| 6 | Connected to Jose/Juana parent candidates | 0.04 | No relationship action; revisit only with direct relationship evidence. |

## Recommended Next Action

Keep the staged conflict draft on `hold_for_conversion_qa`. Do not promote a depiction claim, attach the photograph to a canonical gallery or person page, replace the missing assigned image with the available Table 9 JPG, merge people, rename canonical pages, or use family context to correct the name silently.

Exact next proof-review step: source-control and conversion QA must restore or locate `V-P-HIST-03583-07A.JPG` with SHA-256 `327c170fda815e9226dbef176e889611718d4ba89c088377a4092588778a6b9a`, its extracted page image, and any local ICRC/archive metadata. The follow-up proof review should reread whether `Dario Jose Pulgar-Arriagada` is identified, whether any caption/roster/table/seat marker exists, and whether the image is distinct from the Table 9 source. Any later Pulgar-line merge requires a separate identity-bridge proof review explicitly comparing `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, and Jose/Juana parent candidates.
