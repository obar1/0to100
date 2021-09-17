import logging

from typing import List

from models.readme_md import ReadMeMD
from models.section import Section
from tests.moke.persist_fs import PersistFS

def test_refresh_links(get_config_map, http_url):
    section = Section(get_config_map, http_url, PersistFS)
    readmemd = ReadMeMD(get_config_map,section,PersistFS)
    txt:List[str] = readmemd.read()
    logging.warning(txt)
    actual = readmemd.refresh_links(txt)
    logging.warning(actual)
