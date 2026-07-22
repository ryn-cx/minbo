from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field
from typing import Any
from uuid import UUID

class Attributes(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    canonical: bool
    url: str

class Data1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str

class Target(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data1

class Relationships(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    target: Target

class Data(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    attributes: Attributes
    id: str
    relationships: Relationships
    type: str

class Default(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    background_color: str = Field(..., alias='backgroundColor')
    border_color: str = Field(..., alias='borderColor')
    font_color: str = Field(..., alias='fontColor')

class Secondary(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    background_color: str = Field(..., alias='backgroundColor')
    border_color: str = Field(..., alias='borderColor')
    font_color: str = Field(..., alias='fontColor')

class Styles(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    default: Default
    secondary: Secondary

class CustomAttributes(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    grid: bool
    tile_metadata: str = Field(..., alias='tileMetadata')

class Option(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    accessibility_title: str = Field(..., alias='accessibilityTitle')
    id: str
    parameter: str
    value: str

class Filter(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    multi_select: bool = Field(..., alias='multiSelect')
    options: list[Option]

class Component(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    custom_attributes: CustomAttributes | None = Field(None, alias='customAttributes')
    filters: list[Filter] | None = None
    id: str
    mandatory_params: str | None = Field(None, alias='mandatoryParams')
    template_id: str = Field(..., alias='templateId')

class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    from_: None = Field(..., alias='from')
    to: AwareDatetime

class ContentAction(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    code: str
    requirements: list[None]
    availability: Availability

class WpoConstraints(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    deduplicate_items: bool = Field(..., alias='deduplicateItems')
    deduplicate_source: bool = Field(..., alias='deduplicateSource')

class VideoCountByType(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    episode: int = Field(..., alias='EPISODE')
    extra: int | None = Field(None, alias='EXTRA')

class Icon(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    uri: str

class Label(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    label: str

class Title(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    a11y: str
    label: str

class Elements(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    icon: Icon | None = None
    label: Label | None = None
    title: Title | None = None

class TemplateParams(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str

class Feedback(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    a11y: str

class Elements1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    feedback: Feedback
    icon: Icon
    label: Label

class Off(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    a11y: str
    elements: Elements1

class Feedback1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    label: str

class Elements2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    feedback: Feedback1
    icon: Icon
    label: Label

class On(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    a11y: str
    elements: Elements2

class Option1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    off: Off
    on: On
    value: str

class FeedbackEmpty(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    label: str

class FeedbackIcon(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    uri: str

class Loading(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    a11y: str
    label: str

class LoadingIcon(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    uri: str

class Elements3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    feedback: Feedback1
    feedback_empty: FeedbackEmpty = Field(..., alias='feedbackEmpty')
    feedback_icon: FeedbackIcon = Field(..., alias='feedbackIcon')
    icon: Icon
    label: Label
    loading: Loading
    loading_icon: LoadingIcon = Field(..., alias='loadingIcon')

class Off1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    a11y: str
    elements: Elements3

class Elements4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    feedback: Feedback1
    feedback_icon: FeedbackIcon = Field(..., alias='feedbackIcon')
    icon: Icon
    label: Label
    loading: Loading
    loading_icon: LoadingIcon = Field(..., alias='loadingIcon')

class On1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    a11y: str
    elements: Elements4

class Attributes1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    accessibility_text: str | None = Field(None, alias='accessibilityText')
    badge_type: str | None = Field(None, alias='badgeType')
    display_text: str | None = Field(None, alias='displayText')
    styles: Styles | None = None
    alternate_id: UUID | str | None = Field(None, alias='alternateId', union_mode='left_to_right')
    channel_code: str | None = Field(None, alias='channelCode')
    is_favorite: bool | None = Field(None, alias='isFavorite')
    name: str | None = None
    alias: str | None = None
    component: Component | None = None
    kind: str | None = None
    revision: int | None = None
    code: str | None = None
    system: str | None = None
    aspect_ratio: float | None = Field(None, alias='aspectRatio')
    audio_tracks: list[str] | None = Field(None, alias='audioTracks')
    content_actions: list[ContentAction] | None = Field(None, alias='contentActions')
    duration: int | None = None
    playable_end: AwareDatetime | None = Field(None, alias='playableEnd')
    playable_start: AwareDatetime | None = Field(None, alias='playableStart')
    subtitles: list[str] | None = None
    height: int | None = None
    src: str | None = None
    width: int | None = None
    a11y: str | None = None
    label: str | None = None
    page_metadata_title: str | None = Field(None, alias='pageMetadataTitle')
    title: str | None = None
    wpo_constraints: WpoConstraints | None = Field(None, alias='wpoConstraints')
    canonical: bool | None = None
    url: str | None = None
    description: str | None = None
    display_name: str | None = Field(None, alias='displayName')
    kids_content: bool | None = Field(None, alias='kidsContent')
    long_description: str | None = Field(None, alias='longDescription')
    season_number: int | None = Field(None, alias='seasonNumber')
    video_count_by_type: VideoCountByType | None = Field(None, alias='videoCountByType')
    first_available_date: AwareDatetime | None = Field(None, alias='firstAvailableDate')
    is_family_content: bool | None = Field(None, alias='isFamilyContent')
    is_kids_content: bool | None = Field(None, alias='isKidsContent')
    original_name: str | None = Field(None, alias='originalName')
    premiere_date: AwareDatetime | None = Field(None, alias='premiereDate')
    show_type: str | None = Field(None, alias='showType')
    is_new: bool | None = Field(None, alias='isNew')
    number_of_new_episodes: int | None = Field(None, alias='numberOfNewEpisodes')
    background_color: str | None = Field(None, alias='backgroundColor')
    border_color: str | None = Field(None, alias='borderColor')
    font_color: str | None = Field(None, alias='fontColor')
    action_type: str | None = Field(None, alias='actionType')
    context: str | None = None
    elements: Elements | None = None
    template: str | None = None
    template_params: TemplateParams | None = Field(None, alias='templateParams')
    initial_state: str | None = Field(None, alias='initialState')
    options: list[Option1] | None = None
    off: Off1 | None = None
    on: On1 | None = None
    video_type: str | None = Field(None, alias='videoType')

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum]

class Routes(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum]

class Items(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum]

class Data2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    type: str

class DefaultAction(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data2

class Show(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data2

class Datum3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    type: str

class UserActions(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum3]

class Datum4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str

class Badges(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum4]

class Highlights(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum4]

class ContentRatingSystem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data2

class Datum6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    type: str

class Advisories(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class Data5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str

class Style(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data5

class Collection(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data5

class RatingDescriptors(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class Ratings(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class Data7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    type: str

class PrimaryChannel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data7

class Data8(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str

class ShortPreviewVideo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data8

class TrailerVideo(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data8

class TxCategory(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class TxCorporateGenre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class TxGenres(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class Seasons(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class TxSeriestype(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class TxAvailabilityMessaging(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class AlternateChannels(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum6]

class Route(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data8

class ActionTemplate(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data8

class Data12(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID | str = Field(union_mode='left_to_right')
    type: str

class Edit(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data12

class Relationships1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    images: Images | None = None
    routes: Routes | None = None
    items: Items | None = None
    default_action: DefaultAction | None = Field(None, alias='defaultAction')
    show: Show | None = None
    user_actions: UserActions | None = Field(None, alias='userActions')
    badges: Badges | None = None
    highlights: Highlights | None = None
    content_rating_system: ContentRatingSystem | None = Field(None, alias='contentRatingSystem')
    advisories: Advisories | None = None
    style: Style | None = None
    collection: Collection | None = None
    rating_descriptors: RatingDescriptors | None = Field(None, alias='ratingDescriptors')
    ratings: Ratings | None = None
    primary_channel: PrimaryChannel | None = Field(None, alias='primaryChannel')
    short_preview_video: ShortPreviewVideo | None = Field(None, alias='shortPreviewVideo')
    trailer_video: TrailerVideo | None = Field(None, alias='trailerVideo')
    tx_category: TxCategory | None = Field(None, alias='txCategory')
    tx_corporate_genre: TxCorporateGenre | None = Field(None, alias='txCorporate-genre')
    tx_genres: TxGenres | None = Field(None, alias='txGenres')
    seasons: Seasons | None = None
    tx_seriestype: TxSeriestype | None = Field(None, alias='txSeriestype')
    tx_availability_messaging: TxAvailabilityMessaging | None = Field(None, alias='txAvailabilityMessaging')
    alternate_channels: AlternateChannels | None = Field(None, alias='alternateChannels')
    route: Route | None = None
    action_template: ActionTemplate | None = Field(None, alias='actionTemplate')
    edit: Edit | None = None

class Overlay(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str

class Analytics(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    component_id: str | None = Field(None, alias='componentId')
    id: str | None = None
    type: str
    content_id: UUID | None = Field(None, alias='contentId')
    content_type: str | None = Field(None, alias='contentType')
    overlays: list[Overlay] | None = None

class Meta(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    analytics: Analytics
    items_current_page: int | None = Field(None, alias='itemsCurrentPage')
    items_page_size: int | None = Field(None, alias='itemsPageSize')
    items_total_pages: int | None = Field(None, alias='itemsTotalPages')
    items_total_results: int | None = Field(None, alias='itemsTotalResults')
    refresh_before: AwareDatetime | None = Field(None, alias='refreshBefore')

class IncludedItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    attributes: Attributes1 | None = None
    id: UUID | str = Field(union_mode='left_to_right')
    type: str
    relationships: Relationships1 | None = None
    meta: Meta | None = None

class Attributes2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    brand_id: str = Field(..., alias='brandId')
    theme: str

class Site(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    attributes: Attributes2
    id: str
    type: str

class Meta1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    site: Site

class SearchModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: Data
    included: list[IncludedItem]
    meta: Meta1
