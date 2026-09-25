# TODO: Validate

from __future__ import annotations

from typing import Any

from minbo.parsing import (
    build_url,
    carousels,
    content,
    end_date,
    full_text,
    images,
    mapping,
    number_or_none,
    related,
    sequence,
    shared_fields,
    start_date,
    text_or_none,
)

SERIES_ID_KEY = "seriesId"


# TODO: Validate
def show_content(page: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    return content(page, SERIES_ID_KEY)


# TODO: Validate
def parse_show(page: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    show = show_content(page)
    return {
        "title_key": text_or_none(show.get(SERIES_ID_KEY)),
        "url": build_url(show.get("imageUrlLink")),
        **shared_fields(show),
        "season_count": number_or_none(show.get("numberOfSeasons")),
        "episode_count": number_or_none(show.get("numberOfEpisodes")),
        "seasons": _seasons(show),
        "related": related(page),
        "carousels": carousels(page),
    }


# TODO: Validate
def _seasons(show: dict[str, Any]) -> list[dict[str, Any]]:
    return [_season(listed_season) for listed_season in sequence(show.get("seasons"))]


# TODO: Validate
def _season(listed_season: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    season = mapping(listed_season)
    return {
        "key": text_or_none(season.get("seasonId")),
        "season_number": number_or_none(season.get("seasonNumber")),
        "name": full_text(season.get("title")),
        "summary": full_text(season.get("summary")),
        "episode_count": number_or_none(season.get("numberOfEpisodes")),
        "episodes": _episodes(season),
    }


# TODO: Validate
def _episodes(season: dict[str, Any]) -> list[dict[str, Any]]:
    episodes: dict[Any, dict[str, Any]] = {}
    for listed_episode in sequence(season.get("episodes")):
        episode = _episode(listed_episode)
        episodes.setdefault(episode["episode_number"], episode)
    return list(episodes.values())


# TODO: Validate
def _episode(listed_episode: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    episode = mapping(listed_episode)
    return {
        "episode_number": number_or_none(episode.get("episodeNumber")),
        "title": full_text(episode.get("title")),
        "summary": full_text(episode.get("summary")),
        "url": build_url(episode.get("episodeUrl")),
        "images": images(episode.get("images")),
        "start_date": start_date(episode.get("offeringDates")),
        "end_date": end_date(episode.get("offeringDates")),
    }
