---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260523095445352
task_id: "identity-analysis:research/_staging/conflicts/chunk-f2c5548c9fde-p0053-01-conversion-and-identity-watch.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-f2c5548c9fde-p0053-01-conversion-and-identity-watch.md"
subject: "Arturo entries on source page 53"
source_packet: "research/_staging/source-packets/chunk-f2c5548c9fde-p0053-01-arturo-larrain-lavin-medical-directory.md"
source: "raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf"
converted_file: "raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-41-60.codex.md"
chunk: "raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0041-0060-gu-a-m-dica-nacional-profesiones-m-dic-8fbd29c654/page-0053-chunk-01.md"
chunk_id: CHUNK-f2c5548c9fde-P0053-01
page_reference: "source page 53; printed page 56"
identity_confidence: medium_high_for_exact_directory_rows
conflict_severity: low
evidence_quality: medium_high_for_directory_listing
conversion_confidence: high_with_address_cautions
claim_probability: high_for_scoped_directory_mentions
relevance: contextual
canonical_readiness: scoped_only
promotion_recommendation: promote_scoped_claims_only_no_identity_merge
---

# Identity/Conflict Analysis: Arturo Entries On Source Page 53

## Blockers First

- Do not use the given-name match `Arturo` to connect either directory row to a target family member or to a Pulgar-line person. The reviewed page supplies name, address, and locality only.
- Do not infer birth, death, parents, spouse, children, permanent residence, residence duration, or family relationship from this directory page.
- Preserve the conversion QA cautions in any downstream use: converted `Vicuña Mackenna 4, 7' Piso` should be treated as image-reviewed `Vicuña Mackenna 4, 7º Piso`, and converted `Merced 250 В` should be treated as image-reviewed `Merced 250 B`.
- The staged conflict draft recommends `do_not_promote` as a canonical conflict. Existing proof reviews support only narrow directory/listing or locality claims, not a same-person, duplicate-person, relationship, or chronology conflict.
- No external research was performed. This analysis uses only the staged conflict draft, staged source packet, staged identity/claim drafts, proof-review notes, promoted source packet/claims, and existing wiki pages.

## Literal Source Reading

Assigned staged conflict draft: `research/_staging/conflicts/chunk-f2c5548c9fde-p0053-01-conversion-and-identity-watch.md`.

Image-reviewed readings preserved in the staged source packet and proof reviews:

```text
Larraín García, Arturo     Vicuña Mackenna 4, 7º
                           Piso                  Santiago
Lavín Gallegos, Arturo     Merced 250 B           Santiago
```

Converted Markdown readings preserved as conversion cautions:

```text
| Larraín García, Arturo | Vicuña Mackenna 4, 7' Piso | Santiago |
| Lavín Gallegos, Arturo | Merced 250 В               | Santiago |
```

Interpretation kept separate: these are two professional directory rows in a July 1959 Chilean medical directory. The table does not state family relationships or identity links beyond the two exact name strings.

## Hypotheses And Evidence

### H1: `Larraín García, Arturo` is a separate source-mentioned person, Arturo Larraín García

Supporting evidence:

- The staged conflict draft names `Larraín García, Arturo` as a literal image-reviewed row.
- The staged identity candidate `research/_staging/identities/chunk-f2c5548c9fde-p0053-01-arturo-larrain-garcia-identity-candidate.md` records the exact source mention with address `Vicuña Mackenna 4, 7º Piso` and locality `Santiago`.
- Proof review `research/_staging/reviews/proof-review-chunk-f2c5548c9fde-p0053-01-001-arturo-larrain-garcia-directory-listing-postconv-proof-review-20260522211409006.md` reports the page image was checked and supports the row alignment, name, address, and locality.
- Existing canonical page `wiki/people/arturo-larra-n-garc-a.md` is explicitly scoped as a `source_mentioned` directory-listing page and says the reviewed source does not establish birth, death, residence duration, family relationship, or identity with any other canonical person.

Limitations:

- The only identity anchors are name, address, locality, source date, and directory context.
- The address is a directory/practice address candidate, not proof of permanent residence.
- No parent, spouse, child, age, vital date, or Pulgar-line marker appears in this page row.

Scores:

- Identity confidence: 0.83 for the exact directory-row identity string.
- Conflict severity: low.
- Evidence quality: 0.78 as a dated national medical directory for a directory mention.
- Conversion confidence: 0.88-0.91, with the floor-marker correction preserved.
- Claim probability: 0.90 for the directory-listing claim; 0.93 for the Santiago locality claim.
- Relevance: contextual, relevance confidence 0.84-0.86.
- Canonical readiness: ready only for scoped directory/listing or locality review, not for broader identity merging.

Rank: supported as a separate source-mentioned person.

### H2: `Lavín Gallegos, Arturo` is a separate source-mentioned person, Arturo Lavín Gallegos

Supporting evidence:

- The staged conflict draft names `Lavín Gallegos, Arturo` as a literal image-reviewed row.
- The staged identity candidate `research/_staging/identities/chunk-f2c5548c9fde-p0053-01-arturo-lavin-gallegos-identity-candidate.md` records the exact source mention with address `Merced 250 B` and locality `Santiago`.
- Proof review `research/_staging/reviews/proof-review-chunk-f2c5548c9fde-p0053-01-004-arturo-lavin-gallegos-directory-listing-postconv-proof-review-20260522211617307.md` reports the page image was checked and supports the row alignment, name, address, and locality.
- Existing canonical page `wiki/people/arturo-lav-n-gallegos.md` is explicitly scoped as a `source_mentioned` directory-listing page and says the reviewed source does not establish birth, death, residence duration, family relationship, or identity with any other canonical person.

Limitations:

- The only identity anchors are name, address, locality, source date, and directory context.
- The address is a directory/practice address candidate, not proof of permanent residence.
- The locality proof review gives `canonical_readiness: revise_literal_support_before_promotion` because the address character needed the `B` versus `В` correction, even though locality `Santiago` is supported.
- No parent, spouse, child, age, vital date, or Pulgar-line marker appears in this page row.

Scores:

- Identity confidence: 0.82 for the exact directory-row identity string.
- Conflict severity: low.
- Evidence quality: 0.72-0.78 as a dated national medical directory for a directory/locality mention.
- Conversion confidence: 0.88-0.90, with the Latin `B` correction preserved.
- Claim probability: 0.92 for the directory-listing claim; 0.88 for the Santiago locality claim pending literal-support cleanup.
- Relevance: contextual, relevance confidence 0.84.
- Canonical readiness: ready only for scoped directory/listing review; locality/address wording needs the conversion caution carried forward.

Rank: supported as a separate source-mentioned person.

### H3: Arturo Larraín García and Arturo Lavín Gallegos are the same person or duplicate profiles

Supporting evidence:

- Both rows are on the same 1959 medical-directory page.
- Both have the given name `Arturo` and locality `Santiago`.

Conflicting or limiting evidence:

- The surnames are different: `Larraín García` versus `Lavín Gallegos`.
- The addresses are different: `Vicuña Mackenna 4, 7º Piso` versus `Merced 250 B`.
- The page is an alphabetized directory table and presents them as separate rows.
- No reviewed note supplies a shared relationship, alias, professional credential number, or other bridge between the two rows.

Scores:

- Identity confidence for same-person hypothesis: 0.05.
- Conflict severity: low; this is a false-positive duplicate risk, not an active contradiction.
- Evidence quality for duplicate hypothesis: very low.
- Conversion confidence: not the main issue; the image-reviewed rows distinguish the entries.
- Claim probability: 0.05.
- Relevance: very low for identity merging.
- Canonical readiness: not ready.

Rank: unsupported. Keep as separate source-mentioned identities.

### H4: Either Arturo directory entry is Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío/Dario Pulgar Arriagada, or a Jose/Juana parent candidate

Supporting evidence:

- The only overlap is the given name `Arturo` with `Dario Arturo Pulgar-Smith` / `Dario Arturo Pulgar`.

Conflicting or limiting evidence:

- The staged conflict draft and source packet contain no `Dario`, `Pulgar`, `Pulgar-Smith`, `Pulgar-Arriagada`, `Jose`, or `Juana` name in the two relevant rows.
- Existing page `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to automatically merge with similarly named source clusters.
- Existing page `wiki/people/dar-o-pulgar-arriagada.md` concerns a `Darío Pulgar Arriagada` expropriation notice in 2000, not a 1959 `Larraín García` or `Lavín Gallegos` medical-directory row.
- Existing pages `wiki/people/dario-pulgar-child-passenger-age-11.md` and `wiki/people/dario-pulgar-adult-passenger-age-64.md` concern 1953 passenger-list entries under the surname Pulgar, not the Larraín/Lavín directory rows.
- Existing page `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` concerns an 1888 birth registration and has no name/address overlap with either 1959 Arturo row.
- Existing parent-candidate pages `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md` do not match either directory row by surname, full name, date, relationship, or place beyond broad Chile context.

Scores:

- Identity confidence for Pulgar-line merge: 0.02.
- Conflict severity: low, but the false-positive risk should be recorded because `Arturo` is a family-relevant matched term.
- Evidence quality for a Pulgar link: none.
- Conversion confidence: not applicable to unsupported Pulgar identity link.
- Claim probability: 0.02 for any same-person or relationship claim.
- Relevance: very low for Pulgar-line identity work.
- Canonical readiness: not ready.

Rank: unsupported. The exact proof-review step needed next would be a targeted identity proof review only if a future source supplies a direct bridge such as full name `Dario Arturo Pulgar`, surname `Pulgar`, parent/child names, spouse, birth date, or another unique identifier tying one of these `Arturo` rows to a Pulgar-line person. No such step is justified from this staged draft alone.

## Conflicts

- Same-person conflict: none supported. The two `Arturo` rows are separate directory entries with different surnames and addresses.
- Duplicate-person conflict: no duplicate-person merge is supported against each other or against reviewed Pulgar-line pages.
- Name-variant conflict: none supported. `Arturo` alone is not a name variant for `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Darío/Dario Pulgar Arriagada`.
- Relationship conflict: none stated. The directory page contains no parents, spouse, children, or family relationship assertions.
- Chronology conflict: none stated. The only date context is July 1959 for the directory source; no vital or life-event chronology is asserted for either Arturo row.
- Conversion conflict: two address transcription defects remain material for literal quotation but do not change the identity conclusion: `7' Piso` versus `7º Piso`, and Cyrillic-looking `В` versus Latin `B`.

## Score Summary

| Area | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.83 Larraín / 0.82 Lavín | Exact image-reviewed name rows are supported, but only as source-mentioned identities. |
| Conflict severity | 0.20 | No direct identity, relationship, or chronology contradiction; main risk is false-positive merging by given name. |
| Evidence quality | 0.78 directory listing; 0.72-0.78 locality/address context | Contemporary directory evidence is good for listing/locality, not for vital or relationship facts. |
| Conversion confidence | 0.88-0.91 | Page image reread confirms row alignment; address characters require preserved correction notes. |
| Claim probability | 0.90-0.93 Larraín scoped claims; 0.88-0.92 Lavín scoped claims | High for narrow directory/locality claims, very low for broader identity claims. |
| Relevance | contextual, 0.84-0.86 | Useful professional directory context; no demonstrated family-line relevance. |
| Canonical readiness | scoped_only | Suitable only for scoped source-mentioned person/directory evidence; not a canonical conflict or merge. |

## Recommended Next Action

Do not promote the staged conflict draft as a canonical conflict. Keep the two persons separate as exact-name, source-mentioned directory entries, and carry forward the image-reviewed address corrections in any claim promotion or wiki update. If further promotion occurs, use only the existing proof-reviewed scoped claims: directory listing and locality/address context, with no relationship inference and no Pulgar-line identity merge.
