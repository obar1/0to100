import string

from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.tests.test_ztoh.ztoh_process_fs import ZTOHProcessFS

def str_relaxed(s1):
    remove = string.whitespace + string.punctuation
    mapping = {ord(c): None for c in remove}
    return s1.translate(mapping)




import pytest

@pytest.fixture(scope="session")
def http_url():
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