# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import pytest

if TYPE_CHECKING:
    from minbo import MinBO


# TODO: Validate
@pytest.mark.parametrize(
    ("kind", "media_type"),
    [("movies", "movie"), ("shows", "series")],
)
def test_download(
    client: MinBO,
    kind: Literal["movies", "shows"],
    media_type: str,
) -> None:
    sitemap = client.sitemap(kind)
    assert sitemap.titles
    assert {title.media_type for title in sitemap.titles} == {media_type}
