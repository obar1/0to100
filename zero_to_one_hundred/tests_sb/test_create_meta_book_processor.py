from subprocess import CalledProcessError
from unittest.mock import patch

from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.processors.snatch_book_processor import (
    SnatchBookProcessor,
)


@patch("zero_to_one_hundred.factories.sb_factory.SBFactory.get_processor")
def test_process(get_config_map, persist_fs, process_fs, http_url):
    actual: SnatchBookProcessor = SBFactory(
        get_config_map,
        persist_fs,
        process_fs,
    ).get_processor([None, "snatch_book", http_url])
    for p in actual:
        try:
            p.process()
        except CalledProcessError:
            pass
