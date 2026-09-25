# TODO: Validate
"""Contains the Movie class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from minbo.base_api_endpoint import BaseEndpoint
from minbo.exceptions import MovieNotFoundError, ResourceNotFoundError
from minbo.movie.models import ParsedMovieModel, model_validate_json
from minbo.movie.parse import FEATURE_ID_KEY, movie_content, parse_movie

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Movie(BaseEndpoint):
    """Contains the movie.

    Source: https://www.hbomax.com/movies/{movie_id}

    Example request:
        - GET /movies/{movie_id} HTTP/2
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

    # TODO: Validate
    def __call__(self, movie_id: str) -> ParsedMovieModel:
        """Download and parse the movie file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(movie_id), log_id)

    # TODO: Validate
    def download(self, movie_id: str) -> str:
        """Download the movie file."""
        log_id = self.get_log_id(self.download, locals())
        try:
            response = self._client.download(
                endpoint=f"movies/{movie_id}",
                headers={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise MovieNotFoundError(
                movie_id,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, movie_id)

    # TODO: Validate
    def _validate_download(self, response: str, movie_id: str) -> str:
        movie = movie_content(json.loads(response))
        if movie.get(FEATURE_ID_KEY) != movie_id:
            raise MovieNotFoundError(movie_id, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ParsedMovieModel:
        """Load a movie file into its model."""
        return model_validate_json(
            parse_movie(json.loads(data)),
            log_id or self.default_log_id,
        )
