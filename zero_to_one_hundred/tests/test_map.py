"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from typing import List

import pytest

from models.map import Map
from models.section import Section


@pytest.fixture
def get_map_path(get_repo_root):
    return get_repo_root + "/resources/map.md"


def test_get_map_as_section(get_map_path):
    map_path = Map(get_map_path)
    actual: List[Section] = map_path.get_map_as_section(Section.from_str)
    assert len(actual) == 0
