# Conversion QA Corrections - 2026-05-14

## Concern 1

- Source: `raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md`
- Page/chunk reference: `raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/page-0001-chunk-01.md`
- Converted text: `Birthdate: 1 Jun. 1902[?]`
- Why it looks odd: the current branch context already contains `Dario Pulgar Smith` with a 1964 tourist card preserving `Concepcion 1/6/42`. A 1902 birth year would place this I-94 traveler in a different generation.
- Possible alternate reading: the final digits may still need confirmation from the image; keep the year provisional until a visual reread resolves the field.
- Source reliability: High.
- Conversion confidence: Medium.
- Recommended action: `reread-region`

## Concern 2

- Source: `raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md`
- Page/chunk reference: `raw/chunks/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex/page-0001-chunk-01.md`
- Converted text: `Passport Number: 258 [adjacent handwritten note: 1/22[?]]` and `Visa Issued At: RIO[?]`
- Why it looks odd: both fields depend on small handwriting or abbreviated text in a noisy region; either could be over-read.
- Possible alternate reading: `RIO` may be correct, but the handwritten note after the passport number may be routing or detention notation rather than part of the passport field.
- Source reliability: High.
- Conversion confidence: Medium.
- Recommended action: `reread-region`

## Concern 3

- Source: `raw/converted/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964.codex.md`
- Page/chunk reference: `raw/chunks/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964-codex/page-0001-chunk-01.md`
- Converted text: `Filiação (Nome do Pai e da Mãe)  DARIO Y DOROTHY` and `Lugar e data de nascimento  Concepcion 1/6/42`
- Why it looks odd: the page mixes Portuguese printed labels with Spanish typed values and only gives the parents' forenames. That is enough for identity support but not enough for surname-level parent linkage or normalized date interpretation.
- Possible alternate reading: none proposed beyond keeping the raw date ordering and parent field literal until corroborated.
- Source reliability: High.
- Conversion confidence: Medium-high.
- Recommended action: `spot-check`

## Concern 4

- Source: `raw/converted/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex.md`
- Page/chunk reference: `raw/chunks/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-codex/page-0001-chunk-01.md`
- Converted text: `Nombre: Fidelmiro Segundo Pulgar Arriagada`
- Why it looks odd: `Fidelmiro` is unusual and the converted page itself flags this line as a high-priority reread target.
- Possible alternate reading: another near-form such as `Fidelino`, `Fidemiro`, or a similar given name remains possible until the source image is reread locally.
- Source reliability: High.
- Conversion confidence: Medium.
- Recommended action: `reread-region`

## Concern 5

- Source: `raw/converted/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex.md`
- Page/chunk reference: `raw/chunks/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-codex/page-0001-chunk-01.md`
- Converted text: `Nombre del padre: Juan de Casanova Pulgar`
- Why it looks odd: the compound phrase is unusual and would materially affect canonical identity work if wrong.
- Possible alternate reading: `Casanova` may be correct, but nearby letterforms could justify alternate readings such as `Casanoba` until a targeted reread settles the line.
- Source reliability: High.
- Conversion confidence: Medium.
- Recommended action: `reread-region`

## Concern 6

- Source: `raw/converted/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat.codex.md`
- Page/chunk reference: `raw/chunks/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat-codex/page-0001-chunk-01.md`
- Converted text: `Nombre: Pulgar Arriagada Daniel`
- Why it looks odd: the literal field appears surname-first, while the extracted genealogy leads normalize the child as `Daniel Pulgar Arriagada`.
- Possible alternate reading: the literal reading is likely already correct; the main requirement is to preserve the raw order in evidence notes while normalizing only in interpretation.
- Source reliability: High.
- Conversion confidence: High.
- Recommended action: `pass`