from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.models.toc import Toc
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as sb_persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as sb_process_fs


def test_init(get_config_map, http_url):
    actual = Toc(
        SBConfigMap(sb_persist_fs),
        sb_persist_fs,
        sb_persist_fs,
        [],
    )
    assert len(actual.meta_books) == 0
    mb = MetaBook(
        SBConfigMap(sb_persist_fs),
        sb_persist_fs,
        sb_process_fs,
        http_url,
    )
    actual = Toc(
        SBConfigMap(sb_persist_fs),
        sb_persist_fs,
        sb_process_fs,
        [mb],
    )
    assert str(actual.readme_md).endswith("toc.md")
    assert len(actual.meta_books) == 1
