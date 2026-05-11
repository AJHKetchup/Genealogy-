from __future__ import annotations

from pathlib import Path

from historic_doc_ingest.models import DocumentBlock, IngestedDocument


def write_markdown(document: IngestedDocument, output_path: Path, output_root: Path) -> None:
    parts: list[str] = []
    title = Path(document.source_path).stem
    parts.append(f"# {title}\n")
    parts.append("> Converted from source page images. Page anchors and image references are preserved for audit.\n")

    for page in document.pages:
        parts.append(f"\n<a id=\"page-{page.number:04d}\"></a>\n\n")
        parts.append(f"## Page {page.number}\n\n")
        parts.append(f"![Source page]({relative(page.image_path, output_root)})\n\n")

        for block in page.ordered_blocks():
            rendered = render_block(block, output_root)
            if rendered:
                parts.append(rendered)
                if not rendered.endswith("\n\n"):
                    parts.append("\n\n")

    output_path.write_text("".join(parts).strip() + "\n", encoding="utf-8")


def render_block(block: DocumentBlock, output_root: Path) -> str:
    text = block.text.strip()
    if block.kind == "heading" and text:
        return f"### {single_line(text)}\n\n"
    if block.kind == "caption" and text:
        return f"*{single_line(text)}*\n\n"
    if block.kind == "page_number" and text:
        return f"`Page number: {single_line(text)}`\n\n"
    if block.kind == "footer" and text:
        return f"<small>{escape_angle(text)}</small>\n\n"
    if block.kind == "image":
        caption = block.metadata.get("caption", "")
        alt = caption or "Document image"
        if block.asset_path:
            return f"![{escape_brackets(alt)}]({relative(block.asset_path, output_root)})\n\n"
        return f"<!-- Image region: {block.bbox.x0:.0f},{block.bbox.y0:.0f},{block.bbox.x1:.0f},{block.bbox.y1:.0f} -->\n\n"
    if text:
        return normalize_paragraph(text) + "\n\n"
    return ""


def normalize_paragraph(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def single_line(text: str) -> str:
    return " ".join(text.split())


def escape_angle(text: str) -> str:
    return text.replace("<", "&lt;").replace(">", "&gt;")


def escape_brackets(text: str) -> str:
    return text.replace("[", "(").replace("]", ")")


def relative(path: str | Path, root: Path) -> str:
    path = Path(path)
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()
