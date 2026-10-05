from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import AwareDatetime, BaseModel, ConfigDict
from uuid import UUID
from typing import Any
from datetime import date

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default: str | Any = Field(default=None, union_mode='left_to_right')
    default_wide: str | Any = Field(default=None, union_mode='left_to_right')
    centered_background: str | Any = Field(default=None, union_mode='left_to_right')
    centered_background_small: str | Any = Field(default=None, union_mode='left_to_right')
    cover_artwork: str | Any = Field(default=None, union_mode='left_to_right')
    cover_artwork_horizontal: str | Any = Field(default=None, union_mode='left_to_right')
    cover_artwork_square: str | Any = Field(default=None, union_mode='left_to_right')
    poster_with_logo: str | Any = Field(default=None, union_mode='left_to_right')
    logo_left: str | Any = Field(default=None, union_mode='left_to_right')
    logo_centered: str | Any = Field(default=None, union_mode='left_to_right')
    content_logo_monochromatic: str | Any = Field(default=None, union_mode='left_to_right')
    content_logo_polychromatic: str | Any = Field(default=None, union_mode='left_to_right')

class RelatedItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_key: UUID | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    summary: Any | None = None
    genres: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    maturity_rating: str | Any = Field(default=None, union_mode='left_to_right')
    images: Images | Any = Field(default=None, union_mode='left_to_right')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_key: UUID | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    summary: str | Any = Field(default=None, union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    maturity_rating: Any | None = None
    images: Images | Any = Field(default=None, union_mode='left_to_right')

class Carousel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_id: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    titles: list[Title] | Any = Field(default=None, union_mode='left_to_right')

class ParsedMovieModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_key: UUID | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    summary: str | Any = Field(default=None, union_mode='left_to_right')
    release_year: int | Any = Field(default=None, union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    primary_genre: str | Any = Field(default=None, union_mode='left_to_right')
    brands: list[str] | Any = Field(default=None, union_mode='left_to_right')
    maturity_rating: str | Any = Field(default=None, union_mode='left_to_right')
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    start_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    end_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    trailer_url: str | Any = Field(default=None, union_mode='left_to_right')
    cast: list[str] | Any = Field(default=None, union_mode='left_to_right')
    directors: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    writers: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    producers: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    creators: list[str] | Any = Field(default=None, union_mode='left_to_right')
    release_date: date | str | Any = Field(default=None, union_mode='left_to_right')
    runtime: str | Any = Field(default=None, union_mode='left_to_right')
    related: list[RelatedItem] | Any = Field(default=None, union_mode='left_to_right')
    carousels: list[Carousel] | Any = Field(default=None, union_mode='left_to_right')
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
