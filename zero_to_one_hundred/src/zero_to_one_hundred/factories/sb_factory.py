from enum import Enum

from zero_to_one_hundred.src.zero_to_one_hundred.configs.sb_config_map import (
    SBConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.factories.a_factory import AFactory
from zero_to_one_hundred.src.zero_to_one_hundred.processors.refresh_toc_processor import (
    RefreshTocProcessor,
)
from zero_to_one_hundred.src.zero_to_one_hundred.processors.snatch_book_processor import (
    SnatchBookProcessor,
)
from zero_to_one_hundred.src.zero_to_one_hundred.repository.sb_persist_fs import (
    SBPersistFS,
)

from zero_to_one_hundred.src.zero_to_one_hundred.validator.validator import Validator


class SBFactory(AFactory):
    """SBFactory class."""

    class SUPPORTED_PROCESSOR(Enum):
        snatch_book = 1
        refresh_toc = 2
        help = 3

    extended_help = """
    snatch_book = snatch a book from safari
    ./main.py sb snatch_book https://learning.oreilly.com/library/view/rewire-your-brain/9781119895947
    
    refresh_toc = refresh the toc with al the books info
    ./main.py sb refresh_toc
    """

    def __init__(self, config_map: SBConfigMap, persist_fs: SBPersistFS):
        super().__init__(persist_fs=persist_fs)
        self.config_map = config_map

    def get_processor(self, args):
        cmd, p1, _ = Validator.validate_args(args)
        if cmd == SBFactory.SUPPORTED_PROCESSOR.snatch_book.name:
            http_url = p1
            yield self.snatch_book_processor(http_url)
            yield self.refresh_toc_processor()
        elif cmd == SBFactory.SUPPORTED_PROCESSOR.refresh_toc.name:
            yield self.refresh_toc_processor()
        elif cmd == SBFactory.SUPPORTED_PROCESSOR.help.name:
            yield self.help_processor()
        else:
            yield self.unsupported_processor(cmd, self.SUPPORTED_PROCESSOR)

    def snatch_book_processor(self, http_url):
        return SnatchBookProcessor(self.config_map, self.persist_fs, http_url)

    def refresh_toc_processor(self):
        return RefreshTocProcessor(self.config_map, self.persist_fs)
