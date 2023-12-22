"""DoneSectionProcessor:
done section on fs from http address
"""
# pylint: disable=R0801
from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.processors.a_processor import AProcessor


class DoneSectionProcessor(AProcessor):
    def __init__(self, persist_fs, process_fs, config_map: ConfigMap, http_url: str):
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.config_map = config_map

    def process(self):
        """
        - done existing new_section
        """
        section: Section = Section(
            self.persist_fs,
            self.process_fs,
            self.config_map,
            self.http_url,
            is_done=True,
        )
        section.write_done_section()
