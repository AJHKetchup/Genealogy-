# Genealogy Project Instructions

## Source Preparation Is Stage One

Before research, claims, identity resolution, or narrative work, prepare sources under `raw/sources/`.

For every document-preparation task:

- Treat `raw/sources/` as immutable original evidence. Do not edit originals.
- Create durable derivatives under `raw/codex-conversion-jobs/`, `raw/converted/`, `raw/chunks/`, and `raw/assets/`.
- Preserve a link from every derivative back to the original source path, hash, conversion manifest, and page image.
- Use page-scoped work orders for large sources. Do not ask one agent to convert a massive PDF in a single pass.
- Use the `historical-document-conversion` skill for page-level transcription standards.
- Use the `source-prep-pipeline` skill for end-to-end source intake, conversion job setup, image extraction requirements, chunking, and audit outputs.

## Required Source-Prep Outputs

The minimum complete preparation package for a source is:

- A raw source entry in `raw/source-prep-manifest.json`.
- A conversion job manifest under `raw/codex-conversion-jobs/<job>/manifest.json`.
- One rendered page artifact per work order under `page-images/`.
- One Markdown page output per completed work order under `page-markdown/`.
- Extracted page images/crops under `extracted-images/page-####/` when the source contains photos, illustrations, seals, signatures, maps, charts, or other non-text visual evidence.
- An assembled converted Markdown file under `raw/converted/`.
- Page-scoped chunks and `raw/chunks/<converted-source>/manifest.json`.

## Accuracy Rules

- Preserve literal transcription before translation or interpretation.
- Do not summarize, modernize spelling, silently repair source errors, or hide uncertainty.
- Mark uncertain readings with `[?]`; use `[illegible]` only when no plausible reading is possible.
- Keep captions, marginalia, stamps, page numbers, tables, and image positions in reading order.
- If the page is too dense, split the work by page region and record what remains unresolved.

## Post-Conversion Research Is Stage Two

After `raw/converted/` and `raw/chunks/` exist, do not jump straight into canonical person pages, relationships, or narratives.

## Conversion QA Is The Gate Between Conversion And Research

Before source-packet or claim extraction, run a conversion QA triage pass when a source is newly converted, large, noisy, handwritten, multilingual, or likely relevant to known family members.

Use this path:

`raw/converted/` + `raw/chunks/` + page images -> `research/_conversion-review/` triage notes and page queues -> `research/_staging/` source packets and claims.

For conversion QA:

- Keep the converted Markdown verbatim. Do not silently correct `raw/converted/`, chunk files, or page Markdown.
- Use canonical wiki names, places, relationships, and source history as clues for suspicious readings, not as authority to overwrite the transcript.
- Flag likely name drift or OCR/transcription errors separately, for example `Dario` misread as `David`.
- Queue exact pages, chunks, table rows, captions, signatures, marginal notes, or page regions that deserve careful reread.
- Write QA artifacts under `research/_conversion-review/triage/`, `research/_conversion-review/page-queues/`, and `research/_conversion-review/corrections/`.
- Use `conversion-qa-triage` and the `conversion_qa_reviewer` or `source_quality_reviewer` agent role for this gate.

Use this path:

`raw/converted/` + `raw/chunks/` + `research/_conversion-review/` -> `research/_staging/` source packets -> staged claims -> proof review -> canonical wiki promotion.

For every post-conversion research task:

- Treat `raw/chunks/` as non-interpretive source navigation. Do not add summaries, normalized facts, or claims to chunk files.
- Check `research/_conversion-review/` first. Prioritize pages and regions marked family-relevant or suspicious before broad extraction.
- Write LLM-derived drafts to `research/_staging/` first, including draft source packets, claims, relationship candidates, identity candidates, conflict candidates, and proposed person-page updates.
- Each staged output must include source path, chunk or page reference, literal source support, uncertainty notes, proposed status/confidence, and promotion recommendation.
- Do not write to canonical `wiki/claims/`, `wiki/relationships/`, `wiki/people/`, or `wiki/families/` unless the task is an explicit review/promotion pass. Keep source packets, transcriptions, conversion QA, and staging drafts in `research/`.
- Use `post-conversion-wiki-ingest`, `genealogy-claim-extraction`, and `genealogy-proof-review` skills for post-conversion work.
- Treat `wiki_promoter` as the only agent role allowed to move reviewed material from staging into canonical wiki pages.

## Obsidian Vault Structure

There are two Obsidian vault roots:

- `wiki/` is the final evolving family-history product and exploration view. Keep `wiki/Family Tree.md` and `wiki/index.md` as the user-facing entry points.
- `research/` is the source engine and agent-stack view. Keep `research/00 Research Start.md`, `research/index.md`, `research/Conversion Dashboard.md`, and `research/log.md` as the source-facing entry points.

- Treat the many wiki subfolders as product shelves for the family line, family tree, claims, narratives, and proof layer.
- Treat `research/sources/`, `research/source-packets/`, `research/sources/transcriptions/`, `research/questions/`, `research/tasks/`, `research/research-plan.md`, `research/_conversion-review/`, and `research/_staging/` as the research/agent shelves.
- Keep `wiki/Family Tree.md` readable as the primary family-tree view.
- Keep `research/research-plan.md` focused on what the user should research next online or in archives.
- Keep `index.md` as the canonical map of created pages.
- Keep conversion dashboards in `research/`, not `wiki/`.

## Family Narrative Focus

This project is about the user's family history. Broader history matters only where it explains the lives, records, migrations, occupations, communities, conflicts, language, legal status, or constraints of family members.

- Give every canonical person page a path toward a narrative page in `wiki/narratives/`.
- Build individual narratives from accepted or probable claims, relationship pages, source packets, photos, timelines, and directly relevant context.
- Keep speculative or disputed material visible in uncertainty notes, not smoothed into prose.
- Do not create general historical essays unless they are linked to a specific family entity and explain why that context matters.

## Subagent Pattern

Use subagents when the user explicitly asks for agent workflows or parallel work. For source preparation, prefer:

- A source inventory explorer to classify file types, sizes, page counts, duplicates, and path risks.
- One or more conversion workers, each assigned a disjoint page range or source file.
- A quality reviewer that checks Markdown against page images, extracted crops, completeness audits, and family-relevance/name-drift triage.

For post-conversion research, prefer:

- A `conversion_qa_reviewer` to create `research/_conversion-review/` triage notes before extraction.
- An `evidence_extractor` to create staged source-packet and claim drafts from assigned converted sources or chunks.
- A `claim_reviewer` to inspect staged drafts for source support, uncertainty, conflicts, and promotion readiness.
- An `identity_researcher` to compare same-person, duplicate, name-variant, and conflict candidates without merging canonical people.
- A `wiki_promoter` to apply reviewed staging drafts to canonical wiki pages, update `wiki/index.md`, and log the action in `research/log.md`.

Workers are not alone in the codebase. They must not revert unrelated edits, and they must write only their assigned source/job/page outputs.
