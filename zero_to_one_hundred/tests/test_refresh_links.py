# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from typing import List

from models.refresh_links import RefreshLinks
from models.section import Section
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


def test_refresh_links(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(persist_fs, process_fs, get_config_map, http_url),
        Section(persist_fs, process_fs, get_config_map, http_url_2),
    ]
    refresh_links = RefreshLinks(persist_fs, process_fs, get_config_map, sections)
    refresh_links.refresh_map_links()
