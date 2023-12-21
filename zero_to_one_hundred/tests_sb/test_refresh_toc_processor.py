from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.processors.refresh_toc_processor import (
    RefreshTocProcessor,
)
from zero_to_one_hundred.tests_sb.moke import sb_persist_fs_fake, sb_process_fs_fake


def test_process(get_config_map):
    actual: RefreshTocProcessor = SBFactory(
        get_config_map,
        sb_persist_fs_fake.SBPersistFSFake,
        sb_process_fs_fake.SBProcessFSFake,
    ).get_processor([None, "refresh_toc"])
    for p in actual:
        p.process()
