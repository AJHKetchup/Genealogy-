# Conversion QA Triage: batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964.codex

- Converted file: `raw/converted/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964.codex.md`
- Chunk manifest: `raw/chunks/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964-codex/manifest.json`
- Canonical context checked: `wiki/people/dario-pulgar-smith.md`, `wiki/photos/PH001-dario-pulgar-smith-1964-tourist-card-portrait.md`, `raw/converted/batch-pdf-022-cv-of-dario-arturo-pulgar.codex.md`
- Source reliability: high for the original tourist card, attached portrait, and Brazil-related travel-document context; medium for self-reported birth and parent fields.
- Overall conversion confidence: medium-high.
- Overall recommendation before evidence extraction: `reread-region`

## Page Summary

| Page | Chunk | Source reliability | Conversion confidence | Recommended action | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | `CHUNK-9ef93c009e47-P0001-01` | high / medium-by-field | medium-high | `reread-region` | The literal read is strong, but date-format ambiguity matters before normalization. |

## Concerns

### 1. Birth field is legible, but the normalized date order is still ambiguous
- Page/chunk reference: Page 1, `raw/chunks/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964-codex/page-0001-chunk-01.md`
- Converted text: `Lugar e data de nascimento  Concepcion 1/6/42`
- Why it looks odd: the printed form is Portuguese, while several typed field values are Spanish. The literal slash date is clear enough, but the day/month interpretation should not be normalized without a visual confirmation pass.
- Possible alternate reading: no safer literal alternate than `1/6/42`; normalized interpretations could be `1 June 1942` or `6 January 1942`.
- Source reliability: medium for this field because the card is original but the biographic entry is still self-reported or clerk-entered.
- Conversion confidence: medium-high on the literal string, lower on normalization.
- Recommended action: `reread-region`

### 2. Passport issue date has the same day/month ambiguity
- Page/chunk reference: Page 1, `raw/chunks/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964-codex/page-0001-chunk-01.md`
- Converted text: `Passaporte N.º 214 ... na data 3/9/63`
- Why it looks odd: nothing is obviously garbled, but the slash date will be misused if it is normalized without checking the local image and cross-source date conventions.
- Possible alternate reading: no safer literal alternate than `3/9/63`; normalized interpretations could be `3 September 1963` or `9 March 1963`.
- Source reliability: high for passport-document context, medium for later normalized claim use.
- Conversion confidence: medium-high on the literal string.
- Recommended action: `reread-region`

### 3. Stamp and signature regions remain partially unreadable
- Page/chunk reference: Page 1, `raw/chunks/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964-codex/page-0001-chunk-01.md`
- Converted text: `PANSA`; `27 JAN 64`; `[signature]`; `[partly obscured rectangular stamp ...]`
- Why it looks odd: the main document text is usable, but the right-side stamp panel and holder signature were honestly left partial.
- Possible alternate reading: none beyond the current partial read.
- Source reliability: high for document-context use, low for exact signature reading.
- Conversion confidence: medium for the stamp panel, low for the signature.
- Recommended action: `spot-check`

## Reliability Notes

The parentage line `DARIO Y DOROTHY` looks like a source limitation rather than a conversion failure. Treat it as given-name-only evidence unless another source supplies the full parental names.

## QA Decision

The page is good enough to keep as a high-value travel/identity source, but the birth-date and passport-date regions should be reread locally before normalizing dates into claims.