# PC-Off Internal Research Agents

This workflow runs the genealogy post-conversion agent stack on GitHub-hosted Windows runners, so it does not depend on the local PC or Codex desktop app being on.

It is for internal research and wiki development only. It does not perform external research and does not run source preparation or document conversion.

## Runner

- Workflow: `.github/workflows/internal-research-agents.yml`
- Schedule: hourly at minute 17
- Source triggers: main-branch pushes to converted Markdown, chunk manifests/chunks, controller code, or this workflow
- Conversion trigger: successful `Cloud Source Conversion` workflow completions
- Manual run: GitHub Actions -> Internal Research Agents -> Run workflow
- Parallelism: defaults to 3 Codex workers, with a queue scan limit of 12
- Automatic promotion: enabled in a separate one-worker promotion-only pass after ordinary QA/extraction/review
- Runtime: GitHub-hosted `windows-latest`
- Auth: Codex CLI with ChatGPT-managed `auth.json`
- API keys: forbidden for this lane
- Windows checkout: enables Git `core.longpaths` before checkout because generated chunk paths can exceed the default Windows path limit.

Scheduled and push-triggered GitHub workflows only run from the repository default branch, so this file must be merged to `main` before the PC-off runner is live.

## Required GitHub Secret

The repository must be private. The workflow expects one of these repository secrets:

- `CODEX_AUTH_JSON_B64`, preferred
- `CODEX_AUTH_JSON`, accepted for plain JSON

For unattended long-term runs, also add:

- `CODEX_SECRET_UPDATE_TOKEN`

`CODEX_SECRET_UPDATE_TOKEN` must be a GitHub token scoped only to this repository with repository `Secrets` write permission. GitHub's REST API documentation says fine-grained tokens need repository `Secrets` write permission for creating or updating repository secrets; classic PATs need the broader `repo` scope. The workflow uses this token only to rotate `CODEX_AUTH_JSON_B64` after Codex refreshes ChatGPT auth.

`CODEX_AUTH_JSON_B64` is a base64 encoding of the local `~/.codex/auth.json` file after `codex login`, where:

- `auth_mode` is `chatgpt`
- `tokens.refresh_token` exists

PowerShell helper to produce the base64 secret value:

```powershell
$authPath = Join-Path $env:USERPROFILE ".codex\auth.json"
[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes((Get-Content -LiteralPath $authPath -Raw)))
```

Never commit `auth.json` or paste it into normal issue/PR text. Treat it like a password.

## What The Agents Do

The workflow installs the project and Codex CLI, restores Codex account auth from the secret, verifies the auth is ChatGPT-managed, refuses provider API keys, and runs:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/post-conversion-agent-controller.ps1 -Root . -RunMinutes 45 -MaxWorkers 3 -QueueLimit 12 -PollSeconds 45 -WaitForWorkers -WorkerTimeoutMinutes 15
```

The controller refreshes deterministic state, then launches bounded Codex workers for these lanes:

- `conversion-qa`: review converted/chunked sources for suspicious readings, relevance, and reread needs.
- `evidence-extraction`: stage source packets, atomic claims, relationships, identity candidates, conflicts, and follow-up tasks from converted chunks.
- `identity-analysis`: compare same-person, duplicate, name-variant, and conflict candidates without merging canonical people.
- `proof-review`: score staged drafts for literal support, source quality, conversion confidence, evidence weight, identity confidence, claim probability, relevance, and canonical readiness.
- `wiki-promotion`: runs only in a separate promotion-only pass and only promotes drafts whose review notes say they are ready.

After workers drain, the workflow commits/pushes GitHub-safe research/wiki state through:

```powershell
python -m historic_doc_ingest.genealogy_wiki sync-github-database --root . --internal-research-only --refresh-base --message "Run internal research agents"
```

Before publishing, the hosted sync snapshots generated GitHub-safe outputs, resets the ephemeral checkout to the latest `main`, semantically merges shared state such as `research/log.md` and `research/_agent-queues/task-state.json`, then commits from that fresh base. If another scheduled workflow lands a commit after that point, `sync-github-database` retries rejected pushes by fetching, rebasing the already-created commit, and pushing again. This keeps long internal runs from becoming one-off dead ends when conversion automation is also active.

If the controller records a failure after checkout/auth, the workflow still commits safe queue state, controller state, and run logs under `research/_agent-queues/` before marking the job failed. That keeps failures resumable and visible to the next scheduled run instead of losing them with the ephemeral runner.

## Presentation Wiki

The family-facing site is a separate generated layer, described in `research/_automation/family-presentation-architecture.json`.

The `Publish Wiki Site` workflow rebuilds the internal Ancestry-style presentation automatically on pushes to `main`, hourly at minute 41, and after a successful `Internal Research Agents` run. It renders:

- `index.html`: home person, family tree preview, people, relationships, family lines, LifeStory chapters, and family timeline
- `tree.html`: canonical person/relationship tree
- `people.html`: family profiles and branch pages
- `timeline.html`: family events and person facts only
- `sources.html`: supporting records and citations
- `research.html`: QA, staging, queues, proof review, source usability, and automation state

Converted chunks, source-operation dates, QA prompts, and agent queue internals stay out of the presentation dashboard. They remain available in the source library and research backroom.

## Boundaries

The internal workflow must not:

- perform external research
- call source-prep or document-conversion workers
- use `OPENAI_API_KEY`, `CODEX_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_GENERATIVE_AI_API_KEY`, or `GEMINI_API_KEY`
- edit raw sources, converted Markdown, chunks, or conversion job page Markdown
- promote canonical wiki material unless `allow_promotion=true` and review notes say `canonical_readiness: ready`

## Auth Maintenance

GitHub-hosted runners are ephemeral. Codex refresh tokens are rotating/single-use. If a hosted run refreshes the token and the new `auth.json` is not saved, the next run can fail with `refresh_token_reused`.

The workflow rotates `CODEX_AUTH_JSON_B64` automatically after a successful Codex startup when `CODEX_SECRET_UPDATE_TOKEN` is present. If the secret has already gone stale, reseed `CODEX_AUTH_JSON_B64` once from a fresh local `codex login`; after that, the hosted workflow should keep it current itself. A persistent self-hosted runner would avoid this reseed cycle, but it would again depend on an always-on machine.
