from factories.ztoh_factory import ZTOHFactory
from processors.refresh_links_processor import RefreshLinksProcessor
from tests.conftest import TestPersistFS


def test_process(get_config_map, get_args_refresh_links_processor):
    actual: RefreshLinksProcessor = ZTOHFactory(get_config_map, TestPersistFS).get_processor(
        get_args_refresh_links_processor)
    actual.process()


