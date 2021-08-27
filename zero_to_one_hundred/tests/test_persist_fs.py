"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from unittest.mock import Mock

import pytest
from testfixtures import TempDirectory

from models.section import Section
from repository.persist_fs import PersistFS


@pytest.fixture
def persist_fs(config_loader)->PersistFS:
    return PersistFS(config_loader)

def test_write(wip,persist_fs):
    s=  Section.from_str("https://cloud.google.com/docs")
    persist_fs.write(s)


def test_load_map():
    assert True

