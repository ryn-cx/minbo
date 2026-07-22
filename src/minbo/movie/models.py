from pydantic import AwareDatetime, ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel
from typing import Any
from uuid import UUID
from datetime import date

class Flags(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    has_audio_description: bool = Field(..., alias='hasAudioDescription')
    is_uhd: bool = Field(..., alias='isUHD')
    has_dolby_atmos: bool = Field(..., alias='hasDolbyAtmos')
    has_dolby_vision: bool = Field(..., alias='hasDolbyVision')
    has_pse_advisory: bool = Field(..., alias='hasPSEAdvisory')

class Trailer(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    program_id: None = Field(..., alias='programId')
    edit_id: None = Field(..., alias='editId')
    title: None
    description: None
    url: None

class OfferingDates(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    start_date: AwareDatetime = Field(..., alias='startDate')
    end_date: AwareDatetime = Field(..., alias='endDate')

class Title(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    short: str
    full: str

class Credits(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    starring: str
    directors: str
    writers: str
    producers: str
    creators: str
    sources: str
    sign_interpreters: str = Field(..., alias='signInterpreters')

class ActorItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    name: str

class CastAndCrew(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    actor: list[ActorItem] = Field(..., alias='Actor')
    cast: None = Field(..., alias='Cast')
    producer: None = Field(..., alias='Producer')
    director: None = Field(..., alias='Director')
    writer: None = Field(..., alias='Writer')

class Summary(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    short: str
    full: str

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    default_wide: str = Field(..., alias='default-wide')
    default: str
    centered_background_small: str = Field(..., alias='centered-background-small')
    centered_background: str = Field(..., alias='centered-background')
    cover_artwork: str = Field(..., alias='cover-artwork')
    logo_left: str = Field(..., alias='logo-left')
    content_logo_monochromatic: str = Field(..., alias='content-logo-monochromatic')
    logo_centered: str = Field(..., alias='logo-centered')
    poster_with_logo: str = Field(..., alias='poster-with-logo')
    content_logo_polychromatic: str = Field(..., alias='content-logo-polychromatic')
    cover_artwork_horizontal: str = Field(..., alias='cover-artwork-horizontal')
    cover_artwork_square: str = Field(..., alias='cover-artwork-square')

class LocalizedRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    rating_authority: str
    classifier: str
    descriptors: list[None]

class MovieModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image_url_link: str = Field(..., alias='imageUrlLink')
    feature_id: UUID = Field(..., alias='featureId')
    hbomax_id: UUID = Field(..., alias='hbomaxId')
    flags: Flags
    trailer: Trailer
    genres: list[str]
    brand: list[str]
    category: None
    rating_code: list[None] = Field(..., alias='ratingCode')
    offering_dates: OfferingDates = Field(..., alias='offeringDates')
    title: Title
    credits: Credits
    cast_and_crew: CastAndCrew = Field(..., alias='castAndCrew')
    summary: Summary
    images: Images
    status: str
    rating: dict[str, Any]
    runtime: None
    quality: None
    primary_genre: str = Field(..., alias='primaryGenre')
    secondary_genre: str = Field(..., alias='secondaryGenre')
    genres_formatted: str = Field(..., alias='genresFormatted')
    release_year: str = Field(..., alias='releaseYear')
    release_date: date = Field(..., alias='releaseDate')
    localized_rating: LocalizedRating = Field(..., alias='localizedRating')
