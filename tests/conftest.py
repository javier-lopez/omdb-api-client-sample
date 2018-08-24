import os
import pytest

import omdb


def pytest_sessionstart(session):
    if not os.getenv('OMDB_API_KEY'):
        pytest.exit('ERROR: OMDB_API_KEY environment variable wasnt found,'
                    ' please specify one and retry')
