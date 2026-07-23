# TODO: Validate
"""Contains the Show endpoint."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from good_ass_pydantic_integrator import ReplacementField

from minbo.base_api_endpoint import BaseEndpoint
from minbo.show.models import ShowModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Show(BaseEndpoint[ShowModel, [str]]):
    """Manage the show file.

    Downloads https://www.hbomax.com/show/<show_id> and extracts the
    __NEXT_DATA__ JSON from the page.

    This URL will redirect to https://www.hbomax.com/show/<slug>/<show_id>.

    Example Headers
        - GET /shows/<slug>/<show_id> HTTP/2
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

    _response_model = ShowModel

    @classmethod
    @override
    def _replacement_fields(cls) -> list[ReplacementField]:
        return [
            # Chernobyl's first episode is titled "1:23:45" which is detected as a
            # timedelta.
            ReplacementField(class_name="Title4", field_name="short", new_field="str"),
            ReplacementField(class_name="Title4", field_name="full", new_field="str"),
        ]

    @override
    def download(
        self,
        show_id: str,
        season_number: int | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        season_id = "" if season_number is None else f"s{season_number}/"
        url = f"https://www.hbomax.com/shows/{season_id}{show_id}"
        return self._client.download(url, log_id=log_id)

    @override
    def download_and_parse(
        self,
        show_id: str,
        season_number: int | None = None,
    ) -> ShowModel:
        return self.parse(self.download(show_id, season_number))
