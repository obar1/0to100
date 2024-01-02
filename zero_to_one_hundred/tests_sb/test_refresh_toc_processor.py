from unittest.mock import patch

from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.processors.refresh_toc_processor import (
    RefreshTocProcessor,
)


@patch("zero_to_one_hundred.factories.sb_factory.SBFactory.get_processor")
def test_process(get_config_map, persist_fs, process_fs):
    actual: RefreshTocProcessor = SBFactory(
        get_config_map, persist_fs, process_fs
    ).get_processor([None, "refresh_toc"])
    for p in actual:
        p.process()
