from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from minbo import MinBO
    from minbo.movies import Movies


class TestData(BaseModel):
    id: str
    name: str


TEST_DATA = [
    TestData(id="92b085e4-764c-41ca-a46f-4d76a5b28642", name="long-walk"),
]


@pytest.fixture(scope="session")
def endpoint(client: MinBO) -> Movies:
    return client.movie


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.name)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


class TestMovie:
    def test_download(self, endpoint: Movies, test_data: TestData) -> None:
        download_and_save(
            endpoint,
            test_data.name,
            lambda: endpoint.download(test_data.id),
        )

    def test_parse(self, endpoint: Movies, test_data: TestData) -> None:
        movie = parse_json(endpoint, test_data.name)
        assert movie.props.page_props.mapped_data.idref14.feature_id == test_data.id
