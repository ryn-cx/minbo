from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from minbo import Minbo
    from minbo.show import Show


class TestData(BaseModel):
    id: str
    season: int | None
    name: str


TEST_DATA = [
    TestData(
        id="b692705b-2f12-4a3d-ab4d-579124e0667c",
        season=None,
        name="smiling-friends",
    ),
    TestData(
        id="ab553cdc-e15d-4597-b65f-bec9201fd2dd",
        season=2,
        name="rick-and-morty-s2",
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: Minbo) -> Show:
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
                test_data.id,
                season=test_data.season,
            ),
        )

    def test_parse(self, endpoint: Show, test_data: TestData) -> None:
        show = parse_json(endpoint, test_data.name)
        assert show.series_id
