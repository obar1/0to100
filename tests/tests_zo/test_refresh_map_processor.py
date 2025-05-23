from unittest.mock import patch

from src.zero_to_one_hundred.processors.refresh_map_processor import (
    RefreshMapProcessor,
)


@patch("src.zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor")
def test_process(get_factory):
    actual: RefreshMapProcessor = get_factory.get_processor([None, "refresh_map"])
    for p in actual:
        p.process()
        p.assert_called_once()
