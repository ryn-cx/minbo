# TODO: Validate
"""Contains the Minbo class."""

from __future__ import annotations

import json
import re
import time
import uuid
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any

from get_around import GetAround

from minbo.constants import (
    API_DOMAIN,
    APP_NAME,
    APP_VERSION,
    DISCO_PARAMS,
    OS_NAME,
    PLATFORM,
)
from minbo.exceptions import ExtractionError, HTTPError
from minbo.movie import Movie
from minbo.search import Search
from minbo.show import Show

if TYPE_CHECKING:
    from collections.abc import Mapping

logger = getLogger(__name__)
logger.addHandler(NullHandler())

# HBO Max is a Next.js site, so every page embeds its state as a single JSON blob
# in a ``<script id="__NEXT_DATA__" type="application/json">`` tag near the end of
# the document. The tag is split across lines, so match across newlines.
_NEXT_DATA_RE = re.compile(
    r'<script id="__NEXT_DATA__"[^>]*>(?P<json>.*?)</script>',
    re.DOTALL,
)


class Minbo:
    """HBO Max API wrapper."""

    def __init__(
        self,
        token: str = "",
        get_around_client: GetAround | None = None,
        locale: str = "en-US",
    ) -> None:
        """Initialize the Minbo client.

        Args:
            token: The ``st`` cookie value from an authenticated
                play.hbomax.com session (a JWT access token). Required by the
                JSON API routes (e.g. search); the HTML page routes ignore it.
            get_around_client: A pre-built :class:`GetAround` client. A default
                one is created when omitted.
            locale: The preferred language, e.g. ``en-US``.
        """
        self.token = token
        self.locale = locale
        self.get_around_client = get_around_client or GetAround()
        self.device_id = uuid.uuid4().hex

        self.show = Show(self)
        self.movie = Movie(self)
        self.search = Search(self)

    def _headers(self) -> dict[str, str]:
        return {
            # "Host": Set by httpx
            # "User-Agent":  Set by httpx
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            # "Accept-Encoding": Set by httpx
            "Referer": "https://www.hbomax.com/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=0, i",
        }

    @staticmethod
    def extract_next_data(html: str) -> dict[str, Any]:
        """Extract and decode the ``__NEXT_DATA__`` JSON embedded in a page's HTML."""
        match = _NEXT_DATA_RE.search(html)
        if match is None:
            msg = "Could not find __NEXT_DATA__ script tag in the page HTML"
            raise ExtractionError(msg)
        parsed: dict[str, Any] = json.loads(match.group("json"))
        return parsed

    def download(self, url: str, *, log_id: str) -> dict[str, Any]:
        """Download a page and return its decoded ``__NEXT_DATA__`` JSON.

        Redirects are followed, so a slug-less URL (e.g.
        ``https://www.hbomax.com/shows/<id>``) resolves to its canonical
        ``.../<slug>/<id>`` page rather than raising on the 301.
        """
        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            headers=self._headers(),
            follow_redirects=True,
        )
        if response.status_code != HTTPStatus.OK:
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)
        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return self.extract_next_data(response.text)

    def _api_headers(self) -> dict[str, str]:
        """Build the headers the JSON API (CMS routes) expects."""
        return {
            "Accept": "*/*",
            "Accept-Language": f"{self.locale},en;q=0.9",
            "content-type": "application/json",
            "x-device-info": (
                f"{APP_NAME}/{APP_VERSION} "
                f"({PLATFORM}/{PLATFORM}; Windows/{OS_NAME}; {self.device_id})"
            ),
            "x-disco-client": f"WEB:{OS_NAME}:{APP_NAME}:{APP_VERSION}",
            "x-disco-params": DISCO_PARAMS,
            "x-wbd-preferred-language": f"{self.locale},en",
            "Origin": "https://play.hbomax.com",
            "Referer": "https://play.hbomax.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }

    def download_api(
        self,
        endpoint: str,
        params: Mapping[str, Any],
        *,
        log_id: str,
    ) -> dict[str, Any]:
        """Download from the JSON API and return the decoded response body.

        Unlike :meth:`download` (which scrapes a page's ``__NEXT_DATA__``), this
        hits the play.hbomax.com CMS routes directly. Auth rides on the ``st``
        cookie; the token alone is sufficient (an empty request returns 400).

        Args:
            endpoint: The path after the host, e.g. ``cms/routes/search/result``.
            params: The query parameters.
            log_id: A human-readable identifier for logging.
        """
        logger.debug("Downloading: %s", log_id)
        url = f"https://{API_DOMAIN}/{endpoint}"
        cookies = {"st": self.token} if self.token else None
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params=params,
            headers=self._api_headers(),
            cookies=cookies,
        )
        if not response.is_success:
            msg = f"Unexpected response status code: {response.status_code}"
            raise HTTPError(msg)
        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.json()
