"""ZTOHFactory:
factory with implemented functionality
"""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103
from configs.config import ConfigMap
from processors.create_section_processor import CreateSectionProcessor
from processors.refresh_links_processor import RefreshLinksProcessor
from processors.refresh_puml_processor import RefreshPUMLProcessor
from processors.refresh_map_processor import RefreshMapProcessor


class ZTOHFactory:
    """ZTOHFactory class."""

    def __init__(self, config_map: ConfigMap, persist_fs):
        self.config_map = config_map
        self.persist_fs = persist_fs

    def get_processor(self, args):
        """get the processor"""
        cmd = args[0]
        if cmd == "create_section":
            return self.create_section_processor(args[1])
        if cmd == "refresh_map":
            return self.refresh_map_processor()
        if cmd == "refresh_links":
            return self.refresh_links_processor()
        if cmd == "refresh_puml":
            return self.refresh_puml_processor()
        raise ValueError(args)

    def create_section_processor(self, http_url):
        """create_section_processor"""
        return CreateSectionProcessor(self.config_map, self.persist_fs, http_url)

    def refresh_map_processor(self):
        """refresh_map_processor"""
        return RefreshMapProcessor(self.config_map, self.persist_fs)

    def refresh_links_processor(self):
        """refresh_links_processor"""
        return RefreshLinksProcessor(self.config_map, self.persist_fs)

    def refresh_puml_processor(self):
        """refresh_puml_processor"""
        return RefreshPUMLProcessor(self.config_map, self.persist_fs)
