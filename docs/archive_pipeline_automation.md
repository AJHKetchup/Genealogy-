# Archive Pipeline Automation

This prompt is intended for a recurring Codex automation. It keeps the archive pipeline moving without requiring the user to manually inspect every source.

## Automation Prompt

Run the genealogy archive pipeline for this workspace.

1. Respect `AGENTS.md` and the project skills, especially `$source-prep-pipeline` and `$historical-document-conversion`.
2. Run the source-prep queue commands:
   - `genealogy-wiki prepare-sources --root . --pages-per-job 25`
   - `genealogy-wiki conversion-qc --root .`
   - `genealogy-wiki agent-queues --root . --stale-minutes 360`
   - `genealogy-wiki source-prep-batches --root . --max-pages 8 --limit 25 --stale-minutes 360`
   - `genealogy-wiki source-status --root .`
3. Inspect `research/_agent-queues/source-prep-batches.json` first, then `research/_agent-queues/source-prep.json` if no safe batch exists.
4. If there is a `needs_reread` source-prep batch, prioritize it. Otherwise take a `todo` batch or a single page task. Claim/start the page task ids with one multi-id `agent-task` command and `--no-refresh`, then complete a bounded page range. Use the batch prompt under `research/_agent-queues/prompts/source-prep-batches/` or the single-page prompt under `research/_agent-queues/prompts/source-prep/`. Convert visually from the page image; OCR/PDF text layers and old page outputs are hints only.
5. Write the assigned page Markdown and extracted image crops only to the assigned paths.
6. Mark completed page tasks with one multi-id `genealogy-wiki agent-task complete ... --root . --agent <worker-label> --no-refresh`. Use `fail` or `release` with a short note when a page cannot be repaired in this run.
7. Re-run:
   - `genealogy-wiki prepare-sources --root . --pages-per-job 25`
   - `genealogy-wiki conversion-qc --root .`
   - `genealogy-wiki agent-queues --root . --stale-minutes 360`
   - `genealogy-wiki source-prep-batches --root . --max-pages 8 --limit 25 --stale-minutes 360`
   - `genealogy-wiki source-status --root .`
8. If source-prep tasks are all done for a converted source, let the command assemble and chunk it. Then leave conversion-QA and evidence-extraction queues refreshed for later agents, with page-specific QC artifacts available in `research/_conversion-review/`. Evidence-extraction tasks that overlap QC-held or legacy-repair pages should remain blocked until reread, while clean chunks can keep moving.
9. Do not promote claims to canonical `wiki/` pages. Do not edit originals under `raw/sources/`. Stop after a bounded amount of work and report what changed, what remains queued, and any pages needing human attention.

## Resume Behavior

- Queue refreshes cache page-output reviews in `research/_agent-queues/source-prep-page-cache.json`, keyed by output path, file size, and mtime. This keeps repeated wake-up runs from rereading thousands of unchanged page Markdown files.
- Claimed or in-progress tasks are leases, not permanent locks. `agent-queues --stale-minutes 360` releases tasks with no update for at least six hours so laptop shutdowns, restarts, or killed Codex sessions do not strand pages forever.
- Worker commands should use `--no-refresh` while claiming/completing individual tasks, then refresh queues once at the end of the batch. This keeps small task-state writes cheap and lets the final refresh assemble/chunk completed sources.
- `source-prep-batches` groups only contiguous available pages from the same conversion job and repair class. It speeds scheduling and prompt overhead, but does not relax the per-page visual conversion contract.
- A shutdown in the middle of a page is safe: completed page Markdown/crops remain on disk, task state remains in `task-state.json`, and the next run either sees the page as done or releases the stale claim for reread.

## Cadence

Run hourly while archive ingestion is active. The automation only runs while the laptop and Codex app are available; missed runs are fine because the next run resumes from durable files and stale leases. Pause the automation when no bulk archive work is pending or when costs/compute should be conserved.
