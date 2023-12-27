from enum import Enum

from zero_to_one_hundred.repository.process_fs import ProcessFS

from zero_to_one_hundred.repository.persist_fs import PersistFS

from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.factories.a_factory import AFactory
from zero_to_one_hundred.processors.create_section_processor import (
    CreateSectionProcessor,
)
from zero_to_one_hundred.processors.done_section_processor import DoneSectionProcessor
from zero_to_one_hundred.processors.help_processor import HelpProcessor
from zero_to_one_hundred.processors.refresh_links_processor import RefreshLinksProcessor
from zero_to_one_hundred.processors.refresh_map_processor import RefreshMapProcessor


class ZTOHFactory(AFactory):
    """0to100 Factory class."""

    class SUPPORTED_PROCESSOR(Enum):
        create_section = 1
        done_section = 2
        refresh_map = 3
        refresh_links = 4
        help = 5

    def __init__(self, config_map: ConfigMap, persist_fs: PersistFS, process_fs: ProcessFS):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def get_processor(self, args):
        cmd = args[1]
        if cmd == ZTOHFactory.SUPPORTED_PROCESSOR.create_section.name:
            yield self.create_section_processor(args[2])
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.done_section.name:
            yield self.done_section_processor(args[2])
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.refresh_map.name:
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.refresh_links.name:
            yield self.refresh_links_processor()
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.help.name:
            yield self.help_processor()
        else:
            yield self.unsupported_processor(cmd)

    def create_section_processor(self, http_url):
        return CreateSectionProcessor(self.config_map, self.persist_fs, self.process_fs, http_url)

    def done_section_processor(self, http_url):
        return DoneSectionProcessor(self.config_map, self.persist_fs, self.process_fs, http_url)

    def refresh_map_processor(self):
        return RefreshMapProcessor(self.config_map, self.persist_fs, self.process_fs)

    def refresh_links_processor(self):
        return RefreshLinksProcessor(self.config_map, self.persist_fs, self.process_fs)

    def help_processor(self):
        return HelpProcessor(self.config_map, self.SUPPORTED_PROCESSOR)
