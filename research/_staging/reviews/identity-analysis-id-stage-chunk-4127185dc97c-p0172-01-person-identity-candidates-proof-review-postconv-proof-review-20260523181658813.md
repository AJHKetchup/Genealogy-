---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260523181658813
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
staged_draft: research/_staging/identity-analysis/identity-analysis-id-stage-chunk-4127185dc97c-p0172-01-person-identity-candidates.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-4127185dc97c-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
referenced_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
available_chunk_checked: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
canonical_readiness: hold
---

# Proof Review: Page 172 Identity Candidates

## Blockers First

- The referenced chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md` is unavailable. The available chunk is `page-0001-chunk-01.md` with a different chunk id, so the citation chain is not clean.
- The staged identity draft is correctly not proof-ready. The visible page image and the source packet both show material conflicts with the converted/chunk transcript for entries 513, 514, and 515.
- Entry 513 should not be promoted as `Isidoro del Carmen Diaz`. The visible image supports a Pulgar-related row and a child reading closer to `Pulgar ... Jose Dani...`; the converted/chunk text instead gives `Isolina del Carmen / José`.
- Entry 514 should not be promoted as `Riquelme Juan Teodoro` with father `Belisario Riquelme`. The visible image supports `Rigoberto Juan Bautista` in the child field and the father field appears closer to `se ignora`, while `Mercedes Riquelme` is visible as mother/declarant.
- Entry 515 should not be promoted with `Leiva` parent/declarant readings. The visible lower row supports a Neira-related reading, including father/declarant area closer to `Pedro Pablo Neira`, while the converted/chunk text gives `Pedro Pablo Leiva`.
- No relationship or same-person bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío Pulgar Arriagada, Jose del Carmen Pulgar, Juana de Dios Amagada de Pulgar, or Juana Arriagada de Pulgar is ready from this staged draft.

## Evidence Strengths

- The civil register image is a direct source for the page and visibly supports page `172`, year `1889`, register place wording `Los Anjeles`, district `La Laja`, and entries `513`, `514`, and `515`.
- The source packet accurately flags the core conversion problems and recommends `hold_for_conversion_qa`.
- Entry-level identity risk is high, but the page-level and entry-number context is strong enough to keep this as a targeted conversion-QA lead rather than discard it.

## Scored Judgment

| Metric | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register page image is a direct record source, but the image has bleed-through/crop and handwriting difficulty. |
| conversion_confidence_score | 0.18 | The available converted/chunk transcript conflicts with visible source readings on core identity fields. |
| evidence_quantity_score | 0.42 | One direct page image plus derivative transcript/source packet; enough to identify blockers, not enough to promote identities. |
| agreement_score | 0.22 | Staged draft, chunk transcript, source packet, and visible image disagree on key names and relationships. |
| identity_confidence_score | 0.24 | Page/entry frame is solid; individual child/parent identities are not settled. |
| claim_probability | 0.31 | Probability that the staged identity candidates as written are correct is low. Probability that page 172 contains relevant candidate rows is moderate. |
| relevance_level | 1.00 | The reviewed files directly match the assigned staged draft and page 172 entries 513-515. |
| relevance_confidence | 0.98 | Source packet and source image match the staged draft's page/entry scope. |
| canonical_readiness | 0.02 | Hold. Do not promote names, relationships, or same-person identities. |

## Claim Probability By Entry

| Entry | Draft/conversion claim reviewed | Probability | Review result |
| --- | --- | ---: | --- |
| 513 | Child identity as `Isidoro del Carmen Diaz` or converted `Isolina del Carmen / José` | 0.20 | Revise/hold. Visible source favors a Pulgar child reading, but exact child name remains unresolved. |
| 513 | Father/declarant as `José del Carmen Pulgar` / `José del C. Pulgar` | 0.62 | Hold. Visible source supports a Jose del Carmen Pulgar-like father/declarant, but linkage to any canonical Jose requires a clean field proof. |
| 513 | Mother as `Juana de Dios Amador/Amagada/Arriagada de Pulgar` | 0.36 | Hold. Visible source supports `Juana de Dios ... de Pulgar`, but the surname reading is not secure enough to merge variants. |
| 514 | Child as `Rigoberto Juan Bautista` | 0.70 | Revise after conversion QA. Visible source is closer to this than the converted `Riquelme Juan Teodoro`, but the proof-review note should not rewrite the source transcript. |
| 514 | Father as `Belisario Riquelme` | 0.08 | Hold/reject for promotion. Visible source appears closer to `se ignora`. |
| 514 | Mother/declarant as `Mercedes Riquelme` | 0.78 | Hold for field-level QA; visibly plausible, but not enough to promote relationships while the child/father fields are conflicted. |
| 515 | Father/declarant as `Pedro Pablo Leiva` | 0.10 | Hold/reject for promotion. Visible source favors `Neira` over `Leiva`. |
| 515 | Neira-related father/declarant hypothesis | 0.68 | Hold as a QA hypothesis only; lower row is partly cut/low confidence. |

## Conflicts And Risks

- Literal support conflict: the staged draft and available chunk do not provide stable literal support for the child names and parent fields.
- Relationship jump risk: high. Promoting parent-child or spouse links from the current conversion would attach people to the wrong family lines.
- Identity conflation risk: high for `Amador`, `Amagada`, and `Arriagada`; high for `Leiva` versus `Neira`; high for attaching a Pulgar row to any Dario identity by surname alone.
- Source reliability is not the problem; conversion reliability is the problem.

## Next Action

Keep the staged draft on hold for conversion QA. Resolve the missing `page-0172-chunk-01.md` citation and perform side-by-side field-level QA from the page image for entries 513-515 before any proof promotion.

Priority order:

1. Entry 513 child full name/surname, father/declarant, and mother's surname.
2. Entry 514 child name and father field, especially whether the father is `se ignora`.
3. Entry 515 surname and father/declarant reading, especially `Neira` versus `Leiva`.

Do not edit raw sources, converted Markdown, chunks, source packets, or canonical wiki pages from this proof-review task.
