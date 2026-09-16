# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from minbo.exceptions import ShowNotFoundError

if TYPE_CHECKING:
    from minbo import MinBO

SHOWS = [
    pytest.param(
        "b692705b-2f12-4a3d-ab4d-579124e0667c",
        None,
        id="show asked for without naming a season",
    ),
    pytest.param(
        "ab553cdc-e15d-4597-b65f-bec9201fd2dd",
        2,
        id="show asked for by season",
    ),
    pytest.param(
        "396999a6-3fff-4af3-802b-10c46d10deff",
        None,
        id="miniseries with a single season",
    ),
]

NOT_SHOW_IDS = [
    pytest.param("00000000-0000-0000-0000-000000000000", id="show that does not exist"),
    pytest.param(
        "14a0d4dc-79f0-40f1-8967-fded774b2593",
        id="movie asked for as a show",
    ),
]


# TODO: Validate
@pytest.mark.parametrize(("show_id", "season_number"), SHOWS)
def test_download(client: MinBO, show_id: str, season_number: int | None) -> None:
    show = client.show(show_id, season_number)
    series = show.props.page_props.mapped_data.idref14
    assert str(series.series_id) == show_id
    if season_number is not None:
        listed = [season for season in series.seasons if season.episodes]
        assert [season.season_number for season in listed] == [season_number]


# TODO: Validate
@pytest.mark.parametrize("show_id", NOT_SHOW_IDS)
def test_download_invalid(client: MinBO, show_id: str) -> None:
    with pytest.raises(ShowNotFoundError):
        client.show.download(show_id)
