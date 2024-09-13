from enum import Enum

from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.factories.a_factory import AFactory
from zero_to_one_hundred.processors.create_section_processor import (
    CreateSectionProcessor,
)
from zero_to_one_hundred.processors.done_section_processor import DoneSectionProcessor
from zero_to_one_hundred.processors.refresh_links_processor import RefreshLinksProcessor
from zero_to_one_hundred.processors.refresh_map_processor import RefreshMapProcessor
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS
from zero_to_one_hundred.validator.validator import Validator


class ZTOHFactory(AFactory):
    """0to100 Factory class."""

    class SUPPORTED_PROCESSOR(Enum):
        create_section = 1
        done_section = 2
        refresh_map = 3
        refresh_links = 4
        help = 5

    extended_help = """
    create_section = create a new section
    section=https://www.cloudskillsboost.google/paths/16
    ./main.py zt create_section "$section"

    done_section = tag a section as done
    section=https://www.cloudskillsboost.google/paths/16
    ./main.py zt done_section "$section"
    
    refresh_map = refresh the section map
    ./main.py zt refresh_map
    
    refresh_links = refresh links to sections in the readme.md(s)
    ./main.py zt refresh_links
    """

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
        process_fs: ZTOHProcessFS,
    ):
        super().__init__(persist_fs=persist_fs)
        self.config_map = config_map
        self.process_fs = process_fs

    def get_processor(self, args):
        cmd, p1 = Validator.validate_args(args)
        if cmd == ZTOHFactory.SUPPORTED_PROCESSOR.create_section.name:
            yield self.create_section_processor(p1)
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.done_section.name:
            yield self.done_section_processor(p1)
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.refresh_map.name:
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.refresh_links.name:
            yield self.refresh_links_processor()
            yield self.refresh_map_processor()
        elif cmd == ZTOHFactory.SUPPORTED_PROCESSOR.help.name:
            yield self.help_processor()
        else:
            yield self.unsupported_processor(cmd, self.SUPPORTED_PROCESSOR)

    def create_section_processor(self, http_url):
        return CreateSectionProcessor(
            self.config_map, self.persist_fs, self.process_fs, http_url
        )

    def done_section_processor(self, http_url):
        return DoneSectionProcessor(
            self.config_map, self.persist_fs, self.process_fs, http_url
        )

    def refresh_map_processor(self):
        return RefreshMapProcessor(self.config_map, self.persist_fs, self.process_fs)

    def refresh_links_processor(self):
        return RefreshLinksProcessor(self.config_map, self.persist_fs, self.process_fs)
