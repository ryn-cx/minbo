# TODO: Validate

from __future__ import annotations

from typing import Any

SITE_URL = "https://www.hbomax.com"

IMAGE_NAMES = {
    "default": "default",
    "default_wide": "default-wide",
    "centered_background": "centered-background",
    "centered_background_small": "centered-background-small",
    "cover_artwork": "cover-artwork",
    "cover_artwork_horizontal": "cover-artwork-horizontal",
    "cover_artwork_square": "cover-artwork-square",
    "poster_with_logo": "poster-with-logo",
    "logo_left": "logo-left",
    "logo_centered": "logo-centered",
    "content_logo_monochromatic": "content-logo-monochromatic",
    "content_logo_polychromatic": "content-logo-polychromatic",
}

MEDIA_TYPES = {"series": "series", "feature": "movie"}

CREDIT_ROLES = {
    "cast": "Actor",
    "directors": "Director",
    "writers": "Writer",
    "producers": "Producer",
}


# TODO: Validate
def mapping(value: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    return value if isinstance(value, dict) else {}


# TODO: Validate
def sequence(value: Any) -> list[Any]:  # noqa: ANN401 - Any JSON value.
    return value if isinstance(value, list) else []


# TODO: Validate
def text_or_none(value: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    if value is None:
        return None
    text = str(value).strip()
    return text or None


# TODO: Validate
def number_or_none(value: Any) -> float | None:  # noqa: ANN401 - Any JSON value.
    if isinstance(value, bool) or not isinstance(value, int | float):
        return None
    return value


# TODO: Validate
def year_or_none(value: Any) -> int | None:  # noqa: ANN401 - Any JSON value.
    text = text_or_none(value)
    if text is None or not text.isdigit():
        return None
    return int(text)


# TODO: Validate
def texts(values: Any) -> list[str]:  # noqa: ANN401 - Any JSON value.
    return [str(value) for value in sequence(values) if value is not None]


# TODO: Validate
def build_url(path: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    written_path = text_or_none(path)
    if written_path is None:
        return None
    return f"{SITE_URL}/{written_path.lstrip('/')}"


# TODO: Validate
def full_text(value: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    return text_or_none(mapping(value).get("full"))


# TODO: Validate
def images(raw_images: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    named_images = mapping(raw_images)
    return {
        name: text_or_none(named_images.get(key)) for name, key in IMAGE_NAMES.items()
    }


# TODO: Validate
def start_date(dates: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    return text_or_none(mapping(dates).get("startDate"))


# TODO: Validate
def end_date(dates: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    return text_or_none(mapping(dates).get("endDate"))


# TODO: Validate
def maturity_rating(content_node: dict[str, Any]) -> str | None:
    return text_or_none(mapping(content_node.get("localizedRating")).get("classifier"))


# TODO: Validate
def credits_fields(content_node: dict[str, Any]) -> dict[str, Any]:
    cast_and_crew = mapping(content_node.get("castAndCrew"))
    named_roles = {
        field: [
            str(mapping(person)["name"])
            for person in sequence(cast_and_crew.get(role))
            if mapping(person).get("name")
        ]
        for field, role in CREDIT_ROLES.items()
    }
    written_credits = mapping(content_node.get("credits"))
    return {**named_roles, "creators": _written_names(written_credits.get("creators"))}


# TODO: Validate
def _written_names(value: Any) -> list[str]:  # noqa: ANN401 - Any JSON value.
    line = text_or_none(value)
    if line is None:
        return []
    return [name.strip() for name in line.split(",") if name.strip()]


# TODO: Validate
def media_type(value: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    written_type = text_or_none(value)
    if written_type is None:
        return None
    return MEDIA_TYPES.get(written_type.lower())


# TODO: Validate
def title_card(entity: Any, type_key: str) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    listed_title = mapping(entity)
    return {
        "title_key": text_or_none(listed_title.get("hbomaxId")),
        "media_type": media_type(listed_title.get(type_key)),
        "url": build_url(listed_title.get("imageUrlLink")),
        "title": full_text(listed_title.get("title")),
        "summary": full_text(listed_title.get("summary")),
        "genres": texts(listed_title.get("genres")),
        "maturity_rating": maturity_rating(listed_title),
        "images": images(listed_title.get("images")),
    }


# TODO: Validate
def mapped_data(page: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    page_props = mapping(mapping(mapping(page).get("props")).get("pageProps"))
    return mapping(page_props.get("mappedData"))


# TODO: Validate
def content(page: Any, id_key: str) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    for value in mapped_data(page).values():
        if isinstance(value, dict) and value.get(id_key):
            return value
    return {}


# TODO: Validate
def related(page: Any) -> list[dict[str, Any]]:  # noqa: ANN401 - Any JSON value.
    listed_titles: list[dict[str, Any]] = []
    for value in mapped_data(page).values():
        listed_titles += [
            title_card(entity, "type")
            for entity in sequence(value)
            if mapping(entity).get("hbomaxId") and mapping(entity).get("type")
        ]
    return listed_titles


# TODO: Validate
def carousels(page: Any) -> list[dict[str, Any]]:  # noqa: ANN401 - Any JSON value.
    rows: list[dict[str, Any]] = []
    for value in mapped_data(page).values():
        row = mapping(value)
        if not row.get("collectionId"):
            continue
        rows.append(
            {
                "collection_id": text_or_none(row.get("collectionId")),
                "title": full_text(row.get("title")),
                "titles": [
                    title_card(entity, "category")
                    for entity in sequence(row.get("items"))
                ],
            },
        )
    return rows


# TODO: Validate
def shared_fields(content_node: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": full_text(content_node.get("title")),
        "summary": full_text(content_node.get("summary")),
        "release_year": year_or_none(content_node.get("releaseYear")),
        "genres": texts(content_node.get("genres")),
        "primary_genre": text_or_none(content_node.get("primaryGenre")),
        "brands": texts(content_node.get("brand")),
        "maturity_rating": maturity_rating(content_node),
        "images": images(content_node.get("images")),
        "start_date": start_date(content_node.get("offeringDates")),
        "end_date": end_date(content_node.get("offeringDates")),
        "trailer_url": build_url(mapping(content_node.get("trailer")).get("url")),
        **credits_fields(content_node),
    }
