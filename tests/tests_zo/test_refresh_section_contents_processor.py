from unittest.mock import patch

from src.zero_to_one_hundred.processors.refresh_section_contents_processor import (
    RefreshSectionContentsProcessor,
)


@patch("src.zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor")
def test_process(get_factory):
    actual: RefreshSectionContentsProcessor = get_factory.get_processor(
        [None, "refresh_section_contents"]
    )
    for p in actual:
        p.process()
        p.assert_called_once()
