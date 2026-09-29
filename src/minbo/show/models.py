# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ParsedShowModel as OptionalModel
from .strict_models import ParsedShowModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Carousel,
        Episode,
        Images,
        Images1,
        Images2,
        ParsedShowModel,
        RelatedItem,
        Season,
        Title,
    )
else:
    from .optional_models import (
        Carousel,
        Episode,
        Images,
        Images1,
        Images2,
        ParsedShowModel,
        RelatedItem,
        Season,
        Title,
    )

__all__ = [
    "Carousel",
    "Episode",
    "Images",
    "Images1",
    "Images2",
    "ParsedShowModel",
    "RelatedItem",
    "Season",
    "Title",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ParsedShowModel:
    """Read a downloaded file into ParsedShowModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
