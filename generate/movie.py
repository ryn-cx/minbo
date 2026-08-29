# TODO: Validate
"""Rebuilds MovieModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, MINBO_PATH
from generate.utils import download_if_missing
from minbo import MinBO

MOVIE_IDS = {
    "long-walk": "92b085e4-764c-41ca-a46f-4d76a5b28642",
    "batman-mask-of-the-phantasm": "14a0d4dc-79f0-40f1-8967-fded774b2593",
}
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
    generate_model(FILES_PATH, MINBO_PATH, "MovieModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_movie(MinBO(build_client_automatically()))
