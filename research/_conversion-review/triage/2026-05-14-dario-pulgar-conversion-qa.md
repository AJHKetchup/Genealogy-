# Conversion QA Triage - 2026-05-14

## Scope

- Branch audited: `codex/local-codex-conversion-workbench`
- Source inventory basis: `raw/source-prep-manifest.json` created `2026-05-14`
- Reviewed converted and chunked sources in the current Dario/Pulgar evidence lane.
- Sampled chunk manifests for the reviewed sources were created `2026-05-13`; the source-prep inventory was refreshed `2026-05-14`.

## Sources Triaged

| Source | Reliability | Conversion confidence | Recommended action |
| --- | --- | --- | --- |
| `raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md` | High for direct travel facts, but identity linkage needs caution | Medium | `reread-region` |
| `raw/converted/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964.codex.md` | High for named cardholder and travel-card fields | Medium-high | `spot-check` |
| `raw/converted/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex.md` | High as a civil birth register | Medium | `reread-region` |
| `raw/converted/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat.codex.md` | High as a civil birth register | High | `pass` |

## Reliability Notes

- All four sources are administrative records and are likely reliable for the facts they directly record.
- Source reliability is separate from conversion confidence. The risk here is not fabricated provenance; it is misreading handwriting, mixed-language date fields, and unusual personal names.
- Current canonical context on this branch is thin: `wiki/index.md` only links a minimal `[[people/dario-pulgar-smith]]` stub plus the 1964 photo references. That makes identity drift a real extraction risk.

## Key Findings

- The 1959 I-94 reads as `DARIO A. PULGAR` with a birthdate candidate `1 Jun. 1902[?]`. That does not fit the existing `Dario Pulgar Smith` tourist-card context, which preserves `Concepcion 1/6/42`. Treat these as distinct people until a human reread confirms the I-94 digits and name context.
- The 1964 Brazilian tourist card is strong enough to keep as a confirmed source-context reference for `Dario Pulgar Smith`, but its parentage field only gives the forenames `DARIO Y DOROTHY`. That is not enough for surname-level parent links without corroboration.
- The 1888 birth entry is useful but still risky at the most important extraction points: the child's given name `Fidelmiro` and the father's full name `Juan de Casanova Pulgar` both deserve a targeted visual reread before canonical promotion.
- The 1889 birth entry for Daniel Pulgar Arriagada is structurally clean and internally consistent. The only low-priority uncertainty is the official signature, which is not genealogically central.

## Output Files

- Corrections log: `research/_conversion-review/corrections/2026-05-14-dario-pulgar-conversion-corrections.md`
- Visual reread queue: `research/_conversion-review/page-queues/2026-05-14-dario-pulgar-reread-queue.md`
- Research-plan follow-up: `research/research-plan.md`

## Concise Report

- Sources triaged: I-94 arrival record, 1964 tourist card, 1888 Los Angeles birth entry 172, 1889 Los Angeles birth entry 513.
- Pages or regions queued: I-94 page 1 identity/travel fields; 1888 birth entry 172 name and father fields.
- Suspected readings: `1 Jun. 1902[?]`, `RIO[?]`, `Fidelmiro`, `Juan de Casanova Pulgar`, raw-order `Pulgar Arriagada Daniel`.
- Confusing sections: mixed Portuguese/Spanish date conventions on the tourist card; surname-first naming on the 1889 register; unusual compound naming in the 1888 register.
- Low-priority sources: the 1889 entry is acceptable for extraction after preserving raw name order; the tourist card only needs a spot-check if parent or signature detail is promoted.
- Blockers for human review: avoid merging `Dario Pulgar Smith` with the older `Dario A. Pulgar` I-94 traveler until the birth year and identity fields are visually reread.