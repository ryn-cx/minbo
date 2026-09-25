from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_named_missing,
    load_named_ids,
)

from generate.constants import GENERATOR_PATHS
from generate.parsed import rebuild_parsed_model
from minbo import MinBO
from minbo.movie.parse import parse_movie

MODEL_NAME = "MovieModel"
PARSED_MODEL_NAME = "ParsedMovieModel"


# TODO: Validate
class MovieId(RecordingId[MinBO]):
    movie_id: str

    # TODO: Validate
    def download(self, client: MinBO) -> str:
        return client.movie.download(self.movie_id)


MOVIE_IDS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, MovieId)


# TODO: Validate
def generate_movie(client: MinBO) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, MOVIE_IDS, client)
    rebuild_parsed_model(MODEL_NAME, PARSED_MODEL_NAME, parse_movie)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie(MinBO(build_client_automatically()))
