# Genealogy Wiki Log

## [2026-05-11] init | Genealogy wiki created

- Created raw source layer, wiki layer, schema, index, log, and templates.

## [2026-05-14] promote | No shared staged reviews found

- Checked the shared GitHub workspace state for repo-managed staged reviews and drafts.
- Found no accessible staged review notes or promotable drafts in the shared repository state, so no canonical wiki pages were changed.
- Could not run `genealogy-wiki lint --root .` in this session because local process execution failed in the sandbox (`CreateProcessWithLogonW failed: 1326`).

## [2026-05-14] narrative-review | Canonical narrative layer inspected

- Inspected the shared repository for canonical `wiki/people/`, `wiki/claims/`, `wiki/relationships/`, `wiki/source-packets/`, `wiki/photos/`, `wiki/events/`, `wiki/places/`, `wiki/context/`, and `wiki/narratives/` content.
- Found wiki scaffolding and templates, but no discoverable non-template person pages, accepted/probable claim pages, or compiled individual narratives on `main`.
- Deferred biography creation until reviewed evidence is promoted into canonical person and claim pages.
- Updated `wiki/index.md` and `wiki/research-plan.md` to record the blocker and next narrative prerequisites.
