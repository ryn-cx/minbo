from __future__ import annotations

import logging
from typing import Literal

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
)

from generate.constants import GENERATOR_PATHS
from generate.parsed import rebuild_parsed_model
from minbo import MinBO
from minbo.sitemap.parse import parse_sitemap

MODEL_NAME = "SitemapModel"
PARSED_MODEL_NAME = "ParsedSitemapModel"


# TODO: Validate
class SitemapId(RecordingId[MinBO]):
    kind: Literal["movies", "shows"]

    # TODO: Validate
    def download(self, client: MinBO) -> str:
        return client.sitemap.download(self.kind)


SITEMAPS = load_ids(GENERATOR_PATHS, MODEL_NAME, SitemapId)


# TODO: Validate
def generate_sitemap(client: MinBO) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, SITEMAPS, client)
    rebuild_parsed_model(MODEL_NAME, PARSED_MODEL_NAME, parse_sitemap)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_sitemap(MinBO(build_client_automatically()))
