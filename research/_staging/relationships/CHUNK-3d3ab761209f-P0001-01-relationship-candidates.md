---
type: relationship_candidate_overview
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
chunk_id: CHUNK-3d3ab761209f-P0001-01
status: draft
source_packet: "research/_staging/source-packets/sp-chunk-3d3ab761209f-p0001-01-los-angeles-birth-register-page-172.md"
promotion_recommendation: hold_for_conversion_qa
---

# Relationship Candidates: Birth Register Entries 513-515

## Shared Source Reference

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk/page reference: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md`, `CHUNK-3d3ab761209f-P0001-01`, image page 1, register page 172

## Conversion Confidence And QA Concern

The original image is available and supports the assigned chunk over the assembled converted Markdown for the main relationship structure. Promotion should still wait for proof review because the derivative transcripts disagree materially and entry 515 is cropped at the bottom.

## Candidates

| Candidate id | Relationship candidate | Literal support | Uncertainty | Promotion recommendation |
| --- | --- | --- | --- | --- |
| rel-513-father | Jose del Carmen Pulgar is father of the entry 513 Pulgar Amagada child. | Source image: child surname line begins `Pulgar Ama...`; parent field `Jose del Carmen Pulgar`; declarant `Jose del C. Pulgar / Padre`. | Image supports the Pulgar row, but the child's given name and maternal surname conflict with the assembled converted file; hold until proof review accepts the source-image reading. | `hold_for_conversion_qa` |
| rel-513-mother | Juana de Dios Amagada de Pulgar is mother of the entry 513 Pulgar Amagada child. | Source image supports `Juana de Dios ... de Pulgar`; assigned chunk reads `Juana de Dios Amagada de Pulgar`; converted file reads `Juana de Dios Amador de Pulgar`. | Maternal surname is image-sensitive; do not merge or normalize yet. | `hold_for_conversion_qa` |
| rel-514-mother | Mercedes Riquelme is mother of Juan Bautista Riquelme. | Source image: child field `Riquelme / Juan Bautista`; mother/declarant `Mercedes Riquelme / Madre`. | Image does not visibly support assigned-chunk `Aviles`; child/place readings remain part of the conversion conflict. | `hold_for_conversion_qa` |
| rel-514-father-negative | No father is named for Juan Bautista Riquelme in entry 514. | Source image and assigned chunk support father field `Se ignora`; converted Markdown conflicts by naming a father. | Negative evidence only; not a parent-child link and not disproof of later evidence. | `do_not_promote` as a relationship; carry as conflict/negative-evidence note after proof review. |
| rel-515-father | Pedro Pablo Neira is father of Laura de la Cruz Neira Ulloa. | Assigned chunk and visible entry 515 area: child `Neira Ulloa / Laura de la Cruz`; father/declarant `Pedro Pablo Neira / Padre`; emendation `Neira=emendado= / vale=`. | The converted file reads a different surname and child name; proof review should verify the emendation before tree linkage. | `hold_for_conversion_qa` |
| rel-515-mother | Carmen Ulloa is mother of Laura de la Cruz Neira Ulloa. | Assigned chunk only: mother field `Carmen Ulloa`. | The current image does not visibly confirm the lower mother field because of the bottom crop. | `hold_for_conversion_qa` |

## Non-relationship Note

Record 514's father field should be used as negative evidence for the absence of a stated father in this entry, not as a tree relationship.
