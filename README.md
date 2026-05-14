# Genealogy

Genealogy converts image-heavy historical PDFs into LLM-readable Markdown while preserving document structure: page order, headers, footers, page numbers, body text, image positions, captions, and an auditable link back to page images.

It also includes a genealogy-focused implementation of the LLM wiki pattern split into two Obsidian vaults: a `research/` vault for source preparation, transcriptions, conversion QA, staging drafts, and agent work; and a `wiki/` vault for the evolving family-history product, atomic claims, relationships, family lines, tree views, and narratives.

## GitHub As The Database

After local source preparation, GitHub is the portable database for the project. The laptop-only layer is limited to raw originals, rendered page images, crop work, and active conversion-worker state. The GitHub-backed layer contains the prepared text derivatives and research product that cloud/worktree agents can use from any platform:

- `raw/source-prep-manifest.json`
- `raw/converted/*.codex.md`
- `raw/chunks/**`
- `research/_conversion-review/**`
- `research/_staging/**`
- `research/` entry points, logs, indexes, and research notes
- canonical `wiki/**`

Do not push `raw/sources/`, `raw/codex-conversion-jobs/`, `raw/assets/`, `research/_agent-queues/`, `.genealogy/`, or `obsidian-offline/` as database state. Local source-prep automations create and repair the converted text; cloud/worktree automations can then triage, stage, review, promote, and write narratives from the GitHub-backed text.

Use the local sync bridge when the laptop has produced new converted/chunked/research/wiki state:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/sync-github-database.ps1
```

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

## Source Preparation Pipeline

Before research agents extract claims or write wiki pages, place originals in:

```powershell
raw\sources
```

Then run the source-prep queue:

```powershell
genealogy-wiki prepare-sources --root .
```

This inventories `raw/sources/`, splits large PDFs into manageable page-range jobs, creates missing Codex conversion jobs, assembles jobs whose page Markdown is already complete, chunks completed conversions, and updates `raw/source-prep-manifest.json`.

Build agent task queues:

```powershell
genealogy-wiki agent-queues --root . --stale-minutes 360
```

This writes source-prep, conversion-QA, and evidence-extraction queues under `research/_agent-queues/`, including per-task prompt packets. It also releases stale claimed/in-progress tasks after the configured timeout, so interrupted laptop sessions can resume instead of stranding work. Codex conversion agents then consume the queued page work orders using the project skills:

```powershell
genealogy-wiki source-prep-batches --root . --max-pages 8 --limit 25 --stale-minutes 360
```

This adds `research/_agent-queues/source-prep-batches.json`, grouping contiguous available page tasks from the same job and repair class. Batches reduce re-orientation and task-state overhead, but they do not relax the quality standard: every page still needs visual conversion, complete page Markdown, visual crops when present, uncertainty notes, and a completeness audit.

```powershell
genealogy-wiki codex-next raw\codex-conversion-jobs\cj001-source-title\manifest.json --root .
```

For massive PDFs, tune the agent batch size:

```powershell
genealogy-wiki prepare-sources --root . --pages-per-job 25
```

After conversions are assembled and chunked, run page-level post-conversion QC:

```powershell
genealogy-wiki conversion-qc --root .
genealogy-wiki agent-queues --root . --stale-minutes 360
genealogy-wiki source-prep-batches --root . --max-pages 8 --limit 25 --stale-minutes 360
genealogy-wiki source-status --root .
```

This writes `research/_conversion-review/qc-index.json` plus source-specific triage, page queues, and suspected reading notes. The goal is to reread only the exact pages or regions that are poor, family-relevant, suspicious compared with known family context, or produced by an older conversion pass that does not satisfy the current page-level conversion contract.

`agent-queues` uses those QC decisions to put bad/legacy page outputs back into source-prep as `needs_reread` and to block only affected evidence-extraction chunks with `blocked_needs_reread`; clean chunks from the same giant source can keep moving. `source-status` writes `research/_indexes/source-usability.json` and `research/source-usability.md`, showing which raw sources are not started, still converting, ready for extraction, or ready except for specific pages needing repair.

Queue workers can record durable task state without editing the queue JSON by hand:

```powershell
genealogy-wiki agent-task claim "source-prep:cj001:p0001" --root . --agent source-worker-1
genealogy-wiki agent-task start "source-prep:cj001:p0001" --root . --agent source-worker-1
genealogy-wiki agent-task complete "source-prep:cj001:p0001" --root . --agent source-worker-1
```

This updates `research/_agent-queues/task-state.json` and refreshes the queue manifests.

Batch workers can pass multiple page task ids to the same `agent-task` command:

```powershell
genealogy-wiki agent-task claim "source-prep:cj001:p0001" "source-prep:cj001:p0002" --root . --agent source-worker-1 --no-refresh
```

For unattended batches, add `--no-refresh` to `agent-task claim|start|complete|fail|release` and run one final `agent-queues --stale-minutes 360` at the end. Page-output reviews are cached in `research/_agent-queues/source-prep-page-cache.json` by path, mtime, and file size, so repeated automation wake-ups do not need to reread every unchanged conversion page.

The lower-level primitives remain available when a source needs custom batching:

```powershell
genealogy-wiki codex-job "raw\sources\source.pdf" --root . --id CJ001 --title "Source title" --pages 1,5-7
genealogy-wiki codex-assemble raw\codex-conversion-jobs\cj001-source-title\manifest.json --root .
genealogy-wiki prep-chunk raw\converted\cj001-source-title.codex.md --root .
```

The minimum prepared-source package is a raw original, a conversion manifest with hashes and page outputs, extracted image crops when present, assembled Markdown under `raw/converted/`, and page-scoped chunks under `raw/chunks/`.

## Genealogy Wiki

Create a genealogy research workspace:

```powershell
genealogy-wiki init --root my-family-research
```

This creates:

- `research/00 Research Start.md`: the Obsidian front door for source work, conversion review, staging, and agent operations.
- `wiki/Family Tree.md`: the front-facing family tree view generated from relationship pages.
- `raw/`: immutable source records, converted documents, and assets.
- `research/sources/`: research/source pages with conversion artifacts, transcription links, and source identity.
- `research/sources/transcriptions/`: page-level editable transcription notes.
- `research/source-packets/`: structured source packets with literal transcription, translation, interpretation, and uncertainty kept separate.
- `research/Conversion Dashboard.md`: source conversion inspection and review queue.
- `research/_staging/`: reviewable LLM-derived source packets, claims, relationship candidates, identity/conflict candidates, and proposed wiki updates created after source conversion and chunking.
- `research/_conversion-review/`: conversion QA triage, page queues, and suspected correction notes created after conversion but before extraction.
- `research/_templates/`: page templates used by agents and CLI scaffolding.
- `research/_indexes/`: generated JSON indexes for tools and automation.
- `wiki/people/`: person pages with identity, relationships, timelines, evidence, conflicts, and sources.
- `wiki/families/`: family or household pages.
- `wiki/branches/`: lineage branch pages tied to research goals.
- `wiki/relationships/`: parent, spouse, sibling, same-person, and name-variant assertions with status and confidence.
- `wiki/events/`: dated events with participants, places, and source evidence.
- `wiki/places/`: place pages for jurisdiction and boundary context.
- `wiki/claims/`: atomic factual assertions with status, confidence, source, support, and conflicts.
- `wiki/evidence/`: claim-level evidence analysis.

Confidence is split into three different ideas:

- Source reliability: how trustworthy the source is for the fact being asserted, such as original record, derivative transcript, index, authored account, or oral history.
- Conversion confidence: how sure the system is that the converted text accurately reflects the page image or original media.
- Claim confidence: how strongly the source support justifies the proposed genealogy claim after reliability, conversion quality, conflicts, and context are considered.
- `wiki/conflicts/`: contradictory dates, names, places, relationships, and identity problems.
- `wiki/identity/`: same-person candidate analysis across name variants, dates, places, relatives, occupations, signatures, migration, and source reliability.
- `wiki/photos/`: photo pages and face-cluster pages.
- `research/questions/`: open research questions.
- `research/tasks/`: structured research tasks attached to lineage goals, claims, relationships, or sources.
- `wiki/narratives/`: sourced individual biographies, family chapters, migration stories, source appendices, and uncertainty notes.
- `wiki/context/`: historical context pages that must be linked to a family entity and explain why the context matters to their lived history.
- `wiki/trees/`: optional generated tree variants derived from relationship pages.
- `wiki/index.md`: content-oriented catalog.
- `research/log.md`: append-only source, agent, and promotion log.
- `GENEALOGY_WIKI.md`: the operating manual for an LLM agent maintaining the wiki.

Open `wiki/` as the Obsidian vault when you want to explore the final evolving family-history product. Open `research/` as the Obsidian vault when you want to drive source conversion, research, QA, staging, and agent work.

Photo identity starts with visual crop extraction. Source-prep should crop portraits/headshots embedded inside documents, not only standalone photos. If the source context identifies the person shown, such as a named passport, tourist card, or captioned portrait, the system can auto-tag that crop as `source_context_confirmed` and add it to `research/_indexes/face-reference-index.json`. Unlabeled crops remain unknown/candidate records until more evidence is available.

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

Prepare source conversion queues after dropping files in `raw/sources/`:

```powershell
genealogy-wiki prepare-sources --root my-family-research
genealogy-wiki conversion-qc --root my-family-research
genealogy-wiki agent-queues --root my-family-research --stale-minutes 360
genealogy-wiki source-status --root my-family-research
```

The source-prep agent consumes the created work orders or the prompt packets in `research/_agent-queues/prompts/source-prep/`. Large PDFs are split into page-range jobs by default, and `--pages-per-job` controls the range size. Task claims are durable leases in `research/_agent-queues/task-state.json`; queue refreshes release stale leases so the work can continue after the machine sleeps, restarts, or misses scheduled automation runs. The repo skills `.agents/skills/source-prep-pipeline/SKILL.md` and `.agents/skills/historical-document-conversion/SKILL.md` define how Codex agents and subagents convert pages, crop visual evidence, preserve transcription/translation/interpretation/uncertainty, and audit completeness. OCR or PDF text layers may be used as hints, but they are not treated as authoritative conversion.

After conversion and `genealogy-wiki prep-chunk`, run `genealogy-wiki conversion-qc` before evidence extraction. It flags bad OCR/image-only conversions, family-relevant pages, suspicious readings such as likely name drift, and legacy page outputs missing the full conversion sections. The `conversion-qa-triage` skill then refines those artifacts under `research/_conversion-review/` without changing `raw/converted/` or `raw/chunks/`. Extraction tasks whose page range overlaps a QC hold are blocked until reread, while unrelated chunks remain available. Then post-conversion agents work in `research/_staging/` first. The `post-conversion-wiki-ingest`, `genealogy-claim-extraction`, and `genealogy-proof-review` skills define the staged workflow, and `docs/post_conversion_agent_workflow.md` is the main handoff playbook. Canonical wiki pages are updated only after review/promotion.

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

The CLI is intentionally conservative. It preserves page boundaries and uncertain text instead of inventing clean prose. For high-stakes historical transcription, queue the source for Codex-agent conversion and compare the generated Markdown against page images during conversion QA.

Recommended production workflow for fragile historical material:

1. Drop originals in `raw/sources/`.
2. Run `genealogy-wiki prepare-sources --root .`.
3. Let source-prep Codex agents convert the queued work orders with page images, crops, transcription, translation, interpretation, uncertainty, and completeness audits.
4. Run conversion QA on difficult, family-relevant, noisy, handwritten, tabular, or multilingual sources before claim extraction.
