# PC-Off Internal Research Agents

This workflow runs the genealogy post-conversion agent stack on GitHub-hosted Windows runners, so it does not depend on the local PC or Codex desktop app being on.

It is for internal research and wiki development only. It does not perform external research and does not run source preparation or document conversion.

## Runner

- Workflow: `.github/workflows/internal-research-agents.yml`
- Schedule: hourly at minute 17
- Manual run: GitHub Actions -> Internal Research Agents -> Run workflow
- Parallelism: defaults to 3 Codex workers, with a queue scan limit of 12
- Runtime: GitHub-hosted `windows-latest`
- Auth: Codex CLI with ChatGPT-managed `auth.json`
- API keys: forbidden for this lane

Scheduled GitHub workflows only run from the repository default branch, so this file must be merged to `main` before the hourly PC-off runner is live.

## Required GitHub Secret

The repository must be private. The workflow expects one of these repository secrets:

- `CODEX_AUTH_JSON_B64`, preferred
- `CODEX_AUTH_JSON`, accepted for plain JSON

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
- `wiki-promotion`: disabled by default; only runs when manually dispatched with `allow_promotion=true`.

After workers drain, the workflow commits/pushes GitHub-safe research/wiki state through:

```powershell
python -m historic_doc_ingest.genealogy_wiki sync-github-database --root . --message "Run internal research agents"
```

## Boundaries

The internal workflow must not:

- perform external research
- call source-prep or document-conversion workers
- use `OPENAI_API_KEY`, `CODEX_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_GENERATIVE_AI_API_KEY`, or `GEMINI_API_KEY`
- edit raw sources, converted Markdown, chunks, or conversion job page Markdown
- promote canonical wiki material unless `allow_promotion=true` and review notes say `canonical_readiness: ready`

## Auth Maintenance

GitHub-hosted runners are ephemeral. Codex can refresh ChatGPT-managed auth during a normal run, but the updated file is not automatically written back to repository secrets.

If the workflow later fails with auth/401 errors, reseed `CODEX_AUTH_JSON_B64` from a fresh local `codex login`. A persistent self-hosted runner would avoid this reseed cycle, but it would again depend on an always-on machine.
