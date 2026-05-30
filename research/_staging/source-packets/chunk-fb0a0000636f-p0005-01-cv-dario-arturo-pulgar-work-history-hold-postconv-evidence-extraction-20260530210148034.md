---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530210057546
source_title: "CV of Dario Arturo Pulgar, disputed page 5 chunk"
source_type: curriculum_vitae
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
source_path: "raw/sources/CV of Dario Arturo Pulgar.pdf"
source_sha256: "07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
converted_sha256: "fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
chunk_id: "CHUNK-fb0a0000636f-P0005-01"
chunk_manifest: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json"
page_reference: "page 5 per assigned chunk; aggregate converted file also places the same HABITAT/NFB/Chile Films/CITELCO text later in the file"
page_start: 5
page_end: 5
source_identity: "Document-level CV subject Dario Arturo Pulgar; the assigned page body is a CV continuation and does not itself repeat his name."
family_relevance: high
matched_terms:
  - Dario
  - Pulgar
conversion_confidence: low
conversion_qa_concern: "Proof review identified unresolved conversion control problems. The current assigned chunk contains HABITAT/NFB/Chile Films/CITELCO work-history text, but the job page Markdown for page-0005 contains PROFONANPE/TVE text, the aggregate converted file contains conflicting page-5-like sections, the chunk manifest repeats page-0005 entries with different char counts and hashes, and the expected rendered page image path is not present in the conversion job directory. This packet preserves the derivative disagreement and does not choose a controlling transcript."
uncertainty: "Low that the assigned chunk text says the listed work-history facts; high for whether those facts are truly source page 5 and for any canonical attachment to Dario Arturo Pulgar-Smith without a separate identity-bearing page."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: CV Work History, Disputed Page 5 Chunk

This packet stages only narrow occupational and work-location evidence from the assigned chunk for the document-level CV subject, Dario Arturo Pulgar. It is not promotion-ready because page control is unresolved.

## Literal Support From Assigned Chunk

```text
1979 - 1982
United Nations Centre for Human Settlements (HABITAT)
Nairobi, Kenya
Development Support Communications Officer
```

```text
Supervise operations of five regional information offices in Amman, Jordan; Bangkok, Thailand; Dakar, Senegal; Mexico City, Mexico and Geneva, Switzerland.
```

```text
Carry out pre-feasibility missions in Africa including Uganda, Tanzania, Niger, Mali and Senegal.
```

```text
1974 - 1978
National Film Board of Canada (NFB)
Montreal, Canada
Audio Visual Consultant
```

```text
1972 - 1973
Chile Films
Santiago, Chile
General Manager Distribution and Exhibition, Head of International Department
```

```text
1970 - 1972
Cine, Televisión y Comunicaciones (CITELCO)
Santiago, Chile
Producer
```

## Derivative Transcript Conflict

The assigned chunk `page-0005-chunk-01.md` contains the HABITAT/NFB/Chile Films/CITELCO text above. The conversion job's `page-markdown/page-0005.md` instead contains PROFONANPE/TVE career text. The aggregate converted file also contains both kinds of content in different page sections, and the chunk manifest has duplicate entries for page 5 with the same chunk id and different hashes.

## Evidence Scope

After conversion QA, this packet may support work-history, role, and work-location claims for the CV subject. It does not state birth, death, parents, spouse, children, siblings, household, or any other family relationship.

## Promotion Recommendation

Hold for conversion QA. Restore or regenerate the page image, reconcile page order and chunk hashes, decide which transcription controls page 5, then run proof review and a separate identity-bridge review before attaching any work-history facts to a canonical person page.
