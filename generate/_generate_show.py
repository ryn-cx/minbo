from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.customizer import GAPICustomizer
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_named_missing,
    load_named_ids,
)

from generate.constants import GENERATOR_PATHS
from generate.parsed import rebuild_parsed_model
from minbo import MinBO
from minbo.show.parse import parse_show

MODEL_NAME = "ShowModel"
PARSED_MODEL_NAME = "ParsedShowModel"


# TODO: Validate
def _customizer() -> GAPICustomizer:
    customizer = GAPICustomizer()
    customizer.add_replacement_field("Episode", "title", "title: str | None = None")
    return customizer


# TODO: Validate
class ShowId(RecordingId[MinBO]):
    show_id: str
    season_number: int | None = None

    # TODO: Validate
    def download(self, client: MinBO) -> str:
        return client.show.download(self.show_id, self.season_number)


SHOWS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, ShowId)


# TODO: Validate
def generate_show(client: MinBO) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, SHOWS, client)
    rebuild_parsed_model(MODEL_NAME, PARSED_MODEL_NAME, parse_show, _customizer())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_show(MinBO(build_client_automatically()))
