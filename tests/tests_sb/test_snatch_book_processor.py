from unittest.mock import patch

from src.zero_to_one_hundred.processors.snatch_book_processor import (
    SnatchBookProcessor,
)


@patch("src.zero_to_one_hundred.factories.sb_factory.SBFactory.get_processor")
def test_process(get_factory, http_oreilly_1):
    actual: SnatchBookProcessor = get_factory.get_processor(
        [None, "snatch_book", http_oreilly_1]
    )
    for p in actual:
        p.process()
        p.assert_called_once()
