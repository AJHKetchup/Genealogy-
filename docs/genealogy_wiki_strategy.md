# Genealogy Wiki Strategy

This is the genealogy-specific version of the LLM-maintained wiki pattern.

## Core Principle

The wiki is not a loose summary system. It is a lineage research system built from atomic, sourced claims.

Narratives, biographies, family trees, and research summaries are views over the claim and relationship layer. They should not bypass it.

## Requirement Map

| Need | Implementation |
| --- | --- |
| Claim-level evidence | `wiki/claims/` and `_templates/claim.md` |
| Relationship confidence | `wiki/relationships/` and `_templates/relationship.md` |
| Family tree visualization | `genealogy-wiki tree`, output to `wiki/trees/` |
| Dynamic source material converter | `genealogy-wiki material` stages source media; `genealogy-wiki codex-job` prepares page work orders; `genealogy-wiki codex-assemble` writes converted Markdown |
| Transcription vs translation vs interpretation | Required sections in source packet, claim, and photo templates |
| Conflicting records model | `wiki/conflicts/` and `_templates/conflict.md` |
| Person identity resolution | `wiki/identity/` and `_templates/identity.md` |
| Photo and face clustering | `wiki/photos/`, `_templates/photo.md`, and `_templates/face-cluster.md` |
| Research task layer | `wiki/tasks/` and `_templates/task.md` |
| Narrative builder | `genealogy-wiki narrative`, output to `wiki/narratives/` |
| Historical context relevance filter | `wiki/context/` plus lint requirement for `linked_entity` |
| Generational chronology checks | `genealogy-wiki lint` parent/child and event chronology checks |
| Lineage-first architecture | `GENEALOGY_WIKI.md`, `wiki/branches/`, and `wiki/research-plan.md` |

## Workflow

1. Put immutable source files in `raw/sources/` or converted files in `raw/converted/`.
2. For raw or image-based material, create a dynamic source packet with `genealogy-wiki material`, then prepare local Codex page work orders with `genealogy-wiki codex-job`; for already converted Markdown, use `genealogy-wiki packet`.
3. Extract source statements into claim pages.
4. Link claims into relationship, person, family, event, place, identity, conflict, task, and photo pages.
5. Export indexes with `genealogy-wiki index` or a relationship graph with `genealogy-wiki graph`.
6. Run `genealogy-wiki lint` to catch missing evidence, detached tasks/context, weak packets, and suspicious chronology.
7. Generate tree views with `genealogy-wiki tree`.
8. Compile biographies or branch chapters with `genealogy-wiki narrative`.

## Guardrails

- Do not treat relationship links as facts unless a relationship page supports them.
- Do not collapse same-person candidates into one person page until the identity page supports that conclusion.
- Do not write narrative directly from raw source text.
- Do not let context research drift away from a linked genealogy entity.
- Do not hide contradictions in prose. Represent them in `wiki/conflicts/`.
- Do not add record-type-specific injectors as the main path. Let the converter infer structure from the source, with optional overlays only when they do not replace the generic evidence model.
- Do not accept "meaning-preserving" header summaries as complete transcription. Exact labels belong in the printed header inventory, even if split tables use shorter field keys.
