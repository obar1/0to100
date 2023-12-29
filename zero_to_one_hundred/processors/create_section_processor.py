from zero_to_one_hundred.repository.persist_fs import PersistFS

from zero_to_one_hundred.repository.process_fs import ProcessFS

from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.processors.a_processor import AProcessor
from zero_to_one_hundred.validator.validator import Validator


class CreateSectionProcessor(AProcessor):
    """CreateSectionProcessor:
    create a new new_section on fs from http address"""

    def __init__(self, config_map: ZTOHConfigMap, persist_fs: PersistFS, process_fs: ProcessFS, http_url: str):
        Validator.is_valid_http(http_url)
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.config_map = config_map

    def process(self):
        """
        - add new new_section
        - add def readme_md in new_section
        - add new sections to map at the end
        """
        section: Section = Section(self.config_map, self.persist_fs, self.process_fs, self.http_url, is_done=False)
        section.write()
        readme_md: ReadMeMD = ReadMeMD(self.config_map, self.persist_fs, self.process_fs, Section.from_dir_to_http_url,
                                       section.http_url)
        readme_md.write()
