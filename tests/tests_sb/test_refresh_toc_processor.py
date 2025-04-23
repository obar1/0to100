from unittest.mock import patch

from src.zero_to_one_hundred.processors.refresh_toc_processor import (
    RefreshTocProcessor,
)


@patch("src.zero_to_one_hundred.factories.sb_factory.SBFactory.get_processor")
def test_process(get_factory_provider):
    actual = get_factory_provider.get_processor([None, "refresh_toc"])
    for p in actual:
        p.process()
        p.assert_called_once()
