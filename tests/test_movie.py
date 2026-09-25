# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from minbo.exceptions import MovieNotFoundError

if TYPE_CHECKING:
    from minbo import MinBO

MOVIE_IDS = [
    pytest.param("92b085e4-764c-41ca-a46f-4d76a5b28642", id="the long walk"),
    pytest.param(
        "14a0d4dc-79f0-40f1-8967-fded774b2593",
        id="movie the site links to as a show",
    ),
]

NOT_MOVIE_IDS = [
    pytest.param(
        "00000000-0000-0000-0000-000000000000",
        id="movie that does not exist",
    ),
    pytest.param(
        "b692705b-2f12-4a3d-ab4d-579124e0667c",
        id="series asked for as a movie",
    ),
]


# TODO: Validate
@pytest.mark.parametrize("movie_id", MOVIE_IDS)
def test_download(client: MinBO, movie_id: str) -> None:
    movie = client.movie(movie_id)
    assert str(movie.title_key) == movie_id


# TODO: Validate
@pytest.mark.parametrize("movie_id", NOT_MOVIE_IDS)
def test_download_invalid(client: MinBO, movie_id: str) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movie.download(movie_id)
