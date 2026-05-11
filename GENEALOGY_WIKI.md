# Genealogy Wiki Operating Manual

This wiki follows Karpathy's LLM-maintained wiki pattern, adapted for genealogical research.

## Layers

- `raw/`: immutable source material. Store original PDFs, images, downloaded records, exports, correspondence, and converted Markdown from document ingestion here. Do not edit these files after ingest.
- `wiki/`: LLM-maintained Markdown knowledge base. This is the working research brain.
- `wiki/index.md`: lineage-first catalog of families, branches, people, relationships, events, places, sources, claims, narratives, and open questions.
- `wiki/log.md`: append-only chronological record of ingests, queries, conclusions, corrections, and lint passes.
- `wiki/research-plan.md`: prioritized open work, next searches, and hypotheses to test.

## Genealogy Rules

- Do not merge two people unless evidence supports identity. Keep possible duplicates separate and cross-link them as candidates.
- Every fact about a person, relationship, event, name variant, date, or place needs a source citation or an explicit `unsourced` marker.
- Distinguish evidence from conclusion. A record may say something; the wiki may conclude something else after weighing conflicts.
- Preserve uncertainty. Use `about`, `before`, `after`, `between`, `possibly`, and `probably` instead of inventing precision.
- Track negative evidence, such as searched collections where a person was not found.
- Keep original spelling, place names, and record language in source notes. Normalize only in separate interpretation fields.
- Prefer small, linked pages over giant narrative dumps.
- Treat atomic claims as the foundation of the system. A biography, family tree, or narrative may summarize claims, but claims are the auditable units.
- Keep relationship assertions separate from person pages and assign relationship type, status, confidence, and evidence.
- Keep source transcription, translation, interpretation, and uncertainty in separate sections.
- Context research is allowed only when tied to a person, relationship, event, place, source, photo, or narrative chapter.

## Lineage-First Architecture

Organize from lineage goals outward:

Family -> Branch -> Person -> Relationship -> Event -> Place -> Source -> Claim -> Narrative.

The wiki can still cross-link freely, but this hierarchy is the default path for research and review.

## Ingest Workflow

When a new source arrives:

1. Add it to `raw/sources/` or `raw/converted/`.
2. Create or update one page under `wiki/sources/`.
3. Create a source packet under `wiki/source-packets/` with separated transcription, translation, interpretation, and uncertainty sections.
4. Extract asserted facts into atomic claim pages under `wiki/claims/`.
5. Create or update relationship assertions under `wiki/relationships/`.
6. Update person, family, branch, place, event, photo, conflict, identity-candidate, and task pages as needed.
7. Update `wiki/index.md`.
8. Append an entry to `wiki/log.md`.

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
- Open questions that have no next action.
- Possible duplicates that need identity analysis.
- Claim pages missing status, confidence, source, or evidence.
- Relationship pages missing relationship type, status, confidence, or supporting claims.
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
- Sources: `sources/S001-short-title.md`
- Source packets: `source-packets/SP001-short-title.md`
- Claims: `claims/CL001-short-claim.md`
- Identity: `identity/ID001-person-candidates.md`
- Photos: `photos/PH001-short-description.md`
- Face clusters: `photos/FC001-unknown-cluster.md`
- Tasks: `tasks/T001-short-task.md`
- Narratives: `narratives/N001-short-title.md`
- Conflicts: `conflicts/C001-short-topic.md`
- Questions: `questions/Q001-short-question.md`
