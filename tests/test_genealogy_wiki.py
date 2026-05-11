from historic_doc_ingest.genealogy_wiki import (
    build_claim_index,
    build_relationship_index,
    compile_narrative,
    create_claim,
    create_relationship,
    create_source_packet,
    generate_tree,
    init_genealogy_wiki,
    lint_genealogy_wiki,
    write_claim_index,
    write_relationship_graph,
    write_relationship_index,
)


def test_init_genealogy_wiki_creates_operating_files(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    assert (tmp_path / "GENEALOGY_WIKI.md").exists()
    assert (tmp_path / "wiki" / "index.md").exists()
    assert (tmp_path / "wiki" / "log.md").exists()
    assert (tmp_path / "wiki" / "_templates" / "person.md").exists()
    assert (tmp_path / "wiki" / "_templates" / "claim.md").exists()
    assert (tmp_path / "wiki" / "relationships").exists()
    assert (tmp_path / "wiki" / "source-packets").exists()
    assert (tmp_path / "wiki" / "_indexes").exists()
    assert (tmp_path / "raw" / "converted").exists()


def test_lint_genealogy_wiki_passes_fresh_scaffold(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)

    assert lint_genealogy_wiki(tmp_path) == []


def test_source_packet_preserves_transcription_translation_interpretation_sections(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    raw_file = tmp_path / "raw" / "converted" / "record.md"
    raw_file.write_text("# Record\n", encoding="utf-8")

    packet = create_source_packet(tmp_path, raw_file, "SP001", "Geneva Record", "archive_pdf")
    packet_text = packet.read_text(encoding="utf-8")

    assert "## Literal Transcription" in packet_text
    assert "## Translation" in packet_text
    assert "## Interpretation" in packet_text
    assert "## Uncertain Or Illegible" in packet_text


def test_lint_flags_detached_claim(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    claim = tmp_path / "wiki" / "claims" / "CL001-test.md"
    claim.write_text(
        """---
type: claim
status: accepted
confidence: 9.5
source:
---

# Claim

## Claim

Dario attended an event.

## Literal Source Support

## Interpretation

## Uncertainty
""",
        encoding="utf-8",
    )

    issues = lint_genealogy_wiki(tmp_path)

    assert "claim page missing source: claims/CL001-test.md" in issues


def test_generate_tree_uses_relationship_pages(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    relationship = tmp_path / "wiki" / "relationships" / "R001-parent.md"
    relationship.write_text(
        """---
type: relationship
status: accepted
relationship_type: proven_parent
confidence: 9.0
person_a: [[people/parent]]
person_b: [[people/child]]
---

# Relationship

## Evidence For

## Evidence Against
""",
        encoding="utf-8",
    )

    output = generate_tree(tmp_path)

    assert "proven_parent accepted 9.0" in output.read_text(encoding="utf-8")


def test_compile_narrative_uses_only_accepted_or_probable_claims(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    accepted = tmp_path / "wiki" / "claims" / "CL001-accepted.md"
    accepted.write_text(
        """---
type: claim
status: accepted
confidence: 9.5
subject: Dario
source: [[sources/S001]]
---

# Claim

## Claim

Dario attended the conference.
""",
        encoding="utf-8",
    )
    rejected = tmp_path / "wiki" / "claims" / "CL002-rejected.md"
    rejected.write_text(
        """---
type: claim
status: rejected
confidence: 1.0
subject: Dario
source: [[sources/S002]]
---

# Claim

## Claim

Dario lived on the Moon.
""",
        encoding="utf-8",
    )

    narrative = compile_narrative(tmp_path, "Dario")
    text = narrative.read_text(encoding="utf-8")

    assert "Dario attended the conference." in text
    assert "Moon" not in text


def test_lint_flags_parent_born_after_child(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    (tmp_path / "wiki" / "people" / "parent.md").write_text(
        """---
type: person
birth_year: 1900
death_year:
---

# Parent

[[relationships/R001-parent]]
""",
        encoding="utf-8",
    )
    (tmp_path / "wiki" / "people" / "child.md").write_text(
        """---
type: person
birth_year: 1890
death_year:
---

# Child

[[relationships/R001-parent]]
""",
        encoding="utf-8",
    )
    (tmp_path / "wiki" / "relationships" / "R001-parent.md").write_text(
        """---
type: relationship
status: accepted
relationship_type: parent_child
confidence: 9.0
person_a: [[people/parent]]
person_b: [[people/child]]
---

# Relationship

## Evidence For

## Evidence Against
""",
        encoding="utf-8",
    )

    issues = lint_genealogy_wiki(tmp_path)

    assert "chronology impossible, parent born after child: relationships/R001-parent.md" in issues


def test_create_claim_and_build_claim_index(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    (tmp_path / "wiki" / "people" / "dario.md").write_text(
        """---
type: person
---

# Dario
""",
        encoding="utf-8",
    )
    (tmp_path / "wiki" / "sources" / "S001-record.md").write_text(
        """---
type: source
---

# Source

## Extracted Claims
""",
        encoding="utf-8",
    )

    claim_path = create_claim(
        root=tmp_path,
        claim_id="CL001",
        claim_text="Dario attended the 1929 Geneva Conventions.",
        claim_type="event",
        subject="[[people/dario]]",
        source="[[sources/S001-record]]",
        status="accepted",
        confidence=9.5,
    )

    claims = build_claim_index(tmp_path)

    assert claim_path.exists()
    assert len(claims) == 1
    assert claims[0].status == "accepted"
    assert claims[0].confidence == 9.5
    assert claims[0].text == "Dario attended the 1929 Geneva Conventions."


def test_write_claim_index(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_claim(
        root=tmp_path,
        claim_id="CL001",
        claim_text="Dario attended the conference.",
        claim_type="event",
        subject="[[people/dario]]",
        source="[[sources/S001-record]]",
    )

    index_path = write_claim_index(tmp_path)
    text = index_path.read_text(encoding="utf-8")

    assert '"claims"' in text
    assert "Dario attended the conference." in text


def test_lint_flags_missing_claim_reference_target(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_claim(
        root=tmp_path,
        claim_id="CL001",
        claim_text="Dario attended the conference.",
        claim_type="event",
        subject="[[people/missing-dario]]",
        source="[[sources/missing-source]]",
    )

    issues = lint_genealogy_wiki(tmp_path)

    assert "claim wiki/claims/cl001-dario-attended-the-conference.md subject target missing: [[people/missing-dario]]" in issues
    assert "claim wiki/claims/cl001-dario-attended-the-conference.md source target missing: [[sources/missing-source]]" in issues


def test_create_relationship_and_calculate_confidence_from_claims(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    (tmp_path / "wiki" / "people" / "parent.md").write_text("---\ntype: person\n---\n# Parent\n", encoding="utf-8")
    (tmp_path / "wiki" / "people" / "child.md").write_text("---\ntype: person\n---\n# Child\n", encoding="utf-8")
    (tmp_path / "wiki" / "sources" / "S001-record.md").write_text(
        "---\ntype: source\n---\n# Source\n\n## Extracted Claims\n",
        encoding="utf-8",
    )
    claim_path = create_claim(
        root=tmp_path,
        claim_id="CL001",
        claim_text="The record names Parent as Child's parent.",
        claim_type="relationship",
        subject="[[people/child]]",
        source="[[sources/S001-record]]",
        status="accepted",
        confidence=8.5,
    )
    claim_link = f"[[claims/{claim_path.stem}]]"

    create_relationship(
        root=tmp_path,
        relationship_id="R001",
        relationship_type="proven_parent",
        person_a="[[people/parent]]",
        person_b="[[people/child]]",
        status="accepted",
        supporting_claims=[claim_link],
    )

    relationships = build_relationship_index(tmp_path)

    assert len(relationships) == 1
    assert relationships[0].supporting_claims == [claim_link]
    assert relationships[0].calculated_confidence == 8.5


def test_write_relationship_index(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_relationship(
        root=tmp_path,
        relationship_id="R001",
        relationship_type="possible_sibling",
        person_a="[[people/a]]",
        person_b="[[people/b]]",
    )

    index_path = write_relationship_index(tmp_path)
    text = index_path.read_text(encoding="utf-8")

    assert '"relationships"' in text
    assert "possible_sibling" in text


def test_lint_flags_missing_relationship_targets_and_claims(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_relationship(
        root=tmp_path,
        relationship_id="R001",
        relationship_type="possible_sibling",
        person_a="[[people/missing-a]]",
        person_b="[[people/missing-b]]",
        supporting_claims=["[[claims/missing-claim]]"],
    )

    issues = lint_genealogy_wiki(tmp_path)

    assert "relationship wiki/relationships/r001-people-missing-a-people-missing-b-possible-sibling.md person_a target missing: [[people/missing-a]]" in issues
    assert "relationship wiki/relationships/r001-people-missing-a-people-missing-b-possible-sibling.md references missing claim: [[claims/missing-claim]]" in issues


def test_write_relationship_graph(tmp_path) -> None:
    init_genealogy_wiki(tmp_path)
    create_relationship(
        root=tmp_path,
        relationship_id="R001",
        relationship_type="spouse",
        person_a="[[people/a]]",
        person_b="[[people/b]]",
        status="probable",
        confidence=7.5,
    )

    graph_path = write_relationship_graph(tmp_path)
    text = graph_path.read_text(encoding="utf-8")

    assert '"nodes"' in text
    assert '"edges"' in text
    assert '"type": "spouse"' in text
