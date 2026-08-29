# TODO: Validate
"""Rebuilds ShowModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, MINBO_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from minbo import MinBO

SHOWS = load_ids("ShowModel")
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
    rebuild_model(FILES_PATH, MINBO_PATH, "ShowModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_show(MinBO(build_client_automatically()))
