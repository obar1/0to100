# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from models.section import Section
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


def test_init(get_config_map, http_url):
    actual = Section(persist_fs, process_fs, get_config_map, http_url)
    assert actual.http_url == "http://cloud.google.com/docs"
    assert actual.dir_name == "http§§§cloud.google.com§docs"
    assert actual.dir_readme_md == "http§§§cloud.google.com§docs/readme.md"


def test_write(get_config_map, http_url):
    actual = Section(persist_fs, process_fs, get_config_map, http_url)
    logging.info(actual)


def test_build_from_dir(get_config_map, simple_http, simple_dir):
    assert (
        Section.build_from_dir(
            persist_fs, process_fs, get_config_map, simple_http
        ).dir_name
        == simple_dir
    )
