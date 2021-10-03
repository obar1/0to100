# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
from typing import List

from models.map import Map
from models.section import Section
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


def test_write(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(persist_fs, process_fs, get_config_map, http_url),
        Section(persist_fs, process_fs, get_config_map, http_url_2)
    ]
    actual = Map(persist_fs, get_config_map, sections=sections)
    logging.info(actual)
    logging.info(actual.write(get_config_map.get_repo_sorted))


def test_from_dirs(get_config_map):
    dirs = persist_fs.list_dirs(get_config_map.get_repo_path)
    actual = Map.build_from_dirs(persist_fs, process_fs, get_config_map, dirs)
    logging.info(actual)
