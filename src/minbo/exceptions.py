"""Exceptions."""

from __future__ import annotations


class MinBOError(Exception):
    """Base exception for the minbo library."""


class HTTPError(MinBOError):
    """Raised when an HTTP request fails with an unexpected status code."""

    def __init__(self, status_code: int, body: str) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.body = body
        super().__init__(f"Unexpected response status code: {status_code}\n{body}")


class ExtractionError(MinBOError):
    """Raised when the ``__NEXT_DATA__`` JSON cannot be found in a page's HTML."""
