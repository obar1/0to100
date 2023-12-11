# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.processors.create_section_processor import (
    CreateSectionProcessor,
)
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.tests.moke.process_fs import ProcessFS as process_fs


def test_process(get_config_map, get_args_create_section_processor, http_url):
    actual: CreateSectionProcessor = ZTOHFactory(
        persist_fs, process_fs, get_config_map
    ).get_processor(get_args_create_section_processor + [http_url])
    for p in actual:
        p.process()
