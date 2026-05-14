# Visual Extraction Contract

Every source-prep conversion must preserve meaningful visual evidence as separate crop assets. This applies even when the entire source is already an image scan.

## Required Crop Targets

Crop these when visible:

- portraits and headshots
- group photos, or individual faces within a group when practical
- signatures
- seals, stamps, embossed marks, watermarks, and labels
- maps, diagrams, charts, and tables that are more legible as image evidence
- photographs or illustrations embedded in newspapers, cards, albums, certificates, passports, visas, IDs, and forms

## Naming

Use stable page-local names:

- `page-0001-image-01-portrait.png`
- `page-0001-image-02-stamp-panel.png`
- `page-0001-image-03-signature.png`

Use a descriptive suffix when possible. Keep references inline in the page Markdown near the relevant transcription or visual notes.

## Source-Context Person Tags

If the source itself identifies the person shown, record the identity in the page's `Images, Captions, And Visual Notes` and `Extracted Genealogy Leads` sections.

Accepted source-context examples:

- named passport page with attached passport photo
- identity card or tourist card naming the holder and containing one attached portrait
- labeled portrait caption
- group photo caption that maps names to people or positions
- newspaper image caption naming the person pictured

Do not name an unlabeled person from appearance alone in the source-prep conversion. Preserve the crop and source context so later review or external tooling can work with it.

## Current Example

The 1964 Brazilian tourist card conversion cropped:

- portrait: `raw/codex-conversion-jobs/batch-img-015-ficha-de-turista-issued-by-the-brazilian-consulate-on-january-27-1964/extracted-images/page-0001/page-0001-image-01-portrait.png`
- stamp panel
- holder signature

Because the card names the holder as `DARIO PULGAR SMITH`, the portrait is indexed as source-context confirmed in `research/_indexes/face-reference-index.json`.
