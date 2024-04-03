from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.models.toc import Toc
from zero_to_one_hundred.tests.conftest import str_relaxed


def test_init(get_config_map, persist_fs, process_fs, http_url):
    actual = Toc(
        get_config_map,
        persist_fs,
        process_fs,
        [],
    )
    assert len(actual.meta_books) == 0
    mb = MetaBook(
        get_config_map,
        persist_fs,
        process_fs,
        http_url,
    )
    actual = Toc(
        get_config_map,
        persist_fs,
        process_fs,
        [mb],
    )
    assert str(actual.readme_md).endswith("toc.md")
    assert len(actual.meta_books) == 1


def test_asMarkDown(get_config_map, persist_fs, process_fs, http_url,http_url2):
    metabooks: List[MetaBook] = [
        MetaBook(
        get_config_map,
        persist_fs,
        process_fs,
        http_url,
    ),
        MetaBook(
        get_config_map,
        persist_fs,
        process_fs,
        http_url2,
    ),
    ]
    actual = Toc(
        get_config_map,
        persist_fs,
        process_fs,
        [],
    )
    current = actual.asMarkDown()
    expected = """
# TOC
## `0` books
### 2099/01/01 - 00:00:00
|  ISBN     |       |       |       |  `json-contents`      | `status` |
|---        |---    |---    |---    |---    |---    |
  """
    assert str_relaxed(current) ==str_relaxed(expected)