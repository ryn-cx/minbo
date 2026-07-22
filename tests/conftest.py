# TODO: Validate
import pytest
from get_around import build_client_automatically, get_credential

from minbo import Minbo


@pytest.fixture(scope="session")
def client() -> Minbo:
    # The ``st`` token is only needed by the JSON API routes (search); the HTML
    # page routes (show) work without it, so a missing credential is tolerated.
    try:
        token = get_credential("MINBO_TOKEN")
    except RuntimeError:
        token = ""
    return Minbo(token=token, get_around_client=build_client_automatically())
