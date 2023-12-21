from typing import List

from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.tests.moke import persist_fs_fake, process_fs_fake


def test_write(get_config_map, http_url, http_url_2):
    sections: List[Section] = [
        Section(
            persist_fs_fake,
            process_fs_fake,
            get_config_map,
            http_url,
            False,
        ),
        Section(
            persist_fs_fake,
            process_fs_fake,
            get_config_map,
            http_url_2,
            False,
        ),
    ]
    actual = Map(persist_fs_fake.PersistFSFake, get_config_map, sections=sections)

    print(actual)
    print(actual.write(get_config_map.get_repo_sorted))


def test_from_dirs(get_config_map):
    dirs = persist_fs_fake.PersistFSFake.list_dirs(get_config_map.get_repo_path)
    actual = Map.build_from_dirs(
        persist_fs_fake.PersistFSFake, process_fs_fake, get_config_map, dirs
    )
    print(actual)
