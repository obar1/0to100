from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.done_section_processor import DoneSectionProcessor
from zero_to_one_hundred.tests.moke import persist_fs_fake, process_fs_fake


def test_process(get_config_map, http_url):
    actual: DoneSectionProcessor = ZTOHFactory(
        persist_fs_fake.PersistFSFake, process_fs_fake, get_config_map
    ).get_processor([None, "done_section", http_url])
    for p in actual:
        p.process()
