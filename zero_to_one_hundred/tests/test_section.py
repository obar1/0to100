"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from unittest.mock import Mock

import pytest

from models.section import Section
from processors.create_section_processor import CreateSectionProcessor


@pytest.fixture
def section_processor() -> CreateSectionProcessor:
    return Mock()


def test_convert():
    repo_path = "/home/tmp"
    http_url = "https://cloud.google.com/docs"
    section = Section(http_url)
    actual = section.get_valid_path(repo_path)
    expected = "/home/tmp/https:§§cloud.google.com§docs"
    assert expected == actual
    assert True
