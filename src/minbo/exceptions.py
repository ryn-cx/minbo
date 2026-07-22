# TODO: Validate
"""Exceptions."""

from __future__ import annotations


class MinboError(Exception):
    """Base exception for the minbo library."""


class HTTPError(MinboError):
    """Raised when an HTTP request fails with an unexpected status code."""


class ExtractionError(MinboError):
    """Raised when the ``__NEXT_DATA__`` JSON cannot be found in a page's HTML."""


class ContentNotFoundError(MinboError):
    """Raised when a page's ``__NEXT_DATA__`` holds no recognizable content object."""


class AmbiguousContentError(MinboError):
    """Raised when a page's ``__NEXT_DATA__`` holds more than one content object."""
