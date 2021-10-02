# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from models.section import Section
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


def test_init(get_config_map, http_url):
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    assert actual.isbn == "9780135956977"
    assert actual.contents_path == "./books/9780135956977"
    assert actual.dir_pdf == "./books/9780135956977/9780135956977.pdf"
    assert actual.dir_epub == "./books/9780135956977/9780135956977.epub"
    assert actual.dir_img == "./books/9780135956977/9780135956977.png"


def test_write(get_config_map, http_url):
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    logging.info(actual)


def test_build_from_dir(get_config_map, simple_dir):
    assert (
        Section.build_from_dir(get_config_map, persist_fs, process_fs, simple_dir).isbn
        == simple_dir
    )
