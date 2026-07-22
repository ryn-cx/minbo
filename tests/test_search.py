from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from minbo import Minbo
    from minbo.search import Search
    from minbo.search.models import SearchModel


class TestData(BaseModel):
    query: str
    target_id: UUID


TEST_DATA = [
    TestData(
        query="Chernobyl",
        target_id=UUID("396999a6-3fff-4af3-802b-10c46d10deff"),
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: Minbo) -> Search:
    return client.search


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.query)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


class TestSearch:
    def test_download(self, endpoint: Search, test_data: TestData) -> None:
        download_and_save(
            endpoint,
            test_data.query,
            lambda: endpoint.download(test_data.query),
        )

    def test_parse(self, endpoint: Search, test_data: TestData) -> None:
        search: SearchModel = parse_json(endpoint, test_data.query)
        # The searched-for show must be among the results, carrying its id and name.
        show = next(
            item
            for item in search.included
            if item.type == "show" and item.id == test_data.target_id
        )
        assert show.attributes is not None
        assert show.attributes.name == test_data.query
