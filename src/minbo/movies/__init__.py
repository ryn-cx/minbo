"""Contains the Movie class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, override

from minbo.base_api_endpoint import BaseEndpoint
from minbo.movies.models import MoviesModel


logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Movies(BaseEndpoint[MoviesModel, [str]]):
    """Manage the movies file.

    Downloads https://www.hbomax.com/movies/<movie_id> and extracts the __NEXT_DATA__
    JSON from the page.

    Example Headers
        - GET /movies/<movie_id> HTTP/2
        - Host: www.hbomax.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Sec-GPC: 1
        - Connection: keep-alive
        - Cookie: __REDACTED__
        - Upgrade-Insecure-Requests: 1
        - Sec-Fetch-Dest: document
        - Sec-Fetch-Mode: navigate
        - Sec-Fetch-Site: none
        - Sec-Fetch-User: ?1
        - Priority: u=0, i
    """

    _response_model = MoviesModel


    @override
    def download(self, movie_id: str) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        url = f"https://www.hbomax.com/movies/{movie_id}"
        return self._client.download(url, log_id=log_id)

    @override
    def download_and_parse(self, movie_id: str) -> MoviesModel:
        return self.parse(self.download(movie_id))
