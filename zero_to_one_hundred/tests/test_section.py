from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs


def test_init(get_config_map, http_url):
    actual = Section(get_config_map, process_fs, process_fs, http_url)
    assert actual.http_url == "https://cloud.google.com/abc"
    assert actual.dir_name == "https§§§cloud.google.com§abc"
    assert actual.dir_readme_md == "https§§§cloud.google.com§abc/readme.md"


def test_write(get_config_map, http_url):
    actual = Section(get_config_map, persist_fs, process_fs, http_url)


def test_build_from_dir(get_config_map, simple_http, simple_dir):
    assert (
        Section.build_from_dir(
            persist_fs, process_fs, get_config_map, simple_http
        ).dir_name
        == simple_dir
    )


def test_section_is_quest(get_config_map):
    http_url = "https://www.cloudskillsboost.google/quests/257"
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    assert actual.is_quest


def test_section_is_lab(get_config_map):
    http_url = "https://www.cloudskillsboost.google/course_sessions/3062553/labs"
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    assert actual.is_lab


def test_section_is_template(get_config_map):
    http_url = "https://www.cloudskillsboost.google/course_templates/536"
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    assert actual.is_template


def test_section_is_gamee(get_config_map):
    http_url = "https://www.cloudskillsboost.google/games/4423"
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    assert actual.is_game
