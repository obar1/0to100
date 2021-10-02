"""ZTOHFactory:
factory with implemented functionality
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from configs.config import ConfigMap
from processors.create_section_processor import CreateSectionProcessor
from processors.help_processor import HelpProcessor
from processors.refresh_links_processor import RefreshLinksProcessor
from processors.refresh_map_processor import RefreshMapProcessor
from processors.refresh_puml_processor import RefreshPUMLProcessor
from processors.unsupported_processor import UnsupportedProcessor


class ZTOHFactory:
    """ZTOHFactory class."""

    SUPPORTED_PROCESSOR = [
        "create_section",
        "refresh_map",
        "refresh_links",
        "refresh_puml",
        "help",
    ]

    def __init__(self, config_map: ConfigMap, persist_fs, process_fs):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def get_processor(self, args):
        """get the processor"""
        logging.info(f"args {args}")
        cmd = args[1]
        if cmd == "create_section":
            yield self.create_section_processor(args[2])
        elif cmd == "refresh_map":
            yield self.refresh_map_processor()
        elif cmd == "refresh_links":
            yield self.refresh_links_processor()
        elif cmd == "refresh_puml":
            yield self.refresh_puml_processor()
        elif cmd == "help":
            yield self.help_processor()
        else:
            yield self.unsupported_processor(cmd)

    def create_section_processor(self, http_url):
        """create_section_processor"""
        return CreateSectionProcessor(
            self.config_map, self.persist_fs, http_url, self.process_fs
        )

    def refresh_map_processor(self):
        """refresh_map_processor"""
        return RefreshMapProcessor(self.config_map, self.persist_fs, self.process_fs)

    def refresh_links_processor(self):
        """refresh_links_processor"""
        return RefreshLinksProcessor(self.config_map, self.persist_fs,self.process_fs)

    def refresh_puml_processor(self):
        """refresh_puml_processor"""
        return RefreshPUMLProcessor(self.config_map, self.persist_fs,self.process_fs)

    def help_processor(self):
        """version_processor"""
        return HelpProcessor(self.SUPPORTED_PROCESSOR, self.persist_fs)

    @staticmethod
    def unsupported_processor(cmd):
        return UnsupportedProcessor(cmd)
