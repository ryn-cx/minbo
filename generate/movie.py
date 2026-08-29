# TODO: Validate
"""Rebuilds MovieModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, MINBO_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from minbo import MinBO

MOVIE_IDS = load_ids("MovieModel")
"""The movie id each recording is named after."""


# TODO: Validate
def generate_movie(client: MinBO) -> None:
    """Rebuild MovieModel."""
    for name, movie_id in MOVIE_IDS.items():
        download_if_missing(
            FILES_PATH,
            "MovieModel",
            name,
            lambda movie_id=movie_id: client.movie.download(movie_id),
        )
    rebuild_model(FILES_PATH, MINBO_PATH, "MovieModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie(MinBO(build_client_automatically()))
