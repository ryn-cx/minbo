from pydantic import AwareDatetime, ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel
from uuid import UUID
from typing import Any

class Flags(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    has_audio_description: bool = Field(..., alias='hasAudioDescription')
    is_uhd: bool = Field(..., alias='isUHD')
    has_dolby_atmos: bool = Field(..., alias='hasDolbyAtmos')
    has_dolby_vision: bool = Field(..., alias='hasDolbyVision')
    has_pse_advisory: bool = Field(..., alias='hasPSEAdvisory')

class Trailer(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    program_id: UUID | None = Field(..., alias='programId')
    edit_id: UUID | None = Field(..., alias='editId')
    title: str | None
    description: str | None
    url: str | None

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
    default: str
    centered_background_small: str = Field(..., alias='centered-background-small')
    cover_artwork: str = Field(..., alias='cover-artwork')

class Flags1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    is_watch_free: bool = Field(..., alias='isWatchFree')

class Episode(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    series_id: None = Field(..., alias='seriesId')
    season_number: None = Field(..., alias='seasonNumber')
    episode_number: int = Field(..., alias='episodeNumber')
    quality: str
    images: Images
    flags: Flags1
    episode_url: str = Field(..., alias='episodeUrl')
    offering_dates: OfferingDates = Field(..., alias='offeringDates')
    title: Title
    summary: Summary

class Season(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    season_id: UUID = Field(..., alias='seasonId')
    orgtitle: None
    season_number: int = Field(..., alias='seasonNumber')
    season_number_slug: str = Field(..., alias='seasonNumberSlug')
    number_of_episodes: int = Field(..., alias='numberOfEpisodes')
    title: Title
    summary: Summary
    episodes: list[Episode]

class Images1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    default_wide: str = Field(..., alias='default-wide')
    centered_background_small: str = Field(..., alias='centered-background-small')
    default: str
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
    descriptors: list[str]

class ShowModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image_url_link: str = Field(..., alias='imageUrlLink')
    category: None
    hbomax_id: UUID = Field(..., alias='hbomaxId')
    series_id: UUID = Field(..., alias='seriesId')
    series_title_id: None = Field(..., alias='seriesTitleId')
    flags: Flags
    trailer: Trailer
    genres: list[str]
    brand: list[str]
    episode_count: None = Field(..., alias='episodeCount')
    rating_code: list[None] = Field(..., alias='ratingCode')
    offering_dates: OfferingDates = Field(..., alias='offeringDates')
    title: Title
    credits: Credits
    cast_and_crew: CastAndCrew = Field(..., alias='castAndCrew')
    seasons: list[Season]
    summary: Summary
    images: Images1
    status: str
    rating: dict[str, Any]
    localized_rating: LocalizedRating = Field(..., alias='localizedRating')
    number_of_seasons: int = Field(..., alias='numberOfSeasons')
    number_of_episodes: int = Field(..., alias='numberOfEpisodes')
    quality: str
    primary_genre: str = Field(..., alias='primaryGenre')
    secondary_genre: str = Field(..., alias='secondaryGenre')
    genres_formatted: str = Field(..., alias='genresFormatted')
    release_year: str = Field(..., alias='releaseYear')
