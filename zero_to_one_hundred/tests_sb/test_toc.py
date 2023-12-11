# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0212

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.toc import Toc
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.tests_sb.moke.sb_persist_fs import (
    SBPersistFS as persist_fs,
)
from zero_to_one_hundred.tests_sb.moke.sb_process_fs import (
    SBProcessFS as process_fs,
)


def test_init(get_map_yaml_path, http_url):
    mb = MetaBook(
        SBConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, http_url
    )
    actual = Toc(
        SBConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, [mb]
    )
    assert str(actual.readme_md).endswith("toc.md")
    assert len(actual.meta_books) == 1


def test___repr_flatten(get_map_yaml_path, http_url):
    mb = MetaBook(
        SBConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, http_url
    )
    toc = Toc(SBConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, [mb])
    actual = toc._Toc__repr_flatten(toc.meta_books)
    assert (
        actual
        == r'<span style="color:blue">**9780135956977**</span>|![`img`](9780135956977/9780135956977.png)|[`epub`](9780135956977/9780135956977.epub)|[`pdf`](9780135956977/9780135956977.pdf)|{}|<span style="color:yellow">**WIP**</span>'
    )
