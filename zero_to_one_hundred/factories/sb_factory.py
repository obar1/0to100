from enum import Enum

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.factories.a_factory import AFactory
from zero_to_one_hundred.processors.create_meta_book_processor import (
    CreateMetaBookProcessor,
)
from zero_to_one_hundred.processors.help_processor import HelpProcessor
from zero_to_one_hundred.processors.refresh_metadata_processor import (
    RefreshMetadataProcessor,
)
from zero_to_one_hundred.processors.refresh_toc_processor import RefreshTocProcessor

# pylint: disable=R0801


class SBFactory(AFactory):
    """SBFactory class."""

    class SUPPORTED_PROCESSOR(Enum):
        create_meta_book = 1
        refresh_toc = 2
        refresh_metadata = 3
        help = 4

    def __init__(self, config_map: SBConfigMap, persist_fs, process_fs):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def get_processor(self, args):
        cmd = args[1]
        if cmd == SBFactory.SUPPORTED_PROCESSOR.create_meta_book.name:
            http_url = args[2]
            yield self.create_meta_book_processor(http_url)
            yield self.refresh_metadata(http_url)
            yield self.refresh_toc_processor()
        elif cmd == SBFactory.SUPPORTED_PROCESSOR.refresh_toc.name:
            yield self.refresh_toc_processor()
        elif cmd == SBFactory.SUPPORTED_PROCESSOR.refresh_metadata.name:
            http_url = args[2]
            yield self.refresh_metadata(http_url)
        elif cmd == SBFactory.SUPPORTED_PROCESSOR.help.name:
            yield self.help_processor()
        else:
            yield self.unsupported_processor(cmd)

    def create_meta_book_processor(self, http_url):
        return CreateMetaBookProcessor(
            self.config_map, self.persist_fs, http_url, self.process_fs
        )

    def refresh_toc_processor(self):
        return RefreshTocProcessor(self.config_map, self.persist_fs, self.process_fs)

    def help_processor(self):
        return HelpProcessor(self.config_map, self.persist_fs, self.SUPPORTED_PROCESSOR)

    def refresh_metadata(self, http_url):
        return RefreshMetadataProcessor(
            self.config_map, self.persist_fs, http_url, self.process_fs
        )
