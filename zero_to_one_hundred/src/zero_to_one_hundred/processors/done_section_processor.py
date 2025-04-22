from zero_to_one_hundred.src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.src.zero_to_one_hundred.processors.a_processor import (
    AProcessor,
)
from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)

from zero_to_one_hundred.src.zero_to_one_hundred.validator.validator import Validator


class DoneSectionProcessor(AProcessor):
    """DoneSectionProcessor:
    done section on fs from http address"""

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

    def process(self):
        """
        - done existing new_section
        """
        section = Section(
            self.config_map,
            self.persist_fs,
            self.http_url,
            is_done=True,
        )
        section.write_done_section()
