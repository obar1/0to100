from typing import List


from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.models.section import Section


def test_write(get_config_map, persist_fs, process_fs, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, persist_fs, process_fs, http_url, False),
        Section(get_config_map, persist_fs, process_fs, http_url_2, False),
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)


def test_asMarkDown(get_config_map, persist_fs, process_fs, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, persist_fs, process_fs, http_url, False),
        Section(get_config_map, persist_fs, process_fs, http_url_2, False),
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
    current = actual.asMarkDown()
    expected = """
# map toc.md, 2

## sorted: False


## legend:

| footprints | completed | 
|---|---|
| :footprints: | :green_heart: |




1.[`here`](./0to100/https§§§cloud.google.com§abc/readme.md) :footprints:
1.[`here`](./0to100/https§§§cloud.google.com§zzz/readme.md) :footprints:
"""
    assert current.strip() == expected.strip()
