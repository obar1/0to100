# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0212

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.processors.create_meta_book_processor import (
    CreateMetaBookProcessor,
)
from zero_to_one_hundred.tests_sb.moke.sb_persist_fs import (
    SBPersistFS as persist_fs,
)
from zero_to_one_hundred.tests_sb.moke.sb_process_fs import (
    SBProcessFS as process_fs,
)


def test_process(get_map_yaml_path, get_args_create_meta_book_processor, http_url):
    actual: CreateMetaBookProcessor = SBFactory(
        SBConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs
    ).get_processor(get_args_create_meta_book_processor + [http_url])
    for p in actual:
        p.process()
