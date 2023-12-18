from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.refresh_links_processor import RefreshLinksProcessor
from zero_to_one_hundred.tests.moke.persist_fs_fake import (
    PersistFSFake as persist_fs_fake,
)
from zero_to_one_hundred.tests.moke.process_fs_fake import (
    ProcessFSFake as process_fs_fake,
)


def test_process(get_config_map, get_args_refresh_links_processor):
    actual: RefreshLinksProcessor = ZTOHFactory(
        persist_fs_fake, process_fs_fake, get_config_map
    ).get_processor(get_args_refresh_links_processor)
    for p in actual:
        p.process()
