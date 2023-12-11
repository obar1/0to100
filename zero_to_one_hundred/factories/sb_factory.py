"""SBFactory:
factory with implemented functionality
"""

import logging

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.processors.create_meta_book_processor import (
    CreateMetaBookProcessor,
)
from zero_to_one_hundred.processors.help_processor import HelpProcessor
from zero_to_one_hundred.processors.refresh_toc_processor import (
    RefreshTocProcessor,
)
from zero_to_one_hundred.processors.unsupported_processor import (
    UnsupportedProcessor,
)


class SBFactory:
    """SBFactory class."""

    from enum import Enum

    class SUPPORTED_PROCESSOR(Enum):
        create_meta_book = 1
        refresh_toc = 2
        help = 3

    def __init__(self, config_map: SBConfigMap, persist_fs, process_fs):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def get_processor(self, args):
        """get the processor"""
        logging.debug(f"args {args}")
        cmd = args[1]
        if cmd == SBFactory.SUPPORTED_PROCESSOR.create_meta_book.name:
            yield self.create_meta_book_processor(args[2])
        elif cmd == SBFactory.SUPPORTED_PROCESSOR.refresh_toc.name:
            yield self.refresh_toc_processor()
        elif cmd == SBFactory.SUPPORTED_PROCESSOR.help.name:
            yield self.help_processor()
        else:
            yield self.unsupported_processor(cmd)

    def create_meta_book_processor(self, http_url):
        """create_meta_book_processor"""
        return CreateMetaBookProcessor(
            self.config_map, self.persist_fs, http_url, self.process_fs
        )

    def refresh_toc_processor(self):
        """refresh_map_processor"""
        return RefreshTocProcessor(self.config_map, self.persist_fs, self.process_fs)

    def help_processor(self):
        """help_processor"""
        return HelpProcessor(self.persist_fs, self.SUPPORTED_PROCESSOR)

    @staticmethod
    def unsupported_processor(cmd):
        return UnsupportedProcessor(cmd)
