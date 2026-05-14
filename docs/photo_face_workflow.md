# Photo And Face Workflow

This workflow makes visual evidence first-class in the genealogy pipeline. Source conversion should extract all meaningful visual regions from documents, including portraits and headshots embedded inside scanned forms, cards, passports, newspaper pages, group photos, certificates, and albums.

## What This Repo Owns

The source-prep pipeline owns:

- extracting document images, portraits, headshots, stamps, seals, signatures, maps, and other visual regions into `extracted-images/page-####/`
- linking each crop from the converted page Markdown
- recording crop provenance: raw source, page image, conversion job, converted Markdown, chunk, page number, and source hash
- creating confirmed reference photo pages when the source context identifies the person
- creating unknown/candidate face records when the source does not identify the person
- preserving source context for later review: captions, nearby names, dates, places, page labels, and related text

## Auto-Tag From Source Context

The repo may auto-tag a crop with a named person when the identity comes from the source itself, not from face similarity. Examples:

- an identity card names the holder and contains one attached portrait
- a passport page names the holder and contains the passport photograph
- a labeled portrait says the person name in the caption
- a group photo has a reliable caption mapping names to positions
- a newspaper clipping caption names the pictured person

When this happens:

- set the photo page status to `source_context_confirmed`
- put the person in `people_confirmed`
- write the exact source basis in the photo page and `research/_indexes/face-reference-index.json`
- keep the source path, converted file, chunk, and crop asset linked

The Dario Pulgar Smith tourist card is the first reference example: the card names `DARIO PULGAR SMITH`, and the attached portrait is part of that same named card.

## Unknown Face Records

When a face or headshot is visible but not named by the source:

- crop it anyway
- create or queue an `unknown_face` / `candidate_photo` record
- preserve the source context and page location
- do not put a person in `people_confirmed`
- leave `people_suggested` empty unless there is non-face source context suggesting a candidate

## External Candidate Import

An external tool may later provide candidate collections or match suggestions. This repo should consume those only as review inputs:

```json
{
  "candidate_id": "FACE-CANDIDATE-001",
  "crop_asset": "path/to/crop.png",
  "source_context": "path/to/source-or-page.md",
  "suggested_reference": "FACE-DPS-1964-001",
  "suggestion_source": "external_face_clusterer",
  "review_status": "candidate"
}
```

The repo does not promote these suggestions to `people_confirmed` unless source context or later review supports the identity.

## Current Confirmed Reference

- Dario Pulgar Smith: `wiki/photos/PH001-dario-pulgar-smith-1964-tourist-card-portrait.md`
- Face cluster/reference: `wiki/photos/FC001-dario-pulgar-smith-confirmed-reference.md`

## Guardrail

This repo can auto-tag from source evidence. It should not silently turn unlabeled visual similarity into a confirmed identity.
