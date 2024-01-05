from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.models.toc import Toc


def test_init(get_config_map, persist_fs, process_fs, http_url):
    actual = Toc(
        SBConfigMap(persist_fs),
        persist_fs,
        process_fs,
        [],
    )
    assert len(actual.meta_books) == 0
    mb = MetaBook(
        SBConfigMap(persist_fs),
        persist_fs,
        process_fs,
        http_url,
    )
    actual = Toc(
        SBConfigMap(persist_fs),
        persist_fs,
        process_fs,
        [mb],
    )
    assert str(actual.readme_md).endswith("toc.md")
    assert len(actual.meta_books) == 1
