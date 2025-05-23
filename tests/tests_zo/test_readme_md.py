from src.zero_to_one_hundred.models.readme_md import ReadMeMD
from src.zero_to_one_hundred.models.section import Section


def test_as_mark_down(get_config_map, persist_fs, http_url_1):
    actual = ReadMeMD(
        get_config_map,
        persist_fs,
        Section.from_http_url_to_dir,
        http_url_1,
    )
    current = actual.as_mark_down()
    assert (
        current
        == "ReadMeMD ./0to100/https§§§cloud.google.com§abc/readme.md, https§§§cloud.google.com§abc https://cloud.google.com/abc"
    )
