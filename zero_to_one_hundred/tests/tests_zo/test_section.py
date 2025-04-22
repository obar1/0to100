import os

from pyfakefs.fake_filesystem_unittest import Patcher

from zero_to_one_hundred.src.zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.tests.conftest import str_relaxed


def test_init(get_config_map, persist_fs, http_url_1):
    actual = Section(get_config_map, persist_fs, http_url_1)
    assert actual.http_url == "https://cloud.google.com/abc"
    assert actual.dir_name == "https§§§cloud.google.com§abc"
    assert (
        actual.dir_readme_md
        == get_config_map.get_repo_path + "/" + "https§§§cloud.google.com§abc/readme.md"
    )
    res = actual.get_readme_md_time()
    assert res is not None

    # Test case for URL with hash character
    http_url_with_hash = "https://www.udemy.com/course/master-data-engineering-using-gcp-data-analytics/learn/lecture/34497408#content"
    actual_with_hash = Section(
        get_config_map, persist_fs, http_url_with_hash
    )
    assert actual_with_hash.http_url == http_url_with_hash
    assert (
        actual_with_hash.dir_name
        == "https§§§www.udemy.com§course§master-data-engineering-using-gcp-data-analytics§learn§lecture§34497408§content"
    )
    assert (
        actual_with_hash.dir_readme_md
        == get_config_map.get_repo_path
        + "/"
        + "https§§§www.udemy.com§course§master-data-engineering-using-gcp-data-analytics§learn§lecture§34497408§content/readme.md"
    )
    res_with_hash = actual_with_hash.get_readme_md_time()
    assert res_with_hash is not None





def test_build_from_dir(get_config_map, persist_fs):
    def simple_http():
        return "https://cloud.google.com/docs/<>:?*"

    def simple_dir():
        return "https§§§cloud.google.com§docs§§§§§§"

    assert (
        Section.build_from_dir(
            persist_fs, get_config_map, simple_http()
        ).dir_name
        == simple_dir()
    )

    # Test case for URL with hash character
    http_url_with_hash = "https://www.udemy.com/course/master-data-engineering-using-gcp-data-analytics/learn/lecture/34497408/content"
    dir_name_with_hash = "https§§§www.udemy.com§course§master-data-engineering-using-gcp-data-analytics§learn§lecture§34497408§content"
    assert (
        Section.build_from_dir(
            persist_fs, get_config_map, dir_name_with_hash
        ).http_url
        == http_url_with_hash
    )


def test_section_is_quest(get_config_map, persist_fs):
    http_url = "https://www.cloudskillsboost.google/quests/257"
    actual = Section(get_config_map, persist_fs, http_url)
    assert actual.is_gcp_quest


def test_section_is_lab(get_config_map, persist_fs):
    http_url = "https://www.cloudskillsboost.google/course_sessions/3062553/labs"
    actual = Section(get_config_map, persist_fs, http_url)
    assert actual.is_gcp_lab


def test_section_is_template(get_config_map, persist_fs):
    http_url = "https://www.cloudskillsboost.google/course_templates/536"
    actual = Section(get_config_map, persist_fs, http_url)
    assert actual.is_gcp_template


def test_section_is_gamee(get_config_map, persist_fs):
    http_url = "https://www.cloudskillsboost.google/games/4423"
    actual = Section(get_config_map, persist_fs, http_url)
    assert actual.is_gcp_game


def test_is_datacamp_project(get_config_map, persist_fs):
    http_url = "https://app.datacamp.com/learn/projects/1833"
    actual = Section(get_config_map, persist_fs, http_url)
    assert actual.is_datacamp_project


def test_is_datacamp_tutorial(get_config_map, persist_fs):
    http_url = "https://app.datacamp.com/learn/tutorials/git-push-pull"
    actual = Section(get_config_map, persist_fs, http_url)
    assert actual.is_datacamp_tutorial


def test_is_datacamp_course(get_config_map, persist_fs):
    http_url = "https://app.datacamp.com/learn/courses/writing-efficient-python-code"
    actual = Section(get_config_map, persist_fs, http_url)
    assert actual.is_datacamp_course


def test_gcp_get_format_as_md(get_config_map, persist_fs):
    http_url = "https://www.cloudskillsboost.google/games/4423"
    actual = Section.build_from_dir(persist_fs, get_config_map, http_url)
    assert actual.get_matching_icon_as_md == ":cloud:"


def test_as_mark_down(get_config_map, persist_fs, http_url_1):
    actual = Section(get_config_map, persist_fs, http_url_1)
    current = actual.as_mark_down()
    assert str_relaxed(current) == str_relaxed(
        "1.  [`here`](./0to100/https§§§cloud.google.com§abc/readme.md) `wip`"
    )


def test_look_for_orphan_images_cases(
    get_config_map, persist_fs, http_url_1
):
    http_url = "https://app.datacamp.com/learn/tutorials/git-push-pull"
    actual = Section(get_config_map, persist_fs, http_url)
    lines = """
    ![alt text](image.png) is here
    txt
    ![alt text](image1.png) is here
    txt2
    """
    png_files = ["image1.png", "image2.png"]
    excepted = ["image2.png"]
    assert actual.look_for_orphan_images(lines, png_files) == excepted

    lines = """
    ![alt text](image1.png) is here
    txt
    ![alt text](image2.png) is here
    txt2
    """
    png_files = ["image1.png"]
    excepted = []
    assert actual.look_for_orphan_images(lines, png_files) == excepted

    lines = """
    ![alt text](image1.png) is here
    txt
    ![](image2.png) is here
    txt2
    """
    png_files = ["image1.png", "image2.png"]
    excepted = []
    assert actual.look_for_orphan_images(lines, png_files) == excepted

    lines = """
    ![alt text](image1.png) is here
    txt
    ![alt text](12312324a.png) is here
    txt2
    """
    png_files = ["image1.png", "12312324a.png"]
    excepted = []
    assert actual.look_for_orphan_images(lines, png_files) == excepted
