# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from models.section import Section
from repository.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


def test_init(get_config_map, http_url):
    actual = Section(persist_fs, process_fs, get_config_map, http_url)
    assert actual.http_url == "https://cloud.google.com/abc"
    assert actual.dir_name == "https§§§cloud.google.com§abc"
    assert actual.dir_readme_md == "https§§§cloud.google.com§abc/readme.md"


def test_write(get_config_map, http_url):
    actual = Section(persist_fs, process_fs, get_config_map, http_url)
    logging.debug(actual)


def test_build_from_dir(get_config_map, simple_http, simple_dir):
    assert (
        Section.build_from_dir(
            persist_fs, process_fs, get_config_map, simple_http
        ).dir_name
        == simple_dir
    )

def test_section_is_quest(get_config_map):
    http_url = 'https://www.cloudskillsboost.google/quests/257'
    actual = Section(persist_fs, process_fs, get_config_map, http_url)
    assert actual.is_quest

def test_section_is_lab(get_config_map):
    http_url = 'https://www.cloudskillsboost.google/course_sessions/3062553/labs'
    actual = Section(persist_fs, process_fs, get_config_map, http_url)
    assert actual.is_lab

def test_section_is_template(get_config_map):
    http_url = 'https://www.cloudskillsboost.google/course_templates/536'
    actual = Section(persist_fs, process_fs, get_config_map, http_url)
    assert actual.is_template

def test_section_is_gamee(get_config_map):
    http_url = 'https://www.cloudskillsboost.google/games/4423'
    actual = Section(persist_fs, process_fs, get_config_map, http_url)
    assert actual.is_game
