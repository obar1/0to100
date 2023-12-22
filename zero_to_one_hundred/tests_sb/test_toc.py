from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.models.toc import Toc
from zero_to_one_hundred.tests_sb.moke import sb_persist_fs_fake, sb_process_fs_fake


def test_init(get_map_yaml_path, http_url):
    actual = Toc(
        SBConfigMap(get_map_yaml_path, sb_persist_fs_fake.SBPersistFSFake),
        sb_persist_fs_fake.SBPersistFSFake,
        sb_persist_fs_fake,
        [],
    )
    assert len(actual.meta_books) == 0
    mb = MetaBook(
        SBConfigMap(get_map_yaml_path, sb_persist_fs_fake.SBPersistFSFake),
        sb_persist_fs_fake.SBPersistFSFake,
        sb_process_fs_fake,
        http_url,
    )
    actual = Toc(
        SBConfigMap(get_map_yaml_path, sb_persist_fs_fake.SBPersistFSFake),
        sb_persist_fs_fake.SBPersistFSFake,
        sb_process_fs_fake,
        [mb],
    )
    assert str(actual.readme_md).endswith("toc.md")
    assert len(actual.meta_books) == 1
