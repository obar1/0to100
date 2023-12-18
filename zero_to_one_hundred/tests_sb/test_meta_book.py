# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0212


from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.tests_sb.moke.sb_persist_fs import (
    SBPersistFS as persist_fs,
)
from zero_to_one_hundred.tests_sb.moke.sb_process_fs import (
    SBProcessFS as process_fs,
)


def test_init(get_map_yaml_path, http_url):
    actual = MetaBook(
        SBConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, http_url
    )
    assert str(actual.isbn).endswith("9780135956977")
    assert str(actual.contents_path).endswith("9780135956977")
    assert str(actual.dir_pdf).endswith("9780135956977/9780135956977.pdf")
    assert str(actual.dir_epub).endswith("9780135956977/9780135956977.epub")
    assert str(actual.dir_img).endswith("9780135956977/9780135956977.png")


def test_write(get_map_yaml_path, http_url):
    actual = MetaBook(
        SBConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, http_url
    )
    print(actual)


def test_build_from_dir(get_map_yaml_path):
    assert (
            MetaBook.build_from_dir(
                SBConfigMap(get_map_yaml_path, persist_fs),
                persist_fs,
                process_fs,
                "./books/9780135956977",
            ).isbn
            == "9780135956977"
    )


def test_is_valid_ebook_path():
    dirs = ["0123456789", "books", "ABC"]
    actual = [dir_ for dir_ in dirs if MetaBook.is_valid_ebook_path(dir_)]
    assert actual == ["0123456789"]


def test_get_epub_path(get_map_yaml_path, http_url, http_url_isbn):
    actual = MetaBook(
        SBConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs, http_url
    ).get_epub_path()
    assert str(actual).endswith(http_url_isbn + MetaBook.epub_suffix)
