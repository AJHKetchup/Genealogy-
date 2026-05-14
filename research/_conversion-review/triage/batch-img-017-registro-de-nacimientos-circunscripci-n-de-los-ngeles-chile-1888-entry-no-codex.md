# Conversion QA Triage: batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex

- Converted file: `raw/converted/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex.md`
- Chunk manifest: `raw/chunks/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-codex/manifest.json`
- Canonical context checked: `wiki/people/dario-pulgar-smith.md`, `raw/converted/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat.codex.md`
- Source reliability: high. This is an original civil birth-register image and is primary evidence for the target birth entry.
- Overall conversion confidence: medium-high.
- Overall recommendation before evidence extraction: `reread-region`

## Page Summary

| Page | Chunk | Source reliability | Conversion confidence | Recommended action | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | `CHUNK-8276d0c44e96-P0001-01` | high | medium-high | `reread-region` | Target entry is strong overall, but the child and father name lines should be confirmed before promotion. |

## Concerns

### 1. Child given name is plausible but still high-value enough to verify
- Page/chunk reference: Page 1, `raw/chunks/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-codex/page-0001-chunk-01.md`
- Converted text: `Nombre: Fidelmiro Segundo Pulgar Arriagada`
- Why it looks odd: `Fidelmiro` is uncommon, and the conversion itself notes earlier uncertainty plus reliance on enhanced review crops.
- Possible alternate reading: no safer alternate than the current `Fidelmiro`; another `Fidel-` form remains possible until a local reread confirms it.
- Source reliability: high.
- Conversion confidence: medium.
- Recommended action: `reread-region`

### 2. Father's full name may be correct, but the phrasing is unusual enough to hold
- Page/chunk reference: Page 1, `raw/chunks/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-codex/page-0001-chunk-01.md`
- Converted text: `Nombre del padre: Juan de Casanova Pulgar`
- Why it looks odd: the phrase could be a correct compound name, but it is unusual enough that a line-level reread is justified before canonical use.
- Possible alternate reading: no safer literal alternate; the open question is whether the segmentation or one word form shifts under closer visual review.
- Source reliability: high.
- Conversion confidence: medium.
- Recommended action: `reread-region`

### 3. Neighboring entries are visible but intentionally left contextual
- Page/chunk reference: Page 1, `raw/chunks/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-codex/page-0001-chunk-01.md`
- Converted text: `Entry 171 ... not fully transcribed`; `Entry 173 ... partly cut`; `Entries 174-176 ... not fully transcribed`
- Why it looks odd: this is not a target-entry failure, but it is a confusing section if a later extraction pass assumes the entire spread was fully converted.
- Possible alternate reading: not applicable.
- Source reliability: high for the target entry, lower for non-target neighboring context because it was not fully converted.
- Conversion confidence: high for the decision to scope only entry 172; low for any use of neighboring entries.
- Recommended action: `spot-check`

## QA Decision

Hold the exact child-name and father-name lines behind a local reread. The page is otherwise a strong primary record and should remain near the front of the extraction queue once those two regions are confirmed.