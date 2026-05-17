---
type: source_prep_chunk
chunk_id: CHUNK-c7ef9fee7a24-P0001-06
source_converted: raw/converted/ca221159bd-c-mara-de-senadores-de-l-p0084-0103-c-mara-de-senadores-de-la-naci-n-1936-pages-84-103.codex.md
converted_sha256: c7ef9fee7a244fb1e39c70a343a2f2dd81ccafacc874b9823d06fb4067ec0b61
source: raw/sources/Cámara de Senadores de la Nación, 1936.pdf
source_sha256: 221159bd9b79619cfbcad6b7d590f4fd91fff0a92ecd40b9972437ea865bb289
source_manifest: raw/codex-conversion-jobs/ca221159bd-c-mara-de-senadores-de-l-p0084-0103-c-mara-de-senadores-de-la-naci-n-1936-pages-84-103/manifest.json
page_start: 1
page_end: 1
part: 6
---

## Images, Captions, And Visual Notes

Pipeline-extracted visual crops:
- ![source-caption: a) Peligro. — El brazo en posición ho- rizontal o luz roja, obliga a parar.](../extracted-images/page-0103/page-0103-image-01-railway-signal-danger.png)
  - Kind: diagram; label basis: source-caption; bbox_pct: [20.0, 24.0, 30.0, 46.0]
  - Source context: Railway signal diagram for 'Peligro'
- ![source-caption: b) Precaución. — El brazo formando un ángulo de 45º hacia arriba de la ho- rizontal o luz anaranjada, indica que el conductor del tren debe preparar- se para poder parar en la próxima señal, que en este caso puede estar a peligro.](../extracted-images/page-0103/page-0103-image-02-railway-signal-caution.png)
  - Kind: diagram; label basis: source-caption; bbox_pct: [35.0, 24.0, 45.0, 46.0]
  - Source context: Railway signal diagram for 'Precaución'
- ![source-caption: c) Vía libre. — El brazo formando un ángulo de 90º hacia arriba de la ho- rizontal o luz verde, significa que la próxima señal indica precaución o vía libre; puede ser pasada por lo tanto, sin reducir la velocidad regla- mentaria.](../extracted-images/page-0103/page-0103-image-03-railway-signal-clear-track.png)
  - Kind: diagram; label basis: source-caption; bbox_pct: [50.0, 24.0, 60.0, 46.0]
  - Source context: Railway signal diagram for 'Vía libre'

The page features three diagrams illustrating railway signals, each with a corresponding caption.

1.  **Signal a)**: A diagram showing a railway signal arm in a horizontal position, colored red and white, with a red light visible. The caption describes this as a "Peligro" (Danger) signal.
2.  **Signal b)**: A diagram showing a railway signal arm angled 45 degrees upwards from horizontal, colored red and white, with an orange light visible. The caption describes this as a "Precaución" (Caution) signal.
3.  **Signal c)**: A diagram showing a railway signal arm angled 90 degrees upwards (vertical), colored red and white, with a green light visible. The caption describes this as a "Vía libre" (Clear track) signal.

## Uncertain Or Illegible
None.

## Completeness Audit
All text and visual elements on the page have been transcribed and described.

## Visual Region Manifest
```json
{
  "visual_regions": [
    {
      "region_id": "vr_1",
      "kind": "diagram",
      "bbox_pct": [
        20.0,
        24.0,
        30.0,
        46.0
      ],
      "caption_literal": "a) Peligro. — El brazo en posición ho- rizontal o luz roja, obliga a parar.",
      "caption_type": "source-caption",
      "identity_basis": null,
      "source_context": "Railway signal diagram for 'Peligro'",
      "confidence": 1.0,
      "suggested_filename": "railway_signal_danger"
    },
    {
      "region_id": "vr_2",
      "kind": "diagram",
      "bbox_pct": [
        35.0,
        24.0,
        45.0,
        46.0
      ],
      "caption_literal": "b) Precaución. — El brazo formando un ángulo de 45º hacia arriba de la ho- rizontal o luz anaranjada, indica que el conductor del tren debe preparar- se para poder parar en la próxima señal, que en este caso puede estar a peligro.",
      "caption_type": "source-caption",
      "identity_basis": null,
      "source_context": "Railway signal diagram for 'Precaución'",
      "confidence": 1.0,
      "suggested_filename": "railway_signal_caution"
    },
    {
      "region_id": "vr_3",
      "kind": "diagram",
      "bbox_pct": [
        50.0,
        24.0,
        60.0,
        46.0
      ],
      "caption_literal": "c) Vía libre. — El brazo formando un ángulo de 90º hacia arriba de la ho- rizontal o luz verde, significa que la próxima señal indica precaución o vía libre; puede ser pasada por lo tanto, sin reducir la velocidad regla- mentaria.",
      "caption_type": "source-caption",
      "identity_basis": null,
      "source_context": "Railway signal diagram for 'Vía libre'",
      "confidence": 1.0,
      "suggested_filename": "railway_signal_clear_track"
    }
  ]
}
```
