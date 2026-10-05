# TODO: Validate
from __future__ import annotations

import json
from logging import NullHandler, getLogger

from minbo.base_api_endpoint import BaseEndpoint
from minbo.sitemap.models import ParsedSitemapModel, model_validate_json
from minbo.sitemap.parse import parse_sitemap

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Sitemap(BaseEndpoint):
    # TODO: Validate
    def __call__(self, kind: str) -> ParsedSitemapModel:
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(kind), log_id)

    # TODO: Validate
    def download(self, kind: str) -> str:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            endpoint=f"sitemap/{kind}",
            headers={},
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ParsedSitemapModel:
        return model_validate_json(
            parse_sitemap(json.loads(data)),
            log_id or self.default_log_id,
        )
