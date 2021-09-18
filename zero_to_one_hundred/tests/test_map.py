# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,C0209,W1203,C0200,C0103
import logging
from typing import List

from models.map import Map
from models.section import Section
from tests.moke.persist_fs import PersistFS as persist_fs


def test_write(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, http_url, persist_fs),
        Section(get_config_map, http_url_2, persist_fs),
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
    logging.warning(actual)
    logging.warning(actual.write(get_config_map.get_repo_sorted))


def test_from_dirs(get_config_map):
    dirs = persist_fs.list_dirs(get_config_map.get_repo_path)
    actual = Map.build_from_dirs(get_config_map, persist_fs, dirs)
    logging.warning(actual)
