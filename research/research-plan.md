# Research Plan

## Priority Sources

- Conversion QA triage is blocked at the shared-repo layer until repo-managed source-prep outputs are available for review.

## Human-Facing Reread Queue

- None added in this run because no shared converted pages or chunk manifests were available to assess.

## Source Priority

- Highest priority: publish the current repo-managed conversion artifacts for any newly converted or newly chunked sources before evidence extraction begins.

## Blockers

- Missing shared-repo artifacts expected by the conversion QA gate:
  - `raw/source-prep-manifest.json`
  - `raw/chunks/`
  - `raw/chunks/*/manifest.json`
  - `research/_conversion-review/`
- Legacy local execution blockers are no longer the internal automation path; no-PC post-conversion work is routed through `.github/workflows/internal-research-agents.yml`.

## Follow-Up Search

- Verify whether any remaining source-prep/chunking artifacts need to be published into the shared repository before scheduled triage can process them.
