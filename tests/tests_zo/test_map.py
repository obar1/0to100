from src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from src.zero_to_one_hundred.models.map import Map
from src.zero_to_one_hundred.models.section import Section
from tests.conftest import str_relaxed

# pylint: disable=W0102


def test_as_mark_down(
    get_config_map: ZTOHConfigMap,
    persist_fs,
    http_urls=["https://cloud.google.com/zzz", "https://cloud.google.com/abc"],
):
    sections = [
        Section(get_config_map, persist_fs, http_url, False) for http_url in http_urls
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
    current = actual.as_mark_down()
    expected = """
# map toc_zo.md, 2

## legend:

**legend_icons**
`cloudskillsboost` :cloud:
`youtube` <img src='https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg' alt='YouTube Logo' width='64'>
`udemy` <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Udemy_logo.svg/1920px-Udemy_logo.svg.png' alt='Udemy' width='64'>

'1. TODO: Add an Header [`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) `wip` '
'1. TODO: Add an Header [`here`](./0to100/https§§§cloud.google.com§abc/readme.md) `wip` '
"""
    assert str_relaxed(current) == str_relaxed(expected)


def test_as_mark_down_0(
    get_config_map_sorted_0: ZTOHConfigMap,
    persist_fs,
    http_urls=[
        "https://cloud.google.com/abc",
        "https://cloud.google.com/zzz",
        "https://cloud.google.com/efg",
    ],
):
    sections = [
        Section(get_config_map_sorted_0, persist_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map_sorted_0, persist_fs, sections=sections)
    current = actual.as_mark_down()
    expected = """
# map toc_zo.md, 3
## legend:

'1. TODO: Add an Header [`here`](./0to100/https§§§cloud.google.com§abc/readme.md) `wip` '
'1. TODO: Add an Header [`here`](./0to100/https§§§cloud.google.com§efg/readme.md) `wip` '
'1. TODO: Add an Header [`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) `wip` '
"""
    assert str_relaxed(current) == str_relaxed(expected)


def test_as_mark_down_1(
    get_config_map_sorted_1: ZTOHConfigMap,
    persist_fs,
    http_urls=[
        "https://cloud.google.com/abc",
        "https://cloud.google.com/zzz",
        "https://cloud.google.com/efg",
    ],
):
    sections = [
        Section(get_config_map_sorted_1, persist_fs, http_url, False)
        for http_url in http_urls
    ]
    actual = Map(get_config_map_sorted_1, persist_fs, sections=sections)
    current = actual.as_mark_down()
    expected = """
# map toc_zo.md, 3
## legend:

'1. TODO: Add an Header [`here`](./0to100/https§§§cloud.google.com§abc/readme.md) `wip` '
'1. TODO: Add an Header [`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) `wip` '
'1. TODO: Add an Header [`here`](./0to100/https§§§cloud.google.com§efg/readme.md) `wip` '


"""
    assert str_relaxed(current) == str_relaxed(expected)
