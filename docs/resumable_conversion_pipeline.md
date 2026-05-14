# Resumable Conversion Pipeline

The source-prep pipeline is designed to run whenever this laptop is awake and to recover after sleep, restart, or a killed Codex session.

## Durable State

- Raw sources stay immutable in `raw/sources/`.
- Conversion jobs, page images, work orders, page Markdown, and extracted image crops live under `raw/codex-conversion-jobs/`.
- Assembled conversions and chunks live under `raw/converted/` and `raw/chunks/`.
- Agent task state lives in `research/_agent-queues/task-state.json`.
- Source-prep page review cache lives in `research/_agent-queues/source-prep-page-cache.json`.

## Resume Rules

1. Run `genealogy-wiki prepare-sources --root . --pages-per-job 25`.
2. Run `genealogy-wiki conversion-qc --root .`.
3. Run `genealogy-wiki agent-queues --root . --stale-minutes 360`.
4. Run `genealogy-wiki source-prep-batches --root . --max-pages 8 --limit 25 --stale-minutes 360`.
5. Workers prefer `research/_agent-queues/source-prep-batches.json` when a safe contiguous range exists, then fall back to single page tasks in `source-prep.json`.
6. Workers claim/start page task ids with one multi-id command, for example `genealogy-wiki agent-task claim <task-id-1> <task-id-2> --root . --agent <worker> --no-refresh`.
7. Workers write only the assigned page Markdown and extracted-image crop files.
8. Workers complete only finished page tasks with `genealogy-wiki agent-task complete <task-id-1> <task-id-2> --root . --agent <worker> --no-refresh`.
9. At the end of a bounded batch, rerun `prepare-sources`, `conversion-qc`, `agent-queues --stale-minutes 360`, `source-prep-batches --max-pages 8 --limit 25 --stale-minutes 360`, and `source-status`.

`agent-queues --stale-minutes 360` treats claimed or in-progress tasks as leases. If there is no update for six hours, the task is released and can be picked up by the next run. Use `--stale-minutes 0` only for manual debugging when stale release should be disabled.

`source-prep-page-cache.json` stores the review result for each page output keyed by relative path, file size, and mtime. If a page file changes, the review is recomputed. If it does not change, queue refreshes reuse the cached result.

`source-prep-batches.json` is a speed layer over the same page tasks. It groups contiguous available pages from the same job and repair class so a Codex worker can process a small range without repeatedly re-orienting. It is not a quality shortcut: every completed page must still satisfy the full conversion contract, and a worker should shrink or release a batch when the pages are too complex for accurate range work.

## Laptop Behavior

Automations do not need the machine to be on 24/7. Missed hourly runs are expected. The next available run resumes from files already on disk, releases abandoned leases, and continues from the current queue.

If the machine shuts down mid-page, the next run sees one of three states:

- The page Markdown/crops were written and now pass the page contract, so the task becomes `done`.
- The page output is partial or suspicious, so the task remains `needs_reread`.
- The task was claimed but never completed, so it is released after the stale timeout.
