from subprocess import CalledProcessError
from unittest.mock import patch

from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.processors.create_meta_book_processor import (
    CreateMetaBookProcessor,
)
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as sb_persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as sb_process_fs


@patch("zero_to_one_hundred.factories.sb_factory.SBFactory.get_processor")
def test_process(get_config_map, http_url):
    actual: CreateMetaBookProcessor = SBFactory(
        get_config_map,
        sb_persist_fs,
        sb_process_fs,
    ).get_processor([None, "create_meta_book", http_url])
    for p in actual:
        try:
            p.process()
        except CalledProcessError:
            pass
