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
- Local execution access was unavailable during this run (`CreateProcessWithLogonW failed: 1326`), preventing inspection of local-only workspace files.

## Follow-Up Search

- Verify whether the newer source-prep/chunking workflow exists on another branch and needs to be pushed into the shared repository before this automation can resume normal triage.
