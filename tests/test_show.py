from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from minbo import MinBO
    from minbo.show import Show


class TestData(BaseModel):
    id: UUID
    season: int | None = None
    name: str


TEST_DATA = [
    # Test show without a season.
    TestData(
        id=UUID("b692705b-2f12-4a3d-ab4d-579124e0667c"),
        season=None,
        name="smiling-friends",
    ),
    # Test show with a specific season.
    TestData(
        id=UUID("ab553cdc-e15d-4597-b65f-bec9201fd2dd"),
        season=2,
        name="rick-and-morty-2",
    ),
    # Test mini-series. Also includes an episode titled "1:23:45" which requires a
    # manual replacement field.
    TestData(
        id=UUID("396999a6-3fff-4af3-802b-10c46d10deff"),
        season=None,
        name="chernobyl",
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: MinBO) -> Show:
    return client.show


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.name)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


class TestShow:
    def test_download(self, endpoint: Show, test_data: TestData) -> None:
        download_and_save(
            endpoint,
            test_data.name,
            lambda: endpoint.download(
                str(test_data.id),
                season_number=test_data.season,
            ),
        )

    def test_parse(self, endpoint: Show, test_data: TestData) -> None:
        show = parse_json(endpoint, test_data.name)
        assert show.props.page_props.mapped_data.idref14.series_id == test_data.id
