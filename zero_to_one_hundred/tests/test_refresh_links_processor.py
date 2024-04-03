from unittest.mock import patch
from zero_to_one_hundred.processors.refresh_links_processor import RefreshLinksProcessor


@patch("zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor")
def test_process(get_factory):
    actual: RefreshLinksProcessor = get_factory.get_processor([None, "refresh_links"])
    for p in actual:
        p.process()
