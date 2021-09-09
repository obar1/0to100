import logging
from typing import List

from models.map import Map
from models.section import Section

import pytest

from configs.config import ConfigMap
from tests.conftest import TestPersistFS, http_url, http_url_2


def test_write(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, http_url, TestPersistFS),
        Section(get_config_map, http_url_2, TestPersistFS)
    ]
    actual = Map(get_config_map, TestPersistFS, sections=sections)
    logging.warning(actual)
    logging.warning(actual.write())

#     def from_dirs(cls, dirs:List[str]) -> List[Section]:
def test_from_dirs(get_config_map):
    dirs = TestPersistFS.list_dirs(get_config_map.get_repo_path)
    actual = Map.build_from_dirs(get_config_map, TestPersistFS, dirs)
    logging.warning(actual)
