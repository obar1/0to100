import logging
from typing import List

from models.refresh_links import RefreshLinks
from models.section import Section
from tests.conftest import TestPersistFS


def test_refresh_links(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, http_url, TestPersistFS),
        Section(get_config_map, http_url_2, TestPersistFS)
    ]
    actual = RefreshLinks(get_config_map, TestPersistFS, sections=sections)
    logging.warning(actual)
    logging.warning(actual.refresh_sections_links())
    assert False
