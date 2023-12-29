from typing import List

from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs


def test_write(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, persist_fs, process_fs, http_url, False),
        Section(get_config_map, persist_fs, process_fs, http_url_2, False),
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
