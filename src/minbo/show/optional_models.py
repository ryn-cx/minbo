from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID
from datetime import timedelta

class DeveloperPanelConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    enabled: bool | None = None
    minimized: bool | None = None

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore')
    lg: int | None = None

class Indicator(BaseModel):
    model_config = ConfigDict(extra='ignore')
    badge: int | None = None

class Option(BaseModel):
    model_config = ConfigDict(extra='ignore')
    checkbox: int | None = None

class Input(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field: int | None = None
    option: Option | None = None
    toggle: int | None = None
    toggle_thumb: int | None = None

class Corner(BaseModel):
    model_config = ConfigDict(extra='ignore')
    action: Action | None = None
    full: int | None = None
    indicator: Indicator | None = None
    input: Input | None = None
    lg: int | None = None
    md: int | None = None
    none: int | None = None
    sm: int | None = None

class Chip(BaseModel):
    model_config = ConfigDict(extra='ignore')
    selected: int | None = None
    unselected: int | None = None

class Option1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    emphasis: int | None = None
    selected: int | None = None
    unselected: int | None = None

class Toggle(BaseModel):
    model_config = ConfigDict(extra='ignore')
    emphasis: float | None = None
    selected: int | None = None
    unselected: int | None = None

class Input1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    option: Option1 | None = None
    toggle: Toggle | None = None

class Notify(BaseModel):
    model_config = ConfigDict(extra='ignore')
    container_border: int | None = None

class Stroke(BaseModel):
    model_config = ConfigDict(extra='ignore')
    bold: int | None = None
    chip: Chip | None = None
    extra_bold: int | None = None
    input: Input1 | None = None
    medium: float | None = None
    none: int | None = None
    notify: Notify | None = None
    regular: int | None = None
    thin: float | None = None

class BorderToken(BaseModel):
    model_config = ConfigDict(extra='ignore')
    corner: Corner | None = None
    stroke: Stroke | None = None

class Alt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    surface_00: str | None = None
    surface_01: str | None = None
    surface_01_film: str | None = None
    surface_01_glass: str | None = None

class Base(BaseModel):
    model_config = ConfigDict(extra='ignore')
    scrim_01: str | None = None
    scrim_02: str | None = None
    surface_00: str | None = None
    surface_00_smoke: str | None = None
    surface_01: str | None = None
    surface_01_film: str | None = None
    surface_01_smoke: str | None = None
    surface_02: str | None = None
    surface_03: str | None = None
    surface_accent: str | None = None

class Background(BaseModel):
    model_config = ConfigDict(extra='ignore')
    alt: Alt | None = None
    base: Base | None = None

class Plan(BaseModel):
    model_config = ConfigDict(extra='ignore')
    base_fill: str | None = None
    base_text: str | None = None
    special_fill: str | None = None
    special_text: str | None = None
    tab_fill: str | None = None
    tab_text: str | None = None

class Badge(BaseModel):
    model_config = ConfigDict(extra='ignore')
    fill_highlight_free: str | None = None
    fill_tile_free: str | None = None
    outline_highlight_free: str | None = None
    plan: Plan | None = None
    text_highlight_free: str | None = None
    text_tile_free: str | None = None

class Button(BaseModel):
    model_config = ConfigDict(extra='ignore')
    fill_loud: str | None = None
    fill_loud_hover: str | None = None
    fill_quiet: str | None = None
    fill_quiet_hover: str | None = None
    label_loud: str | None = None
    outline_quiet: str | None = None
    outline_quiet_hover: str | None = None

class Chip1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    fill_selected: str | None = None
    outline_selected: str | None = None
    outline_unselected: str | None = None

class Fill(BaseModel):
    model_config = ConfigDict(extra='ignore')
    action_accent: str | None = None
    action_accent_dim: str | None = None
    action_accent_film: str | None = None
    action_default: str | None = None
    action_disabled_01: str | None = None
    action_disabled_02: str | None = None
    action_light: str | None = None
    action_quiet: str | None = None
    action_shade: str | None = None
    brand_dark: str | None = None
    indicator_advertisement: str | None = None
    indicator_background: str | None = None
    indicator_foreground: str | None = None
    indicator_live: str | None = None
    indicator_quiet: str | None = None
    notify_error: str | None = None
    notify_message: str | None = None
    skeleton: str | None = None
    skeleton_pressed: str | None = None

class Onalt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text_01: str | None = None
    text_02: str | None = None
    text_03: str | None = None

class Onbase(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text_01: str | None = None
    text_02: str | None = None
    text_03: str | None = None
    text_action_accent: str | None = None
    text_action_accent_pressed: str | None = None
    text_notify_error: str | None = None
    text_notify_message: str | None = None

class Foreground(BaseModel):
    model_config = ConfigDict(extra='ignore')
    onalt: Onalt | None = None
    onbase: Onbase | None = None

class Indicator1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    fill_background: str | None = None
    fill_foreground_loud: str | None = None

class FieldModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    action_fill_focus: str | None = None
    action_icon_focus: str | None = None
    action_icon_on_focus: str | None = None
    fill_focus: str | None = None
    text_focus: str | None = None

class Option2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    fill_radio_selected: str | None = None
    outline_selected: str | None = None
    outline_unselected: str | None = None
    text_label: str | None = None

class Toggle1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    icon_thumb: str | None = None
    outline_selected: str | None = None
    outline_unselected: str | None = None

class Input2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field: FieldModel | None = None
    option: Option2 | None = None
    outline_active: str | None = None
    outline_error: str | None = None
    outline_inactive: str | None = None
    toggle: Toggle1 | None = None

class Keyboard(BaseModel):
    model_config = ConfigDict(extra='ignore')
    focus_alt: str | None = None
    focus_base: str | None = None

class Banner(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text_error: str | None = None
    text_message: str | None = None

class Notify1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    banner: Banner | None = None
    icon_error: str | None = None
    icon_message: str | None = None
    outline_error: str | None = None
    outline_message: str | None = None

class Onbase1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    outline_01: str | None = None
    outline_02: str | None = None
    outline_03: str | None = None
    outline_04: str | None = None

class Stroke1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    onbase: Onbase1 | None = None

class ColorToken(BaseModel):
    model_config = ConfigDict(extra='ignore')
    background: Background | None = None
    badge: Badge | None = None
    button: Button | None = None
    chip: Chip1 | None = None
    fill: Fill | None = None
    foreground: Foreground | None = None
    indicator: Indicator1 | None = None
    input: Input2 | None = None
    keyboard: Keyboard | None = None
    notify: Notify1 | None = None
    stroke: Stroke1 | None = None
    transparent: str | None = None

class Gutter(BaseModel):
    model_config = ConfigDict(extra='ignore')
    bp_01: int | None = None
    bp_03: int | None = None
    bp_04: int | None = None
    bp_05: int | None = None
    bp_06: int | None = None

class Margin(BaseModel):
    model_config = ConfigDict(extra='ignore')
    bp_01: int | None = None
    bp_03: int | None = None
    bp_04: int | None = None
    bp_05: int | None = None
    bp_06: int | None = None

class MarginOffset(BaseModel):
    model_config = ConfigDict(extra='ignore')
    bp_01: int | None = None
    bp_03: int | None = None
    bp_04: int | None = None
    bp_05: int | None = None
    bp_06: int | None = None

class Vertical(BaseModel):
    model_config = ConfigDict(extra='ignore')
    bp_01: int | None = None
    bp_03: int | None = None
    bp_04: int | None = None
    bp_05: int | None = None
    bp_06: int | None = None

class Universal(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_12: int | None = Field(None, alias='_12')
    field_16: int | None = Field(None, alias='_16')
    field_20: int | None = Field(None, alias='_20')
    field_24: int | None = Field(None, alias='_24')
    field_28: int | None = Field(None, alias='_28')
    field_32: int | None = Field(None, alias='_32')
    field_36: int | None = Field(None, alias='_36')
    field_40: int | None = Field(None, alias='_40')
    field_44: int | None = Field(None, alias='_44')
    field_48: int | None = Field(None, alias='_48')
    field_60: int | None = Field(None, alias='_60')
    field_68: int | None = Field(None, alias='_68')
    field_72: int | None = Field(None, alias='_72')
    field_80: int | None = Field(None, alias='_80')
    field_100: int | None = Field(None, alias='_100')
    field_120: int | None = Field(None, alias='_120')
    field_00: int | None = Field(None, alias='_00')
    field_02: int | None = Field(None, alias='_02')
    field_04: int | None = Field(None, alias='_04')
    field_08: int | None = Field(None, alias='_08')

class SpacerToken(BaseModel):
    model_config = ConfigDict(extra='ignore')
    gutter: Gutter | None = None
    margin: Margin | None = None
    margin_offset: MarginOffset | None = None
    vertical: Vertical | None = None
    universal: Universal | None = None

class Page(BaseModel):
    model_config = ConfigDict(extra='ignore')
    surface_accent: str | None = Field(None, alias='surface-accent')
    surface_00: str | None = Field(None, alias='surface-00')
    surface_default: str | None = Field(None, alias='surface-default')
    surface_basic: str | None = Field(None, alias='surface-basic')

class Band(BaseModel):
    model_config = ConfigDict(extra='ignore')
    surface_fill_01: str | None = Field(None, alias='surface-fill-01')
    surface_fill_02: str | None = Field(None, alias='surface-fill-02')
    action_light: str | None = Field(None, alias='action-light')
    action_default: str | None = Field(None, alias='action-default')
    surface_fill_gradient_01: str | None = Field(None, alias='surface-fill-gradient-01')
    surface_fill_gradient_02: str | None = Field(None, alias='surface-fill-gradient-02')

class Column(BaseModel):
    model_config = ConfigDict(extra='ignore')
    surface_fill_01: str | None = Field(None, alias='surface-fill-01')
    surface_fill_02: str | None = Field(None, alias='surface-fill-02')
    action_light: str | None = Field(None, alias='action-light')
    action_default: str | None = Field(None, alias='action-default')
    surface_fill_gradient_01: str | None = Field(None, alias='surface-fill-gradient-01')
    surface_fill_gradient_02: str | None = Field(None, alias='surface-fill-gradient-02')

class Backgrounds(BaseModel):
    model_config = ConfigDict(extra='ignore')
    page: Page | None = None
    band: Band | None = None
    column: Column | None = None

class ResolvedTheme(BaseModel):
    model_config = ConfigDict(extra='ignore')
    border_token: BorderToken | None = Field(None, alias='BorderToken')
    color_token: ColorToken | None = Field(None, alias='ColorToken')
    spacer_token: SpacerToken | None = Field(None, alias='SpacerToken')
    backgrounds: Backgrounds | None = None
    font_family: str | None = Field(None, alias='fontFamily')

class AuthState(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class SignIn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class User(BaseModel):
    model_config = ConfigDict(extra='ignore')
    auth_state: AuthState | None = Field(None, alias='authState')
    sign_in: SignIn | None = Field(None, alias='signIn')

class PageView(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class PageName(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class AnalyticsTitle(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class PreviousPageName(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class SiteSection(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class PageCategory(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class UserCountry(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class UserLanguage(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class UserRegion(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class UserCity(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class UserContinent(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Navigation(BaseModel):
    model_config = ConfigDict(extra='ignore')
    page_view: PageView | None = Field(None, alias='pageView')
    page_name: PageName | None = Field(None, alias='pageName')
    analytics_title: AnalyticsTitle | None = Field(None, alias='analyticsTitle')
    previous_page_name: PreviousPageName | None = Field(None, alias='previousPageName')
    site_section: SiteSection | None = Field(None, alias='siteSection')
    page_category: PageCategory | None = Field(None, alias='pageCategory')
    user_country: UserCountry | None = Field(None, alias='userCountry')
    user_language: UserLanguage | None = Field(None, alias='userLanguage')
    user_region: UserRegion | None = Field(None, alias='userRegion')
    user_city: UserCity | None = Field(None, alias='userCity')
    user_continent: UserContinent | None = Field(None, alias='userContinent')

class ModuleName(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class BandName(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class PageDepth(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Interaction(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class CardType(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class CarouselPosition(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class EventAction(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class ElementType(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class EventLabel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Module(BaseModel):
    model_config = ConfigDict(extra='ignore')
    module_name: ModuleName | None = Field(None, alias='moduleName')
    band_name: BandName | None = Field(None, alias='bandName')
    headline: Headline | None = None
    page_depth: PageDepth | None = Field(None, alias='pageDepth')
    interaction: Interaction | None = None
    card_type: CardType | None = Field(None, alias='cardType')
    carousel_position: CarouselPosition | None = Field(None, alias='carouselPosition')
    event_action: EventAction | None = Field(None, alias='eventAction')
    element_type: ElementType | None = Field(None, alias='elementType')
    event_label: EventLabel | None = Field(None, alias='eventLabel')

class Modal(BaseModel):
    model_config = ConfigDict(extra='ignore')
    event_action: EventAction | None = Field(None, alias='eventAction')
    element_type: ElementType | None = Field(None, alias='elementType')
    event_label: EventLabel | None = Field(None, alias='eventLabel')

class Category(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class VideoType(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class ContentId(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class SeasonNumber(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class EpisodeNumber(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class CurrentTime(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class AltText(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class PlayerAction(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class IsPopupVideo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Autoplay(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Video(BaseModel):
    model_config = ConfigDict(extra='ignore')
    category: Category | None = None
    title: Title | None = None
    video_type: VideoType | None = Field(None, alias='videoType')
    content_id: ContentId | None = Field(None, alias='contentID')
    genre: Genre | None = None
    season_number: SeasonNumber | None = Field(None, alias='seasonNumber')
    episode_number: EpisodeNumber | None = Field(None, alias='episodeNumber')
    current_time: CurrentTime | None = Field(None, alias='currentTime')
    alt_text: AltText | None = Field(None, alias='altText')
    player_action: PlayerAction | None = Field(None, alias='playerAction')
    is_popup_video: IsPopupVideo | None = Field(None, alias='isPopupVideo')
    autoplay: Autoplay | None = None

class LinkUrl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class ContentName(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class ContentCategory(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class CastAndCrew(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class RatingCode(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Brand(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore')
    alt_text: AltText | None = Field(None, alias='altText')
    link_url: LinkUrl | None = Field(None, alias='linkURL')
    content_id: ContentId | None = Field(None, alias='contentID')
    content_name: ContentName | None = Field(None, alias='contentName')
    content_category: ContentCategory | None = Field(None, alias='contentCategory')
    genre: Genre | None = None
    cast_and_crew: CastAndCrew | None = Field(None, alias='castAndCrew')
    rating_code: RatingCode | None = Field(None, alias='ratingCode')
    brand: Brand | None = None
    element_type: ElementType | None = Field(None, alias='elementType')

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Element(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Destination(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Cta(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: Text | None = None
    element: Element | None = None
    destination: Destination | None = None

class GateAction(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class GateElement(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class GatedContentTitle(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Gate(BaseModel):
    model_config = ConfigDict(extra='ignore')
    gate_action: GateAction | None = Field(None, alias='gateAction')
    gate_element: GateElement | None = Field(None, alias='gateElement')
    gated_content_title: GatedContentTitle | None = Field(None, alias='gatedContentTitle')

class EmailSubmissionSuccess(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class B2bFieldValue(BaseModel):
    model_config = ConfigDict(extra='ignore')
    data_layer: str | None = Field(None, alias='dataLayer')

class Email(BaseModel):
    model_config = ConfigDict(extra='ignore')
    email_submission_success: EmailSubmissionSuccess | None = Field(None, alias='emailSubmissionSuccess')
    b2b_field_value: B2bFieldValue | None = Field(None, alias='b2bFieldValue')

class Schemas(BaseModel):
    model_config = ConfigDict(extra='ignore')
    user: User | None = None
    navigation: Navigation | None = None
    module: Module | None = None
    modal: Modal | None = None
    video: Video | None = None
    content: Content | None = None
    cta: Cta | None = None
    gate: Gate | None = None
    email: Email | None = None

class Navigation1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    page_view: list[str] | None = Field(None, alias='pageView')
    page_name: list[str] | None = Field(None, alias='pageName')
    analytics_title: list[str] | None = Field(None, alias='analyticsTitle')
    previous_page_name: list[str] | None = Field(None, alias='previousPageName')
    site_section: list[str] | None = Field(None, alias='siteSection')
    page_category: list[str] | None = Field(None, alias='pageCategory')
    user_country: list[str] | None = Field(None, alias='userCountry')
    user_language: list[str] | None = Field(None, alias='userLanguage')
    user_region: list[str] | None = Field(None, alias='userRegion')
    user_city: list[str] | None = Field(None, alias='userCity')
    user_continent: list[str] | None = Field(None, alias='userContinent')

class User1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    sign_in: list[str] | None = Field(None, alias='signIn')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    content_id: list[str] | None = Field(None, alias='contentID')
    content_name: list[str] | None = Field(None, alias='contentName')
    content_category: list[str] | None = Field(None, alias='contentCategory')
    genre: list[str] | None = None
    cast_and_crew: list[str] | None = Field(None, alias='castAndCrew')
    rating_code: list[str] | None = Field(None, alias='ratingCode')
    brand: list[str] | None = None
    link_url: list[str] | None = Field(None, alias='linkURL')

class PageTrack(BaseModel):
    model_config = ConfigDict(extra='ignore')
    navigation: Navigation1 | None = None
    user: User1 | None = None
    content: Content1 | None = None

class Cta1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: list[str] | None = None
    element: list[str] | None = None
    destination: list[str] | None = None

class Module1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    module_name: list[str] | None = Field(None, alias='moduleName')
    band_name: list[str] | None = Field(None, alias='bandName')
    headline: list[str] | None = None
    page_depth: list[str] | None = Field(None, alias='pageDepth')
    interaction: list[str] | None = None
    card_type: list[str] | None = Field(None, alias='cardType')
    carousel_position: list[str] | None = Field(None, alias='carouselPosition')
    event_action: list[str] | None = Field(None, alias='eventAction')
    element_type: list[str] | None = Field(None, alias='elementType')
    event_label: list[str] | None = Field(None, alias='eventLabel')

class Video1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    category: list[str] | None = None
    title: list[str] | None = None
    video_type: list[str] | None = Field(None, alias='videoType')
    content_id: list[str] | None = Field(None, alias='contentID')
    genre: list[str] | None = None
    season_number: list[str] | None = Field(None, alias='seasonNumber')
    episode_number: list[str] | None = Field(None, alias='episodeNumber')
    alt_text: list[str] | None = Field(None, alias='altText')
    is_popup_video: list[str] | None = Field(None, alias='isPopupVideo')
    autoplay: list[str] | None = None

class Content2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    alt_text: list[str] | None = Field(None, alias='altText')
    link_url: list[str] | None = Field(None, alias='linkURL')
    content_id: list[str] | None = Field(None, alias='contentID')
    content_name: list[str] | None = Field(None, alias='contentName')
    content_category: list[str] | None = Field(None, alias='contentCategory')
    genre: list[str] | None = None
    rating_code: list[str] | None = Field(None, alias='ratingCode')
    brand: list[str] | None = None
    element_type: list[str] | None = Field(None, alias='elementType')

class Click(BaseModel):
    model_config = ConfigDict(extra='ignore')
    cta: Cta1 | None = None
    module: Module1 | None = None
    video: Video1 | None = None
    content: Content2 | None = None

class Module2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    module_name: list[str] | None = Field(None, alias='moduleName')
    band_name: list[str] | None = Field(None, alias='bandName')
    page_depth: list[str] | None = Field(None, alias='pageDepth')
    interaction: list[str] | None = None
    card_type: list[str] | None = Field(None, alias='cardType')
    carousel_position: list[str] | None = Field(None, alias='carouselPosition')

class Video2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    category: list[str] | None = None
    title: list[str] | None = None
    video_type: list[str] | None = Field(None, alias='videoType')
    content_id: list[str] | None = Field(None, alias='contentID')
    genre: list[str] | None = None
    season_number: list[str] | None = Field(None, alias='seasonNumber')
    episode_number: list[str] | None = Field(None, alias='episodeNumber')
    current_time: list[str] | None = Field(None, alias='currentTime')
    player_action: list[str] | None = Field(None, alias='playerAction')
    alt_text: list[str] | None = Field(None, alias='altText')
    is_popup_video: list[str] | None = Field(None, alias='isPopupVideo')
    autoplay: list[str] | None = None

class VideoPlayer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    module: Module2 | None = None
    video: Video2 | None = None

class Module3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    module_name: list[str] | None = Field(None, alias='moduleName')
    band_name: list[str] | None = Field(None, alias='bandName')
    headline: list[str] | None = None
    page_depth: list[str] | None = Field(None, alias='pageDepth')
    interaction: list[str] | None = None

class Gate1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    gate_action: list[str] | None = Field(None, alias='gateAction')
    gate_element: list[str] | None = Field(None, alias='gateElement')
    gated_content_title: list[str] | None = Field(None, alias='gatedContentTitle')

class Gating(BaseModel):
    model_config = ConfigDict(extra='ignore')
    module: Module3 | None = None
    gate: Gate1 | None = None

class Module4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    module_name: list[str] | None = Field(None, alias='moduleName')
    band_name: list[str] | None = Field(None, alias='bandName')
    page_depth: list[str] | None = Field(None, alias='pageDepth')

class Email2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    email_submission_success: list[str] | None = Field(None, alias='emailSubmissionSuccess')
    b2b_field_value: list[str] | None = Field(None, alias='b2bFieldValue')

class Email1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    module: Module4 | None = None
    email: Email2 | None = None
    cta: Cta1 | None = None

class Events(BaseModel):
    model_config = ConfigDict(extra='ignore')
    page_track: PageTrack | None = Field(None, alias='pageTrack')
    click: Click | None = None
    video_player: VideoPlayer | None = Field(None, alias='videoPlayer')
    gating: Gating | None = None
    email: Email1 | None = None

class AnalyticsMapping(BaseModel):
    model_config = ConfigDict(extra='ignore')
    schemas: Schemas | None = None
    events: Events | None = None

class RelatedAppUrls(BaseModel):
    model_config = ConfigDict(extra='ignore')
    account: str | None = None
    add_on: str | None = Field(None, alias='addOn')
    create_account: str | None = Field(None, alias='createAccount')
    help: str | None = None
    home: str | None = None
    login: str | None = None
    play: str | None = None
    subscribe: str | None = None

class AnalyticsConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    analytics_mapping: AnalyticsMapping | None = Field(None, alias='analyticsMapping')
    frameworks: list[Any] | None = None
    related_app_urls: RelatedAppUrls | None = Field(None, alias='relatedAppUrls')

class BrazeConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    braze_endpoint: Any | None = Field(None, alias='brazeEndpoint')
    ek: Any | None = None
    email_signup_source: str | None = Field(None, alias='emailSignupSource')
    eps: str | None = None

class UsEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MyEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class HkEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PhEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TwEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AuEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class IdEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SgEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ThEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class HkZh(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class IdId(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MyMs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SgMs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MyZh(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SgZh(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PhTl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TwZh(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ThTh(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BdEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BnEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class KhEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LaEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MoEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MnEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MmEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class NpEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PkEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PwEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PgEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SbEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LkEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TlEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BnMs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MoZh(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BtEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class FjEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class KiEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MvEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MhEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class FmEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class NrEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class NuEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class WsEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ToEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TvEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class VuEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class CkEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class NzEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TkEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class GrEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class IlEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class GrEl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class IlHe(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AlEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AmEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TjEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class CyEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class EeEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class GeEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class IsEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class KzEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class KgEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LvEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LtEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MtEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AmRu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TjRu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class GeRu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class KzRu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class KgRu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class CyEl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class EeEt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LvLv(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LtLt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class HnEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MxEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class NiEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PaEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ArEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BoEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class CoEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class CrEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class DoEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class EcEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SvEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class GtEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PyEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PeEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class UyEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class JmEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MsEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AiEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AgEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AwEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BsEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BbEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BzEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class VgEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class KyEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class CwEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class DmEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class GdEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class GyEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class HtEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class KnEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LcEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class VcEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SrEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TtEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TcEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BrPt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class FrEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AdEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BaEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BgEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class HrEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class CzEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class DkEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class FiEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class HuEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MkEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MdEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MeEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class NlEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class NoEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PtEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class RoEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class RsEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SkEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SiEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class EsEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SeEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BeEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TrEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AdEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class EsEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BaHr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class HrHr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BgBg(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class CzCs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class DkDa(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class FiFi(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class HuHu(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MkMk(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MdRo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class RoRo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class MeSr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class RsSr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class NoNo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PtPt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SkSk(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SiSl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class SeSv(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class FrFr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class PlPl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class NlNl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BeNl(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class BeFr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class TrTr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ClEs(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class UaEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class UaUk(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class VnEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class VnVi(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class IeEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class GbEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AtEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class DeEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ItEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LiEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LuEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ChEn(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class AtDe(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class DeDe(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LiDe(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LuDe(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ChDe(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class LuFr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ChFr(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ItIt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class ChIt(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class CountryLangUris(BaseModel):
    model_config = ConfigDict(extra='ignore')
    us_es: UsEs | None = Field(None, alias='us/es')
    my_en: MyEn | None = Field(None, alias='my/en')
    hk_en: HkEn | None = Field(None, alias='hk/en')
    ph_en: PhEn | None = Field(None, alias='ph/en')
    tw_en: TwEn | None = Field(None, alias='tw/en')
    au_en: AuEn | None = Field(None, alias='au/en')
    id_en: IdEn | None = Field(None, alias='id/en')
    sg_en: SgEn | None = Field(None, alias='sg/en')
    th_en: ThEn | None = Field(None, alias='th/en')
    hk_zh: HkZh | None = Field(None, alias='hk/zh')
    id_id: IdId | None = Field(None, alias='id/id')
    my_ms: MyMs | None = Field(None, alias='my/ms')
    sg_ms: SgMs | None = Field(None, alias='sg/ms')
    my_zh: MyZh | None = Field(None, alias='my/zh')
    sg_zh: SgZh | None = Field(None, alias='sg/zh')
    ph_tl: PhTl | None = Field(None, alias='ph/tl')
    tw_zh: TwZh | None = Field(None, alias='tw/zh')
    th_th: ThTh | None = Field(None, alias='th/th')
    bd_en: BdEn | None = Field(None, alias='bd/en')
    bn_en: BnEn | None = Field(None, alias='bn/en')
    kh_en: KhEn | None = Field(None, alias='kh/en')
    la_en: LaEn | None = Field(None, alias='la/en')
    mo_en: MoEn | None = Field(None, alias='mo/en')
    mn_en: MnEn | None = Field(None, alias='mn/en')
    mm_en: MmEn | None = Field(None, alias='mm/en')
    np_en: NpEn | None = Field(None, alias='np/en')
    pk_en: PkEn | None = Field(None, alias='pk/en')
    pw_en: PwEn | None = Field(None, alias='pw/en')
    pg_en: PgEn | None = Field(None, alias='pg/en')
    sb_en: SbEn | None = Field(None, alias='sb/en')
    lk_en: LkEn | None = Field(None, alias='lk/en')
    tl_en: TlEn | None = Field(None, alias='tl/en')
    bn_ms: BnMs | None = Field(None, alias='bn/ms')
    mo_zh: MoZh | None = Field(None, alias='mo/zh')
    bt_en: BtEn | None = Field(None, alias='bt/en')
    fj_en: FjEn | None = Field(None, alias='fj/en')
    ki_en: KiEn | None = Field(None, alias='ki/en')
    mv_en: MvEn | None = Field(None, alias='mv/en')
    mh_en: MhEn | None = Field(None, alias='mh/en')
    fm_en: FmEn | None = Field(None, alias='fm/en')
    nr_en: NrEn | None = Field(None, alias='nr/en')
    nu_en: NuEn | None = Field(None, alias='nu/en')
    ws_en: WsEn | None = Field(None, alias='ws/en')
    to_en: ToEn | None = Field(None, alias='to/en')
    tv_en: TvEn | None = Field(None, alias='tv/en')
    vu_en: VuEn | None = Field(None, alias='vu/en')
    ck_en: CkEn | None = Field(None, alias='ck/en')
    nz_en: NzEn | None = Field(None, alias='nz/en')
    tk_en: TkEn | None = Field(None, alias='tk/en')
    gr_en: GrEn | None = Field(None, alias='gr/en')
    il_en: IlEn | None = Field(None, alias='il/en')
    gr_el: GrEl | None = Field(None, alias='gr/el')
    il_he: IlHe | None = Field(None, alias='il/he')
    al_en: AlEn | None = Field(None, alias='al/en')
    am_en: AmEn | None = Field(None, alias='am/en')
    tj_en: TjEn | None = Field(None, alias='tj/en')
    cy_en: CyEn | None = Field(None, alias='cy/en')
    ee_en: EeEn | None = Field(None, alias='ee/en')
    ge_en: GeEn | None = Field(None, alias='ge/en')
    is_en: IsEn | None = Field(None, alias='is/en')
    kz_en: KzEn | None = Field(None, alias='kz/en')
    kg_en: KgEn | None = Field(None, alias='kg/en')
    lv_en: LvEn | None = Field(None, alias='lv/en')
    lt_en: LtEn | None = Field(None, alias='lt/en')
    mt_en: MtEn | None = Field(None, alias='mt/en')
    am_ru: AmRu | None = Field(None, alias='am/ru')
    tj_ru: TjRu | None = Field(None, alias='tj/ru')
    ge_ru: GeRu | None = Field(None, alias='ge/ru')
    kz_ru: KzRu | None = Field(None, alias='kz/ru')
    kg_ru: KgRu | None = Field(None, alias='kg/ru')
    cy_el: CyEl | None = Field(None, alias='cy/el')
    ee_et: EeEt | None = Field(None, alias='ee/et')
    lv_lv: LvLv | None = Field(None, alias='lv/lv')
    lt_lt: LtLt | None = Field(None, alias='lt/lt')
    hn_es: HnEs | None = Field(None, alias='hn/es')
    mx_es: MxEs | None = Field(None, alias='mx/es')
    ni_es: NiEs | None = Field(None, alias='ni/es')
    pa_es: PaEs | None = Field(None, alias='pa/es')
    ar_es: ArEs | None = Field(None, alias='ar/es')
    bo_es: BoEs | None = Field(None, alias='bo/es')
    co_es: CoEs | None = Field(None, alias='co/es')
    cr_es: CrEs | None = Field(None, alias='cr/es')
    do_es: DoEs | None = Field(None, alias='do/es')
    ec_es: EcEs | None = Field(None, alias='ec/es')
    sv_es: SvEs | None = Field(None, alias='sv/es')
    gt_es: GtEs | None = Field(None, alias='gt/es')
    py_es: PyEs | None = Field(None, alias='py/es')
    pe_es: PeEs | None = Field(None, alias='pe/es')
    uy_es: UyEs | None = Field(None, alias='uy/es')
    jm_en: JmEn | None = Field(None, alias='jm/en')
    ms_en: MsEn | None = Field(None, alias='ms/en')
    ai_en: AiEn | None = Field(None, alias='ai/en')
    ag_en: AgEn | None = Field(None, alias='ag/en')
    aw_en: AwEn | None = Field(None, alias='aw/en')
    bs_en: BsEn | None = Field(None, alias='bs/en')
    bb_en: BbEn | None = Field(None, alias='bb/en')
    bz_en: BzEn | None = Field(None, alias='bz/en')
    vg_en: VgEn | None = Field(None, alias='vg/en')
    ky_en: KyEn | None = Field(None, alias='ky/en')
    cw_en: CwEn | None = Field(None, alias='cw/en')
    dm_en: DmEn | None = Field(None, alias='dm/en')
    gd_en: GdEn | None = Field(None, alias='gd/en')
    gy_en: GyEn | None = Field(None, alias='gy/en')
    ht_en: HtEn | None = Field(None, alias='ht/en')
    kn_en: KnEn | None = Field(None, alias='kn/en')
    lc_en: LcEn | None = Field(None, alias='lc/en')
    vc_en: VcEn | None = Field(None, alias='vc/en')
    sr_en: SrEn | None = Field(None, alias='sr/en')
    tt_en: TtEn | None = Field(None, alias='tt/en')
    tc_en: TcEn | None = Field(None, alias='tc/en')
    br_pt: BrPt | None = Field(None, alias='br/pt')
    fr_en: FrEn | None = Field(None, alias='fr/en')
    ad_en: AdEn | None = Field(None, alias='ad/en')
    ba_en: BaEn | None = Field(None, alias='ba/en')
    bg_en: BgEn | None = Field(None, alias='bg/en')
    hr_en: HrEn | None = Field(None, alias='hr/en')
    cz_en: CzEn | None = Field(None, alias='cz/en')
    dk_en: DkEn | None = Field(None, alias='dk/en')
    fi_en: FiEn | None = Field(None, alias='fi/en')
    hu_en: HuEn | None = Field(None, alias='hu/en')
    mk_en: MkEn | None = Field(None, alias='mk/en')
    md_en: MdEn | None = Field(None, alias='md/en')
    me_en: MeEn | None = Field(None, alias='me/en')
    nl_en: NlEn | None = Field(None, alias='nl/en')
    no_en: NoEn | None = Field(None, alias='no/en')
    pt_en: PtEn | None = Field(None, alias='pt/en')
    ro_en: RoEn | None = Field(None, alias='ro/en')
    rs_en: RsEn | None = Field(None, alias='rs/en')
    sk_en: SkEn | None = Field(None, alias='sk/en')
    si_en: SiEn | None = Field(None, alias='si/en')
    es_en: EsEn | None = Field(None, alias='es/en')
    se_en: SeEn | None = Field(None, alias='se/en')
    be_en: BeEn | None = Field(None, alias='be/en')
    tr_en: TrEn | None = Field(None, alias='tr/en')
    ad_es: AdEs | None = Field(None, alias='ad/es')
    es_es: EsEs | None = Field(None, alias='es/es')
    ba_hr: BaHr | None = Field(None, alias='ba/hr')
    hr_hr: HrHr | None = Field(None, alias='hr/hr')
    bg_bg: BgBg | None = Field(None, alias='bg/bg')
    cz_cs: CzCs | None = Field(None, alias='cz/cs')
    dk_da: DkDa | None = Field(None, alias='dk/da')
    fi_fi: FiFi | None = Field(None, alias='fi/fi')
    hu_hu: HuHu | None = Field(None, alias='hu/hu')
    mk_mk: MkMk | None = Field(None, alias='mk/mk')
    md_ro: MdRo | None = Field(None, alias='md/ro')
    ro_ro: RoRo | None = Field(None, alias='ro/ro')
    me_sr: MeSr | None = Field(None, alias='me/sr')
    rs_sr: RsSr | None = Field(None, alias='rs/sr')
    no_no: NoNo | None = Field(None, alias='no/no')
    pt_pt: PtPt | None = Field(None, alias='pt/pt')
    sk_sk: SkSk | None = Field(None, alias='sk/sk')
    si_sl: SiSl | None = Field(None, alias='si/sl')
    se_sv: SeSv | None = Field(None, alias='se/sv')
    fr_fr: FrFr | None = Field(None, alias='fr/fr')
    pl_pl: PlPl | None = Field(None, alias='pl/pl')
    nl_nl: NlNl | None = Field(None, alias='nl/nl')
    be_nl: BeNl | None = Field(None, alias='be/nl')
    be_fr: BeFr | None = Field(None, alias='be/fr')
    tr_tr: TrTr | None = Field(None, alias='tr/tr')
    cl_es: ClEs | None = Field(None, alias='cl/es')
    ua_en: UaEn | None = Field(None, alias='ua/en')
    ua_uk: UaUk | None = Field(None, alias='ua/uk')
    vn_en: VnEn | None = Field(None, alias='vn/en')
    vn_vi: VnVi | None = Field(None, alias='vn/vi')
    ie_en: IeEn | None = Field(None, alias='ie/en')
    gb_en: GbEn | None = Field(None, alias='gb/en')
    at_en: AtEn | None = Field(None, alias='at/en')
    de_en: DeEn | None = Field(None, alias='de/en')
    it_en: ItEn | None = Field(None, alias='it/en')
    li_en: LiEn | None = Field(None, alias='li/en')
    lu_en: LuEn | None = Field(None, alias='lu/en')
    ch_en: ChEn | None = Field(None, alias='ch/en')
    at_de: AtDe | None = Field(None, alias='at/de')
    de_de: DeDe | None = Field(None, alias='de/de')
    li_de: LiDe | None = Field(None, alias='li/de')
    lu_de: LuDe | None = Field(None, alias='lu/de')
    ch_de: ChDe | None = Field(None, alias='ch/de')
    lu_fr: LuFr | None = Field(None, alias='lu/fr')
    ch_fr: ChFr | None = Field(None, alias='ch/fr')
    it_it: ItIt | None = Field(None, alias='it/it')
    ch_it: ChIt | None = Field(None, alias='ch/it')

class CountryMapping(BaseModel):
    model_config = ConfigDict(extra='ignore')
    language: str | None = None
    country_code: str | None = Field(None, alias='countryCode')
    bcp47_code: str | None = Field(None, alias='bcp47Code')

class CountryToDefaultLang(BaseModel):
    model_config = ConfigDict(extra='ignore')
    bn: str | None = Field(None, alias='BN')
    mo: str | None = Field(None, alias='MO')
    bo: str | None = Field(None, alias='BO')
    rs: str | None = Field(None, alias='RS')
    es: str | None = Field(None, alias='ES')
    ba: str | None = Field(None, alias='BA')
    kz: str | None = Field(None, alias='KZ')
    mk: str | None = Field(None, alias='MK')
    si: str | None = Field(None, alias='SI')
    fr: str | None = Field(None, alias='FR')
    th: str | None = Field(None, alias='TH')
    ua: str | None = Field(None, alias='UA')
    my: str | None = Field(None, alias='MY')
    nz: str | None = Field(None, alias='NZ')
    cx: str | None = Field(None, alias='CX')
    gp: str | None = Field(None, alias='GP')
    gf: str | None = Field(None, alias='GF')
    re: str | None = Field(None, alias='RE')
    il: str | None = Field(None, alias='IL')
    bb: str | None = Field(None, alias='BB')
    vc: str | None = Field(None, alias='VC')
    dm: str | None = Field(None, alias='DM')
    hn: str | None = Field(None, alias='HN')
    tc: str | None = Field(None, alias='TC')
    sr: str | None = Field(None, alias='SR')
    gt: str | None = Field(None, alias='GT')
    ht: str | None = Field(None, alias='HT')
    ar: str | None = Field(None, alias='AR')
    it: str | None = Field(None, alias='IT')
    us: str | None = Field(None, alias='US')
    vi: str | None = Field(None, alias='VI')
    gu: str | None = Field(None, alias='GU')
    in_: str | None = Field(None, alias='IN')
    kh: str | None = Field(None, alias='KH')
    pk: str | None = Field(None, alias='PK')
    tl: str | None = Field(None, alias='TL')
    pw: str | None = Field(None, alias='PW')
    bg: str | None = Field(None, alias='BG')
    me: str | None = Field(None, alias='ME')
    pl: str | None = Field(None, alias='PL')
    nl: str | None = Field(None, alias='NL')
    lt: str | None = Field(None, alias='LT')
    ee: str | None = Field(None, alias='EE')
    no: str | None = Field(None, alias='NO')
    cc: str | None = Field(None, alias='CC')
    pf: str | None = Field(None, alias='PF')
    fo: str | None = Field(None, alias='FO')
    gl: str | None = Field(None, alias='GL')
    ph: str | None = Field(None, alias='PH')
    bl: str | None = Field(None, alias='BL')
    wf: str | None = Field(None, alias='WF')
    mc: str | None = Field(None, alias='MC')
    sm: str | None = Field(None, alias='SM')
    lu: str | None = Field(None, alias='LU')
    bs: str | None = Field(None, alias='BS')
    lc: str | None = Field(None, alias='LC')
    gy: str | None = Field(None, alias='GY')
    kn: str | None = Field(None, alias='KN')
    uy: str | None = Field(None, alias='UY')
    gd: str | None = Field(None, alias='GD')
    ms: str | None = Field(None, alias='MS')
    jm: str | None = Field(None, alias='JM')
    cr: str | None = Field(None, alias='CR')
    pa: str | None = Field(None, alias='PA')
    um: str | None = Field(None, alias='UM')
    md: str | None = Field(None, alias='MD')
    pg: str | None = Field(None, alias='PG')
    mm: str | None = Field(None, alias='MM')
    np: str | None = Field(None, alias='NP')
    bz: str | None = Field(None, alias='BZ')
    sk: str | None = Field(None, alias='SK')
    se: str | None = Field(None, alias='SE')
    dk: str | None = Field(None, alias='DK')
    hk: str | None = Field(None, alias='HK')
    ge: str | None = Field(None, alias='GE')
    cz: str | None = Field(None, alias='CZ')
    tj: str | None = Field(None, alias='TJ')
    tr: str | None = Field(None, alias='TR')
    ro: str | None = Field(None, alias='RO')
    gr: str | None = Field(None, alias='GR')
    jp: str | None = Field(None, alias='JP')
    tw: str | None = Field(None, alias='TW')
    nf: str | None = Field(None, alias='NF')
    pm: str | None = Field(None, alias='PM')
    mq: str | None = Field(None, alias='MQ')
    yt: str | None = Field(None, alias='YT')
    ch: str | None = Field(None, alias='CH')
    aw: str | None = Field(None, alias='AW')
    ag: str | None = Field(None, alias='AG')
    py: str | None = Field(None, alias='PY')
    mx: str | None = Field(None, alias='MX')
    br: str | None = Field(None, alias='BR')
    do: str | None = Field(None, alias='DO')
    co: str | None = Field(None, alias='CO')
    pe: str | None = Field(None, alias='PE')
    as_: str | None = Field(None, alias='AS')
    bd: str | None = Field(None, alias='BD')
    sb: str | None = Field(None, alias='SB')
    hu: str | None = Field(None, alias='HU')
    pt: str | None = Field(None, alias='PT')
    be: str | None = Field(None, alias='BE')
    hr: str | None = Field(None, alias='HR')
    kg: str | None = Field(None, alias='KG')
    id: str | None = Field(None, alias='ID')
    lv: str | None = Field(None, alias='LV')
    mt: str | None = Field(None, alias='MT')
    au: str | None = Field(None, alias='AU')
    hm: str | None = Field(None, alias='HM')
    sj: str | None = Field(None, alias='SJ')
    ax: str | None = Field(None, alias='AX')
    de: str | None = Field(None, alias='DE')
    li: str | None = Field(None, alias='LI')
    ni: str | None = Field(None, alias='NI')
    cw: str | None = Field(None, alias='CW')
    ec: str | None = Field(None, alias='EC')
    cl: str | None = Field(None, alias='CL')
    mp: str | None = Field(None, alias='MP')
    mn: str | None = Field(None, alias='MN')
    la: str | None = Field(None, alias='LA')
    lk: str | None = Field(None, alias='LK')
    is_: str | None = Field(None, alias='IS')
    cy: str | None = Field(None, alias='CY')
    al: str | None = Field(None, alias='AL')
    am: str | None = Field(None, alias='AM')
    fi: str | None = Field(None, alias='FI')
    xk: str | None = Field(None, alias='XK')
    mf: str | None = Field(None, alias='MF')
    sg: str | None = Field(None, alias='SG')
    az: str | None = Field(None, alias='AZ')
    uz: str | None = Field(None, alias='UZ')
    va: str | None = Field(None, alias='VA')
    ai: str | None = Field(None, alias='AI')
    vg: str | None = Field(None, alias='VG')
    ky: str | None = Field(None, alias='KY')
    sv: str | None = Field(None, alias='SV')
    tt: str | None = Field(None, alias='TT')
    gb: str | None = Field(None, alias='GB')
    ie: str | None = Field(None, alias='IE')
    at: str | None = Field(None, alias='AT')
    pr: str | None = Field(None, alias='PR')
    to: str | None = Field(None, alias='TO')
    ad: str | None = Field(None, alias='AD')

class CountryToRegion(BaseModel):
    model_config = ConfigDict(extra='ignore')
    mc: str | None = None
    hk: str | None = None
    tw: str | None = None
    ph: str | None = None
    sg: str | None = None
    bn: str | None = None
    mo: str | None = None
    ba: str | None = None
    pt: str | None = None
    hu: str | None = None
    no: str | None = None
    ro: str | None = None
    kg: str | None = None
    my: str | None = None
    bo: str | None = None
    rs: str | None = None
    es: str | None = None
    kz: str | None = None
    mk: str | None = None
    si: str | None = None
    fr: str | None = None
    th: str | None = None
    ua: str | None = None
    nz: str | None = None
    cx: str | None = None
    gp: str | None = None
    gf: str | None = None
    re: str | None = None
    ch: str | None = None
    it: str | None = None
    il: str | None = None
    bb: str | None = None
    vc: str | None = None
    dm: str | None = None
    gy: str | None = None
    hn: str | None = None
    mx: str | None = None
    tc: str | None = None
    sr: str | None = None
    cw: str | None = None
    co: str | None = None
    gd: str | None = None
    gt: str | None = None
    sv: str | None = None
    ht: str | None = None
    cr: str | None = None
    pa: str | None = None
    ar: str | None = None
    ni: str | None = None
    ec: str | None = None
    ws: str | None = None
    us: str | None = None
    vi: str | None = None
    gu: str | None = None
    tv: str | None = None
    md: str | None = None
    tk: str | None = None
    in_: str | None = Field(None, alias='in')
    kh: str | None = None
    pk: str | None = None
    se: str | None = None
    tl: str | None = None
    pw: str | None = None
    bg: str | None = None
    ee: str | None = None
    me: str | None = None
    pl: str | None = None
    nl: str | None = None
    lt: str | None = None
    dk: str | None = None
    cc: str | None = None
    pf: str | None = None
    fo: str | None = None
    gl: str | None = None
    bl: str | None = None
    wf: str | None = None
    va: str | None = None
    sm: str | None = None
    li: str | None = None
    lu: str | None = None
    bs: str | None = None
    lc: str | None = None
    vg: str | None = None
    py: str | None = None
    kn: str | None = None
    uy: str | None = None
    ms: str | None = None
    jm: str | None = None
    aw: str | None = None
    um: str | None = None
    mh: str | None = None
    fm: str | None = None
    vn: str | None = None
    ck: str | None = None
    bz: str | None = None
    pg: str | None = None
    mm: str | None = None
    np: str | None = None
    cz: str | None = None
    tr: str | None = None
    cy: str | None = None
    sk: str | None = None
    ge: str | None = None
    tj: str | None = None
    gr: str | None = None
    jp: str | None = None
    nf: str | None = None
    pm: str | None = None
    mq: str | None = None
    yt: str | None = None
    ag: str | None = None
    cl: str | None = None
    br: str | None = None
    do: str | None = None
    pe: str | None = None
    ki: str | None = None
    bt: str | None = None
    as_: str | None = Field(None, alias='as')
    nr: str | None = None
    fj: str | None = None
    be: str | None = None
    bd: str | None = None
    sb: str | None = None
    am: str | None = None
    fi: str | None = None
    hr: str | None = None
    id: str | None = None
    lv: str | None = None
    mt: str | None = None
    au: str | None = None
    hm: str | None = None
    sj: str | None = None
    ax: str | None = None
    de: str | None = None
    ky: str | None = None
    tt: str | None = None
    mp: str | None = None
    mv: str | None = None
    nu: str | None = None
    ad: str | None = None
    mn: str | None = None
    la: str | None = None
    lk: str | None = None
    is_: str | None = Field(None, alias='is')
    al: str | None = None
    xk: str | None = None
    mf: str | None = None
    az: str | None = None
    uz: str | None = None
    ai: str | None = None
    gb: str | None = None
    ie: str | None = None
    at: str | None = None
    pr: str | None = None
    im: str | None = None
    vu: str | None = None
    to: str | None = None

class LanguageVariables(BaseModel):
    model_config = ConfigDict(extra='ignore')
    lang: str | None = None
    country: str | None = None
    region: str | None = None

class Flags(BaseModel):
    model_config = ConfigDict(extra='ignore')
    has_audio_description: bool | None = Field(None, alias='hasAudioDescription')
    is_uhd: bool | None = Field(None, alias='isUHD')
    has_dolby_atmos: bool | None = Field(None, alias='hasDolbyAtmos')
    has_dolby_vision: bool | None = Field(None, alias='hasDolbyVision')
    has_pse_advisory: bool | None = Field(None, alias='hasPSEAdvisory')

class Trailer(BaseModel):
    model_config = ConfigDict(extra='ignore')
    program_id: UUID | str | None = Field(None, alias='programId', union_mode='left_to_right')
    edit_id: UUID | str | None = Field(None, alias='editId', union_mode='left_to_right')
    title: str | None = None
    description: str | None = None
    url: str | None = None

class OfferingDates(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start_date: AwareDatetime | None = Field(None, alias='startDate')
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class Title1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    short: str | None = None
    full: str | None = None

class Credits(BaseModel):
    model_config = ConfigDict(extra='ignore')
    starring: str | None = None
    directors: str | None = None
    writers: str | None = None
    producers: str | None = None
    creators: str | None = None
    sources: str | None = None
    sign_interpreters: str | None = Field(None, alias='signInterpreters')

class ActorItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None

class CastAndCrew1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    actor: list[ActorItem] | None = Field(None, alias='Actor')
    cast: Any | None = Field(None, alias='Cast')
    producer: Any | None = Field(None, alias='Producer')
    director: Any | None = Field(None, alias='Director')
    writer: Any | None = Field(None, alias='Writer')

class Summary(BaseModel):
    model_config = ConfigDict(extra='ignore')
    short: str | None = None
    full: str | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: str | None = None
    centered_background_small: str | None = Field(None, alias='centered-background-small')
    cover_artwork: str | None = Field(None, alias='cover-artwork')

class Flags1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    is_watch_free: bool | None = Field(None, alias='isWatchFree')

class Title3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    short: timedelta | str | None = Field(default=None, union_mode='left_to_right')
    full: timedelta | str | None = Field(default=None, union_mode='left_to_right')

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore')
    series_id: Any | None = Field(None, alias='seriesId')
    season_number: Any | None = Field(None, alias='seasonNumber')
    episode_number: int | None = Field(None, alias='episodeNumber')
    quality: str | None = None
    images: Images | None = None
    flags: Flags1 | None = None
    episode_url: str | None = Field(None, alias='episodeUrl')
    offering_dates: OfferingDates | None = Field(None, alias='offeringDates')
    title: Title3 | None = None
    summary: Summary | None = None

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore')
    season_id: UUID | None = Field(None, alias='seasonId')
    orgtitle: Any | None = None
    season_number: int | None = Field(None, alias='seasonNumber')
    season_number_slug: str | None = Field(None, alias='seasonNumberSlug')
    number_of_episodes: int | None = Field(None, alias='numberOfEpisodes')
    title: Title1 | None = None
    summary: Summary | None = None
    episodes: list[Episode] | None = None

class Images1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default_wide: str | None = Field(None, alias='default-wide')
    centered_background_small: str | None = Field(None, alias='centered-background-small')
    default: str | None = None
    centered_background: str | None = Field(None, alias='centered-background')
    cover_artwork: str | None = Field(None, alias='cover-artwork')
    logo_left: str | None = Field(None, alias='logo-left')
    content_logo_monochromatic: str | None = Field(None, alias='content-logo-monochromatic')
    logo_centered: str | None = Field(None, alias='logo-centered')
    content_logo_polychromatic: str | None = Field(None, alias='content-logo-polychromatic')
    poster_with_logo: str | None = Field(None, alias='poster-with-logo')
    cover_artwork_square: str | None = Field(None, alias='cover-artwork-square')
    cover_artwork_horizontal: str | None = Field(None, alias='cover-artwork-horizontal')

class LocalizedRating(BaseModel):
    model_config = ConfigDict(extra='ignore')
    rating_authority: str | None = None
    classifier: str | None = None
    descriptors: list[str] | None = None

class Idref14(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image_url_link: str | None = Field(None, alias='imageUrlLink')
    category: Any | None = None
    hbomax_id: UUID | None = Field(None, alias='hbomaxId')
    series_id: UUID | None = Field(None, alias='seriesId')
    series_title_id: Any | None = Field(None, alias='seriesTitleId')
    flags: Flags | None = None
    trailer: Trailer | None = None
    genres: list[str] | None = None
    brand: list[str] | None = None
    episode_count: Any | None = Field(None, alias='episodeCount')
    rating_code: list[Any] | None = Field(None, alias='ratingCode')
    offering_dates: OfferingDates | None = Field(None, alias='offeringDates')
    title: Title1 | None = None
    credits: Credits | None = None
    cast_and_crew: CastAndCrew1 | None = Field(None, alias='castAndCrew')
    seasons: list[Season] | None = None
    summary: Summary | None = None
    images: Images1 | None = None
    status: str | None = None
    rating: dict[str, Any] | None = None
    localized_rating: LocalizedRating | None = Field(None, alias='localizedRating')
    number_of_seasons: int | None = Field(None, alias='numberOfSeasons')
    number_of_episodes: int | None = Field(None, alias='numberOfEpisodes')
    quality: str | None = None
    primary_genre: str | None = Field(None, alias='primaryGenre')
    secondary_genre: str | None = Field(None, alias='secondaryGenre')
    genres_formatted: str | None = Field(None, alias='genresFormatted')
    release_year: str | None = Field(None, alias='releaseYear')

class Default(BaseModel):
    model_config = ConfigDict(extra='ignore')
    en_us: str | None = Field(None, alias='en_US')
    url: str | None = None

class Mobile(BaseModel):
    model_config = ConfigDict(extra='ignore')
    en_us: str | None = Field(None, alias='en_US')
    url: str | None = None

class BrowseAudioDescription(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default | None = None
    mobile: Mobile | None = None

class Default1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    en_us: str | None = Field(None, alias='en_US')

class Mobile1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    en_us: str | None = Field(None, alias='en_US')

class UnauthLabel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default1 | None = None
    mobile: Mobile1 | None = None

class AuthLabel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default1 | None = None
    mobile: Mobile1 | None = None

class SecondaryCta(BaseModel):
    model_config = ConfigDict(extra='ignore')
    unauth_label: UnauthLabel | None = Field(None, alias='unauthLabel')
    unauth_url: str | None = Field(None, alias='unauthUrl')
    auth_url: str | None = Field(None, alias='authUrl')
    auth_label: AuthLabel | None = Field(None, alias='authLabel')

class AltText2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    en_us: str | None = Field(None, alias='en_US')

class Logo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    alt_text: AltText2 | None = Field(None, alias='altText')
    url: str | None = None

class Label(BaseModel):
    model_config = ConfigDict(extra='ignore')
    en_us: str | None = Field(None, alias='en_US')

class Link(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: Label | None = None
    url: str | None = Field(None, alias='URL')

class SecondaryLink(BaseModel):
    model_config = ConfigDict(extra='ignore')
    link: Link | None = None

class UnauthLabel1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default1 | None = None
    mobile: Mobile1 | None = None

class AuthLabel1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default1 | None = None
    mobile: Mobile1 | None = None

class PrimaryCta(BaseModel):
    model_config = ConfigDict(extra='ignore')
    unauth_label: UnauthLabel1 | None = Field(None, alias='unauthLabel')
    unauth_url: str | None = Field(None, alias='unauthUrl')
    auth_url: str | None = Field(None, alias='authUrl')
    auth_label: AuthLabel1 | None = Field(None, alias='authLabel')

class SkipToContent(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default1 | None = None
    mobile: Mobile1 | None = None

class Idref15(BaseModel):
    model_config = ConfigDict(extra='ignore')
    browse_audio_description: BrowseAudioDescription | None = Field(None, alias='browseAudioDescription')
    secondary_cta: SecondaryCta | None = Field(None, alias='secondaryCta')
    logo: Logo | None = None
    secondary_links: list[SecondaryLink] | None = Field(None, alias='secondaryLinks')
    primary_cta: PrimaryCta | None = Field(None, alias='primaryCta')
    skip_to_content: SkipToContent | None = Field(None, alias='skipToContent')

class Idref16Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    lang: str | None = None
    url: str | None = None

class UnauthLabel2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default1 | None = None
    mobile: Mobile1 | None = None

class AuthLabel2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default1 | None = None
    mobile: Mobile1 | None = None

class SecondaryCta1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    unauth_label: UnauthLabel2 | None = Field(None, alias='unauthLabel')
    unauth_url: str | None = Field(None, alias='unauthUrl')
    auth_url: str | None = Field(None, alias='authUrl')
    auth_label: AuthLabel2 | None = Field(None, alias='authLabel')

class Logo1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    alt_text: AltText2 | None = Field(None, alias='altText')
    url: str | None = None

class SkipToContent1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: Default1 | None = None
    mobile: Mobile1 | None = None

class Idref19(BaseModel):
    model_config = ConfigDict(extra='ignore')
    secondary_cta: SecondaryCta1 | None = Field(None, alias='secondaryCta')
    logo: Logo1 | None = None
    skip_to_content: SkipToContent1 | None = Field(None, alias='skipToContent')

class Value(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: str | None = None

class Idref20(BaseModel):
    model_config = ConfigDict(extra='ignore')
    value: Value | None = None

class MaxWidthidref20(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: int | None = None

class MaxHeightidref20(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: int | None = None

class Value1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: str | None = None
    medium: str | None = None
    small: str | None = None

class Idref21(BaseModel):
    model_config = ConfigDict(extra='ignore')
    value: Value1 | None = None

class MaxWidthidref21(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: int | None = None
    medium: int | None = None
    small: int | None = None

class MaxHeightidref21(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: int | None = None
    medium: int | None = None
    small: int | None = None

class Value2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: str | None = None

class Idref31(BaseModel):
    model_config = ConfigDict(extra='ignore')
    value: Value2 | None = None

class MaxWidthidref31(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: int | None = None

class MaxHeightidref31(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: int | None = None

class Value3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: str | None = None
    medium: str | None = None
    small: str | None = None

class Idref32(BaseModel):
    model_config = ConfigDict(extra='ignore')
    value: Value3 | None = None

class MaxWidthidref32(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: int | None = None
    medium: int | None = None
    small: int | None = None

class MaxHeightidref32(BaseModel):
    model_config = ConfigDict(extra='ignore')
    large: int | None = None
    medium: int | None = None
    small: int | None = None

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    primary_text: str | None = Field(None, alias='primaryText')
    image: str | None = None
    secondary_text: str | None = Field(None, alias='secondaryText')
    description: str | None = None
    url_slug: str | None = Field(None, alias='urlSlug')

class Idref42(BaseModel):
    model_config = ConfigDict(extra='ignore')
    type: str | None = None
    items: list[Item] | None = None
    parent_url: str | None = Field(None, alias='parentUrl')

class Title4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    short: str | None = None
    full: str | None = None

class Images2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default: str | None = None
    centered_background_small: str | None = Field(None, alias='centered-background-small')
    cover_artwork: str | None = Field(None, alias='cover-artwork')

class Title5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    short: timedelta | str | None = Field(default=None, union_mode='left_to_right')
    full: timedelta | str | None = Field(default=None, union_mode='left_to_right')

class Episode1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    series_id: Any | None = Field(None, alias='seriesId')
    season_number: Any | None = Field(None, alias='seasonNumber')
    episode_number: int | None = Field(None, alias='episodeNumber')
    quality: str | None = None
    images: Images2 | None = None
    flags: Flags1 | None = None
    episode_url: str | None = Field(None, alias='episodeUrl')
    offering_dates: OfferingDates | None = Field(None, alias='offeringDates')
    title: Title5 | None = None
    summary: Summary | None = None

class Idref46Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    season_id: UUID | None = Field(None, alias='seasonId')
    orgtitle: Any | None = None
    season_number: int | None = Field(None, alias='seasonNumber')
    season_number_slug: str | None = Field(None, alias='seasonNumberSlug')
    number_of_episodes: int | None = Field(None, alias='numberOfEpisodes')
    title: Title4 | None = None
    summary: Summary | None = None
    episodes: list[Episode1] | None = None

class Title6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    short: str | None = None
    full: str | None = None

class Images3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default_wide: str | None = Field(None, alias='default-wide')
    centered_background_small: str | None = Field(None, alias='centered-background-small')
    default: str | None = None
    centered_background: str | None = Field(None, alias='centered-background')
    cover_artwork: str | None = Field(None, alias='cover-artwork')
    logo_left: str | None = Field(None, alias='logo-left')
    content_logo_monochromatic: str | None = Field(None, alias='content-logo-monochromatic')
    logo_centered: str | None = Field(None, alias='logo-centered')
    poster_with_logo: str | None = Field(None, alias='poster-with-logo')
    content_logo_polychromatic: str | None = Field(None, alias='content-logo-polychromatic')
    cover_artwork_square: str | None = Field(None, alias='cover-artwork-square')
    cover_artwork_horizontal: str | None = Field(None, alias='cover-artwork-horizontal')

class LocalizedRating1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    rating_authority: str | None = None
    classifier: str | None = None
    descriptors: list[Any] | None = None

class Idref52Item(BaseModel):
    model_config = ConfigDict(extra='ignore')
    hbomax_id: UUID | None = Field(None, alias='hbomaxId')
    type: str | None = None
    title: Title6 | None = None
    image_url_link: str | None = Field(None, alias='imageUrlLink')
    images: Images3 | None = None
    offering_dates: OfferingDates | None = Field(None, alias='offeringDates')
    localized_rating: Any | LocalizedRating1 | None = Field(None, alias='localizedRating')
    genres: list[Any] | None = None
    rank: Any | None = None

class FirstItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title6 | None = None

class Description(BaseModel):
    model_config = ConfigDict(extra='ignore')
    short: Any | None = None
    full: Any | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default_wide: str | None = Field(None, alias='default-wide')
    default: str | None = None
    centered_background_small: str | None = Field(None, alias='centered-background-small')
    centered_background: str | None = Field(None, alias='centered-background')
    cover_artwork: str | None = Field(None, alias='cover-artwork')
    logo_left: str | None = Field(None, alias='logo-left')
    content_logo_monochromatic: str | None = Field(None, alias='content-logo-monochromatic')
    logo_centered: str | None = Field(None, alias='logo-centered')
    poster_with_logo: str | None = Field(None, alias='poster-with-logo')
    content_logo_polychromatic: str | None = Field(None, alias='content-logo-polychromatic')
    cover_artwork_horizontal: str | None = Field(None, alias='cover-artwork-horizontal')
    cover_artwork_square: str | None = Field(None, alias='cover-artwork-square')

class RatingCodeItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    code: list[str] | None = None
    organization: str | None = None
    rating_code: timedelta | str | None = Field(default=None, union_mode='left_to_right')

class Title9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    full_original: Any | None = None
    short_original: Any | None = None
    short: str | None = None
    full: str | None = None

class Images4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default_wide: str | None = Field(None, alias='default-wide')
    default: str | None = None
    centered_background_small: str | None = Field(None, alias='centered-background-small')
    centered_background: str | None = Field(None, alias='centered-background')
    cover_artwork: str | None = Field(None, alias='cover-artwork')
    logo_left: str | None = Field(None, alias='logo-left')
    content_logo_monochromatic: str | None = Field(None, alias='content-logo-monochromatic')
    logo_centered: str | None = Field(None, alias='logo-centered')
    poster_with_logo: str | None = Field(None, alias='poster-with-logo')
    content_logo_polychromatic: str | None = Field(None, alias='content-logo-polychromatic')
    cover_artwork_horizontal: str | None = Field(None, alias='cover-artwork-horizontal')
    cover_artwork_square: str | None = Field(None, alias='cover-artwork-square')

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    series_id: UUID | None = Field(None, alias='seriesId')
    hbomax_url: Any | None = Field(None, alias='hbomaxURL')
    hbomax_id: UUID | None = Field(None, alias='hbomaxId')
    category: str | None = None
    series_title_id: Any | None = Field(None, alias='seriesTitleId')
    image_url_link: str | None = Field(None, alias='imageUrlLink')
    genres: list[str] | None = None
    brand: list[str] | None = None
    rating_code: list[RatingCodeItem] | None = Field(None, alias='ratingCode')
    offering_dates: OfferingDates | None = Field(None, alias='offeringDates')
    title: Title9 | None = None
    summary: Summary | None = None
    images: Images4 | None = None
    status: str | None = None
    badges: list[Any] | None = None
    feature_id: UUID | None = Field(None, alias='featureId')
    url: Any | None = None

class Idref53(BaseModel):
    model_config = ConfigDict(extra='ignore')
    collection_id: str | None = Field(None, alias='collectionId')
    image_to_show: str | None = Field(None, alias='imageToShow')
    first_item: FirstItem | None = Field(None, alias='firstItem')
    title: Title6 | None = None
    description: Description | None = None
    image: Image | None = None
    event_type: str | None = Field(None, alias='eventType')
    items: list[Item1] | None = None

class Title10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    short: str | None = None
    full: str | None = None

class FirstItem1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    title: Title10 | None = None

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default_wide: str | None = Field(None, alias='default-wide')
    centered_background_small: str | None = Field(None, alias='centered-background-small')
    default: str | None = None
    centered_background: str | None = Field(None, alias='centered-background')
    cover_artwork: str | None = Field(None, alias='cover-artwork')
    logo_left: str | None = Field(None, alias='logo-left')
    content_logo_monochromatic: str | None = Field(None, alias='content-logo-monochromatic')
    logo_centered: str | None = Field(None, alias='logo-centered')
    content_logo_polychromatic: str | None = Field(None, alias='content-logo-polychromatic')
    poster_with_logo: str | None = Field(None, alias='poster-with-logo')
    cover_artwork_square: str | None = Field(None, alias='cover-artwork-square')
    cover_artwork_horizontal: str | None = Field(None, alias='cover-artwork-horizontal')

class RatingCodeItem1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    code: list[str] | None = None
    organization: str | None = None
    rating_code: str | None = None

class Title12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    full_original: Any | None = None
    short_original: Any | None = None
    short: str | None = None
    full: str | None = None

class Images5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    default_wide: str | None = Field(None, alias='default-wide')
    centered_background_small: str | None = Field(None, alias='centered-background-small')
    default: str | None = None
    centered_background: str | None = Field(None, alias='centered-background')
    cover_artwork: str | None = Field(None, alias='cover-artwork')
    logo_left: str | None = Field(None, alias='logo-left')
    content_logo_monochromatic: str | None = Field(None, alias='content-logo-monochromatic')
    logo_centered: str | None = Field(None, alias='logo-centered')
    content_logo_polychromatic: str | None = Field(None, alias='content-logo-polychromatic')
    poster_with_logo: str | None = Field(None, alias='poster-with-logo')
    cover_artwork_square: str | None = Field(None, alias='cover-artwork-square')
    cover_artwork_horizontal: str | None = Field(None, alias='cover-artwork-horizontal')

class Item2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__typename: str | None = Field(None, alias='__typename')
    series_id: UUID | None = Field(None, alias='seriesId')
    hbomax_url: Any | None = Field(None, alias='hbomaxURL')
    hbomax_id: UUID | None = Field(None, alias='hbomaxId')
    category: str | None = None
    series_title_id: Any | None = Field(None, alias='seriesTitleId')
    image_url_link: str | None = Field(None, alias='imageUrlLink')
    genres: list[str] | None = None
    brand: list[str] | None = None
    rating_code: list[RatingCodeItem1] | None = Field(None, alias='ratingCode')
    offering_dates: OfferingDates | None = Field(None, alias='offeringDates')
    title: Title12 | None = None
    summary: Summary | None = None
    images: Images5 | None = None
    status: str | None = None
    feature_id: UUID | None = Field(None, alias='featureId')
    url: Any | None = None

class Idref68(BaseModel):
    model_config = ConfigDict(extra='ignore')
    collection_id: str | None = Field(None, alias='collectionId')
    image_to_show: str | None = Field(None, alias='imageToShow')
    first_item: FirstItem1 | None = Field(None, alias='firstItem')
    title: Title10 | None = None
    description: Description | None = None
    image: Image1 | None = None
    event_type: str | None = Field(None, alias='eventType')
    items: list[Item2] | None = None

class Legal(BaseModel):
    model_config = ConfigDict(extra='ignore')
    en_us: str | None = Field(None, alias='en_US')

class SecondaryRowItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: Label | None = None
    url: str | None = None
    open_in_new_tab: bool | None = Field(None, alias='openInNewTab')
    is_ccpa_link: bool | None = Field(None, alias='isCCPALink')

class PrimaryRowItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: Label | None = None
    url: str | None = None

class Idref69(BaseModel):
    model_config = ConfigDict(extra='ignore')
    legal: Legal | None = None
    secondary_row: list[SecondaryRowItem] | None = Field(None, alias='secondaryRow')
    primary_row: list[PrimaryRowItem] | None = Field(None, alias='primaryRow')

class SecondaryRowItem1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: Label | None = None
    url: str | None = None
    open_in_new_tab: bool | None = Field(None, alias='openInNewTab')
    is_ccpa_link: bool | None = Field(None, alias='isCCPALink')

class PrimaryRowItem1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: Label | None = None
    url: str | None = None

class Idref70(BaseModel):
    model_config = ConfigDict(extra='ignore')
    legal: Legal | None = None
    secondary_row: list[SecondaryRowItem1] | None = Field(None, alias='secondaryRow')
    primary_row: list[PrimaryRowItem1] | None = Field(None, alias='primaryRow')

class MappedData(BaseModel):
    model_config = ConfigDict(extra='ignore')
    idref0: str | None = None
    idref1: str | None = None
    idref2: str | None = None
    idref3: str | None = None
    idref4: str | None = None
    idref5: str | None = None
    idref6: str | None = None
    idref7: str | None = None
    idref8: str | None = None
    idref9: str | None = None
    idref10: str | None = None
    idref11: str | None = None
    idref12: str | None = None
    idref13: str | None = None
    idref14: Idref14 | None = None
    idref15: Idref15 | None = None
    idref16: list[Idref16Item] | None = None
    idref17: str | None = None
    idref18: str | None = None
    idref19: Idref19 | None = None
    idref20: Idref20 | None = None
    max_widthidref20: MaxWidthidref20 | None = Field(None, alias='maxWidthidref20')
    max_heightidref20: MaxHeightidref20 | None = Field(None, alias='maxHeightidref20')
    idref21: Idref21 | None = None
    max_widthidref21: MaxWidthidref21 | None = Field(None, alias='maxWidthidref21')
    max_heightidref21: MaxHeightidref21 | None = Field(None, alias='maxHeightidref21')
    idref22: str | None = None
    idref23: str | None = None
    idref24: str | None = None
    idref25: str | None = None
    idref26: str | None = None
    idref27: str | None = None
    idref28: str | None = None
    idref29: str | None = None
    idref30: str | None = None
    idref31: Idref31 | None = None
    max_widthidref31: MaxWidthidref31 | None = Field(None, alias='maxWidthidref31')
    max_heightidref31: MaxHeightidref31 | None = Field(None, alias='maxHeightidref31')
    idref32: Idref32 | None = None
    max_widthidref32: MaxWidthidref32 | None = Field(None, alias='maxWidthidref32')
    max_heightidref32: MaxHeightidref32 | None = Field(None, alias='maxHeightidref32')
    idref33: str | None = None
    idref34: str | None = None
    idref35: str | None = None
    idref36: str | None = None
    idref37: str | None = None
    idref38: str | None = None
    idref39: str | None = None
    idref40: str | None = None
    idref41: str | None = None
    idref42: Idref42 | None = None
    idref43: str | None = None
    idref44: str | None = None
    idref45: str | None = None
    idref46: list[Idref46Item] | None = None
    idref47: str | None = None
    idref48: str | None = None
    idref49: str | None = None
    idref50: str | None = None
    idref51: str | None = None
    idref52: list[Idref52Item] | None = None
    idref53: Idref53 | None = None
    idref54: str | None = None
    idref55: str | None = None
    idref56: str | None = None
    idref57: str | None = None
    idref58: str | None = None
    idref59: str | None = None
    idref60: str | None = None
    idref61: str | None = None
    idref62: str | None = None
    idref63: str | None = None
    idref64: str | None = None
    idref65: str | None = None
    idref66: str | None = None
    idref67: str | None = None
    idref68: Idref68 | None = None
    idref69: Idref69 | None = None
    idref70: Idref70 | None = None

class MediaMelonConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    is_media_melon_enabled: bool | None = Field(None, alias='IS_MEDIA_MELON_ENABLED')
    mm_environment_key: int | None = Field(None, alias='MM_ENVIRONMENT_KEY')

class PageProps(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_app_id: str | None = Field(None, alias='mediaAppId')
    is_published: bool | None = Field(None, alias='isPublished')
    developer_panel_config: DeveloperPanelConfig | None = Field(None, alias='developerPanelConfig')
    version_tag: str | None = Field(None, alias='versionTag')
    supported_countries: list[Any] | None = Field(None, alias='supportedCountries')
    resolved_theme: ResolvedTheme | None = Field(None, alias='resolvedTheme')
    tenant_style_hash: str | None = Field(None, alias='tenantStyleHash')
    ab_testing_module_hash: str | None = Field(None, alias='abTestingModuleHash')
    analytics_config: AnalyticsConfig | None = Field(None, alias='analyticsConfig')
    auth_cookie_name: str | None = Field(None, alias='authCookieName')
    bcp: str | None = None
    braze_config: BrazeConfig | None = Field(None, alias='brazeConfig')
    canonical_url: str | None = Field(None, alias='canonicalURL')
    cdn_base_url: str | None = Field(None, alias='cdnBaseUrl')
    content_type: str | None = Field(None, alias='contentType')
    country_lang_uris: CountryLangUris | None = Field(None, alias='countryLangUris')
    country_mappings: list[CountryMapping] | None = Field(None, alias='countryMappings')
    country_to_default_lang: CountryToDefaultLang | None = Field(None, alias='countryToDefaultLang')
    country_to_region: CountryToRegion | None = Field(None, alias='countryToRegion')
    effective_tenant_id: str | None = Field(None, alias='effectiveTenantId')
    enable_lfe: bool | None = Field(None, alias='enableLFE')
    environment: str | None = None
    experiment_configs: list[Any] | None = Field(None, alias='experimentConfigs')
    event_schedule_dates: Any | None = Field(None, alias='eventScheduleDates')
    formatted_url: str | None = Field(None, alias='formattedURL')
    geo_redirect_url: str | None = Field(None, alias='geoRedirectUrl')
    global_domain: str | None = Field(None, alias='globalDomain')
    has_audio_description: bool | None = Field(None, alias='hasAudioDescription')
    next_global_domain: Any | None = Field(None, alias='nextGlobalDomain')
    hostname_to_override: Any | None = Field(None, alias='hostnameToOverride')
    is_cms_error_page: bool | None = Field(None, alias='isCMSErrorPage')
    is_event_page: bool | None = Field(None, alias='isEventPage')
    is_preview_server: bool | None = Field(None, alias='isPreviewServer')
    is_season_page: bool | None = Field(None, alias='isSeasonPage')
    is_user_out_of_region: bool | None = Field(None, alias='isUserOutOfRegion')
    is_video_watch_page: bool | None = Field(None, alias='isVideoWatchPage')
    labs_sdk_version: str | None = Field(None, alias='labsSDKVersion')
    labs_track_url: str | None = Field(None, alias='labsTrackUrl')
    language_variables: LanguageVariables | None = Field(None, alias='languageVariables')
    logo_path: str | None = Field(None, alias='logoPath')
    mapped_data: MappedData | None = Field(None, alias='mappedData')
    og_site_name: str | None = Field(None, alias='ogSiteName')
    omd_component: str | None = Field(None, alias='omdComponent')
    page_data: str | None = Field(None, alias='pageData')
    media_melon_config: MediaMelonConfig | None = Field(None, alias='mediaMelonConfig')
    prism_script: str | None = Field(None, alias='prismScript')
    related_app_urls: RelatedAppUrls | None = Field(None, alias='relatedAppUrls')
    screen_name: str | None = Field(None, alias='screenName')
    season_seo_page_title: str | None = Field(None, alias='seasonSEOPageTitle')
    selected_season_number: int | None = Field(None, alias='selectedSeasonNumber')
    sentry_dsn: str | None = Field(None, alias='sentryDSN')
    version: str | None = None
    tenant_id: str | None = Field(None, alias='tenantId')
    twitter_handle: str | None = Field(None, alias='twitterHandle')
    user_country: str | None = Field(None, alias='userCountry')
    user_region_cookie: str | None = Field(None, alias='userRegionCookie')
    utm_params: list[str] | None = Field(None, alias='utmParams')
    video_watch_ids: Any | None = Field(None, alias='videoWatchIds')

class Props(BaseModel):
    model_config = ConfigDict(extra='ignore')
    page_props: PageProps | None = Field(None, alias='pageProps')
    field__n_ssp: bool | None = Field(None, alias='__N_SSP')

class Query(BaseModel):
    model_config = ConfigDict(extra='ignore')
    slug: list[str | UUID] | None = None

class ShowModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    props: Props | None = None
    page: str | None = None
    query: Query | None = None
    build_id: str | None = Field(None, alias='buildId')
    asset_prefix: str | None = Field(None, alias='assetPrefix')
    is_fallback: bool | None = Field(None, alias='isFallback')
    is_experimental_compile: bool | None = Field(None, alias='isExperimentalCompile')
    gssp: bool | None = None
    app_gip: bool | None = Field(None, alias='appGip')
    locale: str | None = None
    locales: list[str] | None = None
    default_locale: str | None = Field(None, alias='defaultLocale')
    script_loader: list[Any] | None = Field(None, alias='scriptLoader')
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
