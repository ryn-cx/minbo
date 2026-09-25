from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import AwareDatetime, BaseModel, ConfigDict
from uuid import UUID
from typing import Any
from datetime import date

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default: str | None = None
    default_wide: str | None = None
    centered_background: str | None = None
    centered_background_small: str | None = None
    cover_artwork: str | None = None
    cover_artwork_horizontal: str | None = None
    cover_artwork_square: str | None = None
    poster_with_logo: str | None = None
    logo_left: str | None = None
    logo_centered: str | None = None
    content_logo_monochromatic: str | None = None
    content_logo_polychromatic: str | None = None

class RelatedItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_key: UUID | None = None
    media_type: str | None = None
    url: str | None = None
    title: str | None = None
    summary: Any | None = None
    genres: list[Any] | None = None
    maturity_rating: Any | None = None
    images: Images | None = None

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_key: UUID | None = None
    media_type: str | None = None
    url: str | None = None
    title: str | None = None
    summary: str | None = None
    genres: list[str] | None = None
    maturity_rating: Any | None = None
    images: Images | None = None

class Carousel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_id: str | None = None
    title: str | None = None
    titles: list[Title] | None = None

class ParsedMovieModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_key: UUID | None = None
    url: str | None = None
    title: str | None = None
    summary: str | None = None
    release_year: int | None = None
    genres: list[str] | None = None
    primary_genre: str | None = None
    brands: list[str] | None = None
    maturity_rating: str | None = None
    images: Images | None = None
    start_date: AwareDatetime | None = None
    end_date: AwareDatetime | None = None
    trailer_url: str | None = None
    cast: list[str] | None = None
    directors: list[Any] | None = None
    writers: list[Any] | None = None
    producers: list[Any] | None = None
    creators: list[Any] | None = None
    release_date: date | str | None = Field(default=None, union_mode='left_to_right')
    runtime: str | None = None
    related: list[RelatedItem] | None = None
    carousels: list[Carousel] | None = None
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
