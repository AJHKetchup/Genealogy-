# Conversion QA Triage, 2026-05-14

Role: `conversion_qa_reviewer`

Branch context: `codex/local-codex-conversion-workbench`

Scope: newly converted and newly chunked Pulgar-focused sources reviewed before evidence extraction.

## Sources Triaged

| Source | Chunk / page reference | Source reliability | Conversion confidence | Recommended action | Notes |
| --- | --- | --- | --- | --- | --- |
| `raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md` | `raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/page-0001-chunk-01.md` | High. U.S. immigration form with structured fields and arrival stamp. | Medium. Main typed fields look strong, but several handwritten or faint fields remain uncertain. | `spot-check` | Identity drift risk is higher than source unreliability risk: this may be Dario Arturo Pulgar rather than Dario Pulgar Smith. |
| `raw/converted/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964.codex.md` | `raw/chunks/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964-codex/page-0001-chunk-01.md` | High. Official travel/consular form with attached portrait and date stamp. | High-medium. The conversion preserves uncertainty around signature and stamp drift but the core identity fields read coherently. | `pass` | Already aligned with the existing confirmed portrait context for Dario Pulgar Smith. |
| `raw/converted/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex.md` | `raw/chunks/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-codex/page-0001-chunk-01.md` | High. Civil birth register page with date, parents, residence, and official signature area. | Medium. The targeted entry is coherent, but two key name fields still look suspicious enough to block extraction. | `reread-region` | The converted text explicitly flags rereads, and the odd name phrases are genealogically central. |
| `raw/converted/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat.codex.md` | `raw/chunks/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat-codex/page-0001-chunk-01.md` | High. Civil birth register page with clear parental and informant fields. | High. Only the official signature remains soft, and that does not affect the main family facts. | `pass` | Good candidate for later Pulgar-Arriagada extraction after the 1888 record is stabilized. |

## Concerns And Suspected Readings

### `batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959`

- Converted text: `Birthdate: 1 Jun. 1902[?]`
- Reference: `page-0001-chunk-01`, literal transcription and uncertainty sections.
- Why it looks odd: the year is faint and identity linkage becomes materially different depending on whether the record belongs to an older Dario Pulgar or to the younger Dario Pulgar Smith already represented in the wiki.
- Possible alternate reading: the day and month look stable, but the year should be treated as unresolved until visually spot-checked.
- Source reliability: high.
- Conversion confidence: medium.
- Recommended action: `spot-check`

- Converted text: `Visa Issued At: RIO[?]`
- Reference: `page-0001-chunk-01`, literal transcription and uncertainty sections.
- Why it looks odd: the field is short, faint, and easy to over-normalize; it may matter for travel reconstruction.
- Possible alternate reading: `RIO` is plausible but not firm enough for canonical promotion.
- Source reliability: high.
- Conversion confidence: medium.
- Recommended action: `spot-check`

### `batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964`

- Converted text: `Lugar e data de nascimento  Concepcion 1/6/42`
- Reference: `page-0001-chunk-01`, literal transcription and interpretation sections.
- Why it looks odd: the source mixes Portuguese printed labels with Spanish typed content, so date normalization could drift if someone assumes a U.S. ordering.
- Possible alternate reading: no alternate text reading proposed; only the normalized date order needs caution.
- Source reliability: high.
- Conversion confidence: high-medium.
- Recommended action: `pass`

- Converted text: `Filiação (Nome do Pai e da Mãe)  DARIO Y DOROTHY`
- Reference: `page-0001-chunk-01`, literal transcription and uncertainty sections.
- Why it looks odd: the field preserves only given names, so downstream extraction should not silently invent surnames.
- Possible alternate reading: none; the concern is interpretation scope, not transcription failure.
- Source reliability: high.
- Conversion confidence: high-medium.
- Recommended action: `pass`

### `batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no`

- Converted text: `Nombre: Fidelmiro Segundo Pulgar Arriagada`
- Reference: `page-0001-chunk-01`, focused transcription of entry 172.
- Why it looks odd: `Fidelmiro` is unusual, and the same conversion already notes a post-conversion reread. This is a high-impact field for later person creation.
- Possible alternate reading: `Fidelino`, `Fideligno`, or another similar name-form remain plausible enough that the image region should be checked locally before extraction.
- Source reliability: high.
- Conversion confidence: medium.
- Recommended action: `reread-region`

- Converted text: `Nombre del padre: Juan de Casanova Pulgar`
- Reference: `page-0001-chunk-01`, focused transcription of entry 172.
- Why it looks odd: `de Casanova` reads like an unusual middle-name or compound-surname phrase in this context and could be a conversion drift from a more familiar given-name sequence.
- Possible alternate reading: the final word `Pulgar` looks stable, but the middle phrase should be treated as unresolved until the original region is reread.
- Source reliability: high.
- Conversion confidence: medium.
- Recommended action: `reread-region`

### `batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat`

- Converted text: `Nombre: Pulgar Arriagada Daniel`
- Reference: `page-0001-chunk-01`, entry 513 transcription.
- Why it looks odd: the child name may be in register order rather than modern display order, so downstream extraction should preserve the literal order and normalize only in interpretation.
- Possible alternate reading: interpretation should likely surface `Daniel Pulgar Arriagada`, but the literal transcription is coherent as written.
- Source reliability: high.
- Conversion confidence: high.
- Recommended action: `pass`

- Converted text: `Firma del oficial: Emilio Quiroga[?]`
- Reference: `page-0001-chunk-01`, entry 513 transcription.
- Why it looks odd: the surname ending is soft, but the field is not central to the family facts.
- Possible alternate reading: none needed for claim gating.
- Source reliability: high.
- Conversion confidence: high.
- Recommended action: `pass`

## Confusing Sections

- `batch-img-010` has an identity-link ambiguity rather than a raw-transcription collapse. The form is probably good enough to preserve, but extraction should not merge it into the Dario Pulgar Smith stub without a generational check.
- `batch-img-015` is internally coherent but multilingual. The typed Spanish month names and Portuguese labels should stay literal until normalized in a claim layer.
- `batch-img-017` is the only reviewed source in this pass with a central name-reading blocker.

## Low-Priority Converted Sources Deferred This Pass

- `raw/converted/batch-pdf-041-r3016-11a-2905-950.codex.md`
- `raw/converted/batch-pdf-042-c-mara-de-senadores-de-la-naci-n-1936-pages-1-5.codex.md`
- `raw/converted/batch-pdf-043-s495-2-2.codex.md`
- `raw/converted/batch-pdf-044-s522bis-29-3.codex.md`

Reason: they appear to be newly converted in the source-prep manifest, but they were not the best first QA targets for current canonical context, which is still centered on Dario Pulgar Smith and closely related Pulgar family records.

## Human Review Blockers

- Do not promote claims from `batch-img-017` until the target-entry name region is reread locally against the raw page image.
- Treat `batch-img-010` as a likely older Dario Pulgar record until corroborating sources settle the identity.
