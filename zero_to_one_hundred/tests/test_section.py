import logging
from typing import List

from models.map import Map
from models.section import Section

import pytest

from configs.config import ConfigMap
from tests.moke.persist_fs import PersistFS


def test_write(get_config_map, http_url):
    actual = Section(get_config_map, http_url, PersistFS)
    logging.warning(actual)


def test_build_from_dir(get_config_map, http_url, dir_name):
    actual = Section.build_from_dir(get_config_map, PersistFS, dir_name)
    logging.warning(actual)

