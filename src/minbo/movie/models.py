# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ParsedMovieModel as OptionalModel
from .strict_models import ParsedMovieModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Carousel,
        Images,
        ParsedMovieModel,
        RelatedItem,
        Title,
    )
else:
    from .optional_models import (
        Carousel,
        Images,
        ParsedMovieModel,
        RelatedItem,
        Title,
    )

__all__ = [
    "Carousel",
    "Images",
    "ParsedMovieModel",
    "RelatedItem",
    "Title",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ParsedMovieModel:
    """Read a downloaded file into ParsedMovieModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
