from unittest.mock import patch
from zero_to_one_hundred.processors.refresh_map_processor import RefreshMapProcessor


@patch("zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor")
def test_process(get_factory):
    actual: RefreshMapProcessor = get_factory.get_processor([None, "refresh_map"])
    for p in actual:
        p.process()
