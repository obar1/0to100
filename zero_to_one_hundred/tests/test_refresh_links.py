import logging
from typing import List

from models.refresh_links import RefreshLinks
from models.section import Section
from tests.moke.persist_fs import PersistFS

def test_refresh_links(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, http_url, PersistFS),
        Section(get_config_map, http_url_2, PersistFS)
    ]
    refresh_links = RefreshLinks(get_config_map, PersistFS, sections=sections)
    actual=refresh_links.refresh_sections_links()
    logging.warning(actual)


