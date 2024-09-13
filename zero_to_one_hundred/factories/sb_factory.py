from enum import Enum

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.factories.a_factory import AFactory
from zero_to_one_hundred.processors.refresh_toc_processor import RefreshTocProcessor
from zero_to_one_hundred.processors.snatch_book_processor import (
    SnatchBookProcessor,
)
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS
from zero_to_one_hundred.validator.validator import Validator


class SBFactory(AFactory):
    """SBFactory class."""

    class SUPPORTED_PROCESSOR(Enum):
        snatch_book = 1
        refresh_toc = 2
        help = 3

    def __init__(
        self, config_map: SBConfigMap, persist_fs: SBPersistFS, process_fs: SBProcessFS
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def get_processor(self, args):
        cmd, p1 = Validator.validate_args(args)
        if cmd == SBFactory.SUPPORTED_PROCESSOR.snatch_book.name:
            http_url = p1
            yield self.snatch_book_processor(http_url)
            yield self.refresh_toc_processor()
        elif cmd == SBFactory.SUPPORTED_PROCESSOR.refresh_toc.name:
            yield self.refresh_toc_processor()
        elif cmd == SBFactory.SUPPORTED_PROCESSOR.help.name:
            yield self.help_processor()
        else:
            yield self.unsupported_processor(cmd)

    def snatch_book_processor(self, http_url):
        return SnatchBookProcessor(
            self.config_map, self.persist_fs, self.process_fs, http_url
        )

    def refresh_toc_processor(self):
        return RefreshTocProcessor(self.config_map, self.persist_fs, self.process_fs)
