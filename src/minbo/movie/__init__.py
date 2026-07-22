# TODO: Validate
"""Contains the Movie class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from minbo.base_api_endpoint import BaseEndpoint
from minbo.exceptions import AmbiguousContentError, ContentNotFoundError
from minbo.movie.models import MovieModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Movie(BaseEndpoint[MovieModel, [str]]):
    """Manage the movie file.

    Wraps ``GET https://www.hbomax.com/movies/<id>``, extracting the movie's
    content object from the page's embedded ``__NEXT_DATA__`` JSON.
    """

    _response_model = MovieModel

    @staticmethod
    def _content_object(next_data: dict[str, Any]) -> dict[str, Any]:
        """Pull the movie's content object out of the page's ``__NEXT_DATA__``.

        HBO Max normalizes page state into a ``mappedData`` reference table keyed
        by opaque ``idref<n>`` names. Exactly one entry is the movie itself; it is
        the only value carrying both ``featureId`` and ``runtime``.
        """
        mapped_data = next_data["props"]["pageProps"]["mappedData"]
        matches: list[dict[str, Any]] = [
            value
            for value in mapped_data.values()
            if isinstance(value, dict) and "featureId" in value and "runtime" in value
        ]
        if not matches:
            msg = "No content object found in page __NEXT_DATA__"
            raise ContentNotFoundError(msg)
        if len(matches) > 1:
            msg = f"Expected exactly one content object, found {len(matches)}"
            raise AmbiguousContentError(msg)
        return matches[0]

    @override
    def download(self, id: str) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        # The slug is optional: a movie lives at ``/movies/<id>``. HBO Max
        # redirects this to the canonical ``/movies/<slug>/<id>`` page, which the
        # download client follows, so no slug is needed to fetch a movie.
        url = f"https://www.hbomax.com/movies/{id}"
        next_data = self._client.download(url, log_id=log_id)
        return self._content_object(next_data)

    @override
    def download_and_parse(self, id: str) -> MovieModel:
        return self.parse(self.download(id))
