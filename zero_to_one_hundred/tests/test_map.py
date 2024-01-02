from typing import List


from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.models.section import Section


def test_write(get_config_map, persist_fs, process_fs, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, persist_fs, process_fs, http_url, False),
        Section(get_config_map, persist_fs, process_fs, http_url_2, False),
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
    assert actual is not None


def test_as_md(get_config_map, persist_fs, process_fs, http_url, http_url_2):
    sections: List[Section] = [
        Section(get_config_map, persist_fs, process_fs, http_url, False),
        Section(get_config_map, persist_fs, process_fs, http_url_2, False),
    ]
    actual = Map(get_config_map, persist_fs, sections=sections)
    assert (
        actual.asMarkDown().strip("\n").replace(" ", "")
        == """
# map 0to100.md, 2

## sorted:False

## legend:

| footprints | completed |
|---|---|
| :footprints: | :green_heart: |
> extra
>
| quest | lab | template | game | course |
|---|---|---|----|---|
| :cyclone: | :floppy_disk: | :whale: | :snake: | :pushpin: |

1.  [`here`](https§§§cloud.google.com§abc/readme.md) :footprints: :pushpin:
1.  [`here`](https§§§cloud.google.com§zzz/readme.md) :footprints: :pushpin:
""".strip(
            "\n"
        ).replace(
            " ", ""
        )
    )
