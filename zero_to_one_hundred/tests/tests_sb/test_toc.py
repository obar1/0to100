import pytest

from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.models.toc import Toc
from zero_to_one_hundred.tests.conftest import str_relaxed


def test_init(get_config_map, persist_fs, process_fs, http_oreilly_1):
    actual = Toc(
        get_config_map,
        persist_fs,
        process_fs,
        [],
    )
    assert len(actual.meta_books) == 0
    mb = MetaBook(
        get_config_map,
        persist_fs,
        process_fs,
        http_oreilly_1,
    )
    actual = Toc(
        get_config_map,
        persist_fs,
        process_fs,
        [mb],
    )
    assert str(actual.readme_md).endswith("toc.md")
    assert len(actual.meta_books) == 1


@pytest.mark.usefixtures("mock_time")
def test_asMarkDown(
    get_config_map, persist_fs, process_fs, http_oreilly_1, http_oreilly_2
):
    metabooks = [
        MetaBook(
            get_config_map,
            persist_fs,
            process_fs,
            http_oreilly_1,
        ),
        MetaBook(
            get_config_map,
            persist_fs,
            process_fs,
            http_oreilly_2,
        ),
    ]
    actual = Toc(
        get_config_map,
        persist_fs,
        process_fs,
        [],
    )
    current = actual.asMarkDown()
    expected = """
# TOC
## `0` metabook
### 2099/01/01 - 00:00:00
|  ISBN     |     img  |       `meta-contents`     |  `json-contents`      | `status` |
|---        |---    |---    |---    |---    |
  """
    assert str_relaxed("".join(current)) == str_relaxed("".join(expected))
