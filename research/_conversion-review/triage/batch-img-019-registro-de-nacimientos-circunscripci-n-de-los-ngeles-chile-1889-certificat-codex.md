# Conversion QA Triage: batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat.codex

- Converted file: `raw/converted/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat.codex.md`
- Chunk manifest: `raw/chunks/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat-codex/manifest.json`
- Canonical context checked: `raw/converted/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex.md`
- Source reliability: high. This is an original civil birth-register image and is primary evidence for entry 513.
- Overall conversion confidence: high.
- Overall recommendation before evidence extraction: `pass`

## Page Summary

| Page | Chunk | Source reliability | Conversion confidence | Recommended action | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | `CHUNK-8ce1371a88d0-P0001-01` | high | high | `pass` | Entry 513 reads cleanly enough for extraction; only the official-signature line remains soft. |

## Concerns

### 1. Official signature is still slightly uncertain
- Page/chunk reference: Page 1, `raw/chunks/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat-codex/page-0001-chunk-01.md`
- Converted text: `Emilio Quiroga[?]`
- Why it looks odd: the final surname form is not perfectly clean in the conversion, but the uncertainty sits in a low-value signature field rather than the target birth data.
- Possible alternate reading: `Emilio Quiroga`
- Source reliability: high for the document overall.
- Conversion confidence: high for the record body, medium for the signature alone.
- Recommended action: `pass`

### 2. Neighboring entry 514 remains context only
- Page/chunk reference: Page 1, `raw/chunks/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat-codex/page-0001-chunk-01.md`
- Converted text: `Entry 514 begins below entry 513 but is not fully transcribed in this source-targeted pass.`
- Why it looks odd: this is not a conversion defect for entry 513, but it should be remembered if someone later tries to use entry 514 from the same page without a separate reread.
- Possible alternate reading: not applicable.
- Source reliability: high for entry 513; lower for neighboring context not fully converted.
- Conversion confidence: high for the target entry.
- Recommended action: `spot-check`

## QA Decision

Entry 513 is conversion-ready for evidence extraction. Keep the signature note as uncertainty, but it should not block claim drafting from the child, parent, informant, or date fields.