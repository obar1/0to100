from typing import List, Literal
import re

from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.tests.test_ztoh.ztoh_process_fs import ZTOHProcessFS


def test_write(get_config_map: ZTOHConfigMap, persist_fs: ZTOHPersistFS, process_fs: ZTOHProcessFS, http_url: Literal['https://cloud.google.com/abc'], http_url_2: Literal['https://cloud.google.com/zzz']):
    sections: List[Section] = [
        Section(get_config_map, persist_fs, process_fs, http_url, False),
        Section(get_config_map, persist_fs, process_fs, http_url_2, False),
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)


def test_asMarkDown(get_config_map: ZTOHConfigMap, persist_fs: ZTOHPersistFS, process_fs: ZTOHProcessFS, http_urls =['https://cloud.google.com/abc','https://cloud.google.com/zzz']):
    sections = [Section(get_config_map, persist_fs, process_fs, http_url, False) for http_url in http_urls]
    actual = Map(get_config_map, persist_fs, sections=sections)
    current = actual.asMarkDown()
    expected = """
# map toc.md, 2
## legend:

| footprints | completed | 
|---|---|
| :footprints: | :green_heart: |

1.[`here`](./0to100/https§§§cloud.google.com§abc/readme.md) :footprints:
1.[`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) :footprints:
"""
    assert  re.sub(r'\s', '', current) == re.sub(r'\s', '', expected)


def test_asMarkDown_0(get_config_map_sorted_0: ZTOHConfigMap, persist_fs: ZTOHPersistFS, process_fs: ZTOHProcessFS, http_urls =['https://cloud.google.com/abc','https://cloud.google.com/zzz', 'https://cloud.google.com/efg']):
    sections = [Section(get_config_map_sorted_0, persist_fs, process_fs, http_url, False) for http_url in http_urls]
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
    assert  re.sub(r'\s', '', current) == re.sub(r'\s', '', expected)
