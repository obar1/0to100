import string
import pytest
import os

from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS

def str_relaxed(s1):
    remove = string.whitespace + string.punctuation
    mapping = {ord(c): None for c in remove}
    return s1.translate(mapping)



import pytest


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
def persist_fs():
    yield ZTOHPersistFS()


@pytest.fixture(scope="session")
def process_fs():
    yield ZTOHProcessFS()



import pytest
from unittest.mock import patch

@pytest.fixture(scope="session")
def mock_time():
    with patch("zero_to_one_hundred.repository.ztoh_process_fs.ZTOHProcessFS.get_now", return_value=20990101000000):  # Example timestamp
        yield



@pytest.fixture
def persist_fs():
    yield SBPersistFS()


@pytest.fixture
def process_fs():
    yield SBProcessFS()

