# Genealogy Wiki Operating Manual

This wiki follows Karpathy's LLM-maintained wiki pattern, adapted for genealogical research.

## Layers

- `raw/`: immutable source material. Store original PDFs, images, downloaded records, exports, correspondence, and converted Markdown from document ingestion here. Do not edit these files after ingest.
- `research/`: source/research Obsidian vault for source inspection, conversion dashboards, page transcription, conversion QA, staging drafts, indexes, templates, and agent work queues.
- `wiki/`: family-history Obsidian vault for the final evolving product: people, families, branches, relationships, claims, narratives, photos, context, timelines, and tree views.
- `research/research-plan.md`: prioritized open work, next searches, unresolved questions, and hypotheses to test.
- `research/questions/` and `research/tasks/`: research questions and work queues outside the product vault.
- `wiki/Family Tree.md`: front-facing family tree view generated from relationship pages.
- `wiki/index.md`: lineage-first catalog of families, branches, people, relationships, events, places, claims, narratives, and family-history pages.
- `research/00 Research Start.md`: source and agent-stack front door.

## Genealogy Rules

- Do not merge two people unless evidence supports identity. Keep possible duplicates separate and cross-link them as candidates.
- Every fact about a person, relationship, event, name variant, date, or place needs a source citation or an explicit `unsourced` marker.
- Keep source reliability, conversion confidence, and claim confidence separate. A source can be reliable but poorly converted, clearly converted but weak as evidence, or strong for one fact and weak for another.
- Distinguish evidence from conclusion. A record may say something; the wiki may conclude something else after weighing conflicts.
- Preserve uncertainty. Use `about`, `before`, `after`, `between`, `possibly`, and `probably` instead of inventing precision.
- Track negative evidence, such as searched collections where a person was not found.
- Keep original spelling, place names, and record language in source notes. Normalize only in separate interpretation fields.
- Prefer small, linked pages over giant narrative dumps.
- Treat atomic claims as the foundation of the system. A biography, family tree, or narrative may summarize claims, but claims are the auditable units.
- Keep relationship assertions separate from person pages and assign relationship type, status, confidence, and evidence.
- Keep source transcription, translation, interpretation, and uncertainty in separate sections.
- Context research is allowed only when it explains the lived history of this family through a person, relationship, event, place, source, photo, or narrative chapter.
- Every canonical person page should eventually have a narrative layer: a sourced life story in `wiki/narratives/` built only from accepted or probable claims plus relevant family-specific historical context.
- Treat `raw/chunks/` as non-interpretive navigation aids. Chunks may repeat source text and provenance, but they must not add summaries, normalized facts, or claims.
- Treat `research/_conversion-review/` as the quality gate between verbatim conversion and research extraction. It may flag suspicious readings, likely name drift, important family-relevant pages, and exact page regions for reread, but it must not rewrite converted Markdown.
- Treat QC-held pages as page-specific extraction blocks. Do not freeze a whole archive when only exact pages or regions need reread.
- Treat old OCR, text-layer, or image-only page outputs as repair inputs unless they satisfy the current full page conversion contract.
- Extract visual regions from documents broadly, including portraits/headshots embedded inside scans. Auto-tag a person when the source context identifies the attached or labeled portrait; otherwise preserve the face/headshot as an unknown or candidate crop with source context.
- Put LLM-derived source packets, claims, relationship candidates, identity candidates, and person-page updates in `research/_staging/` first.
- Only a review/promotion pass, performed by the `wiki_promoter` role or an equivalent explicit human direction, may move staged material into canonical wiki folders.
- Keep research navigation, plans, logs, questions, and tasks in `research/`. Keep `wiki/` focused on the genealogy product and family-tree view.

## Lineage-First Architecture

Organize from lineage goals outward:

Family -> Branch -> Person -> Relationship -> Event -> Place -> Source -> Claim -> Narrative.

The wiki can still cross-link freely, but this hierarchy is the default path for research and review.

## Ingest Workflow

When a new source arrives:

1. Add it to `raw/sources/`.
2. Run `genealogy-wiki prepare-sources --root .` to inventory sources, split large PDFs into page-range jobs, create missing Codex conversion jobs, assemble completed jobs, and chunk completed conversions.
3. Run `genealogy-wiki conversion-qc --root .` to write page-level triage, reread queues, and suspected reading notes.
4. Run `genealogy-wiki agent-queues --root . --stale-minutes 360` to write source-prep, conversion-QA, and evidence-extraction queues plus per-task prompt packets, release abandoned task leases, and reuse cached page-output reviews.
5. Run `genealogy-wiki source-status --root .` to see which raw sources are usable, still converting, or held only on specific pages.
6. Let source-prep Codex agents and page/range subagents consume queued work orders using the project skills. Workers should use `agent-task ... --no-refresh` during a bounded batch, then refresh queues once at the end. OCR and PDF text layers are hints only, not the conversion authority.
7. Run conversion QA triage into `research/_conversion-review/` when a converted source is large, noisy, handwritten, tabular, important, or likely to contain family names.
8. Create staged source packets and staged claim drafts under `research/_staging/` from `raw/converted/`, `raw/chunks/`, and the QA page queues.
9. Keep separated transcription, translation, interpretation, uncertainty, and promotion recommendation sections in staged drafts.
10. Review staged claims for literal support, source path, chunk/page reference, uncertainty, status, confidence, and conflicts.
11. Promote reviewed material into `wiki/claims/`, `wiki/relationships/`, and person/family/narrative/tree pages only after review. Keep source packets and transcriptions in `research/`.
12. Update `wiki/index.md`.
13. Append a backstage entry to `research/log.md`.

## Post-Conversion Agent Workflow

After conversion, use this order:

`raw/converted/` + `raw/chunks/` -> `genealogy-wiki conversion-qc` -> `research/_conversion-review/` QA triage -> `research/_staging/` source packets -> staged claims -> proof review -> canonical wiki promotion.

Staged outputs must include source path, chunk or page reference, literal support, uncertainty notes, proposed claim status, and a promotion recommendation. Canonical pages should cite reviewed staged evidence, not raw chunks directly. Parallel subagents are optional and must be explicitly requested by the user.

## Query Workflow

When answering a genealogy question:

1. Read `wiki/index.md` first.
2. Read the relevant person, family, source, evidence, conflict, and place pages.
3. Answer with citations to wiki pages and source pages.
4. If the answer creates a useful synthesis, file it as a new or updated wiki page.
5. Log the query and outcome.

## Lint Workflow

Periodically check for:

- Person pages with no source links.
- Family pages missing relationship evidence.
- Event pages without dates, places, or participants.
- Conflicting dates, places, names, or relationships not represented in `wiki/conflicts/`.
- Orphaned pages missing links from `wiki/index.md`.
- Source pages that do not list extracted claims.
- Research questions in `research/questions/` that have no next action.
- Possible duplicates that need identity analysis.
- Claim pages missing status, confidence, source, or evidence.
- Relationship pages missing relationship type, status, confidence, or supporting claims.
- Source pages missing source reliability notes.
- Source packets missing transcription, translation, interpretation, or uncertainty separation.
- Context pages without a linked genealogy entity.
- Suspicious chronology, such as a parent born after a child, childbearing before age 12, marriage after death, or events after death.

## Citation Style

Use this compact style in wiki pages:

```markdown
[^S001]: [[sources/S001-1850-us-census-smith-household]].
```

Inside facts, cite the source footnote:

```markdown
- Birth: about 1842, Ohio.[^S001]
```

## Page Naming

- People: `people/surname-given-birthyear-deathyear.md`
- Families: `families/surname-surname-marriageyear.md`
- Places: `places/country-region-locality.md`
- Branches: `branches/branch-name.md`
- Relationships: `relationships/R001-person-person-relationship.md`
- Events: `events/EV001-short-event.md`
- Research sources: `research/sources/S001-short-title.md`
- Research source packets: `research/source-packets/SP001-short-title.md`
- Claims: `claims/CL001-short-claim.md`
- Staged drafts: `research/_staging/<workflow>/<draft-id>.md`
- Conversion QA: `research/_conversion-review/<triage|page-queues|corrections>/<source-id>.md`
- Identity: `identity/ID001-person-candidates.md`
- Photos: `photos/PH001-short-description.md`
- Face clusters: `photos/FC001-unknown-cluster.md`
- Research tasks: `research/tasks/T001-short-task.md`
- Narratives: `narratives/N001-short-title.md`
- Conflicts: `conflicts/C001-short-topic.md`
- Research questions: `research/questions/Q001-short-question.md`
