# TODO: Validate
"""Contains the Show class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger

from minbo.base_api_endpoint import BaseEndpoint
from minbo.exceptions import ResourceNotFoundError, ShowNotFoundError
from minbo.show.models import ShowModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Show(BaseEndpoint):
    """Manage the show file.

    A show's page lists every season but fills in the episodes of only one of
    them, and `season_number` picks which. Left out, the site picks the season
    it would show a visitor.

    Source: https://www.hbomax.com/shows/{show_id}

    Example request:
        - GET /shows/{slug}/{show_id} HTTP/2
        - Host: www.hbomax.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.google.com/
        - Sec-GPC: 1
        - Connection: keep-alive
        - Cookie: __REDACTED__
        - Upgrade-Insecure-Requests: 1
        - Sec-Fetch-Dest: document
        - Sec-Fetch-Mode: navigate
        - Sec-Fetch-Site: cross-site
        - Sec-Fetch-User: ?1
        - Priority: u=0, i
    """

    # TODO: Validate
    def __call__(self, show_id: str, season_number: int | None = None) -> ShowModel:
        """Look the show up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(show_id, season_number), log_id)

    # TODO: Validate
    def download(self, show_id: str, season_number: int | None = None) -> str:
        """Download the show file."""
        log_id = self.get_log_id(self.download, locals())
        season = "" if season_number is None else f"s{season_number}/"
        try:
            response = self._client.download(
                endpoint=f"shows/{season}{show_id}",
                headers={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ShowNotFoundError(
                show_id,
                err.status_code,
                err.response,
            ) from err
        return self._validate_download(response, show_id)

    # TODO: Validate
    def _validate_download(self, response: str, show_id: str) -> str:
        # The page names what it was built from by position, so every field on
        # it sits under an idrefN key and the show is always idref14. A movie
        # is served from the same address and carries a featureId there
        # instead, so an id that is not a series reads as no show being found.
        show = json.loads(response)["props"]["pageProps"]["mappedData"]["idref14"]
        if show.get("seriesId") != show_id:
            raise ShowNotFoundError(show_id, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ShowModel:
        """Read a downloaded show file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
