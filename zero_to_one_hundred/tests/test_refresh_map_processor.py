from unittest.mock import patch
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.refresh_map_processor import RefreshMapProcessor


@patch("zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor")
def test_process(get_config_map, persist_fs, process_fs):
    actual: RefreshMapProcessor = ZTOHFactory(
        get_config_map, persist_fs, process_fs
    ).get_processor([None, "refresh_map"])
    for p in actual:
        p.process()
