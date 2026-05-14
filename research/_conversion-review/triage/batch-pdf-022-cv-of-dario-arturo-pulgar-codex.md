# Conversion QA Triage: batch-pdf-022-cv-of-dario-arturo-pulgar.codex

- Converted file: `raw/converted/batch-pdf-022-cv-of-dario-arturo-pulgar.codex.md`
- Chunk manifest: `raw/chunks/batch-pdf-022-cv-of-dario-arturo-pulgar-codex/manifest.json`
- Canonical context checked: `wiki/people/dario-pulgar-smith.md`, `wiki/photos/PH001-dario-pulgar-smith-1964-tourist-card-portrait.md`, `raw/converted/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964.codex.md`, `raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md`
- Source reliability: medium for retrospective identity naming and chronology because this is an authored CV; high for self-reported career and education structure as a contextual source.
- Overall conversion confidence: high.
- Overall recommendation before evidence extraction: `pass` for conversion quality, with `hold-for-human` on identity merge decisions.

## Page Summary

| Page | Chunk | Source reliability | Conversion confidence | Recommended action | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | `CHUNK-3ea42804b71d-P0001-01` | medium | high | `hold-for-human` | Header names `DARIO PULGAR` while the current canonical stub is `Dario Pulgar Smith`. |
| 2 | `CHUNK-3ea42804b71d-P0002-01` | medium | high | `pass` | No material conversion concern. |
| 3 | `CHUNK-3ea42804b71d-P0003-01` | medium | high | `pass` | No material conversion concern. |
| 4 | `CHUNK-3ea42804b71d-P0004-01` | medium | high | `pass` | No material conversion concern. |
| 5 | `CHUNK-3ea42804b71d-P0005-01` | medium | high | `pass` | No material conversion concern. |
| 6 | `CHUNK-3ea42804b71d-P0006-01` | medium | high | `pass` | No material conversion concern. |
| 7 | `CHUNK-3ea42804b71d-P0007-01` | medium | high | `pass` | No material conversion concern. |
| 8 | `CHUNK-3ea42804b71d-P0008-01` | medium | high | `pass` | Only source-side punctuation oddities. |
| 9 | `CHUNK-3ea42804b71d-P0009-01` | medium | high | `pass` | Education chronology is clean and useful as a conflict-check source. |

## Concerns

### 1. Name drift across sources is a proof-review issue, not a conversion failure
- Page/chunk reference: Page 1, `raw/chunks/batch-pdf-022-cv-of-dario-arturo-pulgar-codex/page-0001-chunk-01.md`
- Converted text: `CV of Dario Arturo Pulgar` and `DARIO PULGAR`
- Why it looks odd: the current canonical photo-backed person page is `Dario Pulgar Smith`. This CV omits `Smith` and uses `Arturo`, so it creates merge risk even though the broader chronology may align.
- Possible alternate reading: none; this looks like a source-side name variant rather than a conversion error.
- Source reliability: medium for identity naming.
- Conversion confidence: high.
- Recommended action: `hold-for-human`

### 2. Education chronology is internally clean and useful as a comparator
- Page/chunk reference: Page 9, `raw/chunks/batch-pdf-022-cv-of-dario-arturo-pulgar-codex/page-0009-chunk-01.md`
- Converted text: `1954 - 1959 ... Liceo Enrique Molina`; `1960 - 1963 ... Escuela de Derecho`; `1963 - 1966 ... Escuela de Periodismo`; `1967 - 1968 ... Stanford University`
- Why it looks odd: not odd internally. It matters because it pressures the I-94 `1902` birth-year reading and suggests that cross-source identity review should happen before any person merge.
- Possible alternate reading: none.
- Source reliability: medium.
- Conversion confidence: high.
- Recommended action: `pass`

### 3. Page-8 punctuation oddities appear source-side
- Page/chunk reference: Page 8, `raw/chunks/batch-pdf-022-cv-of-dario-arturo-pulgar-codex/page-0008-chunk-01.md`
- Converted text: `"La Colonia Penal"",` and the visible sentence break ambiguity in the NFB section.
- Why it looks odd: these look like source punctuation or layout quirks, not OCR corruption that would block evidence extraction.
- Possible alternate reading: none needed for genealogy extraction.
- Source reliability: medium.
- Conversion confidence: high.
- Recommended action: `pass`

## QA Decision

The CV conversion is safe for staged extraction as a contextual source. Keep the identity merge itself behind human review, because the name form differs from the current canonical stub.