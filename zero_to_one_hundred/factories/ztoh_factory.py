"""ZTOHFactory:
factory with implemented functionality
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from configs.config import ConfigMap
from processors.create_section_processor import CreateSectionProcessor
from processors.done_section_processor import DoneSectionProcessor
from processors.refresh_links_processor import RefreshLinksProcessor
from processors.refresh_map_processor import RefreshMapProcessor
from processors.help_processor import HelpProcessor
from processors.unsupported_processor import UnsupportedProcessor


class ZTOHFactory:
    """ZTOHFactory class."""

    from enum import Enum

    class SUPPORTED_PROCESSOR(Enum):
        create_section = 1
        done_section = 2
        refresh_map = 3
        refresh_links = 4
        help = 5

    def __init__(self, persist_fs, process_fs, config_map: ConfigMap):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def get_processor(self, args):
        """get the processor"""
        logging.debug(f"args {args}")
        cmd = args[1]
        if cmd == ZTOHFactory.SUPPORTED_PROCESSOR.create_section.name:
            yield self.create_section_processor(args[2])
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.done_section.name:
            yield self.done_section_processor(args[2])
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.refresh_map.name:
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.refresh_links.name:
            yield self.refresh_links_processor()
        elif cmd == "help":
            yield self.help_processor()
        else:
            yield self.unsupported_processor(cmd)

    def create_section_processor(self, http_url):
        """create_section_processor"""
        return CreateSectionProcessor(
            self.persist_fs, self.process_fs, self.config_map, http_url
        )

    def done_section_processor(self, http_url):
        """done_section_processor"""
        return DoneSectionProcessor(
            self.persist_fs, self.process_fs, self.config_map, http_url
        )

    def refresh_map_processor(self):
        """refresh_map_processor"""
        return RefreshMapProcessor(self.persist_fs, self.process_fs, self.config_map)

    def refresh_links_processor(self):
        """refresh_links_processor"""
        return RefreshLinksProcessor(self.persist_fs, self.process_fs, self.config_map)

    def help_processor(self):
        """help_processor"""
        return HelpProcessor(self.persist_fs, self.SUPPORTED_PROCESSOR)

    @staticmethod
    def unsupported_processor(cmd):
        return UnsupportedProcessor(cmd)
