---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260522174957974
task_id: proof-review:research/_staging/claims/chunk-a048d567968b-p0001-04-005-jim-carney-vancouver-hometown-expo-86.md
staged_draft: research/_staging/claims/chunk-a048d567968b-p0001-04-005-jim-carney-vancouver-hometown-expo-86.md
reviewed_claim_type: residence_or_origin
reviewed_subject: "Jim Carney"
reviewed_predicate: "returned to hometown"
reviewed_object: "Vancouver in April 1986 as Commissioner General of the UN pavilion at Expo '86"
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-04-habitat-revisited-jim-carney.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0001-chunk-04.md"
chunk_id: CHUNK-a048d567968b-P0001-04
source_page_image_checked: "unavailable; manifest lists page-images/page-0010.jpg for the supporting converted page 10, but that file was not present in this checkout"
source_quality_score: 0.68
conversion_confidence_score: 0.60
evidence_quantity_score: 0.55
agreement_score: 0.88
identity_confidence_score: 0.86
claim_probability: 0.80
relevance_level: contextual
relevance_confidence: 0.82
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Jim Carney Vancouver Hometown Expo 86

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The staged draft and source packet both record controller `qc:reread-page` and a page-boundary problem: the chunk is assigned to page 1 while the supporting passage is embedded as converted page 10, followed by page 11 material.
- I could not visually verify the exact source page image for the supporting sentence. The manifest lists `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0010.jpg`, but that file is not present in this checkout.
- The source is a 2006 memoir-style retrospective by Jim Carney. It is strong for his own stated recollection, but it is not an independent vital, residence, or municipal record. The wording supports Vancouver as his stated "hometown"; it should not be expanded into a birth-place or long-term residence claim without other evidence.
- No relationship claim is supported by this passage. There is no parent, spouse, child, sibling, or kinship evidence in the reviewed claim context.

## Evidence Strengths

- The staged claim is directly supported by the converted text and chunk: "I remained in the post until April, 1986, when I returned to my hometown, Vancouver, as Commissioner General of the UN pavilion at Expo '86."
- The source title and source packet identify the document as `Habitat Revisited, Jim Carney, 2006`; the first-person narrator is therefore reasonably attributed to Jim Carney for this limited self-referential claim.
- The source packet, converted file, and chunk agree on the relevant wording and on the need to hold for conversion QA.
- Within the reviewed staged draft, source packet, converted file, and chunk, I found no conflicting statement about the April 1986 return, Vancouver as hometown, or the Expo '86 UN pavilion role.

## Scored Judgment

- `source_quality_score: 0.68` - self-authored memoir evidence is credible for the author's own career/origin statement, but retrospective and not an official record.
- `conversion_confidence_score: 0.60` - the converted wording is clear and internally repeated, but the page-image check is unavailable and the chunk/page metadata are inconsistent.
- `evidence_quantity_score: 0.55` - one direct passage supports the claim; no independent corroborating evidence was reviewed for this task.
- `agreement_score: 0.88` - the staged draft, source packet, converted file, and chunk agree on the substance, reduced for unresolved page-boundary QA.
- `identity_confidence_score: 0.86` - the document title and first-person memoir context support attributing the statement to Jim Carney, though the key sentence itself uses "I" rather than restating his full name.
- `claim_probability: 0.80` - probable as a memoir-supported contextual origin/career claim, pending page-image verification.
- `relevance_level: contextual`; `relevance_confidence: 0.82` - useful biographical context for Jim Carney's stated hometown and Expo '86 role, but not a vital event or kinship fact.
- `canonical_readiness: hold_for_conversion_qa`.

## Next Action

Restore or regenerate the missing rendered page image for converted page 10, then visually verify the sentence about returning to Vancouver as Commissioner General of the UN pavilion at Expo '86 and document/correct the chunk page reference. Keep this claim in staging until that conversion QA is complete.
