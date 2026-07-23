import pytest
from get_around import build_client_automatically

from minbo import MinBO


@pytest.fixture(scope="session")
def client() -> MinBO:
    return MinBO(get_around_client=build_client_automatically())
