from typing import List

from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs


def test_write(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, persist_fs, process_fs, http_url, False),
        Section(get_config_map, persist_fs, process_fs, http_url_2, False),
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)


def test_from_dirs(get_config_map):
    dirs = persist_fs.list_dirs(get_config_map.get_repo_path)
    actual = Map.build_from_dirs(persist_fs, process_fs, get_config_map, dirs)
