---
type: source_prep_chunk
chunk_id: CHUNK-3b1fe2b66094-P0063-02
source_converted: raw/converted/ca9010aa1a-s495-2-2-p0051-0075-s495-2-2-pages-51-75.codex.md
converted_sha256: 3b1fe2b660943006c3c2c70da6491cf292e56f36af3c61a77ed14210d1c9e31e
source: raw/sources/S495-2-2.pdf
source_sha256: 9010aa1ac68f01250159adf718dfa284b342139e36030310abc1521c797ea027
source_manifest: raw/codex-conversion-jobs/ca9010aa1a-s495-2-2-p0051-0075-s495-2-2-pages-51-75/manifest.json
page_start: 63
page_end: 63
part: 2
---

## Images, Captions, And Visual Notes
Pipeline-extracted visual crops:
- ![converter-description: Image embedded in the right column, illustrating the article about traffic in Mexico City.](../extracted-images/page-0064/page-0064-image-01-street-scene-cars-pedestrians-buildings.png)
  - Kind: photograph; label basis: converter-description; bbox_pct: [36.4, 13.7, 85.5, 36.7]
  - Source context: Image embedded in the right column, illustrating the article about traffic in Mexico City.
- ![converter-description: Image embedded in the left column, illustrating the article about traffic in Mexico City. The caption below Image 3 refers to 'two aspects of traffic' which might include this image.](../extracted-images/page-0064/page-0064-image-02-street-scene-carriages-automobiles-pedestrians.png)
  - Kind: photograph; label basis: converter-description; bbox_pct: [10.3, 30.4, 35.2, 55.7]
  - Source context: Image embedded in the left column, illustrating the article about traffic in Mexico City. The caption below Image 3 refers to 'two aspects of traffic' which might include this image.
- ![source-caption: Dos aspectos del tráfico en la ciudad antes
de que usaran los nuevos semáforos.—El
del cruce de las calles 16 de septiembre y
5 de Febrero, en donde se ha estado pro-
bando el nuevo semáforo, el cual ha da-
do muy buenos resultados para la nor-
malización del tráfico.](../extracted-images/page-0064/page-0064-image-03-street-corner-pedestrians-signs-5-de-febrero.png)
  - Kind: photograph; label basis: source-caption; bbox_pct: [10.3, 56.5, 35.2, 84.4]
  - Source context: Image embedded in the left column, below Image 2. The caption describes 'two aspects of traffic' and specifically mentions the intersection of 16 de septiembre and 5 de Febrero.

- **Visual Note 1**: In the top right corner, there is a stylized, handwritten-like text that reads "Universal Ilustrado". This appears to be a masthead or publication stamp.
- **Image 1**: A street scene depicting cars, pedestrians, and buildings. The image is placed in the upper right portion of the page, within the right column of text.
- **Image 2**: A street scene showing horse-drawn carriages, early automobiles, and pedestrians. This image is located in the middle of the left column.
- **Image 3**: A street corner with several pedestrians and a building featuring signs. One visible sign reads "ALTO ADELANTE 5 DE FEBRERO Y SEPTIEMBRE" and "PEATONES". This image is located in the lower left portion of the page, below Image 2.
- **Caption for Image 3**: The text below Image 3 describes "Dos aspectos del tráfico", referring to the traffic conditions before new traffic lights were used, specifically mentioning the intersection of 16 de septiembre and 5 de Febrero where a new traffic light was tested. While placed under Image 3, the caption's reference to "two aspects" suggests it might relate to both Image 2 and Image 3, which depict street scenes.

## Uncertain Or Illegible
None.

## Completeness Audit
All visible text and meaningful visual elements on the page have been transcribed or described. The layout, including columns and embedded images, has been preserved in the reading order.

## Visual Region Manifest
```json
{
  "visual_regions": [
    {
      "region_id": "region_0",
      "kind": "photograph",
      "bbox_pct": [
        36.4,
        13.7,
        85.5,
        36.7
      ],
      "caption_literal": null,
      "caption_type": "converter-description",
      "identity_basis": null,
      "source_context": "Image embedded in the right column, illustrating the article about traffic in Mexico City.",
      "confidence": 0.95,
      "suggested_filename": "street_scene_cars_pedestrians_buildings.png",
      "inline_anchor": "capital, por la buena voluntad del señor\ningeniero Luis G. Margain, que se preo-\ncupa del adelanto y de que por ningún mo-\ntivo se estanque el tráfico citadino."
    },
    {
      "region_id": "region_1",
      "kind": "photograph",
      "bbox_pct": [
        10.3,
        30.4,
        35.2,
        55.7
      ],
      "caption_literal": null,
      "caption_type": "converter-description",
      "identity_basis": null,
      "source_context": "Image embedded in the left column, illustrating the article about traffic in Mexico City. The caption below Image 3 refers to 'two aspects of traffic' which might include this image.",
      "confidence": 0.95,
      "suggested_filename": "street_scene_carriages_automobiles_pedestrians.png",
      "inline_anchor": "to y mejoría. Es también a él que se de-"
    },
    {
      "region_id": "region_2",
      "kind": "photograph",
      "bbox_pct": [
        10.3,
        56.5,
        35.2,
        84.4
      ],
      "caption_literal": "Dos aspectos del tráfico en la ciudad antes\nde que usaran los nuevos semáforos.—El\ndel cruce de las calles 16 de septiembre y\n5 de Febrero, en donde se ha estado pro-\nbando el nuevo semáforo, el cual ha da-\ndo muy buenos resultados para la nor-\nmalización del tráfico.",
      "caption_type": "source-caption",
      "identity_basis": null,
      "source_context": "Image embedded in the left column, below Image 2. The caption describes 'two aspects of traffic' and specifically mentions the intersection of 16 de septiembre and 5 de Febrero.",
      "confidence": 0.95,
      "suggested_filename": "street_corner_pedestrians_signs_5_de_febrero.png",
      "inline_anchor": "malización del tráfico."
    }
  ]
}
```
