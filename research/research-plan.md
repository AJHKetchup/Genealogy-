# Research Plan

This is the human-facing work queue. Agents should keep it useful for online research, archive follow-up, source review, and unresolved proof problems.

## Current Focus

- Review the new staged drafts for `SRC-5a5078ab4b0d`, `SRC-aa0e304338ce`, and `SRC-05d0627a5861` under `research/_staging/source-packets/` and `research/_staging/claims/`.
- Resolve the Dario/Pulgar conversion-QA blockers before claim extraction from the 1959 I-94 and before promoting the 1888 Los Angeles birth entry.
- Resolve source identity for `batch-pdf-042-c-mara-de-senadores-de-la-naci-n-1936-pages-1-5` before any evidence extraction. The current converted slice reads as a railways publication, not a Senate source.
- Rerun or reassemble `batch-pdf-043-s495-2-2` and `batch-pdf-044-s522bis-29-3`; both converted Markdown artifacts are empty.
- Keep `SRC-07263f404e4c` / CV of Dario Arturo Pulgar as the next unstaged high-value source once the current reread queue is cleared.

## Conversion QA Follow-Up

- Human reread queue: `research/_conversion-review/page-queues/2026-05-14-dario-pulgar-reread-queue.md`
- Human reread queue: `research/_conversion-review/page-queues/2026-05-14-batch-img-017-entry-172-reread.md`
- Triage summary: `research/_conversion-review/triage/2026-05-14-dario-pulgar-conversion-qa.md`
- Triage summary: `research/_conversion-review/triage/2026-05-14-conversion-qa-batch-img-017-019-batch-pdf-042-044.md`
- Structured concern log: `research/_conversion-review/corrections/2026-05-14-dario-pulgar-conversion-corrections.md`
- Structured concern log: `research/_conversion-review/corrections/2026-05-14-batch-pdf-042-044-blockers.md`

## Priority Questions

- Should the new `SRC-05d0627a5861` Daniel Pulgar Arriagada draft be promoted after a quick human spot-check?
- Does 1888 birth entry 172 truly read `Fidelmiro Segundo Pulgar Arriagada`, and is the father correctly read as `Juan de Casanova Pulgar`?
- Is the 1959 I-94 traveler `Dario A. Pulgar` with birthdate candidate `1 Jun. 1902` a different person from `Dario Pulgar Smith`, whose 1964 tourist card preserves `Concepcion 1/6/42`?
- Can the 1964 tourist-card parentage field `DARIO Y DOROTHY` be corroborated with surname-bearing records before any parent links are promoted?
- For `batch-pdf-042`, is the raw source mislabeled, or were the wrong pages assembled into the converted output?

## Next Searches

- Review the staged passenger-list travel-group draft and confirm the ditto-mark-dependent residence and citizenship cells from the reread crop.
- Compare the 1888 and 1889 Los Angeles / La Laja birth entries against nearby Pulgar-Arriagada civil records for name consistency.
- Stage `SRC-07263f404e4c` / CV of Dario Arturo Pulgar after the current three draft reviews unless a higher-priority reread source is pushed first.
- Cross-check the I-94 against passport, visa, and travel records for an older `Dario A. Pulgar` before attaching it to any existing person page.
- Use the 1964 tourist card as identity-supporting evidence for `Dario Pulgar Smith`, but hold parent extraction until another record supplies surnames or matching household context.
- Confirm whether `batch-pdf-042` is a mislabeled source or a wrong page-range assembly before any source packet is opened.

## Sources To Find Or Review

- `SRC-5a5078ab4b0d` / Passenger List, Royal Mail Lines Limited, August 7, 1953
  - staged packet: `research/_staging/source-packets/src-5a5078ab4b0d-andes-passenger-list-pulgar-family.md`
  - staged claim: `research/_staging/claims/src-5a5078ab4b0d-andes-pulgar-family-travel-group.md`
- `SRC-aa0e304338ce` / Registro de Nacimientos, Los Angeles, Chile, 1888, Entry No. 172
  - staged packet: `research/_staging/source-packets/src-aa0e304338ce-entry-172-fidelmiro-segundo-pulgar-arriagada.md`
  - staged claim: `research/_staging/claims/src-aa0e304338ce-fidelmiro-segundo-pulgar-arriagada-birth-and-parentage.md`
- `SRC-05d0627a5861` / Registro de Nacimientos, Los Angeles, Chile, 1889, Certificate No. 513
  - staged packet: `research/_staging/source-packets/src-05d0627a5861-entry-513-daniel-pulgar-arriagada.md`
  - staged claim: `research/_staging/claims/src-05d0627a5861-daniel-pulgar-arriagada-birth-and-parentage.md`
- `SRC-07263f404e4c` / CV of Dario Arturo Pulgar
- `SRC-db3e1a4b1081` / Arrival-Departure Record, Form I-94 B, March 30, 1959
- `SRC-8dc32ecbbc69` / Ficha de turista, issued by the Brazilian Consulate on January 27, 1964
- `SRC-221159bd9b79` / Cámara de Senadores de la Nación, 1936
- `SRC-9010aa1ac68f` / S495-2-2
- `SRC-7e42bb85abe2` / S522bis-29-3

## Hypotheses To Test

- The I-94 belongs to an older Pulgar traveler and should not be merged with `Dario Pulgar Smith`.
- `Juan de Casanova Pulgar` may be an unusual but correct compound name; a local reread is still required before canonical promotion.
- The 1889 entry is extraction-ready as `Daniel Pulgar Arriagada`, provided the raw surname-first order is preserved in source notes.
- The 1953 passenger list is strong evidence for a travel group, but not by itself for a stronger kinship claim.
- The `batch-pdf-042` mismatch is a source-prep or page-association defect rather than a normal OCR drift issue.

## Negative Searches

- 2026-05-14: No cloud-visible staged drafts were available to review under `research/_staging/source-packets/`, `claims/`, `relationships/`, `identity/`, or `conflicts/` at the start of this pass on branch `codex/local-codex-conversion-workbench`.
- 2026-05-14: `research/index.md` showed an empty `## Staging` section and sampled source pages had empty `## Extracted Claims` tables before this staging pass.
- 2026-05-14: This QA pass did not find evidence strong enough to merge the 1959 I-94 traveler with `Dario Pulgar Smith`.
- 2026-05-14: No staged packet or claim draft was opened for `SRC-07263f404e4c` in this run; it remains the next clean high-value source.

## Lineage Goals

- Prevent premature merging of Pulgar individuals across the 1888, 1889, 1959, and 1964 records.
- Clear the two queued rereads before promoting the I-94 and 1888 birth entry into canonical claims or relationships.
- Keep `batch-pdf-042`, `batch-pdf-043`, and `batch-pdf-044` out of extraction until source identity and conversion completeness are repaired.

## Recently Promoted Findings

- 2026-05-14: The 1889 birth entry for Daniel Pulgar Arriagada is conversion-ready for extraction, provided the raw surname-first order is preserved as evidence language.
- 2026-05-14: The 1964 tourist card remains usable as source-context identity support for `Dario Pulgar Smith`, but not yet for parent-link promotion.
