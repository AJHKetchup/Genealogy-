from __future__ import annotations

from abc import ABC, abstractmethod

from historic_doc_ingest.models import DocumentPage


class RefinementProvider(ABC):
    """Optional second-pass provider for layout-aware OCR correction."""

    @abstractmethod
    def refine_page(self, page: DocumentPage) -> DocumentPage:
        """Return a corrected page while preserving block coordinates and provenance."""


class NoOpRefinementProvider(RefinementProvider):
    def refine_page(self, page: DocumentPage) -> DocumentPage:
        return page
