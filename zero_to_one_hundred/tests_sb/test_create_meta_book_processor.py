
from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.processors.create_meta_book_processor import (
    CreateMetaBookProcessor,
)
from zero_to_one_hundred.tests_sb.moke.sb_persist_fs_fake import (
    SBPersistFSFake as persist_fs,
)
from zero_to_one_hundred.tests_sb.moke.sb_process_fs_fake import (
    SBProcessFSFake as process_fs,
)


def test_process(get_map_yaml_path, get_args_create_meta_book_processor, http_url):
    actual: CreateMetaBookProcessor = SBFactory(
        SBConfigMap(get_map_yaml_path, persist_fs), persist_fs, process_fs
    ).get_processor(get_args_create_meta_book_processor + [http_url])
    for p in actual:
        p.process()
