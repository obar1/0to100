from unittest.mock import patch
from zero_to_one_hundred.processors.done_section_processor import DoneSectionProcessor


@patch("zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor")
def test_process(get_config_map, get_factory, http_url):
    actual: DoneSectionProcessor = get_factory.get_processor(
        [None, "done_section", http_url]
    )
    for p in actual:
        p.process()
