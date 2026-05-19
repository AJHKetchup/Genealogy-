# Post-Conversion Autopilot

This is the architecture for automatic genealogy work after conversion. It follows the Karpathy LLM Wiki pattern: raw sources stay immutable, the wiki/research files are durable Markdown state, and `AGENTS.md` plus project skills are the schema that tells any agent how to maintain the knowledge base.

This lane is API-free. Do not require `OPENAI_API_KEY`, Gemini, Anthropic, or any other provider API key for post-conversion evidence extraction, QA, proof review, or promotion.

## Entry Point

Primary model:

```text
State: Git-tracked Markdown and JSON queues
Agent interface: AGENTS.md, skills, queue prompts, task-state leases
Model runtime: GitHub-hosted Codex CLI with ChatGPT-managed auth, or an equivalent non-API agent session
Provider API keys: forbidden for this post-conversion lane
```

The legacy Codex app automation `post-conversion-genealogy-buildout` is retired and removed from the app automation registry. It attempted to launch a Windows worktree shell and failed before repository code could run; it is kept out of the active architecture because it depends on the local desktop process launcher. Do not replace it with an OpenAI API or other provider API workflow.

The PC-off runner is now the GitHub-hosted workflow:

```text
.github/workflows/internal-research-agents.yml
```

It runs hourly on `windows-latest`, restores ChatGPT-managed Codex auth from `CODEX_AUTH_JSON_B64` or `CODEX_AUTH_JSON`, refuses provider API keys, launches bounded `codex exec` workers through the controller, waits for them to drain, and commits GitHub-safe research/wiki outputs. Setup details are in `docs/internal_research_agents_pc_off.md`.

Local accelerator, for when the Windows workspace is available:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/post-conversion-agent-controller.ps1 -Root . -Once -MaxWorkers 3 -QueueLimit 12
```

Path note: `C:\Users\Big Al\Documents\New project` is a Windows junction to `C:\Users\Big Al\Documents\Genealogy`, so Python commands may print the resolved target path while operating on the same workspace files.

Dry-run syntax:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/post-conversion-agent-controller.ps1 -Root . -Once -DryRun -NoRefresh -NoWorkers
```

## Agent Runner

1. Reads `AGENTS.md`, this document, and `research/_automation/post-conversion-architecture.json`.
2. Runs the post-conversion refresh commands:
   - `PYTHONPATH=src python -m historic_doc_ingest.genealogy_wiki conversion-qc --root .`
   - `PYTHONPATH=src python -m historic_doc_ingest.genealogy_wiki agent-queues --root . --stale-minutes 360 --post-conversion-only`
   - `PYTHONPATH=src python -m historic_doc_ingest.genealogy_wiki source-status --root . --no-refresh-index --no-source-prep-task-refresh`
3. Reads queue manifests and `research/_agent-queues/task-state.json`.
4. Claims a bounded set of available tasks from conversion QA, evidence extraction, identity analysis, or proof review.
5. Performs the assigned worker task through the active non-API agent runtime, writing only the task's allowed output paths.
6. Marks tasks complete or releases them with a concise blocker.
7. Reports changed files, verification, and blockers.

If no non-API model runtime is available, automation may refresh queues and indexes, but it must not pretend to complete LLM judgment tasks.

## API-Free Worker Harness

The no-provider-API worker path is a Codex or Codex-equivalent agent session consuming the durable queue prompts. The GitHub workflow uses Codex CLI with ChatGPT-managed auth, not a provider API key.

For Codex specifically, the problem observed on 2026-05-17 was the Codex app `worktree` runner, not the Codex agent model. The active no-PC runner is the GitHub-hosted workflow, which checks out the repository, restores ChatGPT-managed Codex auth from a repository secret, starts bounded workers, waits for them, and commits allowed outputs back to the repo.

## Parallelism

- Prefer a batch of 3 independent queue tasks per run.
- Allow up to 6 tasks when they have disjoint write paths and are low-risk.
- Prefer proof-review tasks when staged drafts already exist, because they are independent and do not alter source derivatives.
- Do not claim multiple tasks that write the same staged draft, same review note, same source packet, or same canonical target.
- Do not mix promotion into a QA, extraction, or proof-review batch.

Promotion remains disabled unless a separate promotion run is explicitly configured and reviewed material recommends `promote`.

## Adaptive Conversion

The agent runner uses `research/_automation/evidence-scoring-model.json` and `research/_agent-queues/source-relevance-feedback.json` to route important pages back to higher-fidelity conversion.

- Rough Docling/OCR/Flash output is discovery-grade, not final authority for important family facts.
- High or critical relevance requests at least Pro conversion.
- High or critical relevance plus complexity, suspicious readings, handwriting, tables, images, stamps, signatures, seals, marginalia, or low conversion confidence requests Pro with crops.
- The same source/page/tier is not repeated after that tier is fulfilled.
- A higher tier can supersede a lower tier when new research context makes the page more important.
- Context is phrased as a verification question. Example: "The prior conversion reads David Pulgar; project context suggests Dario Pulgar may fit this family. Please verify the visible letters against the image and preserve uncertainty."
- Hard boundary: "please double-check whether this is Dario" is allowed; "change this to Dario" is forbidden unless the visible source itself supports that reading.
- Literal transcription preserves the source. Other-evidence hypotheses belong in uncertainty notes, suspected-reading fields, interpretation, or proof review.

This post-conversion lane does not call Gemini or any other provider API. It can write durable upgrade requests in `source-relevance-feedback.json`; the separate conversion layer decides how to satisfy them.

## Evidence Probability

Proof review is probabilistic. It should not treat `promote` and `not promoted` as the evidence model.

Review notes should score:

- `source_quality_score`
- `conversion_confidence_score`
- `evidence_quantity_score`
- `agreement_score`
- `identity_confidence_score`
- `claim_probability`
- `relevance_level`
- `relevance_confidence`
- `canonical_readiness`

Canonical readiness is operational: whether the current wiki should be updated now. Claim probability is evidentiary: how likely the claim currently appears after weighing source quality, amount of evidence, conflicts, identity risk, and conversion confidence.

## Local Controller

The PowerShell controller is an optional local accelerator. It is useful while the Windows workspace is on, but it is not the no-PC architecture.

1. Runs the post-conversion refresh commands with the resolved workspace root:
   - `genealogy-wiki conversion-qc --root <workspace>`
   - `genealogy-wiki agent-queues --root <workspace> --stale-minutes <n> --post-conversion-only`
   - `genealogy-wiki source-status --root <workspace> --no-refresh-index --no-source-prep-task-refresh`
2. Builds `research/_agent-queues/proof-review.json` from staged drafts.
3. Builds a disabled-by-default `research/_agent-queues/wiki-promotion.json`.
4. Reads queue status plus `research/_agent-queues/task-state.json`.
5. Claims and starts available tasks.
6. Writes one prompt per worker under `research/_agent-queues/post-conversion-worker-prompts/`.
7. Starts background `codex exec` workers for the selected roles.
8. Saves controller state to `research/_agent-queues/post-conversion-controller-state.json`.

## Queue Lanes

| Lane | Worker role | Input queue | Writes |
| --- | --- | --- | --- |
| Conversion QA | `conversion_qa_reviewer` | `research/_agent-queues/conversion-qa.json` | `research/_conversion-review/` |
| Evidence extraction | `evidence_extractor` | `research/_agent-queues/evidence-extraction.json` | `research/_staging/` |
| Identity analysis | `identity_researcher` | `research/_agent-queues/identity-analysis.json` | `research/_staging/identity-analysis/` |
| Proof review | `claim_reviewer` | `research/_agent-queues/proof-review.json` | `research/_staging/reviews/` |
| Promotion | `wiki_promoter` | `research/_agent-queues/wiki-promotion.json` | `research/claims/`, `research/relationships/`, `wiki/` |

Promotion is disabled unless the controller is run with `-AllowPromotion`.

## Guardrails

- Agent runner: claims bounded queue work and writes only assigned outputs.
- Workers: own one queued task and update `task-state.json`.
- Conversion QA workers do not create claims.
- Evidence workers do not edit canonical wiki pages.
- Proof-review workers do not promote.
- Living-family privacy is not a standalone hold for this internal family project; user approval was recorded on 2026-05-17. Promotion workers still require reviewed evidence, source support, and conservative confidence/status labels.

## State Files

- Architecture contract: `research/_automation/post-conversion-architecture.json`
- Controller state: `research/_agent-queues/post-conversion-controller-state.json`
- Task state: `research/_agent-queues/task-state.json`
- Identity-analysis queue: `research/_agent-queues/identity-analysis.json`
- Proof-review queue: `research/_agent-queues/proof-review.json`
- Promotion queue: `research/_agent-queues/wiki-promotion.json`

## Automation Behavior

GitHub Actions is the active no-PC automation surface for post-conversion internal research. The old Codex app heartbeat/crons for this lane are retired and removed because they are local desktop jobs. The API-free architecture remains the queue-and-agent harness: durable tasks, task leases, prompt packets, staging outputs, proof review, and logs. It should not be converted to an API-key workflow. It should not be converted back to a local thread heartbeat unless the user explicitly accepts that the PC must remain on.
