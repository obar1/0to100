from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.refresh_map_processor import RefreshMapProcessor
from zero_to_one_hundred.tests.moke import persist_fs_fake, process_fs_fake


def test_process(get_config_map):
    actual: RefreshMapProcessor = ZTOHFactory(
        persist_fs_fake.PersistFSFake, process_fs_fake, get_config_map
    ).get_processor([None, "refresh_map"])
    for p in actual:
        p.process()
