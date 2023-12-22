# pylint: disable=R0801
from enum import Enum

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
    """ZTOHFactory class."""

    class SUPPORTED_PROCESSOR(Enum):
        create_section = 1
        done_section = 2
        refresh_map = 3
        refresh_links = 4
        help = 5

    def __init__(self, persist_fs, process_fs, config_map: ConfigMap):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def get_processor(self, args):
        print(f"args {args}")
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
        return CreateSectionProcessor(
            self.persist_fs, self.process_fs, self.config_map, http_url
        )

    def done_section_processor(self, http_url):
        return DoneSectionProcessor(
            self.persist_fs, self.process_fs, self.config_map, http_url
        )

    def refresh_map_processor(self):
        return RefreshMapProcessor(self.persist_fs, self.process_fs, self.config_map)

    def refresh_links_processor(self):
        return RefreshLinksProcessor(self.persist_fs, self.process_fs, self.config_map)

    def help_processor(self):
        return HelpProcessor(self.config_map, self.persist_fs, self.SUPPORTED_PROCESSOR)
