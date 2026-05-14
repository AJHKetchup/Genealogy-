# Research Plan

This is the human-facing work queue. Agents should keep it useful for online research, archive follow-up, source review, and unresolved proof problems.

## Current Focus

- Resolve the Dario/Pulgar conversion-QA blockers before claim extraction from the 1959 I-94 and the 1888 Los Angeles birth entry.
- Sync or commit repository-managed staged drafts under `research/_staging/` so cloud-safe proof review can evaluate actual packets and claims instead of source prep only.

## Conversion QA Follow-Up

- Human reread queue: `research/_conversion-review/page-queues/2026-05-14-dario-pulgar-reread-queue.md`
- Triage summary: `research/_conversion-review/triage/2026-05-14-dario-pulgar-conversion-qa.md`
- Structured concern log: `research/_conversion-review/corrections/2026-05-14-dario-pulgar-conversion-corrections.md`

## Priority Questions

- Are the intended staged drafts still local-only or otherwise not visible on branch `codex/local-codex-conversion-workbench`?
- Which first-pass drafts should be pushed first: Passenger List 1953, Los Angeles birth 1888, Los Angeles birth 1889, or Dario Arturo Pulgar CV?
- Is the 1959 I-94 traveler `Dario A. Pulgar` with birthdate candidate `1 Jun. 1902` a different person from `Dario Pulgar Smith`, whose 1964 tourist card preserves `Concepcion 1/6/42`?
- Does 1888 birth entry 172 truly read `Fidelmiro Segundo Pulgar Arriagada`, and is the father correctly read as `Juan de Casanova Pulgar`?
- Can the 1964 tourist-card parentage field `DARIO Y DOROTHY` be corroborated with surname-bearing records before any parent links are promoted?

## Next Searches

- Once staged drafts are visible, start with the four usable-for-extraction family-relevant sources above because they have clean conversion state and likely high genealogy value.
- Cross-check the I-94 against passport, visa, and travel records for an older `Dario A. Pulgar` before attaching it to any existing person page.
- Compare the 1888 and 1889 Los Angeles / La Laja birth entries against nearby Pulgar-Arriagada civil records for name consistency.
- Use the 1964 tourist card as identity-supporting evidence for `Dario Pulgar Smith`, but hold parent extraction until another record supplies surnames or matching household context.

## Sources To Find Or Review

- `SRC-5a5078ab4b0d` / Passenger List, Royal Mail Lines Limited, August 7, 1953
- `SRC-aa0e304338ce` / Registro de Nacimientos, Los Angeles, Chile, 1888, Entry No. 172
- `SRC-05d0627a5861` / Registro de Nacimientos, Los Angeles, Chile, 1889, Certificate No. 513
- `SRC-07263f404e4c` / CV of Dario Arturo Pulgar
- `SRC-db3e1a4b1081` / Arrival-Departure Record, Form I-94 B, March 30, 1959
- `SRC-8dc32ecbbc69` / Ficha de turista, issued by the Brazilian Consulate on January 27, 1964

## Hypotheses To Test

- The missing proof-review workload is a sync/state problem, not a conversion-readiness problem, because QA indexes and prepared source pages are present while `research/_staging/` drafts were not readable in the shared branch state.
- The I-94 belongs to an older Pulgar traveler and should not be merged with `Dario Pulgar Smith`.
- `Juan de Casanova Pulgar` may be an unusual but correct compound name; a local reread is still required before canonical promotion.
- The 1889 entry is extraction-ready as `Daniel Pulgar Arriagada`, provided the raw surname-first order is preserved in source notes.

## Negative Searches

- 2026-05-14: No cloud-visible staged drafts were available to review under `research/_staging/source-packets/`, `claims/`, `relationships/`, `identity/`, or `conflicts/` on branch `codex/local-codex-conversion-workbench`.
- 2026-05-14: `research/index.md` showed an empty `## Staging` section and sampled source pages had empty `## Extracted Claims` tables.
- 2026-05-14: This QA pass did not find evidence strong enough to merge the 1959 I-94 traveler with `Dario Pulgar Smith`.

## Lineage Goals

- Prevent premature merging of Pulgar individuals across the 1888, 1889, 1959, and 1964 records.
- Clear the two queued rereads before promoting the I-94 and 1888 birth entry into canonical claims or relationships.

## Recently Promoted Findings

- 2026-05-14: The 1889 birth entry for Daniel Pulgar Arriagada is conversion-ready for extraction, provided the raw surname-first order is preserved as evidence language.
- 2026-05-14: The 1964 tourist card remains usable as source-context identity support for `Dario Pulgar Smith`, but not yet for parent-link promotion.