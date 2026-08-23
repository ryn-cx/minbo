from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any
from uuid import UUID
from datetime import date, timedelta

class DeveloperPanelConfig(BaseModel):
    enabled: bool
    minimized: bool

class Action(BaseModel):
    lg: int

class Indicator(BaseModel):
    badge: int

class Option(BaseModel):
    checkbox: int

class Input(BaseModel):
    field: int
    option: Option
    toggle: int
    toggle_thumb: int

class Corner(BaseModel):
    action: Action
    full: int
    indicator: Indicator
    input: Input
    lg: int
    md: int
    none: int
    sm: int

class Chip(BaseModel):
    selected: int
    unselected: int

class Option1(BaseModel):
    emphasis: int
    selected: int
    unselected: int

class Toggle(BaseModel):
    emphasis: float
    selected: int
    unselected: int

class Input1(BaseModel):
    option: Option1
    toggle: Toggle

class Notify(BaseModel):
    container_border: int

class Stroke(BaseModel):
    bold: int
    chip: Chip
    extra_bold: int
    input: Input1
    medium: float
    none: int
    notify: Notify
    regular: int
    thin: float

class BorderToken(BaseModel):
    corner: Corner
    stroke: Stroke

class Alt(BaseModel):
    surface_00: str
    surface_01: str
    surface_01_film: str
    surface_01_glass: str

class Base(BaseModel):
    scrim_01: str
    scrim_02: str
    surface_00: str
    surface_00_smoke: str
    surface_01: str
    surface_01_film: str
    surface_01_smoke: str
    surface_02: str
    surface_03: str
    surface_accent: str

class Background(BaseModel):
    alt: Alt
    base: Base

class Plan(BaseModel):
    base_fill: str
    base_text: str
    special_fill: str
    special_text: str
    tab_fill: str
    tab_text: str

class Badge(BaseModel):
    fill_highlight_free: str
    fill_tile_free: str
    outline_highlight_free: str
    plan: Plan
    text_highlight_free: str
    text_tile_free: str

class Button(BaseModel):
    fill_loud: str
    fill_loud_hover: str
    fill_quiet: str
    fill_quiet_hover: str
    label_loud: str
    outline_quiet: str
    outline_quiet_hover: str

class Chip1(BaseModel):
    fill_selected: str
    outline_selected: str
    outline_unselected: str

class Fill(BaseModel):
    action_accent: str
    action_accent_dim: str
    action_accent_film: str
    action_default: str
    action_disabled_01: str
    action_disabled_02: str
    action_light: str
    action_quiet: str
    action_shade: str
    brand_dark: str
    indicator_advertisement: str
    indicator_background: str
    indicator_foreground: str
    indicator_live: str
    indicator_quiet: str
    notify_error: str
    notify_message: str
    skeleton: str
    skeleton_pressed: str

class Onalt(BaseModel):
    text_01: str
    text_02: str
    text_03: str

class Onbase(BaseModel):
    text_01: str
    text_02: str
    text_03: str
    text_action_accent: str
    text_action_accent_pressed: str
    text_notify_error: str
    text_notify_message: str

class Foreground(BaseModel):
    onalt: Onalt
    onbase: Onbase

class Indicator1(BaseModel):
    fill_background: str
    fill_foreground_loud: str

class FieldModel(BaseModel):
    action_fill_focus: str
    action_icon_focus: str
    action_icon_on_focus: str
    fill_focus: str
    text_focus: str

class Option2(BaseModel):
    fill_radio_selected: str
    outline_selected: str
    outline_unselected: str
    text_label: str

class Toggle1(BaseModel):
    icon_thumb: str
    outline_selected: str
    outline_unselected: str

class Input2(BaseModel):
    field: FieldModel
    option: Option2
    outline_active: str
    outline_error: str
    outline_inactive: str
    toggle: Toggle1

class Keyboard(BaseModel):
    focus_alt: str
    focus_base: str

class Banner(BaseModel):
    text_error: str
    text_message: str

class Notify1(BaseModel):
    banner: Banner
    icon_error: str
    icon_message: str
    outline_error: str
    outline_message: str

class Onbase1(BaseModel):
    outline_01: str
    outline_02: str
    outline_03: str
    outline_04: str

class Stroke1(BaseModel):
    onbase: Onbase1

class ColorToken(BaseModel):
    background: Background
    badge: Badge
    button: Button
    chip: Chip1
    fill: Fill
    foreground: Foreground
    indicator: Indicator1
    input: Input2
    keyboard: Keyboard
    notify: Notify1
    stroke: Stroke1
    transparent: str

class Gutter(BaseModel):
    bp_01: int
    bp_03: int
    bp_04: int
    bp_05: int
    bp_06: int

class Margin(BaseModel):
    bp_01: int
    bp_03: int
    bp_04: int
    bp_05: int
    bp_06: int

class MarginOffset(BaseModel):
    bp_01: int
    bp_03: int
    bp_04: int
    bp_05: int
    bp_06: int

class Vertical(BaseModel):
    bp_01: int
    bp_03: int
    bp_04: int
    bp_05: int
    bp_06: int

class Universal(BaseModel):
    field_12: int = Field(..., alias='_12')
    field_16: int = Field(..., alias='_16')
    field_20: int = Field(..., alias='_20')
    field_24: int = Field(..., alias='_24')
    field_28: int = Field(..., alias='_28')
    field_32: int = Field(..., alias='_32')
    field_36: int = Field(..., alias='_36')
    field_40: int = Field(..., alias='_40')
    field_44: int = Field(..., alias='_44')
    field_48: int = Field(..., alias='_48')
    field_60: int = Field(..., alias='_60')
    field_68: int = Field(..., alias='_68')
    field_72: int = Field(..., alias='_72')
    field_80: int = Field(..., alias='_80')
    field_100: int = Field(..., alias='_100')
    field_120: int = Field(..., alias='_120')
    field_00: int = Field(..., alias='_00')
    field_02: int = Field(..., alias='_02')
    field_04: int = Field(..., alias='_04')
    field_08: int = Field(..., alias='_08')

class SpacerToken(BaseModel):
    gutter: Gutter
    margin: Margin
    margin_offset: MarginOffset
    vertical: Vertical
    universal: Universal

class Page(BaseModel):
    surface_accent: str = Field(..., alias='surface-accent')
    surface_00: str = Field(..., alias='surface-00')
    surface_default: str = Field(..., alias='surface-default')
    surface_basic: str = Field(..., alias='surface-basic')

class Band(BaseModel):
    surface_fill_01: str = Field(..., alias='surface-fill-01')
    surface_fill_02: str = Field(..., alias='surface-fill-02')
    action_light: str = Field(..., alias='action-light')
    action_default: str = Field(..., alias='action-default')
    surface_fill_gradient_01: str = Field(..., alias='surface-fill-gradient-01')
    surface_fill_gradient_02: str = Field(..., alias='surface-fill-gradient-02')

class Column(BaseModel):
    surface_fill_01: str = Field(..., alias='surface-fill-01')
    surface_fill_02: str = Field(..., alias='surface-fill-02')
    action_light: str = Field(..., alias='action-light')
    action_default: str = Field(..., alias='action-default')
    surface_fill_gradient_01: str = Field(..., alias='surface-fill-gradient-01')
    surface_fill_gradient_02: str = Field(..., alias='surface-fill-gradient-02')

class Backgrounds(BaseModel):
    page: Page
    band: Band
    column: Column

class ResolvedTheme(BaseModel):
    border_token: BorderToken = Field(..., alias='BorderToken')
    color_token: ColorToken = Field(..., alias='ColorToken')
    spacer_token: SpacerToken = Field(..., alias='SpacerToken')
    backgrounds: Backgrounds
    font_family: str = Field(..., alias='fontFamily')

class TenantStyles(BaseModel):
    design_systems: str = Field(..., alias='designSystems')
    tenant_styles: str = Field(..., alias='tenantStyles')

class AuthState(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class SignIn(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class User(BaseModel):
    auth_state: AuthState = Field(..., alias='authState')
    sign_in: SignIn = Field(..., alias='signIn')

class PageView(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class PageName(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class AnalyticsTitle(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class PreviousPageName(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class SiteSection(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class PageCategory(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class UserCountry(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class UserLanguage(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class UserRegion(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class UserCity(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class UserContinent(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Navigation(BaseModel):
    page_view: PageView = Field(..., alias='pageView')
    page_name: PageName = Field(..., alias='pageName')
    analytics_title: AnalyticsTitle = Field(..., alias='analyticsTitle')
    previous_page_name: PreviousPageName = Field(..., alias='previousPageName')
    site_section: SiteSection = Field(..., alias='siteSection')
    page_category: PageCategory = Field(..., alias='pageCategory')
    user_country: UserCountry = Field(..., alias='userCountry')
    user_language: UserLanguage = Field(..., alias='userLanguage')
    user_region: UserRegion = Field(..., alias='userRegion')
    user_city: UserCity = Field(..., alias='userCity')
    user_continent: UserContinent = Field(..., alias='userContinent')

class ModuleName(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class BandName(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Headline(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class PageDepth(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Interaction(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class CardType(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class CarouselPosition(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class EventAction(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class ElementType(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class EventLabel(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Module(BaseModel):
    module_name: ModuleName = Field(..., alias='moduleName')
    band_name: BandName = Field(..., alias='bandName')
    headline: Headline
    page_depth: PageDepth = Field(..., alias='pageDepth')
    interaction: Interaction
    card_type: CardType = Field(..., alias='cardType')
    carousel_position: CarouselPosition = Field(..., alias='carouselPosition')
    event_action: EventAction = Field(..., alias='eventAction')
    element_type: ElementType = Field(..., alias='elementType')
    event_label: EventLabel = Field(..., alias='eventLabel')

class Modal(BaseModel):
    event_action: EventAction = Field(..., alias='eventAction')
    element_type: ElementType = Field(..., alias='elementType')
    event_label: EventLabel = Field(..., alias='eventLabel')

class Category(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Title(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class VideoType(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class ContentId(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Genre(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class SeasonNumber(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class EpisodeNumber(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class CurrentTime(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class AltText(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class PlayerAction(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class IsPopupVideo(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Autoplay(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Video(BaseModel):
    category: Category
    title: Title
    video_type: VideoType = Field(..., alias='videoType')
    content_id: ContentId = Field(..., alias='contentID')
    genre: Genre
    season_number: SeasonNumber = Field(..., alias='seasonNumber')
    episode_number: EpisodeNumber = Field(..., alias='episodeNumber')
    current_time: CurrentTime = Field(..., alias='currentTime')
    alt_text: AltText = Field(..., alias='altText')
    player_action: PlayerAction = Field(..., alias='playerAction')
    is_popup_video: IsPopupVideo = Field(..., alias='isPopupVideo')
    autoplay: Autoplay

class LinkUrl(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class ContentName(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class ContentCategory(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class CastAndCrew(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class RatingCode(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Brand(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Content(BaseModel):
    alt_text: AltText = Field(..., alias='altText')
    link_url: LinkUrl = Field(..., alias='linkURL')
    content_id: ContentId = Field(..., alias='contentID')
    content_name: ContentName = Field(..., alias='contentName')
    content_category: ContentCategory = Field(..., alias='contentCategory')
    genre: Genre
    cast_and_crew: CastAndCrew = Field(..., alias='castAndCrew')
    rating_code: RatingCode = Field(..., alias='ratingCode')
    brand: Brand
    element_type: ElementType = Field(..., alias='elementType')

class Text(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Element(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Destination(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Cta(BaseModel):
    text: Text
    element: Element
    destination: Destination

class GateAction(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class GateElement(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class GatedContentTitle(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Gate(BaseModel):
    gate_action: GateAction = Field(..., alias='gateAction')
    gate_element: GateElement = Field(..., alias='gateElement')
    gated_content_title: GatedContentTitle = Field(..., alias='gatedContentTitle')

class EmailSubmissionSuccess(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class B2bFieldValue(BaseModel):
    data_layer: str = Field(..., alias='dataLayer')

class Email(BaseModel):
    email_submission_success: EmailSubmissionSuccess = Field(..., alias='emailSubmissionSuccess')
    b2b_field_value: B2bFieldValue = Field(..., alias='b2bFieldValue')

class Schemas(BaseModel):
    user: User
    navigation: Navigation
    module: Module
    modal: Modal
    video: Video
    content: Content
    cta: Cta
    gate: Gate
    email: Email

class Navigation1(BaseModel):
    page_view: list[str] = Field(..., alias='pageView')
    page_name: list[str] = Field(..., alias='pageName')
    analytics_title: list[str] = Field(..., alias='analyticsTitle')
    previous_page_name: list[str] = Field(..., alias='previousPageName')
    site_section: list[str] = Field(..., alias='siteSection')
    page_category: list[str] = Field(..., alias='pageCategory')
    user_country: list[str] = Field(..., alias='userCountry')
    user_language: list[str] = Field(..., alias='userLanguage')
    user_region: list[str] = Field(..., alias='userRegion')
    user_city: list[str] = Field(..., alias='userCity')
    user_continent: list[str] = Field(..., alias='userContinent')

class User1(BaseModel):
    sign_in: list[str] = Field(..., alias='signIn')

class Content1(BaseModel):
    content_id: list[str] = Field(..., alias='contentID')
    content_name: list[str] = Field(..., alias='contentName')
    content_category: list[str] = Field(..., alias='contentCategory')
    genre: list[str]
    cast_and_crew: list[str] = Field(..., alias='castAndCrew')
    rating_code: list[str] = Field(..., alias='ratingCode')
    brand: list[str]
    link_url: list[str] = Field(..., alias='linkURL')

class PageTrack(BaseModel):
    navigation: Navigation1
    user: User1
    content: Content1

class Cta1(BaseModel):
    text: list[str]
    element: list[str]
    destination: list[str]

class Module1(BaseModel):
    module_name: list[str] = Field(..., alias='moduleName')
    band_name: list[str] = Field(..., alias='bandName')
    headline: list[str]
    page_depth: list[str] = Field(..., alias='pageDepth')
    interaction: list[str]
    card_type: list[str] = Field(..., alias='cardType')
    carousel_position: list[str] = Field(..., alias='carouselPosition')
    event_action: list[str] = Field(..., alias='eventAction')
    element_type: list[str] = Field(..., alias='elementType')
    event_label: list[str] = Field(..., alias='eventLabel')

class Video1(BaseModel):
    category: list[str]
    title: list[str]
    video_type: list[str] = Field(..., alias='videoType')
    content_id: list[str] = Field(..., alias='contentID')
    genre: list[str]
    season_number: list[str] = Field(..., alias='seasonNumber')
    episode_number: list[str] = Field(..., alias='episodeNumber')
    alt_text: list[str] = Field(..., alias='altText')
    is_popup_video: list[str] = Field(..., alias='isPopupVideo')
    autoplay: list[str]

class Content2(BaseModel):
    alt_text: list[str] = Field(..., alias='altText')
    link_url: list[str] = Field(..., alias='linkURL')
    content_id: list[str] = Field(..., alias='contentID')
    content_name: list[str] = Field(..., alias='contentName')
    content_category: list[str] = Field(..., alias='contentCategory')
    genre: list[str]
    rating_code: list[str] = Field(..., alias='ratingCode')
    brand: list[str]
    element_type: list[str] = Field(..., alias='elementType')

class Click(BaseModel):
    cta: Cta1
    module: Module1
    video: Video1
    content: Content2

class Module2(BaseModel):
    module_name: list[str] = Field(..., alias='moduleName')
    band_name: list[str] = Field(..., alias='bandName')
    page_depth: list[str] = Field(..., alias='pageDepth')
    interaction: list[str]
    card_type: list[str] = Field(..., alias='cardType')
    carousel_position: list[str] = Field(..., alias='carouselPosition')

class Video2(BaseModel):
    category: list[str]
    title: list[str]
    video_type: list[str] = Field(..., alias='videoType')
    content_id: list[str] = Field(..., alias='contentID')
    genre: list[str]
    season_number: list[str] = Field(..., alias='seasonNumber')
    episode_number: list[str] = Field(..., alias='episodeNumber')
    current_time: list[str] = Field(..., alias='currentTime')
    player_action: list[str] = Field(..., alias='playerAction')
    alt_text: list[str] = Field(..., alias='altText')
    is_popup_video: list[str] = Field(..., alias='isPopupVideo')
    autoplay: list[str]

class VideoPlayer(BaseModel):
    module: Module2
    video: Video2

class Module3(BaseModel):
    module_name: list[str] = Field(..., alias='moduleName')
    band_name: list[str] = Field(..., alias='bandName')
    headline: list[str]
    page_depth: list[str] = Field(..., alias='pageDepth')
    interaction: list[str]

class Gate1(BaseModel):
    gate_action: list[str] = Field(..., alias='gateAction')
    gate_element: list[str] = Field(..., alias='gateElement')
    gated_content_title: list[str] = Field(..., alias='gatedContentTitle')

class Gating(BaseModel):
    module: Module3
    gate: Gate1

class Module4(BaseModel):
    module_name: list[str] = Field(..., alias='moduleName')
    band_name: list[str] = Field(..., alias='bandName')
    page_depth: list[str] = Field(..., alias='pageDepth')

class Email2(BaseModel):
    email_submission_success: list[str] = Field(..., alias='emailSubmissionSuccess')
    b2b_field_value: list[str] = Field(..., alias='b2bFieldValue')

class Email1(BaseModel):
    module: Module4
    email: Email2
    cta: Cta1

class Events(BaseModel):
    page_track: PageTrack = Field(..., alias='pageTrack')
    click: Click
    video_player: VideoPlayer = Field(..., alias='videoPlayer')
    gating: Gating
    email: Email1

class AnalyticsMapping(BaseModel):
    schemas: Schemas
    events: Events

class RelatedAppUrls(BaseModel):
    account: str
    add_on: str = Field(..., alias='addOn')
    create_account: str = Field(..., alias='createAccount')
    help: str
    home: str
    login: str
    play: str
    subscribe: str

class AnalyticsConfig(BaseModel):
    analytics_mapping: AnalyticsMapping = Field(..., alias='analyticsMapping')
    frameworks: list[None]
    related_app_urls: RelatedAppUrls = Field(..., alias='relatedAppUrls')

class BrazeConfig(BaseModel):
    braze_endpoint: None = Field(..., alias='brazeEndpoint')
    ek: None
    email_signup_source: str = Field(..., alias='emailSignupSource')
    eps: str

class UsEs(BaseModel):
    url: str
    start_date: AwareDatetime = Field(..., alias='startDate')
    end_date: AwareDatetime = Field(..., alias='endDate')

class AuEn(BaseModel):
    url: str
    start_date: AwareDatetime = Field(..., alias='startDate')
    end_date: AwareDatetime = Field(..., alias='endDate')

class CountryLangUris(BaseModel):
    us_es: UsEs = Field(..., alias='us/es')
    au_en: AuEn = Field(..., alias='au/en')

class CountryMapping(BaseModel):
    language: str
    country_code: str = Field(..., alias='countryCode')
    bcp47_code: str = Field(..., alias='bcp47Code')

class CountryToDefaultLang(BaseModel):
    bn: str = Field(..., alias='BN')
    mo: str = Field(..., alias='MO')
    bo: str = Field(..., alias='BO')
    rs: str = Field(..., alias='RS')
    es: str = Field(..., alias='ES')
    ba: str = Field(..., alias='BA')
    kz: str = Field(..., alias='KZ')
    mk: str = Field(..., alias='MK')
    si: str = Field(..., alias='SI')
    fr: str = Field(..., alias='FR')
    th: str = Field(..., alias='TH')
    ua: str = Field(..., alias='UA')
    my: str = Field(..., alias='MY')
    nz: str = Field(..., alias='NZ')
    cx: str = Field(..., alias='CX')
    gp: str = Field(..., alias='GP')
    gf: str = Field(..., alias='GF')
    re: str = Field(..., alias='RE')
    il: str = Field(..., alias='IL')
    bb: str = Field(..., alias='BB')
    vc: str = Field(..., alias='VC')
    dm: str = Field(..., alias='DM')
    hn: str = Field(..., alias='HN')
    tc: str = Field(..., alias='TC')
    sr: str = Field(..., alias='SR')
    gt: str = Field(..., alias='GT')
    ht: str = Field(..., alias='HT')
    ar: str = Field(..., alias='AR')
    it: str = Field(..., alias='IT')
    us: str = Field(..., alias='US')
    vi: str = Field(..., alias='VI')
    gu: str = Field(..., alias='GU')
    in_: str = Field(..., alias='IN')
    kh: str = Field(..., alias='KH')
    pk: str = Field(..., alias='PK')
    tl: str = Field(..., alias='TL')
    pw: str = Field(..., alias='PW')
    bg: str = Field(..., alias='BG')
    me: str = Field(..., alias='ME')
    pl: str = Field(..., alias='PL')
    nl: str = Field(..., alias='NL')
    lt: str = Field(..., alias='LT')
    ee: str = Field(..., alias='EE')
    no: str = Field(..., alias='NO')
    cc: str = Field(..., alias='CC')
    pf: str = Field(..., alias='PF')
    fo: str = Field(..., alias='FO')
    gl: str = Field(..., alias='GL')
    ph: str = Field(..., alias='PH')
    bl: str = Field(..., alias='BL')
    wf: str = Field(..., alias='WF')
    mc: str = Field(..., alias='MC')
    sm: str = Field(..., alias='SM')
    lu: str = Field(..., alias='LU')
    bs: str = Field(..., alias='BS')
    lc: str = Field(..., alias='LC')
    gy: str = Field(..., alias='GY')
    kn: str = Field(..., alias='KN')
    uy: str = Field(..., alias='UY')
    gd: str = Field(..., alias='GD')
    ms: str = Field(..., alias='MS')
    jm: str = Field(..., alias='JM')
    cr: str = Field(..., alias='CR')
    pa: str = Field(..., alias='PA')
    um: str = Field(..., alias='UM')
    md: str = Field(..., alias='MD')
    pg: str = Field(..., alias='PG')
    mm: str = Field(..., alias='MM')
    np: str = Field(..., alias='NP')
    bz: str = Field(..., alias='BZ')
    sk: str = Field(..., alias='SK')
    se: str = Field(..., alias='SE')
    dk: str = Field(..., alias='DK')
    hk: str = Field(..., alias='HK')
    ge: str = Field(..., alias='GE')
    cz: str = Field(..., alias='CZ')
    tj: str = Field(..., alias='TJ')
    tr: str = Field(..., alias='TR')
    ro: str = Field(..., alias='RO')
    gr: str = Field(..., alias='GR')
    jp: str = Field(..., alias='JP')
    tw: str = Field(..., alias='TW')
    nf: str = Field(..., alias='NF')
    pm: str = Field(..., alias='PM')
    mq: str = Field(..., alias='MQ')
    yt: str = Field(..., alias='YT')
    ch: str = Field(..., alias='CH')
    aw: str = Field(..., alias='AW')
    ag: str = Field(..., alias='AG')
    py: str = Field(..., alias='PY')
    mx: str = Field(..., alias='MX')
    br: str = Field(..., alias='BR')
    do: str = Field(..., alias='DO')
    co: str = Field(..., alias='CO')
    pe: str = Field(..., alias='PE')
    as_: str = Field(..., alias='AS')
    bd: str = Field(..., alias='BD')
    sb: str = Field(..., alias='SB')
    hu: str = Field(..., alias='HU')
    pt: str = Field(..., alias='PT')
    be: str = Field(..., alias='BE')
    hr: str = Field(..., alias='HR')
    kg: str = Field(..., alias='KG')
    id: str = Field(..., alias='ID')
    lv: str = Field(..., alias='LV')
    mt: str = Field(..., alias='MT')
    au: str = Field(..., alias='AU')
    hm: str = Field(..., alias='HM')
    sj: str = Field(..., alias='SJ')
    ax: str = Field(..., alias='AX')
    de: str = Field(..., alias='DE')
    li: str = Field(..., alias='LI')
    ni: str = Field(..., alias='NI')
    cw: str = Field(..., alias='CW')
    ec: str = Field(..., alias='EC')
    cl: str = Field(..., alias='CL')
    mp: str = Field(..., alias='MP')
    mn: str = Field(..., alias='MN')
    la: str = Field(..., alias='LA')
    lk: str = Field(..., alias='LK')
    is_: str = Field(..., alias='IS')
    cy: str = Field(..., alias='CY')
    al: str = Field(..., alias='AL')
    am: str = Field(..., alias='AM')
    fi: str = Field(..., alias='FI')
    xk: str = Field(..., alias='XK')
    mf: str = Field(..., alias='MF')
    sg: str = Field(..., alias='SG')
    az: str = Field(..., alias='AZ')
    uz: str = Field(..., alias='UZ')
    va: str = Field(..., alias='VA')
    ai: str = Field(..., alias='AI')
    vg: str = Field(..., alias='VG')
    ky: str = Field(..., alias='KY')
    sv: str = Field(..., alias='SV')
    tt: str = Field(..., alias='TT')
    gb: str = Field(..., alias='GB')
    ie: str = Field(..., alias='IE')
    at: str = Field(..., alias='AT')
    pr: str = Field(..., alias='PR')
    to: str = Field(..., alias='TO')
    ad: str = Field(..., alias='AD')

class CountryToRegion(BaseModel):
    mc: str
    hk: str
    tw: str
    ph: str
    sg: str
    bn: str
    mo: str
    ba: str
    pt: str
    hu: str
    no: str
    ro: str
    kg: str
    my: str
    bo: str
    rs: str
    es: str
    kz: str
    mk: str
    si: str
    fr: str
    th: str
    ua: str
    nz: str
    cx: str
    gp: str
    gf: str
    re: str
    ch: str
    it: str
    il: str
    bb: str
    vc: str
    dm: str
    gy: str
    hn: str
    mx: str
    tc: str
    sr: str
    cw: str
    co: str
    gd: str
    gt: str
    sv: str
    ht: str
    cr: str
    pa: str
    ar: str
    ni: str
    ec: str
    ws: str
    us: str
    vi: str
    gu: str
    tv: str
    md: str
    tk: str
    in_: str = Field(..., alias='in')
    kh: str
    pk: str
    se: str
    tl: str
    pw: str
    bg: str
    ee: str
    me: str
    pl: str
    nl: str
    lt: str
    dk: str
    cc: str
    pf: str
    fo: str
    gl: str
    bl: str
    wf: str
    va: str
    sm: str
    li: str
    lu: str
    bs: str
    lc: str
    vg: str
    py: str
    kn: str
    uy: str
    ms: str
    jm: str
    aw: str
    um: str
    mh: str
    fm: str
    vn: str
    ck: str
    bz: str
    pg: str
    mm: str
    np: str
    cz: str
    tr: str
    cy: str
    sk: str
    ge: str
    tj: str
    gr: str
    jp: str
    nf: str
    pm: str
    mq: str
    yt: str
    ag: str
    cl: str
    br: str
    do: str
    pe: str
    ki: str
    bt: str
    as_: str = Field(..., alias='as')
    nr: str
    fj: str
    be: str
    bd: str
    sb: str
    am: str
    fi: str
    hr: str
    id: str
    lv: str
    mt: str
    au: str
    hm: str
    sj: str
    ax: str
    de: str
    ky: str
    tt: str
    mp: str
    mv: str
    nu: str
    ad: str
    mn: str
    la: str
    lk: str
    is_: str = Field(..., alias='is')
    al: str
    xk: str
    mf: str
    az: str
    uz: str
    ai: str
    gb: str
    ie: str
    at: str
    pr: str
    im: str
    vu: str
    to: str

class LanguageVariables(BaseModel):
    lang: str
    country: str
    region: str

class Flags(BaseModel):
    has_audio_description: bool = Field(..., alias='hasAudioDescription')
    is_uhd: bool = Field(..., alias='isUHD')
    has_dolby_atmos: bool = Field(..., alias='hasDolbyAtmos')
    has_dolby_vision: bool = Field(..., alias='hasDolbyVision')
    has_pse_advisory: bool = Field(..., alias='hasPSEAdvisory')

class Trailer(BaseModel):
    program_id: None = Field(..., alias='programId')
    edit_id: None = Field(..., alias='editId')
    title: None
    description: None
    url: None

class OfferingDates(BaseModel):
    start_date: AwareDatetime = Field(..., alias='startDate')
    end_date: AwareDatetime = Field(..., alias='endDate')

class Title1(BaseModel):
    short: str
    full: str

class Credits(BaseModel):
    starring: str
    directors: str
    writers: str
    producers: str
    creators: str
    sources: str
    sign_interpreters: str = Field(..., alias='signInterpreters')

class ActorItem(BaseModel):
    field_type: str = Field(..., alias='@type')
    name: str

class CastAndCrew1(BaseModel):
    actor: list[ActorItem] = Field(..., alias='Actor')
    cast: None = Field(..., alias='Cast')
    producer: None = Field(..., alias='Producer')
    director: None = Field(..., alias='Director')
    writer: None = Field(..., alias='Writer')

class Summary(BaseModel):
    short: str
    full: str

class Images(BaseModel):
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

class LocalizedRating(BaseModel):
    rating_authority: str
    classifier: str
    descriptors: list[None]

class Idref14(BaseModel):
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
    title: Title1
    credits: Credits
    cast_and_crew: CastAndCrew1 = Field(..., alias='castAndCrew')
    summary: Summary
    images: Images
    status: str
    rating: dict[str, Any]
    runtime: str
    quality: None
    primary_genre: str = Field(..., alias='primaryGenre')
    secondary_genre: str = Field(..., alias='secondaryGenre')
    genres_formatted: str = Field(..., alias='genresFormatted')
    release_year: str = Field(..., alias='releaseYear')
    release_date: date = Field(..., alias='releaseDate')
    localized_rating: LocalizedRating = Field(..., alias='localizedRating')

class Default(BaseModel):
    en_us: str = Field(..., alias='en_US')
    url: str

class Mobile(BaseModel):
    en_us: str = Field(..., alias='en_US')
    url: str

class BrowseAudioDescription(BaseModel):
    default: Default
    mobile: Mobile

class Default1(BaseModel):
    en_us: str = Field(..., alias='en_US')

class Mobile1(BaseModel):
    en_us: str = Field(..., alias='en_US')

class UnauthLabel(BaseModel):
    default: Default1
    mobile: Mobile1

class AuthLabel(BaseModel):
    default: Default1
    mobile: Mobile1

class SecondaryCta(BaseModel):
    unauth_label: UnauthLabel = Field(..., alias='unauthLabel')
    unauth_url: str = Field(..., alias='unauthUrl')
    auth_url: str = Field(..., alias='authUrl')
    auth_label: AuthLabel = Field(..., alias='authLabel')

class AltText2(BaseModel):
    en_us: str = Field(..., alias='en_US')

class Logo(BaseModel):
    alt_text: AltText2 = Field(..., alias='altText')
    url: str

class Label(BaseModel):
    en_us: str = Field(..., alias='en_US')

class Link(BaseModel):
    label: Label
    url: str = Field(..., alias='URL')

class SecondaryLink(BaseModel):
    link: Link

class UnauthLabel1(BaseModel):
    default: Default1
    mobile: Mobile1

class AuthLabel1(BaseModel):
    default: Default1
    mobile: Mobile1

class PrimaryCta(BaseModel):
    unauth_label: UnauthLabel1 = Field(..., alias='unauthLabel')
    unauth_url: str = Field(..., alias='unauthUrl')
    auth_url: str = Field(..., alias='authUrl')
    auth_label: AuthLabel1 = Field(..., alias='authLabel')

class SkipToContent(BaseModel):
    default: Default1
    mobile: Mobile1

class Idref15(BaseModel):
    browse_audio_description: BrowseAudioDescription = Field(..., alias='browseAudioDescription')
    secondary_cta: SecondaryCta = Field(..., alias='secondaryCta')
    logo: Logo
    secondary_links: list[SecondaryLink] = Field(..., alias='secondaryLinks')
    primary_cta: PrimaryCta = Field(..., alias='primaryCta')
    skip_to_content: SkipToContent = Field(..., alias='skipToContent')

class Idref16Item(BaseModel):
    lang: str
    url: str

class UnauthLabel2(BaseModel):
    default: Default1
    mobile: Mobile1

class AuthLabel2(BaseModel):
    default: Default1
    mobile: Mobile1

class SecondaryCta1(BaseModel):
    unauth_label: UnauthLabel2 = Field(..., alias='unauthLabel')
    unauth_url: str = Field(..., alias='unauthUrl')
    auth_url: str = Field(..., alias='authUrl')
    auth_label: AuthLabel2 = Field(..., alias='authLabel')

class Logo1(BaseModel):
    alt_text: AltText2 = Field(..., alias='altText')
    url: str

class SkipToContent1(BaseModel):
    default: Default1
    mobile: Mobile1

class Idref19(BaseModel):
    secondary_cta: SecondaryCta1 = Field(..., alias='secondaryCta')
    logo: Logo1
    skip_to_content: SkipToContent1 = Field(..., alias='skipToContent')

class Value(BaseModel):
    large: str

class Idref20(BaseModel):
    value: Value

class MaxWidthidref20(BaseModel):
    large: int

class MaxHeightidref20(BaseModel):
    large: int

class Value1(BaseModel):
    large: str
    medium: str
    small: str

class Idref21(BaseModel):
    value: Value1

class MaxWidthidref21(BaseModel):
    large: int
    medium: int
    small: int

class MaxHeightidref21(BaseModel):
    large: int
    medium: int
    small: int

class Value2(BaseModel):
    large: str

class Idref31(BaseModel):
    value: Value2

class MaxWidthidref31(BaseModel):
    large: int

class MaxHeightidref31(BaseModel):
    large: int

class Value3(BaseModel):
    large: str
    medium: str
    small: str

class Idref32(BaseModel):
    value: Value3

class MaxWidthidref32(BaseModel):
    large: int
    medium: int
    small: int

class MaxHeightidref32(BaseModel):
    large: int
    medium: int
    small: int

class Images1(BaseModel):
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
    cover_artwork_square: str = Field(..., alias='cover-artwork-square')
    cover_artwork_horizontal: str = Field(..., alias='cover-artwork-horizontal')

class Idref45Item(BaseModel):
    hbomax_id: UUID = Field(..., alias='hbomaxId')
    type: str
    title: Title1
    image_url_link: str = Field(..., alias='imageUrlLink')
    images: Images1
    offering_dates: OfferingDates = Field(..., alias='offeringDates')
    localized_rating: None = Field(..., alias='localizedRating')
    genres: list[None]
    rank: None

class FirstItem(BaseModel):
    title: Title1

class Description(BaseModel):
    short: None
    full: None

class Image(BaseModel):
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

class RatingCodeItem(BaseModel):
    code: list[str]
    organization: str
    rating_code: timedelta | str = Field(union_mode='left_to_right')

class Title5(BaseModel):
    full_original: None
    short_original: None
    short: str
    full: str

class Images2(BaseModel):
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

class Item(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    series_id: UUID | None = Field(None, alias='seriesId')
    hbomax_url: None = Field(..., alias='hbomaxURL')
    hbomax_id: UUID = Field(..., alias='hbomaxId')
    category: str
    series_title_id: None = Field(None, alias='seriesTitleId')
    image_url_link: str = Field(..., alias='imageUrlLink')
    genres: list[str]
    brand: list[str]
    rating_code: list[RatingCodeItem] = Field(..., alias='ratingCode')
    offering_dates: OfferingDates = Field(..., alias='offeringDates')
    title: Title5
    summary: Summary
    images: Images2
    status: str
    badges: list[None]
    feature_id: UUID | None = Field(None, alias='featureId')
    url: None = Field(None)

class Idref46(BaseModel):
    collection_id: str = Field(..., alias='collectionId')
    image_to_show: str = Field(..., alias='imageToShow')
    first_item: FirstItem = Field(..., alias='firstItem')
    title: Title1
    description: Description
    image: Image
    event_type: str = Field(..., alias='eventType')
    items: list[Item]

class Title6(BaseModel):
    short: str
    full: str

class FirstItem1(BaseModel):
    title: Title6

class Image1(BaseModel):
    default_wide: str = Field(..., alias='default-wide')
    centered_background_small: str = Field(..., alias='centered-background-small')
    default: str
    centered_background: str = Field(..., alias='centered-background')
    cover_artwork: str = Field(..., alias='cover-artwork')
    logo_left: str = Field(..., alias='logo-left')
    content_logo_monochromatic: str = Field(..., alias='content-logo-monochromatic')
    logo_centered: str = Field(..., alias='logo-centered')
    content_logo_polychromatic: str = Field(..., alias='content-logo-polychromatic')
    poster_with_logo: str = Field(..., alias='poster-with-logo')
    cover_artwork_square: str = Field(..., alias='cover-artwork-square')
    cover_artwork_horizontal: str = Field(..., alias='cover-artwork-horizontal')

class RatingCodeItem1(BaseModel):
    code: list[str]
    organization: str
    rating_code: str

class Title8(BaseModel):
    full_original: None
    short_original: None
    short: str
    full: str

class Images3(BaseModel):
    default_wide: str = Field(..., alias='default-wide')
    centered_background_small: str = Field(..., alias='centered-background-small')
    default: str
    centered_background: str = Field(..., alias='centered-background')
    cover_artwork: str = Field(..., alias='cover-artwork')
    logo_left: str = Field(..., alias='logo-left')
    content_logo_monochromatic: str = Field(..., alias='content-logo-monochromatic')
    logo_centered: str = Field(..., alias='logo-centered')
    content_logo_polychromatic: str = Field(..., alias='content-logo-polychromatic')
    poster_with_logo: str = Field(..., alias='poster-with-logo')
    cover_artwork_square: str = Field(..., alias='cover-artwork-square')
    cover_artwork_horizontal: str = Field(..., alias='cover-artwork-horizontal')

class Item1(BaseModel):
    field__typename: str = Field(..., alias='__typename')
    series_id: UUID | None = Field(None, alias='seriesId')
    hbomax_url: None = Field(..., alias='hbomaxURL')
    hbomax_id: UUID = Field(..., alias='hbomaxId')
    category: str
    series_title_id: None = Field(None, alias='seriesTitleId')
    image_url_link: str = Field(..., alias='imageUrlLink')
    genres: list[str]
    brand: list[str]
    rating_code: list[RatingCodeItem1] = Field(..., alias='ratingCode')
    offering_dates: OfferingDates = Field(..., alias='offeringDates')
    title: Title8
    summary: Summary
    images: Images3
    status: str
    feature_id: UUID | None = Field(None, alias='featureId')
    url: None = Field(None)

class Idref60(BaseModel):
    collection_id: str = Field(..., alias='collectionId')
    image_to_show: str = Field(..., alias='imageToShow')
    first_item: FirstItem1 = Field(..., alias='firstItem')
    title: Title6
    description: Description
    image: Image1
    event_type: str = Field(..., alias='eventType')
    items: list[Item1]

class Idref61Item(BaseModel):
    lang: str
    url: str

class Legal(BaseModel):
    en_us: str = Field(..., alias='en_US')

class SecondaryRowItem(BaseModel):
    label: Label
    url: str | None = None
    open_in_new_tab: bool | None = Field(None, alias='openInNewTab')
    is_ccpa_link: bool | None = Field(None, alias='isCCPALink')

class PrimaryRowItem(BaseModel):
    label: Label
    url: str

class Idref63(BaseModel):
    legal: Legal
    secondary_row: list[SecondaryRowItem] = Field(..., alias='secondaryRow')
    primary_row: list[PrimaryRowItem] = Field(..., alias='primaryRow')

class SecondaryRowItem1(BaseModel):
    label: Label
    url: str | None = None
    open_in_new_tab: bool | None = Field(None, alias='openInNewTab')
    is_ccpa_link: bool | None = Field(None, alias='isCCPALink')

class PrimaryRowItem1(BaseModel):
    label: Label
    url: str

class Idref64(BaseModel):
    legal: Legal
    secondary_row: list[SecondaryRowItem1] = Field(..., alias='secondaryRow')
    primary_row: list[PrimaryRowItem1] = Field(..., alias='primaryRow')

class MappedData(BaseModel):
    idref0: str
    idref1: str
    idref2: str
    idref3: str
    idref4: str
    idref5: str
    idref6: str
    idref7: str
    idref8: str
    idref9: str
    idref10: str
    idref11: str
    idref12: str
    idref13: str
    idref14: Idref14
    idref15: Idref15
    idref16: list[Idref16Item]
    idref17: str
    idref18: str
    idref19: Idref19
    idref20: Idref20
    max_widthidref20: MaxWidthidref20 = Field(..., alias='maxWidthidref20')
    max_heightidref20: MaxHeightidref20 = Field(..., alias='maxHeightidref20')
    idref21: Idref21
    max_widthidref21: MaxWidthidref21 = Field(..., alias='maxWidthidref21')
    max_heightidref21: MaxHeightidref21 = Field(..., alias='maxHeightidref21')
    idref22: str
    idref23: str
    idref24: str
    idref25: str
    idref26: str
    idref27: str
    idref28: str
    idref29: str
    idref30: str
    idref31: Idref31
    max_widthidref31: MaxWidthidref31 = Field(..., alias='maxWidthidref31')
    max_heightidref31: MaxHeightidref31 = Field(..., alias='maxHeightidref31')
    idref32: Idref32
    max_widthidref32: MaxWidthidref32 = Field(..., alias='maxWidthidref32')
    max_heightidref32: MaxHeightidref32 = Field(..., alias='maxHeightidref32')
    idref33: str
    idref34: str
    idref35: str
    idref36: str
    idref37: str
    idref38: str
    idref39: str
    idref40: str
    idref41: str
    idref42: str
    idref43: str
    idref44: str
    idref45: list[Idref45Item]
    idref46: Idref46
    idref47: str
    idref48: str
    idref49: str
    idref50: str
    idref51: str
    idref52: str
    idref53: str
    idref54: str
    idref55: str
    idref56: str
    idref57: str
    idref58: str
    idref59: str
    idref60: Idref60
    idref61: list[Idref61Item]
    idref62: str
    idref63: Idref63
    idref64: Idref64
    idref65: str
    idref66: str
    idref67: str
    idref68: str
    idref69: str

class MediaMelonConfig(BaseModel):
    is_media_melon_enabled: bool = Field(..., alias='IS_MEDIA_MELON_ENABLED')
    mm_environment_key: int = Field(..., alias='MM_ENVIRONMENT_KEY')

class PageProps(BaseModel):
    developer_panel_config: DeveloperPanelConfig = Field(..., alias='developerPanelConfig')
    is_published: bool = Field(..., alias='isPublished')
    media_app_id: str = Field(..., alias='mediaAppId')
    resolved_theme: ResolvedTheme = Field(..., alias='resolvedTheme')
    supported_countries: list[None] = Field(..., alias='supportedCountries')
    tenant_styles: TenantStyles = Field(..., alias='tenantStyles')
    version_tag: str = Field(..., alias='versionTag')
    ab_testing_module_hash: str = Field(..., alias='abTestingModuleHash')
    analytics_config: AnalyticsConfig = Field(..., alias='analyticsConfig')
    auth_cookie_name: str = Field(..., alias='authCookieName')
    bcp: str
    braze_config: BrazeConfig = Field(..., alias='brazeConfig')
    canonical_url: str = Field(..., alias='canonicalURL')
    cdn_base_url: str = Field(..., alias='cdnBaseUrl')
    content_type: str = Field(..., alias='contentType')
    country_lang_uris: CountryLangUris = Field(..., alias='countryLangUris')
    country_mappings: list[CountryMapping] = Field(..., alias='countryMappings')
    country_to_default_lang: CountryToDefaultLang = Field(..., alias='countryToDefaultLang')
    country_to_region: CountryToRegion = Field(..., alias='countryToRegion')
    effective_tenant_id: str = Field(..., alias='effectiveTenantId')
    enable_lfe: bool = Field(..., alias='enableLFE')
    environment: str
    experiment_configs: list[None] = Field(..., alias='experimentConfigs')
    event_schedule_dates: None = Field(..., alias='eventScheduleDates')
    formatted_url: str = Field(..., alias='formattedURL')
    geo_redirect_url: str = Field(..., alias='geoRedirectUrl')
    global_domain: str = Field(..., alias='globalDomain')
    has_audio_description: bool = Field(..., alias='hasAudioDescription')
    next_global_domain: None = Field(..., alias='nextGlobalDomain')
    hostname_to_override: None = Field(..., alias='hostnameToOverride')
    is_cms_error_page: bool = Field(..., alias='isCMSErrorPage')
    is_event_page: bool = Field(..., alias='isEventPage')
    is_preview_server: bool = Field(..., alias='isPreviewServer')
    is_season_page: bool = Field(..., alias='isSeasonPage')
    is_user_out_of_region: bool = Field(..., alias='isUserOutOfRegion')
    is_video_watch_page: bool = Field(..., alias='isVideoWatchPage')
    labs_sdk_version: str = Field(..., alias='labsSDKVersion')
    labs_track_url: str = Field(..., alias='labsTrackUrl')
    language_variables: LanguageVariables = Field(..., alias='languageVariables')
    logo_path: str = Field(..., alias='logoPath')
    mapped_data: MappedData = Field(..., alias='mappedData')
    og_site_name: str = Field(..., alias='ogSiteName')
    omd_component: str = Field(..., alias='omdComponent')
    page_data: str = Field(..., alias='pageData')
    media_melon_config: MediaMelonConfig = Field(..., alias='mediaMelonConfig')
    prism_script: str = Field(..., alias='prismScript')
    related_app_urls: RelatedAppUrls = Field(..., alias='relatedAppUrls')
    screen_name: str = Field(..., alias='screenName')
    season_seo_page_title: str = Field(..., alias='seasonSEOPageTitle')
    selected_season_number: None = Field(..., alias='selectedSeasonNumber')
    sentry_dsn: str = Field(..., alias='sentryDSN')
    version: str
    tenant_id: str = Field(..., alias='tenantId')
    twitter_handle: str = Field(..., alias='twitterHandle')
    user_country: str = Field(..., alias='userCountry')
    user_region_cookie: str = Field(..., alias='userRegionCookie')
    utm_params: list[str] = Field(..., alias='utmParams')

class Props(BaseModel):
    page_props: PageProps = Field(..., alias='pageProps')
    field__n_ssp: bool = Field(..., alias='__N_SSP')

class Query(BaseModel):
    lid: str
    slug: list[str | UUID]

class MovieModel(BaseModel):
    props: Props
    page: str
    query: Query
    build_id: str = Field(..., alias='buildId')
    asset_prefix: str = Field(..., alias='assetPrefix')
    is_fallback: bool = Field(..., alias='isFallback')
    is_experimental_compile: bool = Field(..., alias='isExperimentalCompile')
    gssp: bool
    app_gip: bool = Field(..., alias='appGip')
    locale: str
    locales: list[str]
    default_locale: str = Field(..., alias='defaultLocale')
    script_loader: list[None] = Field(..., alias='scriptLoader')
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
