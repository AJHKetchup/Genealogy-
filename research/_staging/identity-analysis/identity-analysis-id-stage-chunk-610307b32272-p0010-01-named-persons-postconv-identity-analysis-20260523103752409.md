---
type: identity_conflict_analysis
status: draft
worker: postconv-identity-analysis-20260523103752409
task_id: identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-610307b32272-P0010-01-named-persons.md
role: identity_researcher
staged_identity_draft: research/_staging/identity/ID-STAGE-CHUNK-610307b32272-P0010-01-named-persons.md
source_packet: research/_staging/source-packets/chunk-610307b32272-p0010-01-acicr-cr177-diplomatic-conference-index.md
source: raw/sources/ACICR_B_CR_177_001_002.pdf
converted_file: raw/converted/ca35845f12-acicr-b-cr-177-001-002-p0006-0012-acicr-b-cr-177-001-002-pages-6-12.codex.md
chunk: raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0006-0012-acicr-b-cr-177-001-002-pages-6-12-codex/page-0010-chunk-01.md
chunk_id: CHUNK-610307b32272-P0010-01
page_reference: source page 10, entries 184-204
identity_confidence: low
conflict_severity: medium
evidence_quality: fair
conversion_confidence: medium
claim_probability: low_to_medium
relevance: low
canonical_readiness: not_ready
promotion_recommendation: do_not_promote
---

# Identity/Conflict Analysis: Page 10 Named Persons

## Blockers First

- Conversion QA is blocking: the page was flagged for reread, and the staged conflict note specifically flags uncertain readings for `Cahe/Cahen`, `Mehberg/Mehlberg`, `Cahen-Salvado/Cahen-Salvador`, and `Hillin/Hillem`.
- Identity anchors are weak: most mentions are honorific plus surname only. The page gives no ages, residences except Wackeben at Berlin, family relationships, birth/death details, or stable full-name identifiers.
- Canonical readiness is blocked: local canonical wiki search found no existing page matches for the listed page-10 names.
- Relationship promotion is blocked: the related staged relationship note says the page states no parent-child, spouse, sibling, or other family relationship.
- Pulgar-line comparison is not triggered by this staged draft: no Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Jose parent, or Juana parent candidate appears in the assigned staged draft or in the page-10 referenced context reviewed here.

## Literal Source Readings

The assigned staged draft cites these identity-relevant readings from source page 10:

```text
186.- 29.8.29. 1/ de M. Brown à Dr Mehberg à propos du livre de M. Cahen-Salvado
```

```text
ms. 189.- 4.9.29. Note de M. Huber sur le livre de M. Werner
```

```text
ms. 1 ann. ms 200.- 23.10.29. BIT réclame documents pour Dr Hillin.
```

The referenced chunk also includes `M. Wackeben à Berlin`, `M. Georges Cahe Salvador`, `M. Paul Des Gouttes`, `M. Ciraolo`, `M. Clouzot`, `général Demolder`, `M. Bagotzky`, and `M. Draudt`.

## Hypotheses And Evidence

### H1: Page-10 mentions are distinct archival index leads, not mergeable identities.

Evidence supporting this hypothesis:

- The assigned identity draft describes the candidate scope as "surname-only and title-plus-surname named persons in archival index entries."
- The related no-family-relationship draft explicitly states that page 10 names people in correspondence, notes, reports, document requests, translations, and publication status, but states no family relationship.
- The page-10 claims for Des Gouttes/Ciraolo, Huber/Werner, Demolder, Bagotzky, and Draudt are public/documentary activity claims and are all marked `hold_for_conversion_qa`.

Scores:

- Identity confidence: 0.35
- Conflict severity: 0.40
- Evidence quality: 0.55
- Conversion confidence: 0.50
- Claim probability: 0.45
- Relevance: 0.30
- Canonical readiness: 0.10

Assessment: This is the best current hypothesis. Treat the names as leads only.

### H2: `general Demolder` on page 10 is the same person as staged `Paul Demolder`.

Evidence supporting this hypothesis:

- Page 10 entries 191 and 194 refer to `général Demolder`, his corrections, and his report.
- A separate staged claim from `CHUNK-3f469b56e502-P0007-01` names `M. Paul Demolder, Général Major Médecin, Commandant du Service de Santé de la 1re Circonscription militaire` as a Belgian plenipotentiary, with high conversion confidence.
- The shared surname plus general/major-general role in diplomatic-conference material is a meaningful identity hint.

Conflicts and cautions:

- Page 10 does not give Demolder's given name.
- The two references come from different source packets and must not be merged by title and surname alone.
- The page-10 conversion is medium confidence and still has a reread-page flag, although Demolder itself is not the most uncertain reading.

Scores:

- Identity confidence: 0.70
- Conflict severity: 0.30
- Evidence quality: 0.70
- Conversion confidence: 0.65
- Claim probability: 0.70
- Relevance: 0.55
- Canonical readiness: 0.35

Assessment: Likely same person, but requires proof review comparing the page-10 Demolder entries to the staged Paul Demolder plenipotentiary claim before canonical promotion.

### H3: `M. Paul Des Gouttes` on page 10 is the same person as `M. Des Gouttes` in the 1928 CR 177 staged drafts.

Evidence supporting this hypothesis:

- Page 10 names `M. Paul Des Gouttes` in entry 188 concerning corrected minutes by `M. Ciraolo`.
- A related 1928 staged source packet and claims mention `M. Des Gouttes` accepting or being nominated secretary general of the conference.
- The same CR 177 diplomatic conference context gives a plausible continuity clue.

Conflicts and cautions:

- The 1928 draft lacks the given name in its cited wording.
- This is a public-role/documentary continuity hint, not family identity evidence.
- Page 10's line break has a duplicated `pa/par` reading and is flagged for source reread.

Scores:

- Identity confidence: 0.65
- Conflict severity: 0.25
- Evidence quality: 0.60
- Conversion confidence: 0.55
- Claim probability: 0.65
- Relevance: 0.45
- Canonical readiness: 0.30

Assessment: Plausible same person within the CR 177 file sequence, but hold pending page reread and proof review of the Des Gouttes conference-role drafts.

### H4: Name-variant pairs are transcription variants, not separate people.

Candidate pairs:

- `Georges Cahe Salvador` / `Georges Cahen-Salvador` / `Cahen-Salvado`
- `Dr Mehberg` / `Dr Mehlberg`
- `Dr Hillin` / `Dr Hillem`

Evidence supporting this hypothesis:

- The identity-conflict draft explicitly identifies these as converted-name uncertainties.
- The same entries have no independent biographical anchors to support separating or merging people.

Conflicts and cautions:

- These variants cannot be normalized silently. The literal reading must stay separate from interpretation until source-image reread.
- `M. Brown`, `Dr Mehberg/Mehlberg`, and `M. Cahen-Salvado/Cahen-Salvador` appear together in one entry, so a wrong reading could affect multiple identity leads.

Scores:

- Identity confidence: 0.25
- Conflict severity: 0.60
- Evidence quality: 0.45
- Conversion confidence: 0.45
- Claim probability: 0.35
- Relevance: 0.35
- Canonical readiness: 0.05

Assessment: Preserve all literal variants. Do not create canonical identity links from these names until reread resolves the spellings.

## Conflicts

- Name-variant conflict: medium severity for Cahen/Cahe/Salvado/Salvador, Mehberg/Mehlberg, and Hillin/Hillem.
- Duplicate-person risk: medium for Demolder and Des Gouttes because related staged drafts give stronger context, but page 10 alone is insufficient.
- Relationship conflict: none identified. The page states no family relationships.
- Chronology conflict: none identified. Dates on page 10 run from 1929-08-20 through 1929-11-22 and do not conflict with the reviewed staged public-role claims.
- Canonical conflict: none found because no matching canonical wiki pages were found for these names in the local wiki search.

## Recommended Next Action

Run proof review only after conversion QA rereads source page 10 against the PDF image. The exact next proof-review step should compare:

- `research/_staging/identity/ID-STAGE-CHUNK-610307b32272-P0010-01-named-persons.md`
- `research/_staging/identity-conflicts/CONFLICT-STAGE-CHUNK-610307b32272-P0010-01-name-uncertainties.md`
- `research/_staging/tasks/TASK-STAGE-CHUNK-610307b32272-P0010-01-page-reread-identity-review.md`
- the page-10 public-activity claims for Des Gouttes/Ciraolo, Huber/Werner, Demolder, Bagotzky, and Draudt
- `research/_staging/claims/CL-STAGE-CHUNK-3f469b56e502-P0007-01-paul-demolder-plenipotentiary.md` for the Demolder hypothesis

Until that review is complete, keep this staged identity draft as an identity-review lead only and do not promote or merge any person.
