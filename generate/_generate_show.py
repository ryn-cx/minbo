from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_named_missing,
    load_named_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from minbo import MinBO

MODEL_NAME = "ShowModel"


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
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ShowId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_show(MinBO(build_client_automatically()))
