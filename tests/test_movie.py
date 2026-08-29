# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from minbo.exceptions import MovieNotFoundError
from minbo.movie.models import MovieModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from minbo import MinBO

MOVIES = [
    pytest.param(
        "long-walk",
        "92b085e4-764c-41ca-a46f-4d76a5b28642",
        id="the long walk",
    ),
    pytest.param(
        "batman-mask-of-the-phantasm",
        "14a0d4dc-79f0-40f1-8967-fded774b2593",
        id="movie the site links to as a show",
    ),
]


# TODO: Validate
class MovieTest(RecordedEndpoint):
    MODEL = MovieModel


# TODO: Validate
@pytest.mark.parametrize(("name", "movie_id"), MOVIES)
def test_download(client: MinBO, name: str, movie_id: str) -> None:
    MovieTest.download_test(name, lambda: client.movie.download(movie_id))


# TODO: Validate
@pytest.mark.parametrize(("name", "movie_id"), MOVIES)
def test_parse(client: MinBO, name: str, movie_id: str) -> None:
    movie = client.movie.load(MovieTest.recorded_content(name))
    assert str(movie.props.page_props.mapped_data.idref14.feature_id) == movie_id


# TODO: Validate
@pytest.mark.parametrize(
    "movie_id",
    [
        pytest.param(
            "00000000-0000-0000-0000-000000000000",
            id="movie that does not exist",
        ),
        pytest.param(
            "b692705b-2f12-4a3d-ab4d-579124e0667c",
            id="series asked for as a movie",
        ),
    ],
)
def test_download_invalid(client: MinBO, movie_id: str) -> None:
    MovieTest.error_test(
        movie_id,
        lambda: client.movie.download(movie_id),
        MovieNotFoundError,
    )
