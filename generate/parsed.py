# TODO: Validate

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING, Any

from good_ass_pydantic_integrator.generate import generate_model, recording_paths

from generate.constants import GENERATOR_PATHS

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from good_ass_pydantic_integrator.customizer import GAPICustomizer

logger = logging.getLogger(__name__)


# TODO: Validate
def rebuild_parsed_model(
    model_name: str,
    parsed_model_name: str,
    parse: Callable[[Any], dict[str, Any]],
    customizer: GAPICustomizer | None = None,
) -> None:

    # TODO: Validate
    def read(content: str) -> Any:  # noqa: ANN401 - Any JSON value.
        return parse(json.loads(content))

    _write_parsed_recordings(model_name, parsed_model_name, read)
    generate_model(
        GENERATOR_PATHS.files_path,
        GENERATOR_PATHS.package_path,
        parsed_model_name,
        customizer=customizer,
    )


# TODO: Validate
def _write_parsed_recordings(
    model_name: str,
    parsed_model_name: str,
    read: Callable[[str], Any],
) -> None:
    parsed_directory = GENERATOR_PATHS.files_path / parsed_model_name
    parsed_directory.mkdir(parents=True, exist_ok=True)
    written: set[Path] = set()

    for recording in recording_paths(GENERATOR_PATHS.files_path, model_name):
        parsed_path = parsed_directory / recording.name
        parsed_path.write_text(
            json.dumps(read(recording.read_text(encoding="utf-8")), indent=2) + "\n",
            encoding="utf-8",
        )
        written.add(parsed_path)

    for parsed_path in sorted(parsed_directory.glob("*.json")):
        if parsed_path not in written:
            logger.info("Dropping %s/%s.", parsed_model_name, parsed_path.name)
            parsed_path.unlink()
