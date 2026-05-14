# Conversion QA Triage: batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex

- Converted file: `raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md`
- Chunk manifest: `raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/manifest.json`
- Canonical context checked: `wiki/people/dario-pulgar-smith.md`, `wiki/photos/PH001-dario-pulgar-smith-1964-tourist-card-portrait.md`, `raw/converted/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964.codex.md`, `raw/converted/batch-pdf-022-cv-of-dario-arturo-pulgar.codex.md`
- Source reliability: high for the original 1959 transit record and travel event; medium for self-reported biographic fields such as birth date and permanent address.
- Overall conversion confidence: medium.
- Overall recommendation before evidence extraction: `reread-region`

## Page Summary

| Page | Chunk | Source reliability | Conversion confidence | Recommended action | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | `CHUNK-2080170a5175-P0001-01` | high / medium-by-field | medium | `reread-region` | Birth year likely needs visual confirmation; smaller address and visa fields remain soft. |

## Concerns

### 1. Birthdate field conflicts with stronger family context
- Page/chunk reference: Page 1, `raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/page-0001-chunk-01.md`
- Converted text: `Birthdate: 1 Jun. 1902[?]`
- Why it looks odd: the tourist card and CV context point to a 1942 birth cohort for the Dario Pulgar Smith / Dario Arturo Pulgar line. `1902` would make the page-9 education chronology in the CV implausible for the same person.
- Possible alternate reading: `1 Jun. 1942`
- Source reliability: medium for this field because the I-94 is original, but the birth field is still typed or written from traveler-supplied data.
- Conversion confidence: medium.
- Recommended action: `reread-region`

### 2. Permanent address and visa-issue lines stay soft
- Page/chunk reference: Page 1, `raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/page-0001-chunk-01.md`
- Converted text: `Permanent Address: Box 1244 Concepcion[?] Chile` and `Visa Issued At: RIO[?]`
- Why it looks odd: both fields are small and already marked uncertain in the conversion. They are useful leads, but not yet clean enough for direct canonical extraction.
- Possible alternate reading: `Concepción`; `Rio`
- Source reliability: high for travel-document context, medium for the exact place strings.
- Conversion confidence: medium.
- Recommended action: `spot-check`

### 3. Marginal handwriting is present but not decision-grade
- Page/chunk reference: Page 1, `raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/page-0001-chunk-01.md`
- Converted text: `Passport Number: 258 [adjacent handwritten note: 1/22[?]]` and `Carrier directed ... [signature/route notation illegible]`
- Why it looks odd: the tiny marginal note and lower-right route notation are not safely read, but they also do not look central to the family-history extraction target.
- Possible alternate reading: none beyond the current partial read.
- Source reliability: low for genealogy use; high only as document-handling context.
- Conversion confidence: low for the marginal handwriting itself.
- Recommended action: `pass`

## QA Decision

Do not extract a normalized birth date from this source until the birthdate region is reread against the raw image. The travel event itself is usable, but the biographic fields should stay provisional.