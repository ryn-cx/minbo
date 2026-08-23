# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class MinBOError(Exception):
    """Base exception for MinBO."""

    response: str | dict[str, Any] | None = None
    """The data that caused the error, or None if there was none."""


# TODO: Validate
class HTTPError(MinBOError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the site reports that the requested page does not exist."""


# TODO: Validate
class MovieNotFoundError(ResourceNotFoundError):
    """Raised when the requested movie does not exist."""

    # TODO: Validate
    def __init__(
        self,
        movie_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the movie id and the originating response."""
        self.movie_id = movie_id
        super().__init__(status_code, response)


# TODO: Validate
class ShowNotFoundError(ResourceNotFoundError):
    """Raised when the requested show does not exist."""

    # TODO: Validate
    def __init__(
        self,
        show_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the show id and the originating response."""
        self.show_id = show_id
        super().__init__(status_code, response)


# TODO: Validate
class ExtractionError(MinBOError):
    """Raised when a page's HTML carries no `__NEXT_DATA__` script tag."""

    # TODO: Validate
    def __init__(self, response: str) -> None:
        """Initialize with the page the script tag is missing from."""
        self.response = response
        super().__init__("Could not find the __NEXT_DATA__ script tag in the page HTML")
