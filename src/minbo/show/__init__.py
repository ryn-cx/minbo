# TODO: Validate
"""Contains the Show class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from minbo.base_api_endpoint import BaseEndpoint
from minbo.exceptions import AmbiguousContentError, ContentNotFoundError
from minbo.show.models import ShowModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Show(BaseEndpoint[ShowModel, [str]]):
    """Manage the show file.

    Wraps ``GET https://www.hbomax.com/shows/<id>`` (and the per-season
    ``.../s<n>/<id>`` variant), extracting the show's content object from the
    page's embedded ``__NEXT_DATA__`` JSON.
    """

    _response_model = ShowModel

    @staticmethod
    def _content_object(next_data: dict[str, Any]) -> dict[str, Any]:
        """Pull the show's content object out of the page's ``__NEXT_DATA__``.

        HBO Max normalizes page state into a ``mappedData`` reference table keyed
        by opaque ``idref<n>`` names. Exactly one entry is the show itself; it is
        the only value carrying both ``seriesId`` and ``seasons``.
        """
        mapped_data = next_data["props"]["pageProps"]["mappedData"]
        matches: list[dict[str, Any]] = [
            value
            for value in mapped_data.values()
            if isinstance(value, dict) and "seriesId" in value and "seasons" in value
        ]
        if not matches:
            msg = "No content object found in page __NEXT_DATA__"
            raise ContentNotFoundError(msg)
        if len(matches) > 1:
            msg = f"Expected exactly one content object, found {len(matches)}"
            raise AmbiguousContentError(msg)
        return matches[0]

    @override
    def download(
        self,
        id: str,
        *,
        season: int | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        # The slug is optional: a show lives at ``/shows/<id>`` and every
        # non-default season inserts an ``/s<n>/`` segment. HBO Max redirects
        # these to the canonical ``/shows/<slug>/[s<n>/]<id>`` page, which the
        # download client follows, so no slug is needed to fetch a show.
        season_segment = "" if season is None else f"s{season}/"
        url = f"https://www.hbomax.com/shows/{season_segment}{id}"
        next_data = self._client.download(url, log_id=log_id)
        return self._content_object(next_data)

    @override
    def download_and_parse(
        self,
        id: str,
        *,
        season: int | None = None,
    ) -> ShowModel:
        return self.parse(self.download(id, season=season))
