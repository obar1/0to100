from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.done_section_processor import DoneSectionProcessor
from zero_to_one_hundred.tests.moke.persist_fs_fake import (
    PersistFSFake as persist_fs_fake,
)
from zero_to_one_hundred.tests.moke.process_fs_fake import (
    ProcessFSFake as process_fs_fake,
)


def test_process(get_config_map, get_args_create_section_processor, http_url):
    actual: DoneSectionProcessor = ZTOHFactory(
        persist_fs_fake, process_fs_fake, get_config_map
    ).get_processor(get_args_create_section_processor + [http_url])
    for p in actual:
        p.process()
