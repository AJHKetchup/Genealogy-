# Pipeline References

These references shape the source-prep and research loop.

## Codex

- [Codex AGENTS.md documentation](https://developers.openai.com/codex/guides/agents-md): project guidance belongs in `AGENTS.md` so every agent run inherits durable workflow rules.
- [Codex skills documentation](https://developers.openai.com/codex/skills): repeatable workflows should be packaged as skills with focused instructions, references, and optional scripts.
- [Codex subagents documentation](https://developers.openai.com/codex/subagents): highly parallel work can be split across specialized subagents and collected by the parent agent.
- [Codex best practices](https://developers.openai.com/codex/learn/best-practices): long-running work should have clear goal, context, constraints, and done conditions.

## LLM Wiki

- [Andrej Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources are immutable, the LLM-maintained wiki is a persistent compounding artifact, and schema files such as `AGENTS.md` make the agent a disciplined maintainer.

## Local Interpretation

- `raw/sources/` is the immutable archive.
- `raw/codex-conversion-jobs/` and `research/_agent-queues/` are the agent execution layer.
- `raw/converted/` and `raw/chunks/` are LLM-readable evidence, not conclusions.
- `research/_conversion-review/` and `research/_staging/` are review and draft layers.
- `wiki/` is the maintained family-history product built from reviewed claims, relationships, conflicts, identities, narratives, and tree views.
