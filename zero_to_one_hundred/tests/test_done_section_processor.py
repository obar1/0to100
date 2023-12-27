from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.done_section_processor import DoneSectionProcessor
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs


def test_process(get_config_map, http_url):
    actual: DoneSectionProcessor = ZTOHFactory(
        persist_fs, process_fs, get_config_map
    ).get_processor([None, "done_section", http_url])
    for p in actual:
        p.process()
