# Agent Handoff

This document is for future agents resuming work after conversation context is lost.

## Current Project

Workspace: `C:\Users\Big Al\Documents\New project`

The project currently contains two related systems:

1. `historic-doc-ingest`: a Python toolkit for converting image-heavy historical PDFs into Markdown plus an auditable manifest.
2. `genealogy-wiki`: a genealogy-focused implementation of Karpathy's LLM wiki strategy, centered on atomic claims, relationship assertions, source packets, and lineage-first research structure.

## Verification Status

Tests were run successfully after adding Python 3.12 to PATH and installing the package in editable mode with `pip install -e .`.

Command:

```powershell
python -m pytest
```

Result:

```text
17 passed in 0.75s
```

## Important Commands

Install editable package:

```powershell
pip install -e .
```

Install PDF/OCR/dev extras:

```powershell
pip install -e ".[pdf,ocr,dev]"
```

Run tests:

```powershell
python -m pytest
```

Convert a PDF:

```powershell
historic-doc-ingest path\to\document.pdf --out output\document
```

Initialize a genealogy wiki:

```powershell
genealogy-wiki init --root my-family-research
```

Create a source packet:

```powershell
genealogy-wiki packet raw\converted\record.md --root my-family-research --id SP001 --title "Record title" --kind archive_pdf
```

Create a claim:

```powershell
genealogy-wiki claim --root my-family-research --id CL001 --text "Atomic claim text." --type event --subject "[[people/person-name]]" --source "[[sources/S001-record]]"
```

Create a relationship:

```powershell
genealogy-wiki relationship --root my-family-research --id R001 --type proven_parent --person-a "[[people/parent-name]]" --person-b "[[people/child-name]]" --supporting-claim "[[claims/CL001-parent-claim]]"
```

Write structured indexes:

```powershell
genealogy-wiki index --root my-family-research
genealogy-wiki graph --root my-family-research
```

Generate a tree view:

```powershell
genealogy-wiki tree --root my-family-research
```

Compile a narrative:

```powershell
genealogy-wiki narrative "Person Name" --root my-family-research
```

Lint a genealogy wiki:

```powershell
genealogy-wiki lint --root my-family-research
```

## Implemented Checklist

### Historical Document Ingest

- [x] Python package scaffold in `pyproject.toml`.
- [x] CLI entry point: `historic-doc-ingest`.
- [x] PDF page rendering module using PyMuPDF when installed.
- [x] Rendered page image output under `assets/pages/`.
- [x] PDF text/image block extraction.
- [x] Coordinate scaling from PDF points to rendered image pixels.
- [x] Optional local OCR adapter using Tesseract via `pytesseract`.
- [x] Markdown output with page anchors and source page image references.
- [x] JSON manifest with pages, blocks, coordinates, confidence, and metadata.
- [x] Image-region crop support when PDF image blocks are present.
- [x] Nearest-caption attachment heuristic.
- [x] Page quality report with low-confidence and missing-confidence flags.
- [x] Refinement provider interface for future vision/HTR correction.
- [x] Refinement contract document: `docs/refinement_contract.md`.

### Genealogy Wiki Architecture

- [x] CLI entry point: `genealogy-wiki`.
- [x] `genealogy-wiki init` scaffold command.
- [x] `genealogy-wiki lint` command.
- [x] `genealogy-wiki packet` command.
- [x] `genealogy-wiki claim` command.
- [x] `genealogy-wiki relationship` command.
- [x] `genealogy-wiki index` command for claim and relationship JSON.
- [x] `genealogy-wiki graph` command for relationship graph JSON.
- [x] `genealogy-wiki tree` command.
- [x] `genealogy-wiki narrative` command.
- [x] Operating manual: `GENEALOGY_WIKI.md`.
- [x] Strategy map: `docs/genealogy_wiki_strategy.md`.
- [x] Lineage-first wiki directories:
  - [x] `wiki/branches/`
  - [x] `wiki/people/`
  - [x] `wiki/families/`
  - [x] `wiki/relationships/`
  - [x] `wiki/events/`
  - [x] `wiki/places/`
  - [x] `wiki/sources/`
  - [x] `wiki/source-packets/`
  - [x] `wiki/claims/`
  - [x] `wiki/evidence/`
  - [x] `wiki/conflicts/`
  - [x] `wiki/identity/`
  - [x] `wiki/photos/`
  - [x] `wiki/questions/`
  - [x] `wiki/tasks/`
  - [x] `wiki/narratives/`
  - [x] `wiki/context/`
  - [x] `wiki/timelines/`
  - [x] `wiki/trees/`
- [x] Immutable raw source directories:
  - [x] `raw/sources/`
  - [x] `raw/converted/`
  - [x] `raw/assets/`
- [x] Templates for:
  - [x] branch
  - [x] person
  - [x] family
  - [x] relationship
  - [x] event
  - [x] source
  - [x] source packet
  - [x] claim
  - [x] evidence
  - [x] conflict
  - [x] identity
  - [x] photo
  - [x] face cluster
  - [x] research task
  - [x] narrative
  - [x] context
  - [x] generated tree
- [x] Claim-level evidence template with status, confidence, source, literal support, translation, interpretation, uncertainty, supports, and conflicts.
- [x] Relationship confidence template with type, status, confidence, endpoints, supporting claims, and conflicting claims.
- [x] Relationship index with calculated confidence from supporting/conflicting claims.
- [x] Source packet template separating literal transcription, translation, interpretation, and uncertainty.
- [x] Identity-resolution template with comparison matrix.
- [x] Photo and face-cluster templates.
- [x] Research-task template tied to claims, relationships, or lineage goals.
- [x] Narrative template that says narratives must be compiled from accepted/probable claims.
- [x] Context template requiring a linked genealogy entity.
- [x] Mermaid tree generator from relationship pages.
- [x] Narrative compiler skeleton using accepted/probable claim pages.
- [x] Lint checks for required structure.
- [x] Lint checks for orphaned wiki pages not referenced from index.
- [x] Lint checks for claim pages missing source/status/confidence/key sections.
- [x] Lint checks for claim status, confidence range, and missing wiki-link targets.
- [x] Lint checks for relationship pages missing endpoints/type/status/confidence/evidence sections.
- [x] Lint checks for relationship endpoints and referenced claim targets.
- [x] Lint checks for source packets missing transcription/translation/interpretation/uncertainty sections.
- [x] Lint checks for context pages missing `linked_entity`.
- [x] Lint checks for detached research tasks.
- [x] Lint checks for conflict and identity page structure.
- [x] Basic chronology lint:
  - [x] parent born after child
  - [x] parent younger than 12 at child birth
  - [x] event after participant death
  - [x] same participant in two places on same date

## Not Yet Implemented Checklist

### Historical Document Ingest

- [ ] Actual production-grade layout analysis for complex historical pages.
- [ ] Table detection and preservation, especially census and church-register tables.
- [ ] Handwritten text recognition integration.
- [ ] Vision-model refinement provider implementation.
- [ ] Batch ingest across many documents.
- [ ] Source-type-specific extraction profiles: census, church register, passenger list, newspaper clipping, photo back, oral interview, etc.
- [ ] Confidence reconciliation across OCR, PDF text layer, HTR, and vision LLM outputs.
- [ ] Human review UI or review workflow.
- [ ] Rebuild Markdown from edited/refined manifest.
- [ ] Export evidence packets directly from converted documents.

### Genealogy Claim System

- [x] Structured claim index/cache for fast querying across `wiki/claims/`.
- [x] Claim creation command.
- [ ] Claim update command.
- [ ] Claim status transition rules.
- [ ] Claim confidence scoring rubric.
- [x] Basic cross-reference validation between claim pages, sources, source packets, people, and relationships.
- [ ] Deeper cross-reference validation between claims, events, families, places, conflicts, and tasks.
- [ ] Automatic extraction of claims from source packets using an LLM.
- [ ] Automatic support/conflict linking between claims.
- [ ] Claim deduplication and near-duplicate detection.

### Relationship System

- [x] Relationship creation command.
- [x] Relationship confidence scoring from linked claims.
- [ ] Relationship type validation.
- [ ] Automatic detection of missing parent/spouse/sibling evidence.
- [ ] Same-person candidate relationship handling beyond template support.
- [x] Relationship graph export to JSON.

### Family Tree Visualization

- [ ] True ancestor chart layout.
- [ ] True descendant chart layout.
- [ ] Marriage links and sibling grouping.
- [ ] Confidence-coded visual legend.
- [ ] Duplicate-person warnings in the generated chart.
- [ ] Speculative and disputed edge rendering beyond simple Mermaid link styles.
- [ ] Interactive browser/tree UI.

### Source Packet Injector

- [ ] Ingest source packets directly from scanned records.
- [ ] Ingest handwritten documents.
- [ ] Ingest archive PDFs.
- [ ] Ingest old photos.
- [ ] Ingest newspaper clippings.
- [ ] Ingest church registers.
- [ ] Ingest census tables.
- [ ] Ingest Ancestry screenshots.
- [ ] Ingest oral interviews.
- [ ] Automatically populate source packet sections from OCR/HTR/vision outputs.

### Transcription, Translation, Interpretation

- [ ] Enforce non-empty literal transcription for source packets when source text is readable.
- [ ] Translation workflow for multilingual sources.
- [ ] Interpretation workflow that requires citations to literal or translated lines.
- [ ] Uncertainty marking conventions such as `[illegible]`, `[?]`, and alternatives.
- [ ] Validation that narratives do not cite raw sources directly.

### Conflicting Records Model

- [ ] Automatic conflict detection for two birth dates.
- [ ] Automatic conflict detection for two possible spouses.
- [ ] Automatic conflict detection for inconsistent ages across censuses.
- [ ] Automatic conflict detection for same-name people in same town.
- [ ] Automatic conflict detection for conflicting parents.
- [ ] Automatic conflict detection for spelling variants requiring identity analysis.
- [ ] Automatic conflict detection for impossible timelines.
- [ ] Conflict pages generated with evidence on each side.

### Person Identity Resolution

- [ ] Identity scoring model.
- [ ] Name-variant normalization.
- [ ] Date/place/relative/occupation/signature/migration comparison engine.
- [ ] Source reliability weighting.
- [ ] Same-person candidate generation.
- [ ] Duplicate-person merge recommendation workflow.
- [ ] Explicit "do not merge" decision tracking.

### Photo And Face Clustering

- [ ] Face detection.
- [ ] Face embedding/clustering.
- [ ] Unknown face cluster generation.
- [ ] Confirmed identity tags.
- [ ] Suggested identity tags.
- [ ] Photo-back transcription pipeline.
- [ ] Date/location estimation from image clues.
- [ ] Scene description extraction.
- [ ] Links from faces/photos to people, events, and places.

### Research Task Layer

- [ ] Automatic task generation from missing proof.
- [ ] Task priority scoring.
- [ ] Suggested repository/search generation.
- [ ] Task status workflow.
- [ ] Link tasks to lineage goals, claims, relationships, sources, and conflicts.
- [ ] Negative-search capture and reuse.

### Narrative Builder

- [ ] Polished biography generation from accepted/probable claims.
- [ ] Family branch chapter generation.
- [ ] Migration story generation.
- [ ] Historical context insertion only when linked and relevant.
- [ ] Photo caption generation from photo pages and claims.
- [ ] Timeline generation from event and claim pages.
- [ ] Source appendix generation.
- [ ] Uncertainty notes generated from disputed/possible claims.
- [ ] Narrative citation style.

### Historical Context Filter

- [ ] Stronger lint that rejects context pages without meaningful lineage relevance.
- [ ] Context scope rules by person, relationship, place, event, source, photo, and chapter.
- [ ] Drift detection for broad unrelated context research.

### Generational Chronology Checks

- [ ] Mother age threshold distinct from father/parent threshold.
- [ ] Person married after death.
- [ ] Immigration after known death.
- [ ] Siblings born implausibly close together.
- [ ] Child born after mother's likely death.
- [ ] Parent too old at child birth.
- [ ] Event before birth unless explicitly marked as about family/source.
- [ ] Multiple same-date locations with distance/travel plausibility.
- [ ] Calendar/date parsing beyond simple 4-digit years.

### Import/Export

- [ ] GEDCOM import.
- [ ] GEDCOM export.
- [ ] Gramps XML import/export.
- [x] Relationship graph JSON export.
- [ ] Full project JSON graph export.
- [ ] CSV exports for claims, people, relationships, sources, tasks, and conflicts.

## Key Files

- `README.md`: general project usage.
- `GENEALOGY_WIKI.md`: operating manual for agents maintaining the genealogy wiki.
- `docs/genealogy_wiki_strategy.md`: requirement map and guardrails.
- `docs/refinement_contract.md`: contract for vision/HTR page refinement.
- `src/historic_doc_ingest/genealogy_wiki.py`: genealogy wiki CLI, templates, linting, source packets, tree generation, narrative compilation.
- `src/historic_doc_ingest/pipeline.py`: PDF ingestion pipeline.
- `src/historic_doc_ingest/models.py`: document ingest data models.
- `tests/test_genealogy_wiki.py`: genealogy wiki tests.
- `tests/test_markdown.py`: Markdown writer tests.
- `tests/test_quality.py`: quality report tests.

## Current Caveats

- The genealogy system is currently file/template/CLI based. It is not yet a full database or graph engine.
- The source packet injector creates packet files but does not yet perform OCR, HTR, vision extraction, or claim extraction.
- The tree generator creates a Mermaid view from relationship pages, but it is not a true genealogical chart layout yet.
- The narrative compiler is deliberately conservative and currently emits claim bullets rather than polished prose.
- Linting is useful but incomplete; it needs deeper cross-page validation and chronology parsing.

## Suggested Next Implementation Order

1. Add claim extraction from source packets.
2. Add claim update/status-transition commands.
3. Add automatic support/conflict linking between claims.
4. Expand chronology lint using richer parsed events and relationships.
5. Improve tree generation with ancestor/descendant modes.
6. Add narrative generation from indexed claims with citations.
7. Add identity-resolution scoring and duplicate-person candidate generation.
8. Add source-type-specific packet injection for census/church register/photo/interview records.
9. Add CSV exports for claims, relationships, sources, tasks, and conflicts.
10. Add GEDCOM or Gramps import/export.
