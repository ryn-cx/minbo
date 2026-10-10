from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import AwareDatetime, BaseModel, ConfigDict
from typing import Any
from datetime import timedelta
from uuid import UUID

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

class Images1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default: str | Any = Field(default=None, union_mode='left_to_right')
    default_wide: str | Any = Field(default=None, union_mode='left_to_right')
    centered_background: Any | None = None
    centered_background_small: str | Any = Field(default=None, union_mode='left_to_right')
    cover_artwork: str | Any = Field(default=None, union_mode='left_to_right')
    cover_artwork_horizontal: Any | None = None
    cover_artwork_square: Any | None = None
    poster_with_logo: Any | None = None
    logo_left: Any | None = None
    logo_centered: Any | None = None
    content_logo_monochromatic: Any | None = None
    content_logo_polychromatic: Any | None = None

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    episode_number: int | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    summary: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    images: Images1 | Any = Field(default=None, union_mode='left_to_right')
    start_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    end_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: UUID | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    name: Any | None = None
    summary: Any | None = None
    episode_count: int | Any = Field(default=None, union_mode='left_to_right')
    episodes: list[Episode] | Any = Field(default=None, union_mode='left_to_right')

class Images2(BaseModel):
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
    images: Images2 | Any = Field(default=None, union_mode='left_to_right')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_key: UUID | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    summary: str | Any = Field(default=None, union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    maturity_rating: Any | None = None
    images: Images2 | Any = Field(default=None, union_mode='left_to_right')

class Carousel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_id: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    titles: list[Title] | Any = Field(default=None, union_mode='left_to_right')

class ParsedShowModel(BaseModel):
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
    directors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    writers: list[str] | Any = Field(default=None, union_mode='left_to_right')
    producers: list[str] | Any = Field(default=None, union_mode='left_to_right')
    creators: list[str] | Any = Field(default=None, union_mode='left_to_right')
    sources: list[str] | Any = Field(default=None, union_mode='left_to_right')
    sign_interpreters: list[str] | Any = Field(default=None, union_mode='left_to_right')
    season_count: int | Any = Field(default=None, union_mode='left_to_right')
    episode_count: int | Any = Field(default=None, union_mode='left_to_right')
    seasons: list[Season] | Any = Field(default=None, union_mode='left_to_right')
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
