from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Literal


BlockKind = Literal["heading", "body", "caption", "image", "footer", "page_number", "unknown"]


@dataclass(frozen=True)
class BoundingBox:
    x0: float
    y0: float
    x1: float
    y1: float

    @property
    def width(self) -> float:
        return self.x1 - self.x0

    @property
    def height(self) -> float:
        return self.y1 - self.y0

    def normalized(self, page_width: float, page_height: float) -> "BoundingBox":
        return BoundingBox(
            x0=self.x0 / page_width,
            y0=self.y0 / page_height,
            x1=self.x1 / page_width,
            y1=self.y1 / page_height,
        )


@dataclass
class DocumentBlock:
    kind: BlockKind
    bbox: BoundingBox
    text: str = ""
    confidence: float | None = None
    asset_path: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class DocumentPage:
    number: int
    width: float
    height: float
    image_path: str
    blocks: list[DocumentBlock] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def ordered_blocks(self) -> list[DocumentBlock]:
        return sorted(self.blocks, key=lambda block: (block.bbox.y0, block.bbox.x0))


@dataclass
class IngestedDocument:
    source_path: str
    pages: list[DocumentPage]
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_manifest(self) -> dict[str, Any]:
        return asdict(self)


def display_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()
