# TODO: Validate

from __future__ import annotations

from typing import Any

from minbo.parsing import (
    build_url,
    mapped_data,
    mapping,
    media_type,
    sequence,
    text_or_none,
)


# TODO: Validate
def parse_sitemap(page: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    return {
        "titles": [
            {
                "title_key": text_or_none(mapping(item).get("hbomaxId")),
                "title": text_or_none(mapping(item).get("title")),
                "url": build_url(mapping(item).get("imageUrlLink")),
                "media_type": media_type(mapping(item).get("contentType")),
            }
            for value in mapped_data(page).values()
            for item in sequence(mapping(value).get("items"))
            if mapping(item).get("hbomaxId")
        ],
    }
