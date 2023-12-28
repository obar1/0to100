from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.refresh_map_processor import RefreshMapProcessor
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs


def test_process(get_config_map):
    actual: RefreshMapProcessor = ZTOHFactory(get_config_map, persist_fs, process_fs).get_processor([None, "refresh_map"])
    for p in actual:
        p.process()
