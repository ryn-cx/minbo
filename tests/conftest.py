# TODO: Validate
import pytest
from get_around import build_client_automatically

from minbo import MinBO


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> MinBO:
    return MinBO(build_client_automatically())
