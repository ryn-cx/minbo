# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from minbo.base_api_endpoint import BaseEndpoint
from minbo.constants import DECORATORS
from minbo.search.models import SearchModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Search(BaseEndpoint[SearchModel, [str]]):
    """Manage the search file.

    Wraps ``GET cms/routes/search/result`` on the JSON API. Search results are
    not server-rendered into any hbomax.com page, so unlike the rest of minbo
    this route comes from the API rather than a ``__NEXT_DATA__`` scrape.
    """

    _response_model = SearchModel

    @override
    def download(self, query: str, *, page_size: int = 10) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download_api(
            "cms/routes/search/result",
            {
                "include": "default",
                "decorators": DECORATORS,
                "page[items.size]": page_size,
                "contentFilter[query]": query,
            },
            log_id=log_id,
        )

    @override
    def download_and_parse(self, query: str, *, page_size: int = 10) -> SearchModel:
        return self.parse(self.download(query, page_size=page_size))
