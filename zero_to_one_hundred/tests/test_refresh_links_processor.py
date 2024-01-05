from unittest.mock import patch
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.refresh_links_processor import RefreshLinksProcessor


@patch("zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor")
def test_process(get_config_map, persist_fs, process_fs):
    actual: RefreshLinksProcessor = ZTOHFactory(
        get_config_map, persist_fs, process_fs
    ).get_processor([None, "refresh_links"])
    for p in actual:
        p.process()
