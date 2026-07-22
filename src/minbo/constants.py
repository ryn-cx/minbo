# TODO: Validate
"""Path constants for minbo."""

from pathlib import Path

MINBO_PATH = Path(__file__).parent
FILES_PATH = MINBO_PATH / "_files"

# JSON API (play.hbomax.com client). Used for routes HBO Max does not
# server-render into page HTML (e.g. search), unlike the __NEXT_DATA__ pages the
# rest of minbo scrapes.
API_DOMAIN = "default.any-amer.prd.api.hbomax.com"
APP_NAME = "hbomax"
APP_VERSION = "7.7.0"
PLATFORM = "desktop"
OS_NAME = "NT 10.0"
DISCO_PARAMS = "realm=bolt,bid=beam,features=ar"
DECORATORS = "viewingHistory,isFavorite,contentAction,badges"
