# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from factories.ztoh_factory import ZTOHFactory
from processors.create_section_processor import CreateSectionProcessor
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs


def test_process(get_config_map, get_args_create_section_processor, http_url):
    actual: CreateSectionProcessor = ZTOHFactory(
        get_config_map, persist_fs, process_fs
    ).get_processor(get_args_create_section_processor + [http_url])
    for p in actual:
        p.process()
