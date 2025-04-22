from typing import Union

from zero_to_one_hundred.src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.src.zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.src.zero_to_one_hundred.processors.a_processor import (
    AProcessor,
)
from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)
from zero_to_one_hundred.src.zero_to_one_hundred.validator.validator import Validator


class CreateSectionProcessor(AProcessor):
    """CreateSectionProcessor:
    create a new new_section on fs from http address"""

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
        http_url: str,
    ):
        Validator.is_valid_http(http_url)
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.config_map = config_map

    @staticmethod
    def get_readme_md(section: Section) -> Union[ReadMeMD]:
        return ReadMeMD(
            section.config_map,
            section.persist_fs,
            Section.from_http_url_to_dir,
            section.http_url,
        )

    def process(self):
        """
        - add new new_section
        - add def readme_md in new_section
        - add new sections to map at the end
        """
        section = Section(
            self.config_map,
            self.persist_fs,
            self.http_url,
            is_done=False,
        )
        txt = self.config_map.get_repo_path + "/" + section.dir_name
        section.write(txt)
        readme_md = CreateSectionProcessor.get_readme_md(section)
        readme_md.write()
