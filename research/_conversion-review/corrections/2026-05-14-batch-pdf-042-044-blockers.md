# Conversion Correction Notes - 2026-05-14

## `batch-pdf-042-c-mara-de-senadores-de-la-naci-n-1936-pages-1-5`

- Problem type: Source identity / assembly blocker
- Observed issue: The converted artifact title says `Cámara de Senadores de la Nación, 1936 pages 1-5`, but `Page 5` reads `LEY Y REGLAMENTO GENERAL DE LOS FERROCARRILES NACIONALES`.
- Assessment: This does not look like a simple OCR defect. It looks like a mislabeled raw source, a wrong page-range selection, or a bad conversion-job association.
- Action: `hold-for-human`

## `batch-pdf-043-s495-2-2`

- Problem type: Conversion failure
- Observed issue: The converted Markdown artifact is empty.
- Assessment: Likely failed chunk assembly, failed write, or incomplete conversion handoff.
- Action: `rerun-conversion`

## `batch-pdf-044-s522bis-29-3`

- Problem type: Conversion failure
- Observed issue: The converted Markdown artifact is empty.
- Assessment: Likely failed chunk assembly, failed write, or incomplete conversion handoff.
- Action: `rerun-conversion`