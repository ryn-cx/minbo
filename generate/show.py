# TODO: Validate
"""Rebuilds ShowModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, MINBO_PATH
from generate.utils import download_if_missing
from minbo import MinBO

SHOWS = {
    "smiling-friends": ("b692705b-2f12-4a3d-ab4d-579124e0667c", None),
    "rick-and-morty-2": ("ab553cdc-e15d-4597-b65f-bec9201fd2dd", 2),
    "chernobyl": ("396999a6-3fff-4af3-802b-10c46d10deff", None),
}
"""The show id and season number each recording is named after."""


# TODO: Validate
def generate_show(client: MinBO) -> None:
    """Rebuild ShowModel."""
    for name, (show_id, season_number) in SHOWS.items():
        download_if_missing(
            FILES_PATH,
            "ShowModel",
            name,
            lambda show_id=show_id, season_number=season_number: client.show.download(
                show_id,
                season_number,
            ),
        )
    generate_model(FILES_PATH, MINBO_PATH, "ShowModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_show(MinBO(build_client_automatically()))
