---
name: historical-document-conversion
description: Use when converting scanned historical or genealogical documents into high-accuracy Markdown with page images, captions, marginalia, literal transcription, translation, interpretation, uncertainty, and completeness audits. Trigger for census pages, church registers, newspapers, handwritten records, archive PDFs, old photos, and source-packet conversion work.
---

# Historical Document Conversion

Use this skill when the user wants Codex to convert historical source material directly in the local environment, especially when avoiding paid OCR/LLM APIs.

For repository-wide crop rules, see `docs/visual_extraction_contract.md`.

## Core Rule

Preserve evidence before interpretation. Never silently summarize, modernize, normalize spelling, repair grammar, merge people, or hide uncertainty.

Keep these layers separate:

- literal transcription
- translation
- interpretation
- uncertainty or illegibility
- extracted genealogy leads
- completeness audit

## Workflow

1. Prepare a page workbench:

```powershell
genealogy-wiki codex-job "C:\path\source.pdf" --root . --id CJ001 --title "Source title"
```

For a sample or targeted run:

```powershell
genealogy-wiki codex-job "C:\path\source.pdf" --root . --id CJ001 --title "Source title" --pages 1,5-7
```

2. Get the next unfinished page:

```powershell
genealogy-wiki codex-next raw\codex-conversion-jobs\cj001-source-title\manifest.json --root .
```

3. Open the work order and source image. Convert the page visually, crop meaningful non-text visual regions into the work order's `extracted-images/page-####/` folder, then write the requested Markdown file under the job's `page-markdown/` folder.

4. Repeat `codex-next` until no unfinished work orders remain.

5. Assemble the document:

```powershell
genealogy-wiki codex-assemble raw\codex-conversion-jobs\cj001-source-title\manifest.json --root .
```

6. Chunk the assembled document for later research agents:

```powershell
genealogy-wiki prep-chunk raw\converted\cj001-source-title.codex.md --root .
```

## Page Markdown Structure

Use this structure unless the source demands a richer one:

```markdown
# Page N

## Page Metadata

## Layout And Reading Order

## Literal Transcription

## Images, Captions, And Visual Notes

## Translation

## Interpretation

## Uncertain Or Illegible

## Extracted Genealogy Leads

## Completeness Audit
```

## Transcription Standards

- Preserve line breaks when they affect layout, columns, headings, tables, captions, or meaning.
- Preserve source spelling and punctuation, including obvious original typos.
- Use `[?]` immediately after uncertain words or phrases.
- Use `[illegible]` only when no plausible reading can be given.
- Extract meaningful image regions into the assigned `extracted-images/page-####/` folder and reference them inline near their source position.
- Always crop visible portraits/headshots embedded inside larger scans, including ID-card photos, passport photos, group-photo faces when practical, newspaper portrait blocks, and labeled album portraits.
- Mark any image that cannot be confidently cropped with `[IMAGE: approximate location / description / visible caption / reason not cropped]`.
- For tables or forms, preserve row/column structure in Markdown tables when practical.
- If a table is too wide, split it into logical sections while keeping row numbers or source line numbers stable.
- Record page numbers, sheet numbers, stamped numbers, handwritten numbers, and printed labels.

## Genealogy Extraction

Extract leads conservatively. Prefer candidates over conclusions:

- names and name variants
- dates and date ranges
- places
- relationships stated by the source
- occupations, residences, organizations, events
- photo subjects or unknown face/group descriptions
- source-context photo identities when a caption, identity card, passport page, or nearby label names the person shown
- claims that deserve later source-packet or claim pages

Never infer a relationship merely because people appear near each other unless the source says so or the inference is clearly labeled.

## Completeness Audit

End every converted page with a short audit:

- major regions checked
- unreadable or cropped areas
- uncertain names/dates/places
- images/captions accounted for
- whether transcription appears complete

If a page is too dense for one pass, convert the visible page first and recommend targeted crops for the uncertain regions.
