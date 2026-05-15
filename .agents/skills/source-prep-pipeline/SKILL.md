---
name: source-prep-pipeline
description: Prepare raw genealogy and historical source files for research before claim extraction. Use for raw source intake, source inventories, high-accuracy Codex conversion jobs, page-scoped Markdown transcription, extracted image/caption handling, chunking massive converted files, provenance links, and quality review of document-preparation outputs.
---

# Source Prep Pipeline

Use this skill before research agents create claims, relationships, biographies, or conclusions. The goal is to turn unfriendly originals from Cloudflare R2 into auditable, page-scoped Markdown, image crops, and chunks while preserving provenance.

Cloud-first storage split:

- Cloudflare R2 stores raw originals and binary derivatives: rendered page images, extracted crops, audio snippets, and video frames.
- GitHub stores JSON, Markdown, code, conversion manifests, work orders, page Markdown, queues, task state, QA notes, chunks, staging drafts, and wiki text.
- Local `raw/sources/`, `page-images/`, `extracted-images/`, audio snippets, and video frames are disposable worker cache. Do not treat them as the system of record.

For the full quality checklist, read `references/conversion-quality-contract.md` when reviewing or converting real pages. For crop requirements, read `docs/visual_extraction_contract.md`.

## Workflow

1. Queue raw sources for agent conversion:

```powershell
genealogy-wiki cloud-source-prep-heartbeat --root . --pages-per-job 25 --batch-pages 1
```

This restores raw originals from R2 into disposable local cache, inventories sources, splits PDFs into page-range jobs, creates missing conversion jobs, assembles fully completed jobs, chunks completed conversions, writes GitHub queue JSON/Markdown, and uploads binary derivatives back to R2.

For a local-only dry run that does not touch R2:

```powershell
genealogy-wiki cloud-source-prep-heartbeat --root . --no-restore --no-asset-upload --dry-run
```

The lower-level command still exists for focused local preparation after raw cache has been restored:

```powershell
genealogy-wiki prepare-sources --root .
```

Tune page-range size for massive sources:

```powershell
genealogy-wiki prepare-sources --root . --pages-per-job 25
```

Refresh agent queues after preparation or after any page Markdown files are completed:

```powershell
genealogy-wiki agent-queues --root .
```

This writes `research/_agent-queues/source-prep.json`, `conversion-qa.json`, and `evidence-extraction.json` plus prompt packets under `research/_agent-queues/prompts/`.

For faster unattended repair work, write one-page prompts after refreshing the normal queues:

```powershell
genealogy-wiki source-prep-batches --root . --max-pages 1 --limit 80
```

This writes `research/_agent-queues/source-prep-batches.json` and prompt packets. Each source-prep worker gets one page. Run more workers for throughput instead of assigning multiple pages to one worker. Every page still requires visual conversion, full page Markdown, extracted visual crops when present, uncertainty notes, and a completeness audit.

Record task ownership through the CLI, not by hand-editing queue JSON:

```powershell
genealogy-wiki agent-task claim "<task-id>" --root . --agent "<worker-label>"
genealogy-wiki agent-task start "<task-id>" --root . --agent "<worker-label>"
genealogy-wiki agent-task complete "<task-id>" --root . --agent "<worker-label>"
```

This writes `research/_agent-queues/task-state.json` and refreshes the queues.

Controller prompts may still pass task ids through the same command interface, but source-prep conversion assignments should contain only one page task id:

```powershell
genealogy-wiki agent-task claim "<task-id-1>" "<task-id-2>" --root . --agent "<worker-label>" --no-refresh
```

2. Use lower-level job commands only when custom batching is needed:

```powershell
genealogy-wiki codex-job "raw\sources\source.pdf" --root . --id CJ001 --title "Source title"
genealogy-wiki codex-job "raw\sources\source.pdf" --root . --id CJ001-P001-050 --title "Source title pages 1-50" --pages 1-50
```

Prefer page ranges for massive files. Keep job IDs short and stable. The default `prepare-sources` path already creates page-range jobs for PDFs; use manual `codex-job` only when a source needs custom grouping.

3. Convert page work orders using Codex vision and source-specific reasoning:

```powershell
genealogy-wiki codex-next raw\codex-conversion-jobs\<job>\manifest.json --root .
```

Open the returned work order. View the page image, use OCR/text-layer output only as hints when available, write the requested `page-markdown/page-####.md`, and crop meaningful non-text visual evidence into that page's `extracted-images/page-####/` folder. This includes portraits and headshots embedded inside a larger scanned document.

4. Assemble completed pages:

```powershell
genealogy-wiki codex-assemble raw\codex-conversion-jobs\<job>\manifest.json --root .
```

Partial assembly is acceptable; missing pages are listed explicitly.

5. Chunk assembled Markdown:

```powershell
genealogy-wiki prep-chunk raw\converted\<job>.codex.md --root .
```

Chunks are page-scoped by default and written under `raw/chunks/<converted-source>/`.

6. Rebuild the prep index after conversion:

```powershell
genealogy-wiki prep-index --root .
```

Stop source-prep work here. Before source packets or staged claims, run conversion QA triage into `research/_conversion-review/` for large, noisy, handwritten, multilingual, or family-relevant sources. For source packets, staged claims, proof review, identity analysis, or wiki promotion, switch to the post-conversion skills and write drafts under `research/_staging/`.

Check source readiness:

```powershell
genealogy-wiki conversion-qc --root .
genealogy-wiki agent-queues --root .
genealogy-wiki source-status --root .
```

The usability report shows which raw sources are still converting, which are usable for extraction, and which are usable except for specific QC-held pages. Evidence-extraction tasks that overlap held pages are blocked as `blocked_needs_reread`; unrelated chunks remain available.

Do not treat an old page output as done just because `page-markdown/page-####.md` exists. If the queue status is `needs_reread`, overwrite that page output with a fresh visual conversion that satisfies every required section in the work order.

## Output Contract

Every prepared source should have:

- Original file preserved under `raw/sources/`.
- Original file preserved in R2, with a disposable local cache under `raw/sources/` only while a worker runs.
- A GitHub-tracked conversion job manifest with source path, source hash, page image hashes, work orders, extracted-image folders, and chunking metadata.
- Page images uploaded to R2 and recorded in `raw/r2-derived-assets.json`.
- Page Markdown under GitHub-tracked `page-markdown/`.
- Inline references to extracted visual regions, with binary crop files uploaded to R2 and recorded in `raw/r2-derived-assets.json`.
- An assembled converted Markdown file under `raw/converted/`.
- Page-scoped chunks plus a chunk manifest under `raw/chunks/`.

## Agent Use

Use subagents only when the user explicitly asks for agent workflows or parallel work. For source conversion, assign one page per worker; use more workers for throughput. Tell conversion workers exactly which job/page they own and where to write outputs.

Recommended roles:

- `source_inventory`: read-only inventory and batching.
- `source_converter`: page-scoped conversion and image cropping.
- `source_quality_reviewer` or `conversion_qa_reviewer`: read-only comparison of Markdown, crops, chunks, provenance, suspicious readings, and family-relevant page queues.

## Rules

- Never edit originals in `raw/sources/`.
- Do not rely on OCR alone for historical conversion. Treat OCR and PDF text layers as low-trust signals that must be checked visually.
- Treat old OCR/text-layer/page-image-only conversions as repair inputs, not completed work, unless they satisfy the full page conversion contract.
- Keep transcription, translation, interpretation, uncertainty, and genealogy leads separate.
- Extract photographs, illustrations, seals, signatures, maps, charts, and other non-text visual evidence as separate files when visible.
- Extract portraits and headshots inside scans as separate crop assets, even when the whole source is already an image.
- If the source context identifies the person in an attached portrait or labeled photo, record that identity in the page notes as source-context evidence. If the face is unlabeled, describe it without naming the person.
- Preserve links back to source file, source SHA-256, conversion manifest, page image, page output, and chunk manifest.
- Treat audio/video as a separate transcription branch; do not force it through OCR.
- Do not extract genealogy claims or update canonical wiki pages as part of source preparation.
