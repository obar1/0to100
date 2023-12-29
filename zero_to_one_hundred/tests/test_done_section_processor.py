from unittest.mock import patch
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.done_section_processor import DoneSectionProcessor
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs


@patch("zero_to_one_hundred.factories.ztoh_factory.ZTOHFactory.get_processor")
def test_process(get_config_map, http_url):
    actual: DoneSectionProcessor = ZTOHFactory(
        get_config_map, persist_fs, process_fs
    ).get_processor([None, "done_section", http_url])
    for p in actual:
        p.process()
