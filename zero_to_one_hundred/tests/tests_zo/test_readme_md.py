import os

from pyfakefs.fake_filesystem_unittest import Patcher
from zero_to_one_hundred.src.zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.src.zero_to_one_hundred.models.section import Section


def test_as_mark_down(get_config_map, persist_fs, process_fs, http_url_1):
    actual = ReadMeMD(
        get_config_map,
        persist_fs,
        process_fs,
        Section.from_http_url_to_dir,
        http_url_1,
    )
    current = actual.as_mark_down()
    assert (
        current
        == "ReadMeMD ./0to100/https§§§cloud.google.com§abc/readme.md, https§§§cloud.google.com§abc https://cloud.google.com/abc"
    )

def test_write(fs ,get_config_map, persist_fs, process_fs, http_url_1):

    with Patcher() as patcher:
        map_yaml = """
        type: zero-to-one-hundred-map
repo:
  path: "./0to100"
  idx_id: "toc_zo.md"
  idx_sort: "00:00:00" # order by modified date
legend:
  icons:
    - name: cloudskillsboost
      icon: ':cloud:'
      regex: "cloudskillsboost"
    - name: youtube
      icon: "<img src='https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg' alt='YouTube Logo' width='64'>"
      regex: "youtube"
    - name: udemy
      icon: "<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Udemy_logo.svg/1920px-Udemy_logo.svg.png' alt='Udemy' width='64'>"
      regex: "udemy"
"""
        fs.create_file('/home/xsazcd/git/obar1/0to100.git/zero_to_one_hundred/tests/tests_zo/resources/map.yaml', contents=map_yaml.strip())
        actual = ReadMeMD(
        get_config_map,
        persist_fs,
        process_fs,
        Section.from_http_url_to_dir,
        http_url_1,
        )
        actual.write()
        assert patcher.fs.exists(actual.readme_md)