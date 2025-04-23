from unittest.mock import patch

from src.zero_to_one_hundred.processors.done_section_processor import (
    DoneSectionProcessor,
)


@patch("src.zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor")
def test_process(get_config_map, get_factory, http_url_1):
    actual: DoneSectionProcessor = get_factory.get_processor(
        [None, "done_section", http_url_1]
    )
    for p in actual:
        p.process()
        p.assert_called_once()
