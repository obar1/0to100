import string
from unittest.mock import patch

import pytest


def str_relaxed(s1):
    remove = string.whitespace + string.punctuation
    mapping = {ord(c): None for c in remove}
    return s1.translate(mapping)


@pytest.fixture
def fake_filesystem(fs):  # pylint:disable=invalid-name
    """Variable name 'fs' causes a pylint warning. Provide a longer name
    acceptable to pylint for use in tests.
    """
    yield fs


@pytest.fixture(scope="session")
def http_url_1():
    yield "https://cloud.google.com/abc"


@pytest.fixture(scope="session")
def http_url_2():
    yield "https://cloud.google.com/zzz"


@pytest.fixture(scope="session")
def http_url_3():
    yield "https://cloud.google.com/zzz/123"


@pytest.fixture(scope="session")
def http_url_4():
    yield "https://cloudskillsboost.google/"


@pytest.fixture(scope="session")
def mock_time():
    with patch(
        "zero_to_one_hundred.repository.ztoh_process_fs.ZTOHProcessFS.get_now",
        return_value=20990101000000,
    ):  # Example timestamp
        yield
