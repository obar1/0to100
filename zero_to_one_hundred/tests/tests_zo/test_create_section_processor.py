from unittest.mock import patch

from zero_to_one_hundred.src.zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.src.zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.src.zero_to_one_hundred.models.yt_readme_md import YTReadMeMD
from zero_to_one_hundred.src.zero_to_one_hundred.processors.create_section_processor import (
    CreateSectionProcessor,
)


@patch(
    "zero_to_one_hundred.src.zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor"
)
def test_process(get_config_map, get_factory, http_url_1):
    actual: CreateSectionProcessor = get_factory.get_processor(
        ["zo", "create_section", http_url_1]
    )
    for p in actual:
        p.process()
        p.assert_called_once()


def test_get_readme_md(get_config_map, persist_fs, http_url_1, http_url_yt):
    actual = Section(get_config_map, persist_fs, http_url_1)
    assert isinstance(CreateSectionProcessor.get_readme_md(actual), ReadMeMD)

    actual = Section(get_config_map, persist_fs, http_url_yt)
    assert isinstance(CreateSectionProcessor.get_readme_md(actual), YTReadMeMD)
