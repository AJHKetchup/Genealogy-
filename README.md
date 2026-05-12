# Historic Document Ingest

This project converts image-heavy historical PDFs into LLM-readable Markdown while preserving document structure: page order, headers, footers, page numbers, body text, image positions, captions, and an auditable link back to page images.

It also includes a genealogy-focused implementation of the LLM wiki pattern: immutable raw sources, an LLM-maintained Markdown wiki, atomic claims, relationship assertions, source packets, an operating schema, an index, a chronological log, page templates, generated tree views, narrative compilation, and lint checks for common genealogy research risks.

Simple OCR is treated as one signal, not the whole answer. The pipeline is designed as staged evidence:

1. Render each PDF page to an image.
2. Detect page regions and reading order.
3. OCR text blocks with confidence metadata.
4. Attach image regions and nearby captions.
5. Optionally pass page evidence to a vision-capable LLM/refinement provider.
6. Emit Markdown, assets, and a JSON manifest for review.

## Install

Core install has no hard OCR/PDF dependencies:

```powershell
pip install -e .
```

For PDF rendering and local OCR:

```powershell
pip install -e ".[pdf,ocr]"
```

Local OCR requires the Tesseract binary to be installed and on `PATH`.

## Usage

```powershell
historic-doc-ingest path\to\document.pdf --out output\document
```

Useful options:

```powershell
historic-doc-ingest path\to\document.pdf --out output\document --dpi 400 --ocr-lang eng
historic-doc-ingest path\to\document.pdf --out output\document --no-ocr
```

## Genealogy Wiki

Create a genealogy research workspace:

```powershell
genealogy-wiki init --root my-family-research
```

This creates:

- `raw/`: immutable source records, converted documents, and assets.
- `wiki/people/`: person pages with identity, relationships, timelines, evidence, conflicts, and sources.
- `wiki/families/`: family or household pages.
- `wiki/branches/`: lineage branch pages tied to research goals.
- `wiki/relationships/`: parent, spouse, sibling, same-person, and name-variant assertions with status and confidence.
- `wiki/events/`: dated events with participants, places, and source evidence.
- `wiki/places/`: place pages for jurisdiction and boundary context.
- `wiki/sources/`: source pages with transcriptions, extracted claims, and citations.
- `wiki/source-packets/`: structured packets with literal transcription, translation, interpretation, and uncertainty kept separate.
- `wiki/claims/`: atomic factual assertions with status, confidence, source, support, and conflicts.
- `wiki/evidence/`: claim-level evidence analysis.
- `wiki/conflicts/`: contradictory dates, names, places, relationships, and identity problems.
- `wiki/identity/`: same-person candidate analysis across name variants, dates, places, relatives, occupations, signatures, migration, and source reliability.
- `wiki/photos/`: photo pages and face-cluster pages.
- `wiki/questions/`: open research questions.
- `wiki/tasks/`: structured research tasks attached to lineage goals, claims, or relationships.
- `wiki/narratives/`: post-wiki biographies, family chapters, migration stories, source appendices, and uncertainty notes.
- `wiki/context/`: historical context pages that must be linked to a genealogy entity.
- `wiki/trees/`: generated Mermaid tree views derived from relationship pages.
- `wiki/index.md`: content-oriented catalog.
- `wiki/log.md`: append-only research log.
- `GENEALOGY_WIKI.md`: the operating manual for an LLM agent maintaining the wiki.

Check the wiki structure:

```powershell
genealogy-wiki lint --root my-family-research
```

Create a structured evidence packet from a difficult source:

```powershell
genealogy-wiki packet raw\converted\geneva-record.md --root my-family-research --id SP001 --title "1929 Geneva record" --kind archive_pdf
```

Stage any source material and create a dynamic packet without assuming a document-specific schema:

```powershell
genealogy-wiki material C:\path\to\source.jpg --root my-family-research --id SP002 --title "Unidentified historical record" --kind unknown --feature handwriting --feature "table/grid"
```

Prepare a local Codex conversion job when you want Codex itself to convert scanned pages in this workspace without API cost:

```powershell
genealogy-wiki codex-job C:\path\to\source.pdf --root my-family-research --id CJ001 --title "Historical source" --pages 1,5-7
genealogy-wiki codex-next my-family-research\raw\codex-conversion-jobs\cj001-historical-source\manifest.json --root my-family-research
genealogy-wiki codex-assemble my-family-research\raw\codex-conversion-jobs\cj001-historical-source\manifest.json --root my-family-research
```

The repo skill `.agents/skills/historical-document-conversion/SKILL.md` tells future Codex agents how to use these page work orders for literal transcription, translation, interpretation, uncertainty, image/caption notes, genealogy leads, and completeness audits.

Create an atomic claim:

```powershell
genealogy-wiki claim --root my-family-research --id CL001 --text "Dario Jose Pulgar Arriagada attended the 1929 Geneva Conventions." --type event --subject "[[people/dario-jose-pulgar-arriagada]]" --source "[[sources/S001-league-of-nations-record]]" --status accepted --confidence 9.5
```

Export the structured claim index:

```powershell
genealogy-wiki index --root my-family-research
```

Create a relationship assertion:

```powershell
genealogy-wiki relationship --root my-family-research --id R001 --type proven_parent --person-a "[[people/parent-name]]" --person-b "[[people/child-name]]" --supporting-claim "[[claims/CL001-parent-claim]]" --status accepted
```

Export a relationship graph JSON view:

```powershell
genealogy-wiki graph --root my-family-research
```

Generate a tree view from relationship pages:

```powershell
genealogy-wiki tree --root my-family-research
```

Compile a narrative only from accepted/probable claim pages:

```powershell
genealogy-wiki narrative "Dario Jose Pulgar Arriagada" --root my-family-research
```

The genealogy wiki is designed to pair with `historic-doc-ingest`: put converted Markdown and manifests under `raw/converted/`, or use `genealogy-wiki material` to stage any raw source under `raw/sources/`. The material packet is document-agnostic: it records the source media, a verbatim extraction contract, exact printed header/label inventory, dynamic layout inventory, reading order, literal transcription, translation, interpretation, uncertainty, candidate entities, claims, relationship evidence, conflicts, research tasks, and a completeness audit without hardcoding a census, church-register, photo, or interview schema.

Outputs:

- `document.md`: LLM-readable Markdown with page anchors and image references.
- `manifest.json`: structured evidence for every page, region, image, and OCR confidence.
- `assets/pages/page-0001.png`: rendered source page images.
- `assets/images/...`: extracted page image regions when available.
- Per-page quality flags in the manifest, including low-confidence text, missing confidence data, and uncaptioned image regions.

## Accuracy Model

The CLI is intentionally conservative. It preserves page boundaries and uncertain text instead of inventing clean prose. For high-stakes transcription, prepare a Codex conversion job and review page images directly against the generated Markdown.

Recommended production workflow for fragile historical material:

1. Run the CLI at 400-600 DPI.
2. Review `manifest.json` for pages with `metadata.quality.needs_review = true`.
3. Prepare a `genealogy-wiki codex-job` for pages that require visual transcription.
4. Convert the page work orders in Codex, then assemble the final Markdown with `genealogy-wiki codex-assemble`.
