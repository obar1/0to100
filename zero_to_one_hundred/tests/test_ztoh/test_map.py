import os

from pyfakefs.fake_filesystem_unittest import Patcher

from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.tests.conftest import str_relaxed

# pylint: disable=W0102


def test_asMarkDown(
    get_config_map: ZTOHConfigMap,
    persist_fs,
    process_fs,
    http_urls=["https://cloud.google.com/zzz", "https://cloud.google.com/abc"],
):
    sections = [
        Section(get_config_map, persist_fs, process_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
    current = actual.asMarkDown()
    expected = """
# map toc.md, 2
## legend:

| footprints | completed | 
|---|---|
| :footprints: | :green_heart: |

1.[`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) :footprints:
1.[`here`](./0to100/https§§§cloud.google.com§abc/readme.md) :footprints:
"""
    assert str_relaxed(current) == str_relaxed(expected)


def test_asMarkDown_0(
    get_config_map_sorted_0: ZTOHConfigMap,
    persist_fs,
    process_fs,
    http_urls=[
        "https://cloud.google.com/abc",
        "https://cloud.google.com/zzz",
        "https://cloud.google.com/efg",
    ],
):
    sections = [
        Section(get_config_map_sorted_0, persist_fs, process_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map_sorted_0, persist_fs, sections=sections)
    current = actual.asMarkDown()
    expected = """
# map toc.md, 3
## legend:

| footprints | completed | 
|---|---|
| :footprints: | :green_heart: |

1.[`here`](./0to100/https§§§cloud.google.com§abc/readme.md) :footprints:
1.[`here`](./0to100/https§§§cloud.google.com§efg/readme.md) :footprints:
1.[`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) :footprints:

"""
    assert str_relaxed(current) == str_relaxed(expected)


def test_asMarkDown_1(
    get_config_map_sorted_1: ZTOHConfigMap,
    persist_fs,
    process_fs,
    http_urls=[
        "https://cloud.google.com/abc",
        "https://cloud.google.com/zzz",
        "https://cloud.google.com/efg",
    ],
):
    sections = [
        Section(get_config_map_sorted_1, persist_fs, process_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map_sorted_1, persist_fs, sections=sections)
    current = actual.asMarkDown()
    expected = """
# map toc.md, 3
## legend:

| footprints | completed | 
|---|---|
| :footprints: | :green_heart: |

1.[`here`](./0to100/https§§§cloud.google.com§abc/readme.md) :footprints:
1.[`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) :footprints:
1.[`here`](./0to100/https§§§cloud.google.com§efg/readme.md) :footprints:


"""
    assert str_relaxed(current) == str_relaxed(expected)


def test_write(
    get_config_map: ZTOHConfigMap,
    persist_fs,
    process_fs,
    http_urls=["https://cloud.google.com/abc", "https://cloud.google.com/zzz"],
):
    sections = [
        Section(get_config_map, persist_fs, process_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
    txt = actual.asMarkDown()
    with Patcher(allow_root_user=False) as patcher:
        res = actual.write(txt)
        assert res > 0
        assert os.path.exists(actual.readme_md)
