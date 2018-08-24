"""Public interface, accessible via:
import omdb
"""
from .client import OMDB

# internal client instance used for our requests.
_client = OMDB()


def search(pattern=None):
    return _client.search(pattern)


def get_by_id(id=None):
    return _client.get_by_id(id)


def get_by_title(title=None):
    return _client.get_by_title(title)
