# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ParsedSitemapModel as OptionalModel
from .strict_models import ParsedSitemapModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        ParsedSitemapModel,
        Title,
    )
else:
    from .optional_models import (
        ParsedSitemapModel,
        Title,
    )

__all__ = [
    "ParsedSitemapModel",
    "Title",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ParsedSitemapModel:
    """Read a downloaded file into ParsedSitemapModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
