from subprocess import CalledProcessError
from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.processors.create_meta_book_processor import (
    CreateMetaBookProcessor,
)
from zero_to_one_hundred.tests_sb.moke import sb_persist_fs_fake, sb_process_fs_fake


def test_process(get_config_map, http_url):
    actual: CreateMetaBookProcessor = SBFactory(
        get_config_map,
        sb_persist_fs_fake.SBPersistFSFake,
        sb_process_fs_fake.SBProcessFSFake,
    ).get_processor([None, "create_meta_book", http_url])
    for p in actual:
        try:
            p.process()
        except CalledProcessError:
            pass
