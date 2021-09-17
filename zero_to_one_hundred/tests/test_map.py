import logging
from typing import List

from models.map import Map
from models.section import Section

import pytest

from configs.config import ConfigMap
from tests.moke.persist_fs import PersistFS
from tests.conftest import http_url, http_url_2

def test_write(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, http_url, PersistFS),
        Section(get_config_map, http_url_2, PersistFS)
    ]
    actual = Map(get_config_map, PersistFS, sections=sections)
    logging.warning(actual)
    logging.warning(actual.write())


def test_from_dirs(get_config_map):
    dirs = PersistFS.list_dirs(get_config_map.get_repo_path)
    actual = Map.build_from_dirs(get_config_map, PersistFS, dirs)
    logging.warning(actual)
