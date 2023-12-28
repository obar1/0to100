from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.create_section_processor import (
    CreateSectionProcessor,
)
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs


def test_process(get_config_map, http_url):
    actual: CreateSectionProcessor = ZTOHFactory(
        persist_fs, process_fs, get_config_map
    ).get_processor([None, "create_section", http_url])
    for p in actual:
        p.process()
