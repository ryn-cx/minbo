# TODO: Validate
"""Contains the MinBO class."""

from __future__ import annotations

import json
import re
import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from minbo.exceptions import ExtractionError, HTTPError
from minbo.movies import Movies
from minbo.show import Show

logger = getLogger(__name__)
logger.addHandler(NullHandler())

# HBO Max is a Next.js site, so every page embeds its state as a single JSON blob
# in a ``<script id="__NEXT_DATA__" type="application/json">`` tag near the end of
# the document. The tag is split across lines, so match across newlines.
_NEXT_DATA_RE = re.compile(
    r'<script id="__NEXT_DATA__"[^>]*>(?P<json>.*?)</script>',
    re.DOTALL,
)


class MinBO:
    """HBO Max API wrapper.

    Scrapes the anonymously-accessible pages at ``www.hbomax.com``, extracting
    each page's server-rendered ``__NEXT_DATA__`` JSON. No login or API token is
    required.
    """

    def __init__(
        self,
        get_around_client: GetAround | None = None,
        locale: str = "en-US",
    ) -> None:
        """Initialize the MinBO client.

        Args:
            get_around_client: A pre-built :class:`GetAround` client. A default
                one is created when omitted.
            locale: The preferred language, e.g. ``en-US``.
        """
        self.locale = locale
        self.get_around_client = get_around_client or GetAround()

        self.show = Show(self)
        self.movie = Movies(self)

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
            raise HTTPError(response.status_code, response.text)
        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return self.extract_next_data(response.text)
