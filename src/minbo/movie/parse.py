# TODO: Validate

from __future__ import annotations

from typing import Any

from minbo.parsing import (
    build_url,
    carousels,
    content,
    related,
    shared_fields,
    text_or_none,
)

FEATURE_ID_KEY = "featureId"


# TODO: Validate
def movie_content(page: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    return content(page, FEATURE_ID_KEY)


# TODO: Validate
def parse_movie(page: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    movie = movie_content(page)
    return {
        "title_key": text_or_none(movie.get(FEATURE_ID_KEY)),
        "url": build_url(movie.get("imageUrlLink")),
        **shared_fields(movie),
        "release_date": text_or_none(movie.get("releaseDate")),
        "runtime": text_or_none(movie.get("runtime")),
        "related": related(page),
        "carousels": carousels(page),
    }
