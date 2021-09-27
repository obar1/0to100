# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-section,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
from typing import List

from models.readme_md import ReadMeMD
from models.section import Section
from tests.moke.persist_fs import PersistFS as persist_fs


def test_refresh_links(get_config_map, http_url):
    section = Section(get_config_map, http_url, persist_fs)
    readmemd = ReadMeMD(get_config_map, section, persist_fs)
    txt: List[str] = readmemd.read()
    logging.info(txt)
    readmemd.refresh_links(txt)
