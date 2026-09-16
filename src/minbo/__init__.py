# TODO: Validate
"""Contains the MinBO class."""

from __future__ import annotations

import re
from http import HTTPStatus
from logging import NullHandler, getLogger
from time import monotonic, sleep

from get_around import GetAround

from minbo.exceptions import ExtractionError, HTTPError, ResourceNotFoundError
from minbo.movie import Movie
from minbo.show import Show

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_DOMAIN = "www.hbomax.com"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
)
"""The site blocks any request whose user agent is not a browser."""

NEXT_DATA_RE = re.compile(
    r'<script id="__NEXT_DATA__"[^>]*>(?P<json>.*?)</script>',
    re.DOTALL,
)
"""The script tag a page keeps its data in."""


# TODO: Validate
class MinBO:
    """HBO Max API wrapper.

    There is no JSON API behind hbomax.com. A page is HTML with everything the
    page was built from written into a `__NEXT_DATA__` script tag, so a
    download fetches the page and returns the JSON out of that tag.
    """

    # TODO: Validate
    def __init__(
        self,
        get_around_client: GetAround | None = None,
        locale: str = "en-US",
        sleep_time: float = 0,
    ) -> None:
        """Initializes the MinBO client.

        The client holds one attribute per endpoint, so `client.show(id)` looks
        a show up and `client.show.download(id)` and `client.show.load(data)`
        are the halves of it.
        """
        self.get_around_client = get_around_client or GetAround()
        self.locale = locale
        self.sleep_time = sleep_time

        self.movie = Movie(self)
        self.show = Show(self)

    # TODO: Validate
    def _headers(self) -> dict[str, str]:
        return {
            # "Host": Set by httpx
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            # "Accept-Encoding": Set by httpx
            "Referer": "https://www.hbomax.com/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=0, i",
        }

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        headers: dict[str, str],
        log_id: str,
    ) -> str:
        """Downloads a page and returns the JSON from its `__NEXT_DATA__` tag.

        Raises:
            ResourceNotFoundError: If the site has no page at that address.
            HTTPError: If the request is answered with any other error status.
            ExtractionError: If the page carries no `__NEXT_DATA__` script tag.
        """
        logger.debug("Downloading: %s", log_id)
        url = f"https://{API_DOMAIN}/{endpoint}"
        start = monotonic()
        response = self.get_around_client.get(
            url,
            headers=self._headers() | headers,
            follow_redirects=True,
            timeout=30,
        )

        if response.status_code != HTTPStatus.OK:
            if response.status_code == HTTPStatus.NOT_FOUND:
                raise ResourceNotFoundError(response.status_code, response.text)
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, monotonic() - start)

        next_data = NEXT_DATA_RE.search(response.text)
        if next_data is None:
            raise ExtractionError(response.text)

        sleep(self.sleep_time)
        return next_data.group("json")
