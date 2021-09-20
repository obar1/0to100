# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from models.section import Section
from tests.moke.persist_fs import PersistFS as persist_fs


def test_write(get_config_map, http_url):
    actual = Section(get_config_map, http_url, persist_fs)
    logging.warning(actual)


def test_build_from_dir(get_config_map, dir_name):
    actual = Section.build_from_dir(get_config_map, persist_fs, dir_name)
    logging.warning(actual)
