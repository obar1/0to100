"""ZTOHFactory:
"""
# pylint: disable=R0903,E0401,W0703,W1201

from typing import List

from configs.config import Config, ConfigMap
from processors.refresh_links_processor import RefreshLinksProcessor
from processors.refresh_puml_processor import RefreshPUMLProcessor
from processors.refresh_sections_processor import RefreshSectionsProcessor
from processors.create_section_processor import CreateSectionProcessor





class ZTOHFactory:
    """ZTOHFactory class."""

    def __init__(self, config_map: ConfigMap, PersistFS):
        self.config_map = config_map
        self.PersistFS=PersistFS

    def get_processor(self,args):
        """get the processor """
        cmd=args[0]
        if cmd=="create_section":
            return self.create_section_processor(args[1])
        elif cmd == "refresh_sections":
            return self.refresh_sections_processor()
        elif cmd == "refresh_links":
            return self.refresh_links_processor()
        elif cmd == "refresh_puml":
            return self.refresh_puml_processor()
        else:
            raise ValueError(args)

    def create_section_processor(self,http_url):
        return CreateSectionProcessor(self.config_map, self.PersistFS, http_url)

    def refresh_sections_processor(self):
        return RefreshSectionsProcessor(self.config_map, self.PersistFS)

    def refresh_links_processor(self):
        return RefreshLinksProcessor(self.config_map, self.PersistFS)

    def refresh_puml_processor(self):
        return RefreshPUMLProcessor(self.config_map, self.PersistFS)

