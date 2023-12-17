from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.refresh_links_processor import RefreshLinksProcessor
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs


def test_process(get_config_map, get_args_refresh_links_processor):
    actual: RefreshLinksProcessor = ZTOHFactory(
        persist_fs, process_fs, get_config_map
    ).get_processor(get_args_refresh_links_processor)
    for p in actual:
        p.process()
