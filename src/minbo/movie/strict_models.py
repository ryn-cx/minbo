from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel
from uuid import UUID
from typing import Any
from datetime import date

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    default: str
    default_wide: str
    centered_background: str
    centered_background_small: str
    cover_artwork: str
    cover_artwork_horizontal: str
    cover_artwork_square: str
    poster_with_logo: str
    logo_left: str
    logo_centered: str
    content_logo_monochromatic: str
    content_logo_polychromatic: str

class Images1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    default: str | None
    default_wide: str | None
    centered_background: str | None
    centered_background_small: str | None
    cover_artwork: str | None
    cover_artwork_horizontal: str
    cover_artwork_square: str | None
    poster_with_logo: str | None
    logo_left: str
    logo_centered: str | None
    content_logo_monochromatic: str
    content_logo_polychromatic: str | None

class RelatedItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_key: UUID
    media_type: str
    url: str
    title: str
    summary: None
    genres: list[None]
    maturity_rating: None
    images: Images1

class Images2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    default: str
    default_wide: str
    centered_background: str
    centered_background_small: str
    cover_artwork: str
    cover_artwork_horizontal: str
    cover_artwork_square: str
    poster_with_logo: str
    logo_left: str
    logo_centered: str
    content_logo_monochromatic: str
    content_logo_polychromatic: str

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_key: UUID
    media_type: str
    url: str
    title: str
    summary: str
    genres: list[str]
    maturity_rating: None
    images: Images2

class Carousel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    collection_id: str
    title: str
    titles: list[Title]

class ParsedMovieModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_key: UUID
    url: str
    title: str
    summary: str
    release_year: int
    genres: list[str]
    primary_genre: str
    brands: list[str]
    maturity_rating: str
    images: Images
    start_date: AwareDatetime
    end_date: AwareDatetime
    trailer_url: str | None
    cast: list[str]
    directors: list[None]
    writers: list[None]
    producers: list[None]
    creators: list[None]
    release_date: date | str = Field(union_mode='left_to_right')
    runtime: str
    related: list[RelatedItem]
    carousels: list[Carousel]
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
